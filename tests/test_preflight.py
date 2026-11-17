import contextlib
import copy
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import urllib.error

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import check_availability as check
from build_index import ROOT, validate


class PreflightTests(unittest.TestCase):
    def invoke(self, args):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = check.main(args)
        return code, json.loads(output.getvalue())

    def test_directory_identity_is_only_advertised(self):
        result = check.inspect_directory({'data': [{'id': 'model-v1'}]}, 'model-v1')
        self.assertEqual(result['status'], 'listed')
        self.assertFalse(result['upstreamIdentityVerified'])
        self.assertFalse(result['inferenceAvailabilityVerified'])

    def test_alias_does_not_match_a_snapshot(self):
        result = check.inspect_directory({'data': [{'id': 'model'}]}, 'model-v1')
        self.assertFalse(result['directoryContainsModel'])

    def test_invalid_or_duplicate_entries_are_rejected(self):
        for document in [{}, {'data': [None]}, {'data': [{'id': 'x'}, {'id': 'x'}]}]:
            with self.subTest(document=document), self.assertRaises(ValueError):
                check.inspect_directory(document, 'x')

    def test_live_mode_requires_execute_and_makes_no_request(self):
        with patch.object(check.urllib.request, 'build_opener') as opener:
            code, report = self.invoke(['--models-url', 'https://provider.invalid/v1/models', '--model', 'x'])
        opener.assert_not_called()
        self.assertEqual(code, 2)
        self.assertEqual(report['status'], 'not-executed')

    def test_offline_directory_does_not_claim_live_connectivity(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / 'models.json'
            file.write_text('{"data":[{"id":"x"}]}', encoding='utf8')
            code, report = self.invoke(['--directory-json', str(file), '--model', 'x'])
        self.assertEqual(code, 0)
        self.assertFalse(report['liveConnectivityVerified'])

    def test_inference_urls_and_credential_urls_are_not_requested(self):
        for url in ['https://provider.invalid/v1/chat/completions', 'https://provider.invalid/v1/models?key=secret', 'https://user:secret@provider.invalid/models']:
            with self.subTest(url=url), patch.object(check.urllib.request, 'build_opener') as opener:
                code, report = self.invoke(['--models-url', url, '--model', 'x', '--execute'])
                opener.assert_not_called()
                self.assertEqual(code, 1)
                self.assertNotIn('secret', json.dumps(report))

    def test_http_error_does_not_expose_key_or_body(self):
        error = urllib.error.HTTPError('https://provider.invalid/models', 403, 'sensitive provider message', {}, None)
        with patch.dict(check.os.environ, {'EVAL_TEST_KEY': 'fixture-secret'}), patch.object(check.urllib.request, 'build_opener') as opener:
            opener.return_value.open.side_effect = error
            code, report = self.invoke(['--models-url', 'https://provider.invalid/models', '--model', 'x', '--api-key-env', 'EVAL_TEST_KEY', '--execute'])
            request = opener.return_value.open.call_args.args[0]
        self.assertEqual(request.get_method(), 'GET')
        self.assertIsNone(request.data)
        self.assertEqual(code, 1)
        self.assertEqual(report['httpStatus'], 403)
        self.assertNotIn('fixture-secret', json.dumps(report))
        self.assertNotIn('sensitive', json.dumps(report))

    def test_redirect_is_not_followed(self):
        self.assertIsNone(check.NoRedirect().redirect_request(None, None, 302, '', {}, 'https://other.invalid/models'))

    def test_unrelated_tool_types_cannot_enter_core(self):
        data = json.loads((ROOT / 'data/benchmarks.json').read_text(encoding='utf8'))
        for entry_type in ['terminal-feed', 'browser-extension', 'original-proposal']:
            invalid = copy.deepcopy(data)
            invalid['benchmarks'][0]['entryType'] = entry_type
            with self.subTest(entry_type=entry_type), self.assertRaises(AssertionError):
                validate(invalid)


if __name__ == '__main__':
    unittest.main()
