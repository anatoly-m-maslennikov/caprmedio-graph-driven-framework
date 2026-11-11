# CA-O-10003@1
# CA-O-10016@2
# CA-D-270@27

"""Private Create Draft workflow. Caller supplies Project and model bindings."""
from __future__ import annotations

from datetime import datetime, timezone

from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier

from ATOM_LIFECYCLE import common, effects
from ATOM_LIFECYCLE.carrier import logical_view, render_carrier
from ATOM_LIFECYCLE.placement import derive_destination, resolve_container

_FIELDS = frozenset({'role', 'form', 'scope_unit', 'container', 'summary', 'body', 'label', 'tier',
                     'topics', 'relations', 'priority', 'work_sequence_number',
                     'ai_agent_confidence_threshold'})
_GENERATED = frozenset({'filename', 'file_name', 'path', 'output_path', 'destination',
                        'carrier_destination'})
def _summary(body):
    return common.atom_summary(body).group(1).strip()


def _body(source, values):
    body = values.get('body', source)
    if not isinstance(body, str):
        raise common.InputError('body', 'Body must be text.', format='Markdown string')
    if 'summary' in values:
        summary = values['summary']
        if not isinstance(summary, str) or not summary.strip() or '\n' in summary:
            raise common.InputError('summary', 'Summary must be one nonempty line.', format='Nonempty single-line string')
        if 'body' in values:
            if _summary(body) != summary:
                raise common.InputError('summary', 'Summary and body disagree.', format='Matching Summary section')
        elif source:
            match = common.atom_summary(body)
            body = body[:match.start(1)] + summary + body[match.end(1):]
        else:
            body = f'## Summary\n\n{summary}\n'
    _summary(body)
    return body


def _clean(values, warnings, field):
    if not isinstance(values, dict):
        raise common.InputError(field, 'Properties must be a dictionary.', format='Object')
    cleaned = {}
    for key, value in values.items():
        if key in _GENERATED:
            warnings.append('Generated carrier filename, path and destination are ignored.')
        elif key not in _FIELDS:
            raise common.InputError(str(key), 'Unsupported or generated property.', format='Admitted logical property')
        else:
            cleaned[key] = value
    return cleaned


def _required_properties(old_body, values, view):
    errors = []
    fields = {'role': values.get('role', view.get('role')),
              'form': values.get('form', view.get('form'))}
    for field, value in fields.items():
        if not isinstance(value, str) or not value.strip():
            errors.append(common.InputError(field, f'{field} is required.', format='Nonempty string'))
    try:
        container = common.logical_container(values, view)
    except common.InputError as error:
        errors.append(error)
    try:
        body = _body(old_body, values)
    except common.InputError as error:
        errors.append(error)
    if errors:
        raise common.InputError.combine(errors)
    return fields['role'], fields['form'], container, body


def _replacement_relations(original, supplied, predecessor):
    """Keep explicit replacement targets and add the selected Current Atom."""
    def read(value):
        if not isinstance(value, dict):
            raise common.InputError('relations', 'Relations must be a mapping.', format='Object')
        aliases = [key for key in value if isinstance(key, str) and key.casefold() == 'is_replacement_for']
        if any(key not in {'is_replacement_for', 'IS_REPLACEMENT_FOR'} for key in aliases):
            raise common.InputError('relations', 'Ambiguous replacement relation spelling.', format='IS_REPLACEMENT_FOR')
        lists = [value[key] for key in aliases]
        if any(not isinstance(items, list) or any(not isinstance(x, str) or not x for x in items)
               for items in lists):
            raise common.InputError('relations', 'Replacement targets must be a list of Atom IDs.', format='List of Atom IDs')
        if len(lists) == 2 and lists[0] != lists[1]:
            raise common.InputError('relations', 'Conflicting replacement relation aliases.', format='One replacement relation')
        return lists[0] if lists else []

    inherited = read(original)
    requested = read(supplied)
    merged = dict(supplied)
    targets = list(dict.fromkeys([*inherited, *requested, predecessor]))
    merged.pop('IS_REPLACEMENT_FOR', None)
    merged['is_replacement_for'] = targets
    return merged


def prepare_draft(selection, model, params, *, source_pin=None):  # noqa: C901
    """Validate and prepare one Draft without effects."""
    warnings = []
    if not isinstance(params, dict) or set(params) - {'newAtom', 'sourceCurrent', 'changes'}:
        raise common.InputError('parameters', 'Provide newAtom or sourceCurrent and changes.', format='Workflow input object')
    if 'newAtom' not in params and 'sourceCurrent' not in params:
        raise common.InputError('newAtom', 'Supply new Atom properties or a sourceCurrent selector.', format='Object of Atom properties')
    if 'newAtom' in params and 'sourceCurrent' in params:
        raise common.InputError('sourceCurrent', 'Choose exactly one Draft source.', format='Resupply either newAtom or sourceCurrent to select the Draft source')
    pin = None
    if 'newAtom' in params:
        if 'changes' in params:
            raise common.InputError('changes', 'Changes apply to an existing source.', format='Resupply newAtom to select it without changes')
        values = _clean(params['newAtom'], warnings, 'newAtom')
        view = {}
        old_body = ''
    else:
        pin = source_pin or common.read_target(selection, params['sourceCurrent'], field='sourceCurrent')
        if pin.status.casefold() == 'archived':
            raise common.InputError('sourceCurrent', 'Archived sources are not accepted.', format='Exact Current or Draft selector')
        values = _clean(params.get('changes', {}), warnings, 'changes')
        parsed = parse_carrier(pin.raw, pin.path)
        view = logical_view(parsed.metadata, model)
        old_body = parsed.body
    role, form, container, body = _required_properties(old_body, values, view)
    summary = _summary(body)
    old_summary = _summary(old_body) if pin else None
    from ATOM_LIFECYCLE.status_model import canonical_status, StatusModelError
    try:
        admitted = canonical_status(model, role, form, 'Draft') == 'Draft'
    except StatusModelError:
        admitted = False
    if not admitted:
        raise common.InputError('role', 'Draft is not admitted for this Role and Form.', format='Admitted Role and Form')
    same = pin is not None and summary == old_summary and role == view.get('role')
    atom_id = pin.atom_id if same else common.allocate_id(selection, role)
    version = (pin.version if pin.status.casefold() == 'draft' else pin.version + 1) if same else 1
    updated = view.get('updated_at') if same and pin.status.casefold() == 'draft' else datetime.now(timezone.utc).isoformat()
    scope, parent = resolve_container(selection, {'container': container, 'role': role, 'form': form}, atom_id, model=model)
    fields = {key: value for key, value in values.items() if key not in {'summary', 'body', 'scope_unit'}}
    if pin and not same and pin.status.casefold() != 'draft':
        original = view.get('relations', {})
        fields['relations'] = _replacement_relations(original, values.get('relations', original), pin.atom_id)
    fields.update({'atom_id': atom_id, 'ref_id': f'{atom_id}@{version}-draft', 'version': version,
                   'status': 'draft', 'updated_at': updated, 'container': container,
                   'role': role, 'form': form})
    destination = derive_destination(selection, atom_id=atom_id, version=version, status='Draft',
                                     role=role, form=form, summary=summary, scope_unit=scope, parent=parent,
                                     label=values.get('label', view.get('label')),
                                     tier=values.get('tier', view.get('tier')),
                                     work_sequence=values.get('work_sequence_number', view.get('work_sequence_number')))
    fields['destination'] = {'file': {'name': destination.name,
                                     'path': destination.parent.relative_to(selection.root).as_posix()}}
    raw = render_carrier(pin.raw if pin else None, fields, model=model,
                         body=body if not pin or {'summary', 'body'} & values.keys() else None)
    common.validate_candidate(selection, model, raw, destination)
    return {'pin': pin, 'selector': params.get('sourceCurrent'), 'destination': destination,
            'raw': raw, 'atom_id': atom_id, 'version': version, 'same': same, 'warnings': warnings}


def save_draft(selection, plan):
    """Save a previously prepared Draft after checking its source pin again."""
    pin, destination, raw = plan['pin'], plan['destination'], plan['raw']
    atom_id, version, same, warnings = plan['atom_id'], plan['version'], plan['same'], plan['warnings']
    if pin:
        current = common.read_target(selection, plan['selector'], field='sourceCurrent')
        if current.sha256 != pin.sha256:
            raise common.SourceChanged('Source changed while creating the Draft.')
    if same and pin.status.casefold() == 'draft':
        if destination == pin.path:
            outcome = effects.replace(selection.root, pin.path, pin.sha256, raw)
        else:
            outcome = common.write_destination(selection.root, destination, raw)
            if not outcome.errors:
                removed = effects.remove(selection.root, pin.path, pin.sha256)
                outcome.effects.extend(removed.effects)
                outcome.errors.extend(removed.errors)
    else:
        outcome = common.write_destination(selection.root, destination, raw)
    data = {} if outcome.errors else {'savedDraft': common.saved(selection, destination, atom_id,
                                                                  f'{atom_id}@{version}-draft', version, 'Draft')}
    return common.result(effects=outcome.effects, errors=outcome.errors, warnings=warnings, **data)


def create_draft(selection, model, params):
    """Prepare and save one Draft, without promoting it."""
    return save_draft(selection, prepare_draft(selection, model, params))
