"""Offline publication checks: schema, task boundaries, local links and generated index."""
import hashlib
import json
from pathlib import Path
import re
from build_index import ROOT, validate, render

data=json.loads((ROOT/'data/benchmarks.json').read_text(encoding='utf8'))
count=validate(data)
assert (ROOT/'INDEX.md').read_text(encoding='utf8')==render(data)
pack=json.loads((ROOT/'data/modeltest-tasks.json').read_text(encoding='utf8'))
assert len(pack['packs'])==3
assert re.fullmatch('[0-9a-f]{40}',pack['sourceCommit'])
ids=[]
for p in pack['packs']:
    assert re.fullmatch('[0-9a-f]{64}',p['sha256'])
    assert '/'+pack['sourceCommit']+'/' in p['sourceUrl']
    for task in p['tasks']:
        ids.append(task['id'])
        assert not {'models','records','tokenUsage','account','balance','apiKey','outputs'} & task.keys()
assert len(ids)==len(set(ids))==16
assert all(t['status']=='unmeasured' for t in pack['packs'][1]['tasks'])
broken=[];secret_hits=[]
patterns=[rb'-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----',rb'\bgh[pousr]_[A-Za-z0-9]{30,}\b',rb'\bsk-(?:proj-|ant-|or-v1-)?[A-Za-z0-9_-]{24,}\b']
files=[p for p in ROOT.rglob('*') if p.is_file() and not any(x in {'.git','results','private','__pycache__'} for x in p.relative_to(ROOT).parts)]
for p in files:
    b=p.read_bytes()
    if any(re.search(pattern,b) for pattern in patterns):secret_hits.append(str(p.relative_to(ROOT)))
    if p.suffix=='.md':
        for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',b.decode('utf8')):
            if '://' in target or target.startswith('#'):continue
            destination=(p.parent/target.split('#')[0]).resolve()
            if not destination.is_relative_to(ROOT) or not destination.exists():broken.append((str(p.relative_to(ROOT)),target))
assert not broken,broken
assert not secret_hits,secret_hits
assert json.loads((ROOT/'templates/run-record.json').read_text(encoding='utf8'))['status']=='unrun'
print(json.dumps({'entries':count,'publicTasks':len(ids),'localFilesChecked':len(files),'brokenLocalLinks':0,'secretPatternHits':0,'modelCalls':0}))
