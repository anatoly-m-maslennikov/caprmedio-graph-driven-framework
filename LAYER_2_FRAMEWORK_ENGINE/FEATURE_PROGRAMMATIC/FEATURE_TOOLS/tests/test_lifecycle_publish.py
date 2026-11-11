from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from ATOM_LIFECYCLE import effects, publish
from ATOM_LIFECYCLE.source import SourcePin
from lifecycle_placement_test_support import with_fixture_placement


ROOT = Path('/project')
DRAFT = b'''---
atom_id: CA-R-9
ref_id: CA-R-9@1-draft
role: Requirement
form: Rule
status: Draft
version: 1
container:
  scope_unit: TEST
relations:
  is_replacement_for: [CA-R-1, CA-R-1, CA-R-2]
---
## Summary

Example
'''


def pin(atom_id, raw=DRAFT, status='Active', version=1, ref=None):
    from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier
    metadata = parse_carrier(raw, ROOT / 'a.md').metadata
    return SourcePin(ROOT / (atom_id + '.md'), atom_id, ref or atom_id, version, status, 'digest', raw, metadata)


def run_case(*, changed=False, fail_second=False, destination=ROOT / 'current.md'):
    draft = pin('CA-R-9', status='Draft', ref='CA-R-9@1-draft')
    targets = {name: pin(name) for name in ('CA-R-1', 'CA-R-2')}
    selection = SimpleNamespace(root=destination.parent)
    model = SimpleNamespace(allowed=lambda role, form: {'Draft', 'Active', 'Archived'})
    archives = []

    def select(selection, ref, *, expected_version):
        item = draft if ref == draft.ref_id else targets[ref]
        if changed and ref == 'CA-R-2':
            return SourcePin(item.path, item.atom_id, item.ref_id, item.version, item.status, 'bad', item.raw, item.metadata)
        return item

    def archive(selection, model, params):
        archives.append(params['target']['ref_id'])
        if fail_second and len(archives) == 2:
            return {'effects': [], 'warnings': [], 'errors': [{'code': 'failed'}]}
        return {'effects': [{'operation': 'archive', 'target': archives[-1]}], 'warnings': [], 'errors': []}

    with (patch.object(publish, 'read_target', return_value=draft),
          patch.object(publish, 'resolve_replacement', side_effect=lambda selection, ref: targets[ref]),
          patch.object(publish, '_destination', return_value=destination),
          patch.object(publish, '_current_collision', return_value=False),
          patch.object(publish, 'validate_candidate'),
          patch.object(publish.source, 'select_source', side_effect=select),
          patch('ATOM_LIFECYCLE.state_actions.archive_atom', side_effect=archive),
          patch.object(publish, 'write_destination', return_value=effects.Result(effects=[{'operation': 'create'}])) as write,
          patch.object(publish.effects, 'remove', return_value=effects.Result(effects=[{'operation': 'remove'}])) as remove):
        result = publish.promote_draft(selection, model, {'target': {'ref_id': draft.ref_id, 'version': 1}, 'targetStatus': 'Active'})
    return result, archives, write.call_count, remove.call_count


@with_fixture_placement
def test_many_to_one_archives_each_target_once():
    result, archives, writes, removes = run_case()
    assert not result['errors']
    assert archives == ['CA-R-1', 'CA-R-2']
    assert (writes, removes) == (1, 1)


@with_fixture_placement
def test_changed_digest_stops_before_any_archive():
    result, archives, writes, removes = run_case(changed=True)
    assert result['errors'] and archives == []
    assert result['effects'] == [] and (writes, removes) == (0, 0)


@with_fixture_placement
def test_occupied_successor_stops_before_any_archive():
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as directory:
        occupied = Path(directory) / 'current.md'
        occupied.mkdir()
        result, archives, writes, removes = run_case(destination=occupied)
        assert result['outcome'] == 'needs_input', result
        assert 'occupied' in result['requested_input']['target']['error']
        assert not result['effects'] and not archives and (writes, removes) == (0, 0)


@with_fixture_placement
def test_archive_failure_reports_partial_effects_and_stops():
    result, archives, writes, removes = run_case(fail_second=True)
    assert result['errors'] and archives == ['CA-R-1', 'CA-R-2']
    assert len(result['effects']) == 1 and (writes, removes) == (0, 0)


def test_pending_promotion_backend_failures_keep_prior_effects():
    from contextlib import contextmanager
    from ATOM_LIFECYCLE import backend
    from lifecycle_placement_test_support import fixture_rules

    pending = publish.PromotionPending(ROOT, None, None, (), 'Active', ({'operation': 'archive'},), ('warning',))
    missing = backend.execute(SimpleNamespace(root=ROOT), SimpleNamespace(), 'atom_lifecycle_update', {},
                              pending_promotion=pending)
    assert missing['outcome'] == 'failed' and missing['effects'] == list(pending.effects)
    assert missing['warnings'] == list(pending.warnings)

    @contextmanager
    def busy(_root):
        raise BlockingIOError()
        yield

    model = SimpleNamespace(candidate_schema=SimpleNamespace(placement=fixture_rules()))
    with patch.object(backend, '_project_write_lock', busy):
        result = backend.execute(SimpleNamespace(root=ROOT), model, 'atom_lifecycle_update', {},
                                 pending_promotion=pending)
    assert result['outcome'] == 'failed' and result['errors'][0]['code'] == 'project_busy'
    assert result['effects'] == list(pending.effects) and result['warnings'] == list(pending.warnings)


@with_fixture_placement
def test_same_identity_promotion_requires_predecessor_summary_and_role():
    base = DRAFT.replace(b'CA-R-9@1-draft', b'CA-R-9@2-draft').replace(
        b'version: 1', b'version: 2').replace(
        b'is_replacement_for: [CA-R-1, CA-R-1, CA-R-2]', b'is_replacement_for: []')
    predecessor_raw = base.replace(b'CA-R-9@2-draft', b'CA-R-9').replace(
        b'status: Draft', b'status: Active').replace(b'version: 2', b'version: 1')
    selection = SimpleNamespace(root=ROOT)
    model = SimpleNamespace(allowed=lambda role, form: {'Draft', 'Active', 'Archived'})
    for predecessor_status in ('Active', 'Archived'):
        for change in ('unchanged', 'summary', 'role'):
            raw = base
            if change == 'summary':
                raw = raw.replace(b'Example', b'Changed')
            if change == 'role':
                raw = raw.replace(b'role: Requirement', b'role: Method')
            draft = pin('CA-R-9', raw=raw, status='Draft', version=2, ref='CA-R-9@2-draft')
            ref = 'CA-R-9@1' if predecessor_status == 'Archived' else 'CA-R-9'
            predecessor = pin('CA-R-9', raw=predecessor_raw, status=predecessor_status, version=1, ref=ref)
            def select(_selection, selected, *, expected_version):
                return draft if selected == draft.ref_id else predecessor

            with (patch.object(publish, 'read_target', return_value=draft),
                  patch.object(publish, 'resolve_replacement', return_value=predecessor),
                  patch.object(publish, '_destination', return_value=ROOT / 'current.md'),
                  patch.object(publish, 'validate_candidate'),
                  patch.object(publish.source, 'select_source', side_effect=select),
                  patch('ATOM_LIFECYCLE.state_actions.archive_atom', return_value={
                      'effects': [{'operation': 'archive'}], 'warnings': [], 'errors': []}) as archive,
                  patch.object(publish, 'write_destination', return_value=effects.Result(effects=[{'operation': 'create'}])) as write,
                  patch.object(publish.effects, 'remove', return_value=effects.Result(effects=[{'operation': 'remove'}])) as remove):
                result = publish.promote_draft(selection, model, {
                    'target': {'ref_id': draft.ref_id, 'version': 2}, 'targetStatus': 'Active'})
            if change == 'unchanged':
                assert not result['errors'] and result['outcome'] == 'completed', result
                assert (write.call_count, remove.call_count) == (1, 1)
                assert archive.call_count == (predecessor_status == 'Active')
            else:
                assert result['outcome'] == 'needs_input' and not result['effects'], result
                assert (archive.call_count, write.call_count, remove.call_count) == (0, 0, 0)


@with_fixture_placement
def test_composed_update_preserves_status_and_version():
    import tempfile
    from project_selection import resolve_project
    from scope_declaration_test_support import write_scope_unit_declarations

    scratch = Path(__file__).resolve().parents[4] / '.caprmedio_tmp/CA-P-2791/CA-P-2934/publish'
    scratch.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=scratch) as directory:
        root = Path(directory)
        control = root / '.caprmedio_test'
        control.mkdir()
        (control / 'caprmedio_project_settings.toml').write_text(
            '[project]\nname="TEST"\n[artifacts.identity]\nproject_prefix="CA"\n'
            '[paths]\ncontrol_root=".caprmedio_test"\n')
        write_scope_unit_declarations(root, control_root=control, rows=[])
        selection = resolve_project(root)
        path = control / '04_requirement/CA-R-1-RULE--example.md'
        path.parent.mkdir()
        path.write_text('---\nidentity:\n  atom_id: CA-R-1\n  ref_id: CA-R-1\n'
                        'context:\n  container:\n    scope_unit: TEST\n  role: Requirement\n'
                        '  form: Rule\nstate:\n  status: Active\n  version: 2\n'
                        '  updated_at: 2026-01-01T00:00:00+00:00\n---\n## Summary\n\nExample\n')
        model = SimpleNamespace(allowed=lambda role, form: {'Draft', 'Active', 'Archived'})
        outcome = publish.update_atom(selection, model, {'sourceCurrent': {'ref_id': 'CA-R-1', 'version': 2},
                                                          'changes': {'body': '## Summary\n\nExample\n\nUpdated.\n'}})
        assert not outcome['errors'], outcome
        assert outcome['artifact']['version'] == 3
        assert outcome['artifact']['status'] == 'Active'
        assert (root / outcome['artifact']['path']).exists()
        assert 'status: active' in (root / outcome['artifact']['path']).read_text()
        assert not list(control.rglob('*-draft*.md'))
        assert list(control.rglob('CA-R-1@2-*.md'))
        next_outcome = publish.update_atom(selection, model, {'sourceCurrent': {'ref_id': 'CA-R-1', 'version': 3},
                                                               'changes': {'body': '## Summary\n\nExample\n\nUpdated again.\n'}})
        assert not next_outcome['errors'], next_outcome
        assert next_outcome['artifact']['status'] == 'Active'
        assert next_outcome['artifact']['version'] == 4
        request = {'sourceCurrent': {'ref_id': 'CA-R-1', 'version': 4},
                   'changes': {'body': '## Summary\n\nExample\n\nPending promotion.\n'}}
        with patch.object(publish, '_promote_draft', return_value={
                'outcome': 'needs_input', 'effects': [], 'errors': [], 'warnings': [],
                'requested_input': {'target': {'error': 'Destination is occupied.'}}}):
            pending = publish.update_atom(selection, model, request)
        assert pending['outcome'] == 'needs_input' and pending['pending_promotion']
        token = pending['pending_promotion']
        assert token.draft.path.exists() and token.predecessor.path.exists()
        assert token.predecessor.status == 'archived' and not path.exists()
        before = (token.draft.path.read_bytes(), token.predecessor.path.read_bytes())
        refused = publish.update_atom(selection, model, {'changes': {'summary': 'Other'}}, pending_promotion=token)
        assert refused['outcome'] == 'needs_input' and refused['pending_promotion'] is token
        assert refused['effects'] == pending['effects']
        assert before == (token.draft.path.read_bytes(), token.predecessor.path.read_bytes())
        resumed = publish.update_atom(selection, model, {}, pending_promotion=token)
        assert resumed['outcome'] == 'completed' and not resumed['errors'], resumed
        assert resumed['effects'][:len(pending['effects'])] == pending['effects']
        assert resumed['artifact']['version'] == 5 and not token.draft.path.exists()
        assert token.predecessor.path.read_bytes() == before[1]

        stale_request = {'sourceCurrent': {'ref_id': 'CA-R-1', 'version': 5},
                         'changes': {'body': '## Summary\n\nExample\n\nStale promotion.\n'}}
        with patch.object(publish, '_promote_draft', return_value={
                'outcome': 'needs_input', 'effects': [], 'errors': [], 'warnings': [],
                'requested_input': {'target': {'error': 'Destination is occupied.'}}}):
            stale = publish.update_atom(selection, model, stale_request)
        stale_token = stale['pending_promotion']
        stale_token.draft.path.write_bytes(stale_token.draft.path.read_bytes() + b'changed\n')
        failed = publish.update_atom(selection, model, {}, pending_promotion=stale_token)
        assert failed['outcome'] == 'failed' and failed['effects'] == stale['effects']
        assert stale_token.predecessor.path.exists() and stale_token.draft.path.exists()


@with_fixture_placement
def test_noop_update_and_same_identity_promotion_preserve_current():
    import tempfile
    from project_selection import resolve_project
    from scope_declaration_test_support import write_scope_unit_declarations
    from ATOM_LIFECYCLE import draft

    scratch = Path(__file__).resolve().parents[4] / '.caprmedio_tmp/CA-P-2791/CA-P-2934/publish'
    scratch.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=scratch) as directory:
        root = Path(directory)
        control = root / '.caprmedio_test'
        control.mkdir()
        (control / 'caprmedio_project_settings.toml').write_text(
            '[project]\nname="TEST"\n[artifacts.identity]\nproject_prefix="CA"\n'
            '[paths]\ncontrol_root=".caprmedio_test"\n')
        write_scope_unit_declarations(root, control_root=control, rows=[])
        selection = resolve_project(root)
        path = control / '04_requirement/CA-R-1-RULE--example.md'
        path.parent.mkdir()
        path.write_text('---\nidentity:\n  atom_id: CA-R-1\n  ref_id: CA-R-1\n'
                        'context:\n  container:\n    scope_unit: TEST\n  role: Requirement\n'
                        '  form: Rule\nstate:\n  status: Active\n  version: 2\n'
                        '  updated_at: 2026-01-01T00:00:00+00:00\n---\n## Summary\n\nExample\n')
        model = SimpleNamespace(allowed=lambda role, form: {'Draft', 'Active', 'Archived', 'Resolved'})
        original = path.read_bytes()
        selector = {'ref_id': 'CA-R-1', 'version': 2}
        update = publish.update_atom(selection, model, {'sourceCurrent': selector, 'changes': {}})
        assert update['outcome'] == 'completed', update
        assert update['effects'] == [] and path.read_bytes() == original
        assert not list(control.rglob('*-draft*.md')) and not list(control.rglob('CA-R-1@*.md'))

        created = draft.create_draft(selection, model, {'sourceCurrent': selector, 'changes': {}})
        assert not created['errors'], created
        draft_path = root / created['savedDraft']['path']
        result = publish.promote_draft(selection, model, {
            'target': {'ref_id': 'CA-R-1@3-draft', 'version': 3}, 'targetStatus': 'Active'})
        assert result['outcome'] == 'completed', result
        assert not draft_path.exists() and path.read_bytes() == original
        assert not list(control.rglob('CA-R-1@*.md'))
        assert len(result['effects']) == 1 and result['effects'][0]['operation'] == 'remove'

        # A changed requested Status is a promotion, not an unchanged Draft discard.
        created = draft.create_draft(selection, model, {'sourceCurrent': selector, 'changes': {}})
        assert not created['errors'], created
        result = publish.promote_draft(selection, model, {
            'target': {'ref_id': 'CA-R-1@3-draft', 'version': 3}, 'targetStatus': 'Resolved'})
        assert result['outcome'] == 'completed', result
        assert result['artifact']['version'] == 3 and result['artifact']['status'] == 'Resolved'
        assert list(control.rglob('CA-R-1@2-*.md'))

        # An explicit replacement remains actionable even when the body is unchanged.
        other = control / '04_requirement/CA-R-2-RULE--other.md'
        other.write_bytes(original.replace(b'CA-R-1', b'CA-R-2').replace(b'Example', b'Other'))
        created = draft.create_draft(selection, model, {
            'sourceCurrent': {'ref_id': 'CA-R-1', 'version': 3},
            'changes': {'relations': {'is_replacement_for': ['CA-R-2']}}})
        assert not created['errors'], created
        result = publish.promote_draft(selection, model, {
            'target': {'ref_id': 'CA-R-1@4-draft', 'version': 4}, 'targetStatus': 'Resolved'})
        assert result['outcome'] == 'completed', result
        assert result['artifact']['version'] == 4
        assert not other.exists() and list(control.rglob('CA-R-2@2-*.md'))
