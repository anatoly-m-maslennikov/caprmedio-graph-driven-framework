# CA-O-10011@3
# CA-R-1521@34
# CA-D-480@24
# CA-D-664@8
# CA-D-461@33
# CA-D-475@27

"""Compose Current Status actions for a verified containment tree."""

from dataclasses import replace
import hashlib

from .carrier import logical_view, render_carrier
from .common import InputError, SourceChanged, read_target, result, validate_candidate
from .placement_model import active_placement
from .plan_cascade import _companion_pins, select_archive_cascade
from .state_actions import _archive_target, _companion, _current, _destination_field, _publish, _status, prepare_current_status


_TERMINAL = frozenset({'done', 'canceled'})


def _check_destination(pin, path, companion):
    if path == pin.path:
        return
    candidates = (path, path.with_suffix('')) if companion is not None else (path,)
    if any(candidate.exists() or candidate.is_symlink() for candidate in candidates):
        raise InputError('target', 'A Status destination is occupied.')


def _plan(selection, model, parent, status, tree, *, plan, entering_backlog, reopening):
    closing_plan = plan and isinstance(status, str) and status.casefold() in _TERMINAL
    actions = []
    for pin in tree:
        target = status
        if pin != parent and closing_plan:
            if pin.status.casefold() in _TERMINAL:
                continue
            target = 'Canceled'
        if reopening and pin != parent:
            _current(selection, pin)
            _status(model, logical_view(pin.metadata, model), target, 'targetStatus')
        else:
            path, _ = prepare_current_status(selection, model, pin, target)
            if not entering_backlog or reopening:
                _check_destination(pin, path, _companion(pin))
        actions.append((pin, target))
    # A Backlog child needs its parent's new status and matching directory.
    if entering_backlog or reopening:
        actions.reverse()
    return actions


def _relocation_headers(selection, model, pin, source, destination, pins):
    expected = {child.atom_id: child for child in pins.values() if child.path.is_relative_to(source)}
    descendants = _companion_pins(selection, pin, model)
    descendants.pop(pin.atom_id)
    if descendants.keys() != expected.keys() or any(
        (child.path, child.sha256) != (expected[atom_id].path, expected[atom_id].sha256)
        for atom_id, child in descendants.items()
    ):
        raise SourceChanged('Contained Atoms changed during the Status cascade.')
    rewrites = {}
    moved = {}
    for child in descendants.values():
        relative = child.path.relative_to(source)
        target = destination / relative
        raw = render_carrier(child.raw, {'destination': _destination_field(selection, target)})
        validate_candidate(selection, model, raw, target, authored=False)
        rewrites[relative] = (child.sha256, raw)
        moved[child.atom_id] = _rebind(child, target, raw, child.status)
    return rewrites, moved


def _rebind(pin, path, raw, status):
    return replace(pin, path=path, raw=raw, sha256=hashlib.sha256(raw).hexdigest(), status=status)


def _check_terminal_children(selection, model, current, pins):
    for child in select_archive_cascade(selection, current, model)[:-1]:
        expected = pins.get(child.atom_id)
        if (expected is None or (child.path, child.sha256) != (expected.path, expected.sha256)
                or child.status.casefold() not in _TERMINAL):
            raise SourceChanged('Contained Plans changed during the Status cascade.')


def _apply(selection, model, pin, status, pins, *, verify_source, check_logical):
    current = read_target(selection, _archive_target(pin))
    if current.sha256 != pin.sha256 or current.path != pin.path:
        raise SourceChanged('An Atom changed during the Status cascade.')
    path, raw = prepare_current_status(selection, model, current, status, verify_source=verify_source)
    companion = _companion(current)
    _check_destination(current, path, companion)
    rewrites, moved = None, {}
    if companion is not None and path != pin.path:
        rewrites, moved = _relocation_headers(selection, model, current, companion, path.with_suffix(''), pins)
    if check_logical and status.casefold() in _TERMINAL:
        _check_terminal_children(selection, model, current, pins)
    output = _publish(selection, current, path, raw, status, pin.ref_id, companion=companion, rewrites=rewrites)
    if not output['errors']:
        pins.update(moved)
        pins[pin.atom_id] = _rebind(current, path, raw, status)
    return output


def change_status_workflow(selection, model, params):
    parent = read_target(selection, params.get('target'))
    status = params.get('targetStatus')
    plan = logical_view(parent.metadata, model).get('role') == 'Plan'
    if not plan and _companion(parent) is None:
        path, raw = prepare_current_status(selection, model, parent, status)
        return _publish(selection, parent, path, raw, status, parent.ref_id)
    shared_backlog = plan and active_placement().placement('Plan', 'Backlog')[0] == 'role'
    entering_backlog = shared_backlog and isinstance(status, str) and status.casefold() == 'backlog'
    reopening = (plan and parent.status.casefold() in _TERMINAL and isinstance(status, str)
                 and status.casefold() not in _TERMINAL | {'draft', 'archived'})
    tree = select_archive_cascade(selection, parent, model)
    pins = {pin.atom_id: pin for pin in tree}
    actions = _plan(selection, model, parent, status, tree, plan=plan,
                    entering_backlog=entering_backlog, reopening=reopening)
    completed = []
    artifact = None
    for index, (pin, target) in enumerate(actions):
        try:
            # The initial source was checked before the cascade. A moved parent
            # can change the rule for a child's old, already pinned location.
            output = _apply(selection, model, pins[pin.atom_id], target, pins,
                            verify_source=not (entering_backlog or reopening) or pin == parent,
                            check_logical=shared_backlog)
        except SourceChanged as error:
            output = result(errors=[{'code': 'source_changed', 'message': str(error)}])
        except (OSError, ValueError, RuntimeError):
            output = result(errors=[{'code': 'cascade_failed', 'message': 'A planned Status action could not run.'}])
        completed.extend(output['effects'])
        if output['errors']:
            remaining = [{**_archive_target(pin), 'target_status': target} for pin, target in actions[index:]]
            return result(effects=completed, errors=output['errors'], remaining_targets=remaining)
        if pin == parent:
            artifact = output['artifact']
    return result(effects=completed, artifact=artifact)
