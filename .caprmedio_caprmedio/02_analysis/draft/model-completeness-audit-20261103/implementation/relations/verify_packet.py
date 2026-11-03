"""Verify prospective Relation fixes without modifying Current carriers."""
from pathlib import Path
import hashlib
import json
import re

here = Path(__file__).resolve().parent
repo = next(p for p in here.parents if (p / '.git').exists())
manifest = json.loads((here / 'source-candidate-map.json').read_text())
texts = {}
for item in manifest['sources']:
    source = repo / item['source_path']
    candidate = repo / item['candidate_path']
    assert candidate.suffix == '.txt'
    assert hashlib.sha256(source.read_bytes()).hexdigest() == item['source_sha256'], source
    assert hashlib.sha256(candidate.read_bytes()).hexdigest() == item['candidate_sha256'], candidate
    text = candidate.read_text()
    body = text.split('---', 2)[2]
    summary = re.search(r'## Summary\s*\n(.*?)(?=\n## |\Z)', body, re.S)[1].strip()
    assert summary == item['candidate_summary']
    if not item['fresh_id_required']:
        assert summary == item['source_summary']
    else:
        assert 'atom_id: CA-R-draft' in text and 'version: 1' in text
    children = re.findall(r'^### (.+)$', body, re.M)
    assert 1 <= len(children) <= 2 and len(children) == len(set(children))
    assert set(children) <= {'Formal Claim', 'Prose Claim'}
    if 'Formal Claim' in children:
        assert children[0] == 'Formal Claim'
    assert 'IS_DEFINED_BY' not in text
    texts[item['source_atom_id']] = text
assert 'Entity Definition' in texts['CA-R-2278']  # Explicit retired-form distinction, not a surviving qualification.
assert 'Requirement role and Declaration form' in texts['CA-R-2278']
assert 'Relation//IS_DECLARED_BY ((IS_DERIVED_RELATION_OF)) Relation//GOVERNS' in texts['CA-R-2279']
assert 'Relation//GOVERNS ((HAS_INVERSE)) Relation//IS_DECLARED_BY' not in texts['CA-R-2279']
assert 'not an unconditional HAS_INVERSE' in texts['CA-R-2279']
assert 'A Declaration addresses a Node' not in texts['CA-R-2618']
assert 'for a Declaration it is a Node' not in texts['CA-R-2618']
assert '(Node, Node.**)' not in texts['CA-R-2618']
assert 'Every count concerns' not in texts['CA-R-2588']
assert 'Either slot may be omitted and remains unspecified' in texts['CA-R-2588']
assert 'For a derived inverse bound by HAS_INVERSE' in texts['CA-R-2486']
assert 'qualified or other non-inverse derived view' in texts['CA-R-2486']
print('PASS: seven exact source/candidate pins; preserved stable Summaries; new identity flagged; qualified derivation, entity endpoints, independent count slots and inverse-only minimal policy retained.')

assert 'governed Implementation Carrier' in texts['CA-R-1020']
assert 'specification Atom it implements' in texts['CA-R-1020']
assert 'evidence Carrier' in texts['CA-R-1021']
assert 'Evaluation or Implementation Carrier it supports' in texts['CA-R-1021']
assert 'Carrier//$evidence_carrier ((evidence_for)) Carrier//$supported_carrier' in texts['CA-R-1021']
relocation = manifest['endpoint_permission_relocation']
assert hashlib.sha256((repo / relocation['source_path']).read_bytes()).hexdigest() == relocation['source_sha256']
print('PASS: R1958 exact source pin and both relocated Relation endpoint restrictions preserved before source-owner removal.')

assert "Carrier//$implementation_carrier ((implementation_of)) Atom//$specification_atom" in texts["CA-R-1020"]
