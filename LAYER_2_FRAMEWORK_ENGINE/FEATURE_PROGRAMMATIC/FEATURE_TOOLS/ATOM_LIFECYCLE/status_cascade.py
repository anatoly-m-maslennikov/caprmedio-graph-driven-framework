# CA-O-10011@4
# CA-R-1525@25
# CA-R-1521@34
# CA-D-480@24
# CA-D-664@8
# CA-D-461@33
# CA-D-475@27

"""Compose Current Status actions for a verified containment tree."""

from .timing import trace

from dataclasses import dataclass, replace
import hashlib

from .assets.change_current_status import SOURCE_SHA256, WORKFLOW_BINDING, change_current_status
from .carrier import logical_view, render_carrier
from .common import InputError, SourceChanged, read_target, result, validate_candidate
from .placement_model import active_placement
from .plan_cascade import _companion_pins, select_archive_cascade
from .source import SourceSelectionError, _selector
from .state_actions import _archive_target, _companion, _current, _destination_field, _publish, _status, prepare_current_status
from .status_workflow_definition import DefinitionChanged, bind_definition_check
from .status_workflow_journal import StatusRunJournal


_TERMINAL = frozenset({'done', 'canceled'})


def _check_destination(pin, path, companion):
    if path == pin.path:
        return
    candidates = (path, path.with_suffix('')) if companion is not None else (path,)
    if any(candidate.exists() or candidate.is_symlink() for candidate in candidates):
        raise InputError('target', 'A Status destination is occupied.')


@trace('status.plan')
def _plan(selection, model, parent, pins, actions, *, entering_backlog, reopening):
    for atom_id, target in actions:
        pin = pins[atom_id]
        if reopening and pin != parent:
            _current(selection, pin)
            _status(model, logical_view(pin.metadata, model), target, 'targetStatus')
        else:
            path, _ = prepare_current_status(selection, model, pin, target)
            if not entering_backlog or reopening:
                _check_destination(pin, path, _companion(pin))


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


@trace('status.apply')
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


@dataclass(frozen=True)
class StatusInvocation:
    ref_id: str
    version: int
    target_status: str


def _invocation(selection, params):
    if not isinstance(params, dict) or any(not isinstance(field, str) for field in params):
        raise InputError('arguments', 'Supply a mapping with target and targetStatus.')
    target, status = params.get('target'), params.get('targetStatus')
    errors = [InputError(field, 'Remove this unsupported field.')
              for field in sorted(params.keys() - {'target', 'targetStatus'})]
    try:
        if not isinstance(target, dict) or target.keys() != {'ref_id', 'version'}:
            raise ValueError
        if type(target['version']) is not int or target['version'] < 1:
            raise ValueError
        _, version, _ = _selector(selection, target['ref_id'], target['version'])
        if version is not None:
            raise ValueError
    except ValueError:
        errors.append(InputError('target', 'Supply a Current Atom ID and positive Version.',
                                 format='object with ref_id and version'))
    if not isinstance(status, str) or not status.strip() or status.casefold() in {'draft', 'archived'}:
        errors.append(InputError('targetStatus', 'Supply a Current Status.', format='Current Status'))
    if errors:
        raise InputError.combine(errors)
    return StatusInvocation(target['ref_id'], target['version'], status)


@dataclass(frozen=True)
class StatusAtom:
    atom_id: str
    status: str


@dataclass(frozen=True)
class StatusTree:
    parent: StatusAtom
    child_first: tuple[StatusAtom, ...]
    is_plan: bool
    shared_backlog: bool


class StatusRun:
    """Read pinned inputs, preflight the Workflow's plan and dispatch one bound Action."""

    def __init__(self, selection, model, invocation):
        self.selection = selection
        self.model = model
        self.parent = read_target(selection, {'ref_id': invocation.ref_id, 'version': invocation.version})
        self.check_definition = bind_definition_check()
        self.journal = StatusRunJournal(selection, WORKFLOW_BINDING, SOURCE_SHA256)
        self.pins = {}
        self.actions = ()
        self.parent_first = False
        self.shared_backlog = False
        self.effects = []
        self.warnings = []
        self.action_results = []
        self.errors = []
        self.failed_action = None
        self.artifact = None
        self.blocked = False
        self.started = False

    def read_status_tree(self):
        is_plan = logical_view(self.parent.metadata, self.model).get('role') == 'Plan'
        self.shared_backlog = is_plan and active_placement().placement('Plan', 'Backlog')[0] == 'role'
        tree = (select_archive_cascade(self.selection, self.parent, self.model)
                if is_plan or _companion(self.parent) is not None else (self.parent,))
        self.pins = {pin.atom_id: pin for pin in tree}
        return StatusTree(StatusAtom(self.parent.atom_id, self.parent.status),
                          tuple(StatusAtom(pin.atom_id, pin.status) for pin in tree),
                          is_plan, self.shared_backlog)

    def preflight(self, *, actions, parent_first, entering_backlog, reopening):
        self.actions = tuple(actions)
        self.parent_first = parent_first
        _plan(self.selection, self.model, self.parent, self.pins, self.actions,
              entering_backlog=entering_backlog, reopening=reopening)

    def _apply_one(self, pin, status):
        try:
            return _apply(self.selection, self.model, pin, status, self.pins,
                          verify_source=not self.parent_first or pin.atom_id == self.parent.atom_id,
                          check_logical=self.shared_backlog)
        except InputError as error:
            return result(errors=[{'code': 'invalid_input', 'message': str(error), 'field': error.field}])
        except (SourceChanged, SourceSelectionError) as error:
            return result(errors=[{'code': 'source_changed', 'message': str(error)}])
        except (OSError, ValueError, RuntimeError):
            return result(errors=[{'code': 'cascade_failed', 'message': 'A planned Status Action could not run.'}])

    def _target(self, atom_id, status):
        return {**_archive_target(self.pins[atom_id]), 'target_status': status}

    def _action(self, atom_id, status):
        return {'step': WORKFLOW_BINDING['step'], 'action': WORKFLOW_BINDING['action'],
                'target': self._target(atom_id, status)}

    def invoke(self, *, step, action, atom_id, target_status):
        index = len(self.action_results)
        if (self.errors or index >= len(self.actions) or self.actions[index] != (atom_id, target_status)
                or (step, action) != (WORKFLOW_BINDING['step'], WORKFLOW_BINDING['action'])):
            raise RuntimeError('Invalid Action dispatch in the installed Status Workflow.')
        try:
            self.check_definition()
        except DefinitionChanged as error:
            self.errors.append({'code': 'definition_revalidation_required', 'message': str(error)})
            self.blocked = True
            return False
        if not self.started:
            self.journal.started()
            self.started = True
        output = self._apply_one(self.pins[atom_id], target_status)
        entry = self._action(atom_id, target_status)
        observed = {**entry, **output}
        observed['step_run_id'] = self.journal.step(observed)
        self.action_results.append(observed)
        self.effects.extend(output['effects'])
        self.warnings.extend(output['warnings'])
        if output['errors']:
            self.errors.extend(output['errors'])
            self.failed_action = entry
            return False
        if atom_id == self.parent.atom_id:
            self.artifact = output['artifact']
        return True

    def finish(self):
        data = {'workflow_binding': dict(WORKFLOW_BINDING), 'action_results': self.action_results}
        if self.started:
            data['workflow_run_id'] = self.journal.run_id
        if self.errors:
            next_index = len(self.action_results)
            if self.failed_action is not None:
                data['failed_action'] = self.failed_action
            remaining = next_index if self.blocked else next_index - 1
            data['remaining_targets'] = [self._target(*target) for target in self.actions[remaining:]]
            data['unrun_actions'] = [self._action(*target) for target in self.actions[next_index:]]
        else:
            if self.artifact is None or len(self.action_results) != len(self.actions):
                raise RuntimeError('The installed Status Workflow stopped before completing its plan.')
            data['artifact'] = self.artifact
        outcome = 'blocked' if self.blocked else 'failed' if self.errors else 'completed'
        self.warnings.extend(self.journal.finish(outcome, self.errors))
        return result(outcome=outcome, effects=self.effects, errors=self.errors, warnings=self.warnings, **data)


@trace('change_status')
def change_status_workflow(selection, model, params):
    invocation = _invocation(selection, params)
    run = StatusRun(selection, model, invocation)
    change_current_status(invocation=invocation, engine=run)
    return run.finish()
