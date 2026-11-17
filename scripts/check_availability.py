"""Check an OpenAI-compatible model directory without inference requests.

Defaults to an offline directory JSON. Live GET requires --execute.
Directory presence is an advertised identity, not proof of upstream model identity.
"""
import argparse
from datetime import datetime, timezone
import json
import math
import os
from pathlib import Path
import socket
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request


def inspect_directory(document, model):
    if not isinstance(document, dict) or not isinstance(document.get('data'), list):
        raise ValueError('Expected a model directory object with a data array')
    rows = document['data']
    if any(not isinstance(row, dict) or not isinstance(row.get('id'), str) for row in rows):
        raise ValueError('Each directory entry must contain a string id')
    matches = [row for row in rows if row['id'] == model]
    if len(matches) > 1:
        raise ValueError('Duplicate requested model id in directory')
    return {'requestedModelId': model, 'directoryContainsModel': bool(matches),
            'status': 'listed' if matches else 'not-listed',
            'identityEvidence': 'provider-directory-only',
            'upstreamIdentityVerified': False, 'inferenceAvailabilityVerified': False}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model', required=True, help='Exact requested ID or snapshot')
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument('--directory-json', type=Path, help='Saved models response; offline')
    source.add_argument('--models-url', help='Full models directory URL; GET only')
    parser.add_argument('--api-key-env', help='Name of an environment variable; never the key itself')
    parser.add_argument('--execute', action='store_true', help='Allow live GET; never invokes inference')
    parser.add_argument('--timeout', type=float, default=15)
    args = parser.parse_args(argv)
    report = {'checkedAt': datetime.now(timezone.utc).isoformat(), 'inferenceRequests': 0}
    try:
        if args.directory_json:
            if args.execute or args.api_key_env:
                raise ValueError('Offline directory mode does not accept authentication or --execute')
            document = json.loads(args.directory_json.read_text(encoding='utf8'))
            report['mode'] = 'offline-snapshot'
            report['liveConnectivityVerified'] = False
        else:
            url = urllib.parse.urlsplit(args.models_url)
            if url.username or url.password or url.query or url.fragment or not url.hostname:
                raise ValueError('Use a URL without credentials, query or fragment')
            local = url.hostname in {'127.0.0.1', 'localhost', '::1'}
            if url.scheme != 'https' and not (url.scheme == 'http' and local):
                raise ValueError('HTTPS required except for local loopback')
            if url.path.rstrip('/').split('/')[-1] != 'models':
                raise ValueError('Only a models directory endpoint is allowed')
            if not math.isfinite(args.timeout) or not 0 < args.timeout <= 120:
                raise ValueError('Timeout must be between 0 and 120 seconds')
            report['mode'] = 'live-directory'
            if not args.execute:
                report.update(status='not-executed', liveConnectivityVerified=False)
                print(json.dumps(report))
                return 2
            headers = {'Accept': 'application/json', 'User-Agent': 'ai-benchmark-index-preflight'}
            if args.api_key_env:
                key = os.environ.get(args.api_key_env)
                if not key:
                    raise ValueError('Configured API key environment variable is missing')
                headers['Authorization'] = 'Bearer ' + key
            request = urllib.request.Request(args.models_url, headers=headers, method='GET')
            with urllib.request.build_opener(NoRedirect()).open(request, timeout=args.timeout) as response:
                body = response.read(4 * 1024 * 1024 + 1)
                if len(body) > 4 * 1024 * 1024:
                    raise ValueError('Directory response too large')
                document = json.loads(body)
                report.update(httpStatus=response.status, liveConnectivityVerified=True)
        report.update(inspect_directory(document, args.model))
        print(json.dumps(report))
        return 0 if report['directoryContainsModel'] else 1
    except urllib.error.HTTPError as error:
        # Never print headers, provider response bodies or exception URL strings.
        report.update(status='http-error', httpStatus=error.code)
    except (urllib.error.URLError, socket.timeout, TimeoutError, ssl.SSLError):
        report.update(status='connection-error')
    except (ValueError, OSError) as error:
        report.update(status='invalid-input-or-response', errorType=type(error).__name__)
    print(json.dumps(report))
    return 1


if __name__ == '__main__':
    sys.exit(main())
