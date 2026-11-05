import hashlib, importlib.util, json, re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
root = Path.cwd().resolve()
helper = root / '.caprmedio_caprmedio/03_plan/CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/model-header-content-20261103/integration/adopt.py'
spec = importlib.util.spec_from_file_location('model_adopt', helper)
a = importlib.util.module_from_spec(spec); spec.loader.exec_module(a); a.ROOT = root
core = Path('.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL')
source = root / core / '07_delivery/CA-D-479-CORE_META_MODEL-ENG_DECISION--use-stable-headings-for-atom-body-properties.md'
out = root / '.caprmedio_caprmedio/02_analysis/draft/epic-completion-20261104/application/content-order-20261105'
raw = source.read_bytes(); meta, body = a.read(raw)
old = 'For ordinary RMED, carry one `## Summary` and one `## Claim` as sibling Properties, optionally followed by `## Semantics` and `## Details` in that order. Claim has no direct value and contains one or both `### Formal Claim` and `### Prose Claim`, with unique sibling names. Formal Claim contains a CFEL-labelled code fence; Prose Claim contains ordinary Markdown. Omit absent optional Properties. Do not duplicate Claim in frontmatter.'
new = 'Serialize declared Content Properties in this order: `## Summary`, `## Claim`, `## Semantics`, then `## Details`. Omit absent optional Properties. Within Claim, place `### Prose Claim` before `### Formal Claim` when present. For a Workflow, place `### Mermaid Scheme` first within Claim, before Prose Claim and Formal Claim when present.\n\nFor ordinary RMED, carry one `## Summary` and one `## Claim` as sibling Properties. Claim has no direct value and contains one or both `### Prose Claim` and `### Formal Claim`, with unique sibling names. Formal Claim contains a CFEL-labelled code fence; Prose Claim contains ordinary Markdown. Do not duplicate Claim in frontmatter.'
assert body.count(old) == 1
body = body.replace(old, new)
with a.atom_identity_lock(root):
    paths = list(a.control_root(root).rglob('CA-D-479*.md'))
    versions = [int(m[1]) for p in paths if (m := re.search(rb'(?m)^version:\s*(\d+)\s*$', p.read_bytes()))]
    version = max(versions) + 1
    filename = f'CA-D-479@{version}-draft-CORE_META_MODEL-ENG_DECISION--use-stable-headings-for-atom-body-properties.md'
    relative = core / '07_delivery/draft'
    target = a.checked_path((relative / filename).as_posix())
    meta.pop('current_scope_unit', None); meta.pop('claim_target_scope_unit', None)
    meta.update({'status':'Draft', 'version':version, 'updated_at':datetime.now(ZoneInfo('Asia/Tbilisi')).strftime('%Y-%m-%d %H:%M:%S %z'), 'relations':{'IS_CONTAINED_BY':{'scope_unit':'CA-SU-11'}}, 'carrier_destination':{'file':{'name':filename, 'path':relative.as_posix()}}})
    data = a.render(meta, body)
    with target.open('xb') as f: f.write(data)
    assert target.read_bytes() == data and a.summary(a.read(data)[1]) == a.summary(a.read(raw)[1])
    receipt = {'source':str(source.relative_to(root)), 'source_sha256':hashlib.sha256(raw).hexdigest(), 'draft':str(target.relative_to(root)), 'draft_sha256':hashlib.sha256(data).hexdigest(), 'native_workflow_admission':False, 'journal_append':False}
    (out / 'delivery-receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))
