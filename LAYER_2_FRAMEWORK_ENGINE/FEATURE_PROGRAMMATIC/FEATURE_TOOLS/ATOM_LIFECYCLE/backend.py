# CA-M-405@14
# CA-M-465@29
# CA-R-1105@28
# CA-O-10009@2
# CA-O-10011@3
# CA-O-10016@2
# CA-O-10018@2
# CA-O-10023@2
# CA-O-10024@3

"""Runtime backend for the six adopted Atom Lifecycle Tools."""

from __future__ import annotations

from .timing import lifecycle_tool

from contextlib import contextmanager, nullcontext
import fcntl
import os
import stat

from project_runtime import owned_temporary_root
from VALIDATE_ATOMS.validate_atoms_workers.read_io import open_regular

from .common import InputError, SourceChanged, logical_container, result
from .carrier import logical_view
from .draft import create_draft
from .placement_model import bind_placement
from .publish import _error, _relations, promote_draft, update_atom
from .source import ArchiveNotLoadedError, SourceSelectionError, _selector, query_reader, select_sources
from .state_actions import archive_workflow, direct_update
from .status_cascade import change_status_workflow


ROUTES = {
    "atom_lifecycle_create_draft": create_draft,
    "atom_lifecycle_archive": archive_workflow,
    "atom_lifecycle_change_status": change_status_workflow,
    "atom_lifecycle_direct_update": direct_update,
    "atom_lifecycle_promote_draft": promote_draft,
    "atom_lifecycle_update": update_atom,
}


def _batch_targets(selection, name, params):
    fields = {'target'} if name == 'atom_lifecycle_archive' else {'target', 'targetStatus'}
    targets = params.get('targets')
    if set(params) != {'targets'} or not isinstance(targets, list) or not targets:
        raise InputError('targets', 'Supply a nonempty list of target operations.')
    for entry in targets:
        if not isinstance(entry, dict) or set(entry) != fields:
            raise InputError('targets', 'Each target must contain exactly the required fields.')
        target = entry['target']
        if (not isinstance(target, dict) or set(target) != {'ref_id', 'version'}
                or not isinstance(target['ref_id'], str) or type(target['version']) is not int
                or target['version'] < 1):
            raise InputError('targets', 'Each target requires an Atom reference and positive Version.')
        try:
            _, revision, draft = _selector(selection, target['ref_id'], target['version'])
        except SourceSelectionError as error:
            raise InputError('targets', 'Each target requires a valid Atom reference and Version.') from error
        if ((name == 'atom_lifecycle_archive' and revision is not None)
                or (name == 'atom_lifecycle_promote_draft' and not draft)):
            raise InputError('targets', 'Each target must match the requested lifecycle operation.')
        if 'targetStatus' in entry and (not isinstance(entry['targetStatus'], str) or not entry['targetStatus'].strip()):
            raise InputError('targets', 'Each promotion requires a target Status.')
    return targets


def _flat_targets(selection, model, targets):
    refs = [entry['target']['ref_id'] for entry in targets]
    identities = [_selector(selection, ref, None)[0] for ref in refs]
    if len(set(identities)) != len(identities):
        return None
    pins = select_sources(selection, refs)
    for entry in targets:
        pin = pins[entry['target']['ref_id']]
        if pin.version != entry['target']['version']:
            return None
        view = logical_view(pin.metadata, model)
        role = str(view.get('role', '')).casefold()
        if role in {'plan', 'operations'} or set(logical_container({}, view)) != {'scope_unit'}:
            return None
        companion = pin.path.with_suffix('')
        if companion.exists() or companion.is_symlink():
            return None
    return pins


def _independent_promotion(selection, targets, pins, reader):
    # Only group promotions whose previous Current has already been archived.
    if any(_relations(pin) or pin.version <= 1 for pin in pins.values()):
        return False
    ids = tuple(pin.atom_id for pin in pins.values())
    if reader.lifecycle_candidates(selection, atom_ids=ids, references=ids):
        return False
    refs = [f'{pin.atom_id}@{pin.version - 1}' for pin in pins.values()]
    predecessors = select_sources(selection, refs)
    return all(predecessors[ref].status.casefold() == 'archived' for ref in refs)


def _batch_refresh(selection, model, name, targets):
    reader = query_reader()
    if reader is None or not callable(getattr(reader, 'group_lifecycle_refresh', None)):
        return nullcontext()
    try:
        pins = _flat_targets(selection, model, targets)
        if pins is None or (name == 'atom_lifecycle_promote_draft'
                            and not _independent_promotion(selection, targets, pins, reader)):
            return nullcontext()
    except (OSError, RuntimeError, TypeError, ValueError, KeyError):
        return nullcontext()
    return reader.group_lifecycle_refresh()


def _batch(selection, model, name, params, action):
    targets = _batch_targets(selection, name, params)
    with _batch_refresh(selection, model, name, targets) as publication:
        outcome = _batch_run(selection, model, targets, action)
    if publication and publication.get('error'):
        outcome['outcome'] = 'failed'
        outcome.setdefault('errors', []).append(
            {'code': 'projection_refresh_failed', 'message': publication['error']})
    return outcome


def _batch_run(selection, model, targets, action):
    effects, warnings, target_results = [], [], []
    for index, entry in enumerate(targets):
        try:
            outcome = action(selection, model, entry)
        except InputError as error:
            outcome = result(outcome='needs_input', requested_input=error.requested_input)
        except (OSError, RuntimeError, ValueError) as error:
            if isinstance(error, (SourceSelectionError, SourceChanged)):
                code = ('archive_not_loaded' if isinstance(error, ArchiveNotLoadedError) else
                        'source_selection_failed' if isinstance(error, SourceSelectionError) else 'source_changed')
                outcome = result(errors=[{'code': code, 'message': str(error)}])
            else:
                outcome = result(errors=[_error(error)])
        effects.extend(outcome.get('effects', []))
        warnings.extend(outcome.get('warnings', []))
        target_results.append({'target': entry['target'], **outcome})
        if outcome.get('outcome') != 'completed' or outcome.get('errors'):
            errors = outcome.get('errors') or [
                {'code': 'invalid_input', 'field': field, 'message': detail.get('error')}
                for field, detail in outcome.get('requested_input', {}).items()
            ] or [{'code': 'backend_failure', 'message': 'Lifecycle operation failed.'}]
            return result(effects=effects, errors=errors, warnings=warnings,
                          target_results=target_results, remaining_targets=targets[index + 1:])
    return result(effects=effects, warnings=warnings, target_results=target_results, remaining_targets=[])


@contextmanager
def _project_write_lock(root):
    temporary = owned_temporary_root(root, "atom_lifecycle")
    directory = open_regular(temporary, directory=True)
    try:
        flags = os.O_RDWR | os.O_CREAT | os.O_NOFOLLOW | os.O_NONBLOCK
        lock = os.open("write.lock", flags, mode=0o600, dir_fd=directory)
        try:
            if not stat.S_ISREG(os.fstat(lock).st_mode):
                raise OSError("Lifecycle write lock is not a regular file.")
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            yield
        finally:
            os.close(lock)
    finally:
        os.close(directory)


@lifecycle_tool
def execute(selection, model, name, params, *, pending_source=None):
    action = ROUTES.get(name)
    if action is None:
        return result(errors=[{"code": "unsupported_operation", "message": "Unknown lifecycle Tool."}])
    placement = getattr(getattr(model, 'candidate_schema', None), 'placement', None)
    if placement is None:
        return result(errors=[{"code": "placement_model_unavailable",
                               "message": "The installed model has no compiled Atom placement rules."}])
    try:
        with bind_placement(placement), _project_write_lock(selection.root):
            if isinstance(params, dict) and 'targets' in params and name in {
                    'atom_lifecycle_archive', 'atom_lifecycle_promote_draft'}:
                return _batch(selection, model, name, params, action)
            if action is update_atom:
                return action(selection, model, params, pending_source=pending_source)
            return action(selection, model, params)
    except InputError as error:
        return result(outcome="needs_input", requested_input=error.requested_input)
    except SourceChanged as error:
        return result(errors=[{"code": "source_changed", "message": str(error)}])
    except SourceSelectionError as error:
        code = "archive_not_loaded" if isinstance(error, ArchiveNotLoadedError) else "source_selection_failed"
        return result(errors=[{"code": code, "message": str(error)}])
    except BlockingIOError:
        return result(errors=[{"code": "project_busy", "message": "Another lifecycle write is in progress."}])
    except (OSError, RuntimeError, ValueError) as error:
        return result(errors=[_error(error)])
