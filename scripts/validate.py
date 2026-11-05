"""Validate local research tables; no network access or third-party dependencies."""
from pathlib import Path
import csv, json, re
ROOT = Path(__file__).resolve().parents[1]
def rows(name):
    with (ROOT / 'data' / name).open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))
sources=json.loads((ROOT/'sources/registry.json').read_text(encoding='utf-8'))
ids={s['source_id'] for s in sources}
assert len(ids)==len(sources)
components=rows('ownership_components_2025.csv')
for r in rows('ownership_comparison_2025.csv'):
    assert int(r['h100e_sum_of_component_medians']) == sum(int(c['h100e_median']) for c in components if c['owner']==r['owner'])
for r in rows('lab_usage_2025.csv'):
    assert 0 < float(r['h100e_p5']) <= float(r['h100e_median']) <= float(r['h100e_p95'])
    assert r['observation_date']=='2025-12-31'
relationships=rows('relationships.csv')
assert len({r['relationship_id'] for r in relationships})==len(relationships)
for file in (ROOT/'data').glob('*.csv'):
    with file.open(encoding='utf-8',newline='') as f:
        reader=csv.DictReader(f)
        for r in reader:
            assert None not in r, file
            for key in ['source_id','source_ids']:
                if key in r:
                    assert set(r[key].split(';')) <= ids, (file,r)
for file in ROOT.rglob('*.md'):
    for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)',file.read_text(encoding='utf-8')):
        if '://' not in link and not link.startswith('#'):
            assert (file.parent/link.split('#')[0]).exists(), (file,link)
print(f'PASS: {len(sources)} sources; {len(relationships)} relationships; ownership derivations; lab intervals; CSV structure; local file links.')
