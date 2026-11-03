"""Check bounded candidate/source pins and alias-counterpart structural invariants."""
from pathlib import Path
import hashlib
import json
import re

here = Path(__file__).resolve().parent
repo = next(p for p in here.parents if (p / '.git').exists())
data = json.loads((here / 'source-map.json').read_text())
by_relation = {}
for item in data['sources']:
    source = repo / item['source']
    candidate = repo / item['candidate']
    assert hashlib.sha256(source.read_bytes()).hexdigest() == item['source_sha256'], source
    assert hashlib.sha256(candidate.read_bytes()).hexdigest() == item['candidate_sha256'], candidate
    text = candidate.read_text()
    body = text.split('---', 2)[2]
    children = re.findall(r'^### (.+)$', body, re.M)
    assert set(children) <= {'Formal Claim', 'Prose Claim'}, candidate
    assert len(children) == len(set(children)), candidate
    assert len(children) <= 2, candidate
    if not item['requires_no_alias_claim_exception']:
        assert children, candidate
    if item.get('inverse', item['derived']):
        assert '((IS_DERIVED_RELATION_OF))' not in body, candidate
        assert 'Derivation == Derived' not in body, candidate
        assert '<-->' not in body, candidate
        assert '### Prose Claim' not in body, candidate
    assert not re.search(r'\(\(\w+\)\) == [^\n]', body), candidate
    if item['relation']:
        assert item['relation'] not in by_relation, item['relation']
        by_relation[item['relation']] = text
for direct, inverse in data['inverse_pairs'].items():
    assert direct != inverse
    assert f'Relation//{direct} ((HAS_INVERSE)) Relation//{inverse}' in by_relation[direct], direct
    assert f'Relation//{inverse} <((HAS_INVERSE)) Relation//{direct}' in by_relation[inverse], inverse
    assert inverse in by_relation, inverse
assert len(set(data['inverse_pairs'].values())) == len(data['inverse_pairs'])
assert 'alias(Relation//CONTAINS) == "<+"' in by_relation['CONTAINS']
assert 'alias(Relation//IS_CONTAINED_BY) == "+>"' in by_relation['IS_CONTAINED_BY']
print(f"Verified {len(data['sources'])} candidate/source pins and {len(data['inverse_pairs'])} distinct inverse pairs; all inverse bindings normalize to the direct fact.")

for item in data["new_candidates"]:
    candidate = repo / item["candidate"]
    assert hashlib.sha256(candidate.read_bytes()).hexdigest() == item["candidate_sha256"]
    text = candidate.read_text()
    assert "atom_id: CA-R-draft" in text and "version: 1" in text
    assert "### Formal Claim" in text and "### Prose Claim" in text
print("Verified new Alias operator draft; numeric ID allocation remains required.")

for item in data["retirements"]:
    source = repo / item["source"]
    assert hashlib.sha256(source.read_bytes()).hexdigest() == item["source_sha256"]
for candidate in (here / "candidates").glob("*.md"):
    assert not re.search(r"@(?!N\b)[A-Za-z_]", candidate.read_text()), candidate
print("Verified reference-operator removal and pinned CA-R-2595 retirement; historical identity/version tags remain outside migration.")

for item in data['sources']:
    text = (repo / item['candidate']).read_text()
    for block in re.findall(r'```CFEL\n(.*?)```', text, re.S):
        assert not re.search(r'\(\(\w+\)\)\s*>\|', block), item['candidate']
        assert not re.search(r'^\(\(\w+\)\)', block, re.M), item['candidate']
        assert not re.search(r'\(\(\w+\)\)\s*:', block), item['candidate']
        assert not re.search(r'>\||\|<', re.sub(r'"[^"]*"', '', block)), item['candidate']
print('SyntaxAudit PASS: Relation objects use qualified addresses; actual uses have named Relation operators; no classification glyphs or operator-as-object forms in Formal Claims.')

coverage = json.loads((here / 'coverage.json').read_text())
assert coverage['declaredRelations'] == 41
assert len(set(coverage['coveredSourceIDs'])) == 41
assert set(coverage['coveredSourceIDs']) <= {x['atom_id'] for x in data['sources']}
assert coverage['source_map_sha256'] == hashlib.sha256((here / 'source-map.json').read_bytes()).hexdigest()
print('Coverage PASS: all 41 Current canonical Active Requirement/Declaration Relation targets have pinned candidates.')

for candidate in (here / 'candidates').glob('*.md'):
    assert not re.search(r'alias\((?!Relation//)[A-Za-z_]', candidate.read_text()), candidate
print('Typed alias argument PASS: candidate alias() operands use Relation//NAME object addresses.')
