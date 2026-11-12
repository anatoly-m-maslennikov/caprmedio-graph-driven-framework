# CA-O-10002@2
# CA-R-3006@9
# CA-R-2511@11
# CA-R-970308624@3

"""Bounded input checks for prepared lifecycle Atom candidates.

Validation uses finite declaration constraints from the build-time assets.
"""
from __future__ import annotations

from .timing import trace

from datetime import datetime
from pathlib import Path
import re

from ATOM_LIFECYCLE.carrier import logical_view
from ATOM_LIFECYCLE.source import query_reader, select_context, select_source
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier
from ATOM_LIFECYCLE.status_model import canonical_status, StatusModelError
from carrier_aliases import matches_named_value


@trace('validation.candidate')
def validate_candidate(selection, model, raw: bytes, path: Path, *, authored: bool = True) -> None:
    """Reject malformed prepared identity, required fields and Status values."""
    from ATOM_LIFECYCLE.common import InputError

    try:
        parsed = parse_carrier(raw, path)
        view = logical_view(parsed.metadata, model)
    except ValueError as error:
        raise InputError('carrier', 'Candidate Carrier is malformed.', format='UTF-8 Markdown with valid YAML Header') from error

    for field in ('atom_id', 'ref_id', 'role', 'form', 'status'):
        value = view.get(field)
        if not isinstance(value, str) or not value or value != value.strip():
            raise InputError(field, f'{field} must be a nonempty exact string.', format='Nonempty exact string')
    try:
        prefix = selection.settings['artifacts']['identity']['project_prefix']
        if not isinstance(prefix, str) or not prefix:
            raise ValueError
    except (KeyError, TypeError, ValueError) as error:
        raise InputError('atom_id', 'Project identity prefix is unavailable.', format='Project Atom ID') from error
    atom_id = view['atom_id']
    if not re.fullmatch(re.escape(prefix) + r'-[A-Z]-[0-9]+', atom_id):
        raise InputError('atom_id', 'Atom ID is invalid for this Project.', format='Project Atom ID')
    if atom_id[len(prefix) + 1] != view['role'][0].upper():
        raise InputError('atom_id', 'Atom ID Role letter does not match Role.', format='Role-prefixed Atom ID')
    version = view.get('version')
    if type(version) is not int or version < 1:
        raise InputError('version', 'Version must be a positive integer.', format='Positive integer')
    if view['ref_id'] not in (atom_id, f'{atom_id}@{version}', f'{atom_id}@{version}-draft'):
        raise InputError('ref_id', 'Ref ID does not identify this Atom revision.', format='Atom ID or qualified revision')
    _validate_state(view, model)
    _validate_declared_schema(model, parsed, view, authored)
    _validate_containment(selection, model, view)
    _validate_authored_work_report(selection, model, parsed, view, prefix, authored)


def _validate_authored_work_report(selection, model, parsed, view, prefix, authored):
    if authored and view['status'] != 'Archived' and matches_named_value(view['form'], 'Work Report'):
        _validate_work_report(selection, model, parsed, view, prefix)


def _validate_work_report(selection, model, parsed, view, prefix):
    from ATOM_LIFECYCLE.common import InputError, atom_summary, logical_container

    if not matches_named_value(view['role'], 'Plan'):
        raise InputError('role', 'A Work Report must have the Plan Role.')
    relations = view.get('relations', {})
    if not isinstance(relations, dict):
        raise InputError('relations', 'Relations must be a mapping.')
    aliases = [key for key in relations if isinstance(key, str) and key.casefold() == 'is_work_report_for']
    if (any(key not in {'IS_WORK_REPORT_FOR', 'is_work_report_for'} for key in aliases)
            or not aliases or any(relations[key] != relations[aliases[0]] for key in aliases)):
        raise InputError('relations', 'Supply one unambiguous Work Report target.')
    targets = relations[aliases[0]]
    if (not isinstance(targets, list) or len(targets) != 1 or not isinstance(targets[0], str)
            or re.fullmatch(re.escape(prefix) + r'-P-[0-9]+', targets[0]) is None
            or targets[0] == view['atom_id']):
        raise InputError('relations', 'Supply one distinct Plan base Atom ID.')
    try:
        indexed = query_reader() is not None
        target = select_context(selection, targets[0]) if indexed else select_source(selection, targets[0])
        target_view = logical_view(target.metadata, model)
        if (target.status.casefold() in {'draft', 'archived'}
                or not matches_named_value(target_view.get('role'), 'Plan')
                or not matches_named_value(target_view.get('form'), 'Plan')):
            raise ValueError('Not a Current Plan')
        if logical_container({}, view) != logical_container({}, target_view):
            raise InputError('container', 'Work Report and reported Plan must have the same Container.')
        target_body = (f'## Summary\n\n{target.summary}\n' if indexed and target.summary is not None else
                       '' if indexed else parse_carrier(target.raw, target.path).body)
        if atom_summary(parsed.body).group(1).strip() != atom_summary(target_body).group(1).strip():
            raise InputError('summary', 'Work Report and reported Plan must have the same Summary.')
    except InputError:
        raise
    except (ValueError, OSError, RuntimeError) as error:
        raise InputError('relations', 'The reported Current Plan cannot be resolved safely.') from error


_TERMINAL_PLANS = frozenset({'Done', 'Canceled'})


def _validate_containment(selection, model, view):
    if view['role'] == 'Plan' and view['status'] not in _TERMINAL_PLANS | {'Draft', 'Archived'}:
        _validate_plan_ancestors(selection, model, view)


def _validate_plan_ancestors(selection, model, view):
    from ATOM_LIFECYCLE.common import InputError, logical_container

    seen = {view['atom_id']}
    parent_id = view['container'].get('atom')
    while parent_id is not None:
        if parent_id in seen or len(seen) >= 32:
            raise InputError('container', 'Containing Atom chain is cyclic or too deep.')
        seen.add(parent_id)
        parent = select_context(selection, parent_id) if query_reader() is not None else select_source(selection, parent_id)
        if parent.status.casefold() in {'done', 'canceled'}:
            raise InputError('status', 'A Plan inside a Done or Canceled Plan must also be Done or Canceled.',
                             allowed_values=sorted(_TERMINAL_PLANS & model.allowed(view['role'], view['form'])))
        parent_view = logical_view(parent.metadata, model)
        parent_id = logical_container({}, parent_view).get('atom')


def _validate_state(view, model):
    from ATOM_LIFECYCLE.common import InputError

    container = view.get('container')
    values = [container[key] for key in ('scope_unit', 'atom') if key in container] if isinstance(container, dict) else []
    if len(values) != 1 or not isinstance(values[0], str) or not values[0].strip():
        raise InputError('container.scope_unit', 'Supply one Scope Unit or containing Atom.', format='One nonempty reference')
    updated = view.get('updated_at')
    try:
        timestamp = datetime.fromisoformat(updated.replace('Z', '+00:00')) if isinstance(updated, str) else updated
        if not isinstance(timestamp, datetime) or timestamp.utcoffset() is None:
            raise ValueError
    except ValueError as error:
        raise InputError('updated_at', 'Updated At requires an offset-bearing timestamp.', format='Offset-bearing timestamp') from error
    allowed = model.allowed(view['role'], view['form'])
    try:
        view['status'] = canonical_status(model, view['role'], view['form'], view['status'])
    except StatusModelError:
        raise InputError('status', 'Status is not admitted by the applicable model.',
                         allowed_values=sorted(allowed))


def _validate_declared_schema(model, parsed, view, authored):
    """Apply the explicitly supplied, source-bound Workbench schema, if present."""
    from ATOM_LIFECYCLE.common import InputError

    schema = getattr(model, 'candidate_schema', None)
    if schema is None:
        return
    row = {'header_json': parsed.metadata, 'role': view['role'], 'form': view['form'],
           'content_markdown': parsed.body}
    errors = []
    try:
        schema.validate_role_form(view['role'], view['form'])
    except ValueError as error:
        field = 'role' if view['role'] not in schema.role_form.roles else 'form'
        errors.append(InputError(field, str(error), format='Declared Role and Form'))
    try:
        schema.header(1).validate(row)
    except ValueError as error:
        name = re.match(r'Header (\S+) requires (.+)', str(error))
        field = name[1].rsplit('.', 1)[-1] if name else 'header'
        errors.append(InputError(field, str(error), format=name[2] if name else 'Declared Header format'))
    if authored:
        errors.extend(InputError(field, message, allowed_values=allowed,
                                 format=None if allowed else 'Declared Header constraint')
                      for field, message, allowed in schema.header_constraints.validate(view, metadata=parsed.metadata))
    try:
        schema.content.validate(row)
        if authored:
            schema.content_constraints.validate(row)
    except ValueError as error:
        errors.append(InputError('body', str(error), format='Declared Content heading structure'))
    if errors:
        raise InputError.combine(errors)
