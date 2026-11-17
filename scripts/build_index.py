"""Render the Markdown index from a reviewed, local JSON catalog. No model calls."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GROUPS = {'quick': '快速检查与日常任务', 'visual': '视觉、图形与整活', 'agent': 'Agent、博弈与长任务', 'standard': '成熟 benchmark 与专项能力'}
TAGS = {'priority': '★ 回归优先', 'supporting': '△ 辅助观察', 'exclude': '— 不入核心回归'}


def render(data):
    lines = ['# 全部测评索引', '', '由 `data/benchmarks.json` 生成。★ 是固定条件重复测试的优先候选，不代表一道题就能证明降智。状态与来源核验状态分开。', '']
    for group, title in GROUPS.items():
        lines += [f'<a id="{group}"></a>', '', '## ' + title, '', '| 测试／来源 | 测什么、怎么玩 | 如何判分 | 回归用途 | 门槛／当前状态 |', '| --- | --- | --- | --- | --- |']
        for e in data['benchmarks']:
            if e['category'] != group:
                continue
            cell = lambda text: str(text).replace('|', '／').replace('\n', ' ')
            lines.append('| ' + ' | '.join(map(cell, [f"[{e['name']}]({e['sourceUrl']})", e['ability'], e['scoring'], TAGS[e['regression']] + '：' + e['regressionNote'], e['burden'] + '；' + e['status'] + '；' + e['sourceReview']])) + ' |')
        lines.append('')
    return '\n'.join(lines).rstrip() + '\n'


def validate(data):
    entries = data['benchmarks']
    ids = [e['id'] for e in entries]
    assert len(ids) == len(set(ids)), 'Duplicate IDs'
    required = {'id', 'name', 'category', 'ability', 'scoring', 'regression', 'regressionNote', 'burden', 'status', 'sourceUrl', 'sourceReview', 'licenseNote'}
    for e in entries:
        assert required <= e.keys(), e['id']
        assert e['category'] in GROUPS and e['regression'] in TAGS, e['id']
        assert e['sourceUrl'].startswith('https://'), e['id']
        assert e['sourceReview'] in {'reviewed-primary', 'historical-lead', 'original-proposal', 'local-public-source'}, e['id']
        assert e['licenseNote'], e['id']
    assert len(entries) >= 40
    assert any(e['regression'] == 'priority' for e in entries)
    return len(entries)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    data = json.loads((ROOT / 'data/benchmarks.json').read_text(encoding='utf8'))
    count = validate(data)
    path = ROOT / 'INDEX.md'
    body = render(data)
    if args.check:
        assert path.read_text(encoding='utf8') == body, 'Run python scripts/build_index.py'
    else:
        path.write_text(body, encoding='utf8', newline='\n')
    print(json.dumps({'entries': count, 'generatedIndexMatches': True, 'modelCalls': 0}))
