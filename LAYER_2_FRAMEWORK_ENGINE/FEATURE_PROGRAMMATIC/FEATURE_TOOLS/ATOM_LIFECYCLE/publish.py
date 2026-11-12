# CA-O-10005@1
# CA-O-10018@2
# CA-O-10024@3
# CA-D-446@30

"""Private ordered promotion and composed update operations."""
from __future__ import annotations

from .timing import trace

import hashlib
import re
from pathlib import Path

from ATOM_LIFECYCLE import effects, source
from ATOM_LIFECYCLE.carrier import logical_view, render_carrier, same_authored_carrier
from ATOM_LIFECYCLE.common import InputError, SourceChanged, read_target, result, saved, validate_candidate, write_destination
from ATOM_LIFECYCLE.draft import _summary
from ATOM_LIFECYCLE.placement import derive_destination, resolve_container
from ATOM_LIFECYCLE.status_model import canonical_status, encode_status, StatusModelError
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier
from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS


def _same_pin(left, right):
    return (left.path == right.path and left.sha256 == right.sha256 and left.ref_id == right.ref_id
            and left.version == right.version and left.status.casefold() == right.status.casefold())


def _indexed_archive(selection, identity, reader):
    """Read the first eligible indexed candidate, without falling back on stale data."""
    indexed = source.query_reader()
    candidates = indexed.lifecycle_archive_candidates(selection, identity)
    if not isinstance(candidates, (list, tuple)):
        raise source.SourceSelectionError('Indexed Archive candidates are invalid')
    for row in candidates:
        if not isinstance(row, (list, tuple)) or len(row) != 2:
            raise source.SourceSelectionError('Indexed Archive candidate is invalid')
        reference, path = row
        selected_id, version, draft = source._selector(selection, reference, None)
        if selected_id != identity or version is None or draft:
            continue
        if (not isinstance(path, Path) or not path.is_absolute() or '..' in path.parts
                or not path.is_relative_to(selection.root)):
            raise source.SourceSelectionError('Indexed Atom path is outside the selected Project')
        if not source._matches_revision(path, identity, version, None):
            continue
        try:
            return source._unique_candidate(reader, (path,), reference, identity, version, None)
        except source.ArchiveNotLoadedError:
            raise
        except source.SourceSelectionError as exc:
            raise InputError('relations.is_replacement_for', 'Indexed Archived replacement is stale or invalid.') from exc
    raise source.SourceSelectionError('Replacement target is missing or ambiguous')


@trace('promotion.resolve_replacement')
def resolve_replacement(selection, atom_id):  # noqa: C901
    """Resolve a base identity to one Current, or verified Archived evidence."""
    identity, qualified, draft = source._selector(selection, atom_id, None)
    if qualified or draft:
        raise InputError('relations.is_replacement_for', 'Replacement references must be base Atom IDs.')
    reader = ReadContext(roots=[str(selection.root)], limits=dict(CEILINGS))
    try:
        queried = source.query_reader() is not None
        if queried:
            candidates = tuple(path for path in source._candidate_paths(reader, selection, identity, references=(identity,))
                               if source._matches_revision(path, identity, None, None))
            if candidates:
                try:
                    return source._unique_candidate(reader, candidates, identity, identity, None, None)
                except source.ArchiveNotLoadedError:
                    raise
                except source.SourceSelectionError as exc:
                    raise InputError('relations.is_replacement_for', 'Indexed Current replacement is stale or invalid.') from exc
            return _indexed_archive(selection, identity, reader)
        candidates = source._candidate_paths(reader, selection, identity)
        current = []
        archived = []
        for path in candidates:
            match = re.match(r'(?:[1-9][0-9]*-)?' + re.escape(identity) + r'(?:@([1-9][0-9]*)(-draft)?)?(?=-|\.)', path.name)
            if not match:
                raise source.SourceSelectionError('Malformed replacement carrier identity')
            version, is_draft = match.groups()
            if not version:
                suffix = re.search(r'@([1-9][0-9]*)\.md$', path.name)
                version = suffix.group(1) if suffix else None
            if is_draft:
                continue
            ref = f'{identity}@{version}' if version else identity
            pin = source._read_candidate(reader, path, ref, identity, version, None)
            if pin is not None:
                (archived if version else current).append(pin)
        source._check_currentness(reader, selection, identity, candidates)
        if len(current) > 1 or (not current and not archived):
            raise source.SourceSelectionError('Replacement target is missing or ambiguous')
        if current:
            return current[0]
        latest = max(pin.version for pin in archived)
        matches = [pin for pin in archived if pin.version == latest]
        if len(matches) != 1:
            raise source.SourceSelectionError('Archived replacement target is ambiguous')
        return matches[0]
    except source.ArchiveNotLoadedError:
        raise
    except InputError:
        raise
    except (OSError, ValueError, RuntimeError) as exc:
        raise InputError('relations.is_replacement_for', 'Replacement target cannot be resolved safely.') from exc



@trace('promotion.check_id')
def _current_collision(selection, atom_id):
    reader = ReadContext(roots=[str(selection.root)], limits=dict(CEILINGS))
    candidates = source._candidate_paths(reader, selection, atom_id, references=(atom_id,))
    if source.query_reader() is not None:
        try:
            source._unique_candidate(reader, candidates, atom_id, atom_id, None, None)
        except source.ArchiveNotLoadedError:
            raise
        except source.SourceSelectionError:
            return False
        return True
    found = [pin for path in candidates
             if source._matches_revision(path, atom_id, None, None)
             if (pin := source._read_candidate(reader, path, atom_id, atom_id, None, None)) is not None]
    source._check_currentness(reader, selection, atom_id, candidates)
    return bool(found)

def _relations(pin):
    relations = pin.metadata.get('relations', {})
    if not isinstance(relations, dict):
        raise InputError('relations.is_replacement_for', 'Relations must be a mapping.')
    canonical = relations.get('IS_REPLACEMENT_FOR')
    legacy = relations.get('is_replacement_for')
    if 'IS_REPLACEMENT_FOR' in relations and 'is_replacement_for' in relations and canonical != legacy:
        raise InputError('relations.is_replacement_for', 'Replacement relation aliases disagree.')
    value = relations.get('IS_REPLACEMENT_FOR', relations.get('is_replacement_for', []))
    if not isinstance(value, list) or any(not isinstance(x, str) or not x for x in value):
        raise InputError('relations.is_replacement_for', 'Replacement targets must be a list of Atom IDs.')
    return list(dict.fromkeys(value))


def _destination(selection, pin, status, model):
    view = logical_view(pin.metadata, model)
    body = parse_carrier(pin.raw, pin.path).body
    match = re.search(r'(?im)^#{1,2}\s+Summary\s*\n+([^\n]+)', body)
    if not match:
        raise InputError('target', 'Draft Summary is missing.')
    scope, parent = resolve_container(selection, view, pin.atom_id, model=model)
    return derive_destination(selection, atom_id=pin.atom_id, version=pin.version, status=status,
                              role=view.get('role'), form=view.get('form'), label=view.get('label'),
                              summary=match.group(1).strip(), scope_unit=scope, parent=parent, tier=view.get('tier'),
                              work_sequence=view.get('work_sequence_number'))


def _error(exc):
    if isinstance(exc, source.ArchiveNotLoadedError):
        return {'code': 'archive_not_loaded', 'message': str(exc), 'field': None}
    if isinstance(exc, InputError):
        return {'code': 'invalid_input', 'message': str(exc), 'field': exc.field}
    if isinstance(exc, SourceChanged):
        return {'code': 'source_changed', 'message': str(exc), 'field': None}
    return {'code': 'backend_failure', 'message': 'Lifecycle operation failed.', 'field': None}


def _ensure_leaf(selection, model, pin, field):
    from ATOM_LIFECYCLE.plan_cascade import has_shared_plan_children

    companion = pin.path.with_suffix('')
    if companion.exists() or companion.is_symlink() or has_shared_plan_children(selection, pin, model):
        raise InputError(field, 'A containing or folder-backed Atom cannot be replaced by this workflow.')


def _check_destination(path, predecessors, field):
    if not path.exists() and not path.is_symlink():
        return
    if not path.is_symlink() and any(
        pin.path == path and pin.status.casefold() != 'archived' for pin in predecessors
    ):
        return
    raise InputError(field, 'The derived Current Carrier destination is occupied.')


def _promotion_predecessor(selection, ref, staged):
    """Use a pinned archived predecessor without scanning unrelated history."""
    pin = staged.get(ref) if staged is not None else None
    if pin is None or pin.status.casefold() != 'archived':
        return resolve_replacement(selection, ref)
    if _current_collision(selection, ref):
        raise SourceChanged('A Current replacement target appeared after preparation.')
    current = source.select_source(selection, pin.ref_id, expected_version=pin.version)
    if not _same_pin(current, pin):
        raise SourceChanged('Replacement target changed after preparation.')
    return current


@trace('promotion.promote')
def _promote_draft(selection, model, params, *, staged=None, expected_draft=None):  # noqa: C901
    """Resolve all predecessor targets, archive them, then publish and remove Draft."""
    from ATOM_LIFECYCLE.state_actions import archive_atom

    all_effects, warnings = [], []
    try:
        if not isinstance(params, dict) or set(params) - {'target', 'targetStatus'}:
            raise InputError('target', 'Expected an exact target and a Current Status.')
        if 'targetStatus' not in params:
            raise InputError('targetStatus', 'Supply the requested Current Status.', format='Current Status')
        pin = read_target(selection, params.get('target'))
        if expected_draft is not None and not _same_pin(pin, expected_draft):
            raise SourceChanged('Draft changed after preparation.')
        if pin.status.casefold() != 'draft':
            raise InputError('target', 'Target must be a Draft.')
        _ensure_leaf(selection, model, pin, 'target')
        view = logical_view(pin.metadata, model)
        status = params['targetStatus']
        try:
            admitted = status in model.allowed(view.get('role'), view.get('form')) and canonical_status(model, view.get('role'), view.get('form'), status) == status
        except (StatusModelError, TypeError):
            admitted = False
        if (not isinstance(status, str) or status.casefold() in {'draft', 'archived'} or not admitted):
            allowed = model.allowed(view.get('role'), view.get('form')) - {'Draft', 'Archived'}
            raise InputError('targetStatus', 'Target Status is not an allowed Current Status.', allowed_values=allowed)
        pins = {ref: _promotion_predecessor(selection, ref, staged) for ref in _relations(pin)}
        if pin.version == 1 and _current_collision(selection, pin.atom_id):
            raise InputError('target', 'Draft identity already has a Current Atom.')
        # A same-identity Draft supersedes its current preceding revision even
        # when no replacement relation is required for the ordinary update.
        if pin.version > 1 and pin.atom_id not in pins:
            previous = _promotion_predecessor(selection, pin.atom_id, staged)
            if previous.version != pin.version - 1:
                raise InputError('target', 'Draft predecessor Version is stale.')
            pins[pin.atom_id] = previous
        if pin.atom_id in pins and pins[pin.atom_id].version != pin.version - 1:
            raise InputError('target', 'Draft predecessor Version is stale.')
        if staged is not None:
            if set(pins) != set(staged) or any(not _same_pin(pins[ref], previous) for ref, previous in staged.items()):
                raise SourceChanged('Replacement target changed after preparation.')
        if pin.version > 1:
            predecessor = pins[pin.atom_id]
            previous_view = logical_view(predecessor.metadata, model)
            draft_summary = _summary(parse_carrier(pin.raw, pin.path).body)
            previous_summary = _summary(parse_carrier(predecessor.raw, predecessor.path).body)
            if view.get('role') != previous_view.get('role') or draft_summary != previous_summary:
                raise InputError('target', 'A changed Summary or Content Role requires a new Atom ID at Version 1.')
        for predecessor in pins.values():
            if predecessor.status.casefold() != 'archived':
                _ensure_leaf(selection, model, predecessor, 'target')
        selected = source.select_sources(selection, [predecessor.ref_id for predecessor in pins.values()])
        for predecessor in pins.values():
            current = selected[predecessor.ref_id]
            if not _same_pin(current, predecessor):
                raise SourceChanged('Replacement target changed after resolution.')
        destination = _destination(selection, pin, status, model)
        raw = render_carrier(pin.raw, {'status': encode_status(status), 'ref_id': pin.atom_id,
                                       'destination': {'file': {'name': destination.name,
                                           'path': destination.parent.relative_to(selection.root).as_posix()}}})
        validate_candidate(selection, model, raw, destination)
        _check_destination(destination, pins.values(), 'target')
        predecessor = pins.get(pin.atom_id) if pin.version > 1 else None
        if (predecessor is not None and predecessor.status.casefold() != 'archived'
                and destination == predecessor.path
                and all(item.atom_id == predecessor.atom_id or item.status.casefold() == 'archived'
                        for item in pins.values())
                and same_authored_carrier(predecessor.raw, raw, model)
                and canonical_status(model, previous_view.get('role'), previous_view.get('form'), predecessor.status) == status):
            current = source.select_source(selection, predecessor.ref_id, expected_version=predecessor.version)
            draft = source.select_source(selection, pin.ref_id, expected_version=pin.version)
            if (current.path != predecessor.path or current.sha256 != predecessor.sha256
                    or draft.path != pin.path or draft.sha256 != pin.sha256):
                raise SourceChanged('Source changed before no-op promotion.')
            removed = effects.remove(selection.root, pin.path, pin.sha256)
            return result(effects=removed.effects, errors=removed.errors, warnings=warnings,
                          **({} if removed.errors else {'artifact': saved(selection, predecessor.path,
                              predecessor.atom_id, predecessor.ref_id, predecessor.version, status)}))
        for predecessor in pins.values():
            if predecessor.status.casefold() == 'archived':
                continue
            current = source.select_source(selection, predecessor.ref_id, expected_version=predecessor.version)
            if current.sha256 != predecessor.sha256:
                raise SourceChanged('Replacement target changed after resolution.')
            archived = archive_atom(selection, model, {'target': {'ref_id': predecessor.ref_id, 'version': predecessor.version}})
            all_effects.extend(archived['effects'])
            warnings.extend(archived.get('warnings', []))
            if archived['errors']:
                return result(effects=all_effects, errors=archived['errors'], warnings=warnings)
        current = source.select_source(selection, pin.ref_id, expected_version=pin.version)
        if current.sha256 != pin.sha256:
            raise SourceChanged('Draft changed after resolution.')
        with effects.publication_guard() as publication:
            written = write_destination(selection.root, destination, raw)
            all_effects.extend(written.effects)
            errors = list(written.errors)
            if not errors:
                removed = effects.remove(selection.root, pin.path, pin.sha256)
                all_effects.extend(removed.effects)
                errors.extend(removed.errors)
        if isinstance(publication, dict) and publication.get('error'):
            errors.append({'code': 'projection_refresh_failed', 'message': publication['error']})
        if errors:
            return result(effects=all_effects, errors=errors, warnings=warnings)
        return result(effects=all_effects, warnings=warnings,
                      artifact=saved(selection, destination, pin.atom_id, pin.atom_id, pin.version, status))
    except (InputError, ValueError, OSError, RuntimeError) as exc:
        if not all_effects and isinstance(exc, InputError):
            return result(outcome="needs_input", requested_input=exc.requested_input, warnings=warnings)
        return result(effects=all_effects, errors=[_error(exc)], warnings=warnings)


def promote_draft(selection, model, params):
    return _promote_draft(selection, model, params)


@trace('update')
def update_atom(selection, model, params, *, pending_source=None):  # noqa: C901
    """Compose Draft creation, exact predecessor archival and promotion."""
    from ATOM_LIFECYCLE.draft import prepare_draft, save_draft
    from ATOM_LIFECYCLE.state_actions import archive_atom

    all_effects, warnings = [], []
    old = None
    try:
        if not isinstance(params, dict) or set(params) - {'sourceCurrent', 'changes'} or 'sourceCurrent' not in params:
            raise InputError('sourceCurrent', 'Expected sourceCurrent and optional changes.')
        old = read_target(selection, params['sourceCurrent'], field='sourceCurrent')
        if pending_source is not None and old.sha256 != pending_source:
            return result(errors=[{'code': 'source_changed', 'message': 'The captured Current Atom changed while input was pending.',
                                   'field': 'sourceCurrent'}])
        if old.status.casefold() in {'draft', 'archived'}:
            raise InputError('sourceCurrent', 'Update requires a Current Atom.')
        # A content-only revision retains the parent Carrier location and its
        # existing child folder. Structural changes still require a leaf.
        changes = params.get('changes', {})
        content_only = isinstance(changes, dict) and bool(changes) and set(changes) <= {'body'}
        if not content_only:
            _ensure_leaf(selection, model, old, 'sourceCurrent')
        plan = prepare_draft(selection, model, params, source_pin=old)
        parsed = parse_carrier(plan['raw'], plan['destination'])
        proposed = source.SourcePin(plan['destination'], plan['atom_id'],
                                    f"{plan['atom_id']}@{plan['version']}-draft",
                                    plan['version'], 'Draft', hashlib.sha256(plan['raw']).hexdigest(),
                                    plan['raw'], parsed.metadata)
        view = logical_view(parsed.metadata, model)
        old_view = logical_view(old.metadata, model)
        try:
            status = canonical_status(model, old_view.get('role'), old_view.get('form'), old.status)
            if status not in model.allowed(view.get('role'), view.get('form')):
                raise StatusModelError('Captured Current Status is not admitted for the proposed Role and Form.')
        except StatusModelError as error:
            raise InputError('sourceCurrent', 'Captured Current Status is not allowed on the proposed Atom.') from error
        targets = {ref: resolve_replacement(selection, ref) for ref in _relations(proposed)}
        if proposed.version == 1 and _current_collision(selection, proposed.atom_id):
            raise InputError('sourceCurrent', 'Proposed identity already has a Current Atom.')
        destination = _destination(selection, proposed, status, model)
        candidate = render_carrier(proposed.raw, {'status': encode_status(status), 'ref_id': proposed.atom_id,
            'destination': {'file': {'name': destination.name,
                'path': destination.parent.relative_to(selection.root).as_posix()}}})
        validate_candidate(selection, model, candidate, destination)
        for target in targets.values():
            if target.status.casefold() != 'archived':
                _ensure_leaf(selection, model, target, 'relations')
            selected = source.select_source(selection, target.ref_id, expected_version=target.version)
            if selected.sha256 != target.sha256:
                raise SourceChanged('Replacement target changed during preparation.')
        if content_only and (plan['atom_id'] != old.atom_id or destination != old.path):
            _ensure_leaf(selection, model, old, 'sourceCurrent')
            content_only = False
        _check_destination(destination, (old, *targets.values()), 'changes')
        if (proposed.atom_id == old.atom_id and destination == old.path
                and all(target.atom_id == old.atom_id or target.status.casefold() == 'archived'
                        for target in targets.values())
                and same_authored_carrier(old.raw, candidate, model)):
            current = read_target(selection, params['sourceCurrent'], field='sourceCurrent')
            if current.path != old.path or current.sha256 != old.sha256:
                raise SourceChanged('Source changed before no-op update.')
            return result(warnings=warnings, artifact=saved(selection, old.path, old.atom_id,
                          old.ref_id, old.version, status))
        created = save_draft(selection, plan)
        all_effects.extend(created['effects'])
        warnings.extend(created.get('warnings', []))
        if created['errors']:
            return result(effects=all_effects, errors=created['errors'], warnings=warnings)
        draft = created['savedDraft']
        checked_draft = source.select_source(selection, draft['ref_id'], expected_version=draft['version'])
        if not _same_pin(checked_draft, proposed):
            raise SourceChanged('Draft changed after creation.')
        _ensure_leaf(selection, model, checked_draft, 'target')
        if checked_draft.atom_id == old.atom_id and checked_draft.version != old.version + 1:
            raise InputError('target', 'Draft predecessor Version is stale.')
        if checked_draft.atom_id != old.atom_id and _current_collision(selection, checked_draft.atom_id):
            raise InputError('target', 'Draft identity already has a Current Atom.')
        for target in targets.values():
            selected_target = source.select_source(selection, target.ref_id, expected_version=target.version)
            if not _same_pin(selected_target, target):
                raise SourceChanged('Replacement target changed after Draft creation.')
        _check_destination(destination, (old, *targets.values()), 'target')
        current = read_target(selection, params['sourceCurrent'], field='sourceCurrent')
        if current.sha256 != old.sha256:
            raise SourceChanged('Source changed after Draft creation.')
        if content_only:
            from ATOM_LIFECYCLE.state_actions import _prepare_archive, _publish
            archive_path, archive_raw, archived_ref = _prepare_archive(selection, model, current)
            archived = _publish(selection, current, archive_path, archive_raw, 'Archived', archived_ref)
        else:
            archived = archive_atom(selection, model, {'target': params['sourceCurrent']})
        all_effects.extend(archived['effects'])
        warnings.extend(archived.get('warnings', []))
        if archived['errors']:
            return result(effects=all_effects, errors=archived['errors'], warnings=warnings)
        archived_ref = f'{old.atom_id}@{old.version}'
        selected = source.select_sources(selection, [archived_ref, draft['ref_id']])
        archived_pin = selected[archived_ref]
        if old.atom_id in targets or draft['atom_id'] == old.atom_id:
            targets[old.atom_id] = archived_pin
        draft_pin = selected[draft['ref_id']]
        if not _same_pin(draft_pin, proposed):
            raise SourceChanged('Draft changed after creation.')
        promoted = _promote_draft(selection, model, {'target': {'ref_id': draft['ref_id'],
                                      'version': draft['version']}, 'targetStatus': status}, staged=targets,
                                  expected_draft=draft_pin)
        all_effects.extend(promoted['effects'])
        warnings.extend(promoted.get('warnings', []))
        if promoted['outcome'] == 'needs_input':
            errors = [{'code': 'invalid_input', 'field': field,
                       'message': details.get('error', 'Promotion needs additional input.')}
                      for field, details in promoted.get('requested_input', {}).items()]
            return result(effects=all_effects, warnings=warnings,
                          errors=errors or [{'code': 'invalid_input', 'message': 'Promotion needs additional input.'}])
        data = {'artifact': promoted['artifact']} if 'artifact' in promoted else {}
        return result(effects=all_effects, errors=promoted['errors'], warnings=warnings, **data)
    except (InputError, ValueError, OSError, RuntimeError) as exc:
        if not all_effects and isinstance(exc, InputError):
            return result(outcome="needs_input", requested_input=exc.requested_input, warnings=warnings,
                          pending_source=old.sha256 if old is not None and old.status.casefold() not in {'draft', 'archived'} else None)
        return result(effects=all_effects, errors=[_error(exc)], warnings=warnings)
