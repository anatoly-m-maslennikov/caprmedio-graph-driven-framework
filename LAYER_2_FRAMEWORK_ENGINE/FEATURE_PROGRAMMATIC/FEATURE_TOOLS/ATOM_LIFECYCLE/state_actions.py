# CA-O-10000@1
# CA-O-10001@1
# CA-O-10007@1
# CA-O-10009@2

"""Private actions on one exactly selected Atom; caller composes cascades.

Effects require exclusion of concurrent writers to the selected source.
"""

from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier
from ATOM_LIFECYCLE import effects
from ATOM_LIFECYCLE.carrier import logical_view, render_carrier
from ATOM_LIFECYCLE.draft import _body, _clean, _summary
from ATOM_LIFECYCLE.common import InputError, SourceChanged, logical_container, read_target, result, saved, validate_candidate, write_destination
from ATOM_LIFECYCLE.placement import archived_owner, derive_destination, resolve_container
from ATOM_LIFECYCLE.plan_cascade import has_shared_plan_children, select_archive_cascade
from ATOM_LIFECYCLE.status_model import canonical_status, encode_status, StatusModelError


def _view(raw, path, model):
    parsed = parse_carrier(raw, path)
    return logical_view(parsed.metadata, model), parsed.body


def _destination(selection, pin, view, body, status, model, *, archive=False, verify_source=True):
    scope, parent = resolve_container(selection, view, pin.atom_id, model=model)
    if verify_source and parent is not None and pin.status.casefold() not in {'draft', 'archived'}:
        current = derive_destination(selection, atom_id=pin.atom_id, version=pin.version,
                                     status=pin.status, role=view.get('role'), form=view.get('form'),
                                     summary=_summary(body), scope_unit=scope,
                                     label=view.get('label'), tier=view.get('tier'), parent=parent,
                                     work_sequence=view.get('work_sequence_number'))
        if pin.path.parent != current.parent:
            raise InputError('target', 'Atom location disagrees with its logical container')
    return derive_destination(selection, atom_id=pin.atom_id, version=pin.version,
                              status=status, role=view.get('role'), form=view.get('form'),
                              summary=_summary(body), scope_unit=scope, parent=parent,
                              label=view.get('label'), tier=view.get('tier'),
                              work_sequence=view.get('work_sequence_number'),
                              source_path=pin.path if archive else None)


def _archived_edit_destination(selection, model, pin, old, old_body, new, body):
    old_container = logical_container({}, old)
    new_container = logical_container({}, new)
    owner = archived_owner(selection, pin.path, old['role'])
    if 'scope_unit' in old_container:
        old_scope, _ = resolve_container(selection, old, pin.atom_id, model=model)
        old_path = _archived_path(selection, pin, old, old_body, old_scope)
        if archived_owner(selection, old_path, old['role']) != owner:
            raise InputError('target', 'Archived Atom location disagrees with its logical container')
    if old_container != new_container:
        owner, _ = resolve_container(selection, new, pin.atom_id, model=model)
    elif 'atom' in new_container and old.get('form') != new.get('form'):
        resolve_container(selection, new, pin.atom_id, model=model)
    placement_fields = ('form', 'label', 'tier', 'work_sequence_number')
    if (old_container != new_container or any(old.get(key) != new.get(key) for key in placement_fields)
            or _summary(old_body) != _summary(body)):
        return _archived_path(selection, pin, new, body, owner)
    return pin.path


def _archived_path(selection, pin, view, body, scope):
    return derive_destination(selection, atom_id=pin.atom_id, version=pin.version, status=pin.status,
                              role=view['role'], form=view['form'], summary=_summary(body), scope_unit=scope,
                              label=view.get('label'), tier=view.get('tier'),
                              work_sequence=view.get('work_sequence_number'), archived_update=True)


def _status(model, view, value, field):
    allowed = model.allowed(view.get('role'), view.get('form'))
    try:
        valid = value in allowed and canonical_status(model, view.get('role'), view.get('form'), value) == value
    except StatusModelError:
        valid = False
    if not valid:
        raise InputError(field, 'Status is not admitted by the applicable model', allowed_values=sorted(allowed))


def _current(selection, pin):
    if pin.status.casefold() in {'draft', 'archived'}:
        raise InputError('target', 'A Current Atom is required')
    if pin.path in selection.declaration_paths:
        raise InputError('target', 'This Atom is a bound Scope Unit source and requires Scope Unit lifecycle handling.')


def _destination_field(selection, path):
    return {'file': {'name': path.name, 'path': path.parent.relative_to(selection.root).as_posix()}}


def _publish(selection, pin, path, raw, status, ref_id, *, companion=None, rewrites=None):
    if path == pin.path:
        outcome = effects.replace(selection.root, path, pin.sha256, raw)
    else:
        outcome = write_destination(selection.root, path, raw)
        if companion is not None and not outcome.errors:
            from ATOM_LIFECYCLE.directory_effect import move_directory

            moved = move_directory(selection.root, companion, path.with_suffix(''), rewrites=rewrites)
            outcome.effects.extend(moved.effects)
            outcome.errors.extend(moved.errors)
        if not outcome.errors:
            removed = effects.remove(selection.root, pin.path, pin.sha256)
            outcome.effects.extend(removed.effects)
            outcome.errors.extend(removed.errors)
    data = {} if outcome.errors else {'artifact': saved(selection, path, pin.atom_id, ref_id, pin.version, status)}
    return result(effects=outcome.effects, errors=outcome.errors, **data)


def _prepare_archive(selection, model, pin):
    _current(selection, pin)
    view, body = _view(pin.raw, pin.path, model)
    _status(model, view, 'Archived', 'target')
    path = _destination(selection, pin, view, body, 'Archived', model, archive=True)
    ref_id = f'{pin.atom_id}@{pin.version}'
    raw = render_carrier(pin.raw, {'status': 'archived', 'ref_id': ref_id, 'destination': _destination_field(selection, path)})
    validate_candidate(selection, model, raw, path, authored=False)
    return path, raw, ref_id


def _companion(pin):
    path = pin.path.with_suffix('')
    return path if path.exists() or path.is_symlink() else None


def archive_atom(selection, model, params):
    pin = read_target(selection, params.get('target'))
    if _companion(pin) is not None or has_shared_plan_children(selection, pin, model):
        raise InputError('target', 'Archive the contained Atoms before moving the parent Carrier.')
    path, raw, ref_id = _prepare_archive(selection, model, pin)
    return _publish(selection, pin, path, raw, 'Archived', ref_id)


def _archive_target(pin):
    return {'ref_id': pin.ref_id, 'version': pin.version}


def _prepare_archive_cascade(selection, model, targets):
    prepared = []
    destinations = set()
    for target in targets:
        path, raw, ref_id = _prepare_archive(selection, model, target)
        companion = _companion(target)
        paths = {path, path.with_suffix('')} if companion is not None else {path}
        if paths & destinations or any(item.exists() or item.is_symlink() for item in paths):
            raise InputError('target', 'An archive destination is occupied.')
        destinations.update(paths)
        prepared.append((target, path, raw, ref_id, companion))
    return prepared


def _archive_cascade_target(selection, model, target, path, raw, ref_id, companion):
    current = read_target(selection, _archive_target(target))
    if current.sha256 != target.sha256 or current.path != target.path or _companion(current) != companion:
        raise SourceChanged('An Atom changed during the archive cascade.')
    if ((companion is not None and len(select_archive_cascade(selection, current, model)) != 1)
            or has_shared_plan_children(selection, current, model)):
        raise SourceChanged('A containing Atom has additional descendants.')
    return _publish(selection, current, path, raw, 'Archived', ref_id, companion=companion)


def archive_workflow(selection, model, params):
    """The caller composes separate single-Atom actions for the selected tree."""
    pin = read_target(selection, params.get('target'))
    _current(selection, pin)
    companion = _companion(pin)
    if companion is None and logical_view(pin.metadata, model).get('role') != 'Plan':
        path, raw, ref_id = _prepare_archive(selection, model, pin)
        return _publish(selection, pin, path, raw, 'Archived', ref_id)
    prepared = _prepare_archive_cascade(selection, model, select_archive_cascade(selection, pin, model))
    completed = []
    for index, entry in enumerate(prepared):
        try:
            output = _archive_cascade_target(selection, model, *entry)
        except (OSError, ValueError, RuntimeError):
            output = result(errors=[{'code': 'cascade_failed', 'message': 'A planned Archive action could not run.'}])
        completed.extend(output['effects'])
        if output['errors']:
            return result(effects=completed, errors=output['errors'],
                          remaining_targets=[_archive_target(item[0]) for item in prepared[index:]])
    return result(effects=completed, artifact=output['artifact'])


def prepare_current_status(selection, model, pin, target, *, verify_source=True):
    _current(selection, pin)
    view, body = _view(pin.raw, pin.path, model)
    if not isinstance(target, str) or target.casefold() in {'draft', 'archived'}:
        raise InputError('targetStatus', 'A Current Status is required')
    _status(model, view, target, 'targetStatus')
    path = _destination(selection, pin, view, body, target, model, verify_source=verify_source)
    raw = render_carrier(pin.raw, {'status': encode_status(target), 'destination': _destination_field(selection, path)})
    validate_candidate(selection, model, raw, path, authored=False)
    return path, raw


def change_status(selection, model, params):
    pin = read_target(selection, params.get('target'))
    if _companion(pin) is not None or has_shared_plan_children(selection, pin, model):
        raise InputError('target', 'Apply the contained Status actions before moving the parent Carrier.')
    target = params.get('targetStatus')
    path, raw = prepare_current_status(selection, model, pin, target)
    return _publish(selection, pin, path, raw, target, pin.ref_id)


def direct_update(selection, model, params):
    pin = read_target(selection, params.get('target'))
    warnings = []
    changes = _clean(params.get('changes'), warnings, 'changes')
    if not changes:
        raise InputError('changes', 'Supply at least one property change')
    # A companion directory signifies contained Atoms; this Action is non-container.
    if _companion(pin) is not None or has_shared_plan_children(selection, pin, model):
        raise InputError('target', 'Direct updates of container Atoms are unsupported')
    old, old_body = _view(pin.raw, pin.path, model)
    body = _body(old_body, changes)
    fields = {key: value for key, value in changes.items() if key not in {'summary', 'body', 'scope_unit'}}
    if {'scope_unit', 'container'} & changes.keys():
        fields['container'] = logical_container(changes, old)
    raw = render_carrier(pin.raw, fields, body=body, model=model)
    new, body = _view(raw, pin.path, model)
    if old.get('role') != new.get('role'):
        raise InputError('changes', 'Changing Role requires a new Atom')
    try:
        status = canonical_status(model, new.get('role'), new.get('form'), pin.status)
    except StatusModelError as error:
        raise InputError('changes.fields', str(error)) from error
    if pin.status.casefold() == 'archived':
        path = _archived_edit_destination(selection, model, pin, old, old_body, new, body)
    else:
        if 'atom' in logical_container({}, old):
            _destination(selection, pin, old, old_body, pin.status, model)
        path = _destination(selection, pin, new, body, pin.status, model, verify_source=False)
    raw = render_carrier(raw, {'destination': _destination_field(selection, path)})
    validate_candidate(selection, model, raw, path)
    output = _publish(selection, pin, path, raw, status, pin.ref_id)
    output['warnings'].extend(warnings)
    return output
