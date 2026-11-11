"""Apply the reviewed Property-order model and its direct schema prerequisites."""
from pathlib import Path
import contextlib
import importlib.util
import json
import re
from datetime import datetime
from zoneinfo import ZoneInfo

ROOT = Path.cwd()
HERE = Path(__file__).resolve().parent
CONTROL = ROOT / '.caprmedio_caprmedio'
CORE = CONTROL / 'CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL'


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


n = module('property_order_adoption', CONTROL / '03_plan/CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/model-header-content-20261103/integration/adopt.py')
n.ROOT = ROOT
order = module('property_order_transform', HERE / 'migration/prepare_order.py')


def current(identity):
    role = '07_delivery' if '-D-' in identity else '04_requirement'
    found = list((CORE / role).glob(identity + '-*.md'))
    assert len(found) == 1, (identity, found)
    return found[0]


def format_source(meta, body):
    ranked = {key: value for key in order.HEADER_ORDER if (value := meta.get(key)) is not None and key in meta}
    ranked.update({key: value for key, value in meta.items() if key not in ranked})
    if ranked.get('relations') == {}:
        ranked.pop('relations')
    body, hold, _, _, check = order.reorder_content(body)
    assert not hold and check['preservation_check'] == 'PASS'
    return n.render(ranked, body)


def main():
    target = HERE / 'model-application'
    target.mkdir(exist_ok=True)
    assert not (target / 'adoption-plan.json').exists()
    candidates = {}
    inputs = []

    def accept(row):
        source = ROOT / row['source']
        preview = ROOT / row['preview']
        assert n.sha(source.read_bytes()) == row['source_sha256'], source
        assert n.sha(preview.read_bytes()) == row['preview_sha256'], preview
        source_meta, source_body = n.read(source.read_bytes())
        _, body = n.read(preview.read_bytes())
        assert n.summary(body) == n.summary(source_body), source
        candidates[source] = (source_meta, body)
        inputs.append(row)

    rel = json.loads((HERE / 'relation/manifest.json').read_text())
    for row in rel['sources']:
        if 'source' in row:
            accept(row)
    prereq = json.loads((HERE / 'relation/prerequisites/manifest.json').read_text())
    for row in prereq['sources']:
        if 'preview' in row:
            accept(row)
    layout = json.loads((HERE / 'layout/manifest.json').read_text())
    by_id = {row['id']: row for row in layout['outputs']}
    for key in ('R2719', 'R2498', 'R2500', 'R2961', 'D479', 'R2709', 'D657-current', 'D657-draft'):
        accept(by_id[key])

    # Add only the order chain and new name to Current Header, not unrelated Draft edits.
    header_path = current('CA-R-2719')
    meta, body = n.read(header_path.read_bytes())
    if 'Ref ID' not in body:
        body = body.replace('in(ID, ', 'in(ID, Ref ID, ')
    header_preview = n.read((ROOT / by_id['R2719']['preview']).read_bytes())[1]
    chain = re.search(r'Atom.Header.ID ;>[\s\S]*?(?=\n```)', header_preview)[0]
    body = body.replace('\n```\n', ';\n\n' + chain + '\n```\n', 1)
    candidates[header_path] = (meta, body)

    relation_path = current('CA-R-2709')
    meta, body = n.read(relation_path.read_bytes())
    replacement_body = n.read((ROOT / by_id['R2709']['preview']).read_bytes())[1]
    assert n.summary(body) == n.summary(replacement_body)
    candidates[relation_path] = (meta, replacement_body)

    delivery_path = current('CA-D-479')
    meta, body = n.read(delivery_path.read_bytes())
    sentence = ('Serialize Content headings in their declared sibling order. Omit absent optional Properties. '
                'Other admitted sibling Properties follow the ordered Properties, with no required order among them. '
                'For a declared Workflow Claim, Mermaid Scheme precedes Prose Claim, which precedes Formal Claim.\n\n')
    marker = 'Applicability: Structured Main Content of Markdown Atom carriers.\n\n'
    assert marker in body
    body = body.replace(marker, marker + sentence, 1)
    candidates[delivery_path] = (meta, body)

    # The renamed Container replaces the obsolete storage-only containment Properties.
    promotions = []
    for identity in ('CA-R-2955', 'CA-R-2951', 'CA-R-2779', 'CA-R-2783', 'CA-R-2784'):
        found = list((CORE / '04_requirement/draft').glob(identity + '@*-*.md'))
        assert len(found) == 1, (identity, found)
        path = found[0]
        meta, body = n.read(path.read_bytes())
        if identity == 'CA-R-2951':
            meta['form'] = 'Relation Declaration'
        promotions.append((path, meta, body))
    retirements = [current(identity) for identity in ('CA-R-2698', 'CA-R-2699', 'CA-R-2700')]

    # Keep the direct consumers on the same logical storage path.
    snapshot = json.loads((CONTROL / '02_analysis/draft/epic-completion-20261104/coverage/ordered-source-migration-20261105/property-audit/snapshot.json').read_text())
    for row in snapshot['carriers']:
        path = ROOT / row['path']
        if not path.exists() or path in retirements:
            continue
        meta, body = candidates.get(path, n.read(path.read_bytes()))
        changed = body.replace('Header.Relations.IS_CONTAINED_BY', 'Header.Container')
        topics = meta.get('topics', {})
        updated_topics = dict(topics) if isinstance(topics, dict) else topics
        if isinstance(topics, dict):
            for key, value in topics.items():
                if isinstance(value, str):
                    updated_topics[key] = value.replace('Header.Relations.IS_CONTAINED_BY', 'Header.Container')
                elif isinstance(value, list):
                    updated_topics[key] = [item.replace('Header.Relations.IS_CONTAINED_BY', 'Header.Container') if isinstance(item, str) else item for item in value]
        if changed != body or updated_topics != topics:
            meta = dict(meta, topics=updated_topics)
            candidates[path] = (meta, changed)

    operations, outputs = {}, []
    now = datetime.now(ZoneInfo('Asia/Tbilisi')).strftime('%Y-%m-%d %H:%M:%S %z')

    def operation(path, after):
        relative = path.relative_to(ROOT).as_posix()
        assert relative not in operations, relative
        before = path.read_bytes() if path.exists() else None
        operations[relative] = {'path': relative, 'before': before.decode() if before is not None else None,
                               'before_sha256': n.sha(before) if before is not None else None,
                               'after': after.decode() if after is not None else None,
                               'after_sha256': n.sha(after) if after is not None else None}

    def archive(path):
        raw = path.read_bytes()
        meta, _ = n.read(raw)
        target_path = path.parent / 'archive' / f'{path.stem}@{meta["version"]}.md'
        assert not target_path.exists(), target_path
        operation(target_path, raw)

    with n.atom_identity_lock(ROOT):
        retained = list(CONTROL.rglob('CA-[RMED]-*.md'))
        maximum = max(int(match[1]) for path in retained if (match := re.match(r'CA-R-(\d+)', path.name)))
        versions = {}
        for path in retained:
            identity = re.match(r'(CA-[RMED]-\d+)(?!\d)', path.name)
            version = re.search(rb'(?m)^version:\s*(\d+)\s*$', path.read_bytes())
            if identity and version:
                versions[identity[1]] = max(versions.get(identity[1], 0), int(version[1]))

        def allocate():
            nonlocal maximum
            while True:
                maximum += 1
                identity = f'CA-R-{maximum}'
                if not n.atom_id_has_preserved_history_evidence(ROOT, identity):
                    return identity

        def install(meta, body, identity=None):
            identity = identity or allocate()
            form = meta.get('form', 'Rule')
            slug = re.sub(r'[^a-z0-9]+', '-', n.summary(body).lower()).strip('-')
            path = CORE / '04_requirement' / f'{identity}-CORE_META_MODEL-{form.upper().replace(" ", "_")}--{slug}.md'
            assert not path.exists(), path
            meta.update(atom_id=identity, ref_id=identity, status='Active', version=1, updated_at=now,
                        container={'scope_unit': 'CA-SU-11'}, role='Requirement', tier=3)
            meta['carrier_destination'] = {'file': {'name': path.name, 'path': path.parent.relative_to(ROOT).as_posix()}}
            operation(path, format_source(meta, body))
            outputs.append({'atom_id': identity, 'path': path.relative_to(ROOT).as_posix(), 'version': 1})

        for path, (meta, body) in candidates.items():
            if meta['status'] != 'Draft':
                archive(path)
                meta.update(version=versions[meta['atom_id']] + 1, updated_at=now, ref_id=meta['atom_id'])
            operation(path, format_source(meta, body))
            outputs.append({'atom_id': meta['atom_id'], 'path': path.relative_to(ROOT).as_posix(), 'version': meta['version']})
        for path, meta, body in promotions:
            install(meta, body, meta['atom_id'])
            operation(path, None)
        for path in retirements:
            archive(path)
            operation(path, None)
        relation_meta, relation_body = n.read((HERE / 'relation/IS_ORDERED_RIGHT_AFTER.unallocated.preview.txt').read_bytes())
        install(relation_meta, relation_body)
        ref_body = (HERE / 'layout/R-UNALLOCATED-ref-id.preview.txt').read_text()
        install({'topics': {'main_subject': 'CAPRMEDIO_MODEL <+ Atom.Header.Ref ID'}, 'form': 'Declaration'}, '\n' + ref_body)
        default_body = (HERE / 'layout/R-UNALLOCATED-property-order-default.preview.txt').read_text()
        install({'topics': {'main_subject': 'CAPRMEDIO_MODEL <+ Node.**'}, 'form': 'Rule'}, '\n' + default_body)
        plan = {'status': 'PREPARED_REVIEWED_MODEL_BINDING', 'native_workflow_admission': False, 'journal_append': False,
                'prepared_at': now, 'review': 'permissions/property-order-preview-review-20261105.json',
                'source_inputs': inputs, 'outputs': outputs, 'operations': list(operations.values())}
        (target / 'adoption-plan.json').write_text(json.dumps(plan, indent=2) + '\n')
        n.HERE = target
        outer = n.atom_identity_lock
        n.atom_identity_lock = lambda _: contextlib.nullcontext()
        try:
            n.apply()
        finally:
            n.atom_identity_lock = outer
    print(json.dumps({'outputs': len(outputs), 'operations': len(operations)}, indent=2))


if __name__ == '__main__':
    main()
