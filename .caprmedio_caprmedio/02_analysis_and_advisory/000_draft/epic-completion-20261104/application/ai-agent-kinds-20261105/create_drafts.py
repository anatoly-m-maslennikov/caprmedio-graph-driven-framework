import hashlib, importlib.util, json, re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

root = Path.cwd().resolve()
helper = root / '.caprmedio_caprmedio/03_plan/CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/model-header-content-20261103/integration/adopt.py'
spec = importlib.util.spec_from_file_location('model_adopt', helper)
a = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)
a.ROOT = root
out = root / '.caprmedio_caprmedio/02_analysis/draft/epic-completion-20261104/application/ai-agent-kinds-20261105'
relative = Path('.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft')
items = [('ai-agent', 'AI Agent', 'Node/Continuant/Actor/AI Agent'), ('subagent', 'Subagent', 'Node/Continuant/Actor/AI Agent//Subagent'), ('main-agent', 'Main Agent', 'Node/Continuant/Actor/AI Agent//Main Agent')]
receipt = out / 'creation-receipt.json'
if receipt.exists():
    raise RuntimeError('already created')
with a.atom_identity_lock(root):
    retained = list(a.control_root(root).rglob('CA-[RMED]-*.md'))
    maximum = max(int(m[1]) for p in retained if (m := re.match(r'CA-R-(\d+)', p.name)))
    rows = []
    now = datetime.now(ZoneInfo('Asia/Tbilisi')).strftime('%Y-%m-%d %H:%M:%S %z')
    for slug, name, subject in items:
        while True:
            maximum += 1
            identity = f'CA-R-{maximum}'
            if not a.atom_id_has_preserved_history_evidence(root, identity):
                break
        filename = f'{identity}@1-draft-CORE_META_MODEL-DECLARATION--declare-{slug}.md'
        target = a.checked_path((relative / filename).as_posix())
        meta = {'atom_id': identity, 'status': 'Draft', 'subjects': {'active': f'CAPRMEDIO_MODEL <+ {subject}'}, 'version': 1, 'relations': {'IS_CONTAINED_BY': {'scope_unit': 'CA-SU-11'}}, 'tier': 3, 'role': 'Requirement', 'form': 'Declaration', 'updated_at': now, 'carrier_destination': {'file': {'name': filename, 'path': relative.as_posix()}}}
        body = '\n\n' + (out / f'{slug}.preview.txt').read_text()
        data = a.render(meta, body)
        with target.open('xb') as f:
            f.write(data)
        assert target.read_bytes() == data
        read_meta, read_body = a.read(data)
        assert read_meta == meta and a.summary(read_body) == f'Declare {name}'
        rows.append({'atom_id': identity, 'path': str(target.relative_to(root)), 'sha256': hashlib.sha256(data).hexdigest(), 'active_subject': meta['subjects']['active']})
    receipt.write_text(json.dumps({'route': 'user-authorized manual Draft creation', 'native_workflow_admission': False, 'journal_append': False, 'outputs': rows}, indent=2) + '\n')
print(json.dumps(rows, indent=2))
