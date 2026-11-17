"""Search the local catalog. No network and no model calls."""
import argparse
import json
from pathlib import Path

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('query', nargs='?', default='')
p.add_argument('--category', choices=['quick','visual','agent','standard'])
p.add_argument('--regression', choices=['priority','supporting','exclude'])
a=p.parse_args()
data=json.loads((Path(__file__).resolve().parents[1]/'data/benchmarks.json').read_text(encoding='utf8'))
for e in data['benchmarks']:
    if a.category and e['category']!=a.category: continue
    if a.regression and e['regression']!=a.regression: continue
    if a.query.lower() not in json.dumps(e,ensure_ascii=False).lower(): continue
    print(f"[{e['regression']}] {e['name']}\n  {e['ability']}\n  判分：{e['scoring']}\n  {e['sourceUrl']}\n")
