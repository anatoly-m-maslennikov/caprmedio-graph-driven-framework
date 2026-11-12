"""Batch lifecycle operations run in order and report partial results."""
from contextlib import contextmanager, nullcontext
from pathlib import Path
import sys
from types import SimpleNamespace
from unittest.mock import Mock, patch

import pytest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
from ATOM_LIFECYCLE import backend  # noqa: E402
from ATOM_LIFECYCLE.common import InputError, result  # noqa: E402
from project_selection import ProjectSelection  # noqa: E402


@pytest.fixture
def runtime():
    selection = object.__new__(ProjectSelection)
    object.__setattr__(selection, 'root', Path('/project'))
    object.__setattr__(selection, 'settings', {'artifacts': {'identity': {'project_prefix': 'CA'}}})
    model = SimpleNamespace(candidate_schema=SimpleNamespace(placement=object()))
    locks = []

    @contextmanager
    def lock(root):
        locks.append(root)
        yield

    with patch.object(backend, '_project_write_lock', side_effect=lock), \
            patch.object(backend, 'bind_placement', side_effect=lambda _: nullcontext()):
        yield selection, model, locks


def entry(ref, *, status=None):
    value = {'target': {'ref_id': ref, 'version': 1}}
    if status is not None:
        value['targetStatus'] = status
    return value


@pytest.mark.parametrize('name,entries', [
    ('atom_lifecycle_archive', [entry('CA-R-1'), entry('CA-R-2')]),
    ('atom_lifecycle_promote_draft', [entry('CA-R-1@1-draft', status='Active'),
                                     entry('CA-R-2@1-draft', status='Done')]),
])
def test_batch_uses_one_lock_and_preserves_order(runtime, name, entries):
    selection, model, locks = runtime
    action = Mock(side_effect=lambda _s, _m, value: result(effects=[{'target': value['target']['ref_id']}]))
    with patch.dict(backend.ROUTES, {name: action}):
        output = backend.execute(selection, model, name, {'targets': entries})
    assert output['outcome'] == 'completed'
    assert locks == [selection.root]
    assert [call.args[2] for call in action.call_args_list] == entries
    assert [value['target'] for value in output['effects']] == [item['target']['ref_id'] for item in entries]
    assert [value['target'] for value in output['target_results']] == [item['target'] for item in entries]
    assert output['remaining_targets'] == []


@pytest.mark.parametrize('targets', [
    [],
    [entry('CA-R-1'), {'target': {'ref_id': 'CA-R-2', 'version': 0}}],
    [entry('CA-R-1'), {'target': {'ref_id': 'other', 'version': 1}}],
    [entry('CA-R-1'), entry('CA-R-2@1-draft')],
    [entry('CA-R-1'), {'target': {'ref_id': 'CA-R-2', 'version': 1}, 'targetStatus': 'Done'}],
])
def test_batch_rejects_malformed_entries_before_any_effect(runtime, targets):
    selection, model, _ = runtime
    action = Mock()
    with patch.dict(backend.ROUTES, {'atom_lifecycle_archive': action}):
        output = backend.execute(selection, model, 'atom_lifecycle_archive', {'targets': targets})
    assert output['outcome'] == 'needs_input'
    assert 'targets' in output['requested_input']
    action.assert_not_called()


def test_promotion_batch_rejects_current_reference_before_any_effect(runtime):
    selection, model, _ = runtime
    targets = [entry('CA-R-1@1-draft', status='Active'), entry('CA-R-2', status='Active')]
    action = Mock()
    with patch.dict(backend.ROUTES, {'atom_lifecycle_promote_draft': action}):
        output = backend.execute(selection, model, 'atom_lifecycle_promote_draft', {'targets': targets})
    assert output['outcome'] == 'needs_input'
    action.assert_not_called()


def test_batch_reports_effects_and_stops_on_failure(runtime):
    selection, model, _ = runtime
    targets = [entry('CA-R-1'), entry('CA-R-2'), entry('CA-R-3')]
    action = Mock(side_effect=[result(effects=[{'target': 'first'}]),
                               result(effects=[{'target': 'partial'}],
                                      errors=[{'code': 'effect_uncertain', 'message': 'write failed'}],
                                      remaining_targets=[{'ref_id': 'child', 'version': 1}])])
    with patch.dict(backend.ROUTES, {'atom_lifecycle_archive': action}):
        output = backend.execute(selection, model, 'atom_lifecycle_archive', {'targets': targets})
    assert output['outcome'] == 'failed'
    assert output['effects'] == [{'target': 'first'}, {'target': 'partial'}]
    assert output['remaining_targets'] == [targets[2]]
    assert output['target_results'][1]['remaining_targets'] == [{'ref_id': 'child', 'version': 1}]
    assert action.call_count == 2


def test_batch_reports_a_requested_correction_as_failure(runtime):
    selection, model, _ = runtime
    targets = [entry('CA-R-1'), entry('CA-R-2')]
    action = Mock(side_effect=InputError('target', 'Atom is missing'))
    with patch.dict(backend.ROUTES, {'atom_lifecycle_archive': action}):
        output = backend.execute(selection, model, 'atom_lifecycle_archive', {'targets': targets})
    assert output['errors'] == [{'code': 'invalid_input', 'field': 'target', 'message': 'Atom is missing'}]
    assert output['remaining_targets'] == [targets[1]]
    assert action.call_count == 1


def test_single_target_keeps_existing_result(runtime):
    selection, model, _ = runtime
    params = entry('CA-R-1')
    action = Mock(return_value=result(effects=[{'target': 'first'}]))
    with patch.dict(backend.ROUTES, {'atom_lifecycle_archive': action}):
        output = backend.execute(selection, model, 'atom_lifecycle_archive', params)
    assert output == result(effects=[{'target': 'first'}])
    action.assert_called_once_with(selection, model, params)
