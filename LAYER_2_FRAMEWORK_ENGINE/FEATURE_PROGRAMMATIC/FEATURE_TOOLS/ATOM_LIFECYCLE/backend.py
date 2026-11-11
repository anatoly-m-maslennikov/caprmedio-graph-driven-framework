# CA-O-10009@2
# CA-O-10011@3
# CA-O-10016@2
# CA-O-10018@2
# CA-O-10023@2
# CA-O-10024@3

"""Runtime backend for the six adopted Atom Lifecycle Tools."""

from __future__ import annotations

from contextlib import contextmanager
import fcntl
import os
import stat

from project_runtime import owned_temporary_root
from VALIDATE_ATOMS.validate_atoms_workers.read_io import open_regular

from .common import InputError, SourceChanged, result
from .draft import create_draft
from .placement_model import bind_placement
from .publish import PromotionPending, promote_draft, update_atom
from .source import SourceSelectionError
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


def execute(selection, model, name, params, *, pending_source=None, pending_promotion=None):
    prior = {'effects': pending_promotion.effects, 'warnings': pending_promotion.warnings} if isinstance(pending_promotion, PromotionPending) else {}
    action = ROUTES.get(name)
    if action is None:
        return result(**prior, errors=[{"code": "unsupported_operation", "message": "Unknown lifecycle Tool."}])
    if pending_promotion is not None and action is not update_atom:
        return result(**prior, errors=[{"code": "invalid_input", "message": "Pending promotion requires Update."}])
    placement = getattr(getattr(model, 'candidate_schema', None), 'placement', None)
    if placement is None:
        return result(**prior, errors=[{"code": "placement_model_unavailable",
                               "message": "The installed model has no compiled Atom placement rules."}])
    try:
        with bind_placement(placement), _project_write_lock(selection.root):
            if action is update_atom:
                return action(selection, model, params, pending_source=pending_source, pending_promotion=pending_promotion)
            return action(selection, model, params)
    except InputError as error:
        return result(**prior, outcome="needs_input", requested_input=error.requested_input)
    except SourceChanged as error:
        return result(**prior, errors=[{"code": "source_changed", "message": str(error)}])
    except SourceSelectionError as error:
        return result(**prior, errors=[{"code": "source_selection_failed", "message": str(error)}])
    except BlockingIOError:
        return result(**prior, errors=[{"code": "project_busy", "message": "Another lifecycle write is in progress."}])
    except (OSError, RuntimeError, ValueError):
        return result(**prior, errors=[{"code": "backend_failure", "message": "Lifecycle operation failed."}])
