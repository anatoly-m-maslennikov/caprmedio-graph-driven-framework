# CA-D-282@26
# CA-D-283@34
# CA-D-296@33
# CA-D-461@33
# CA-D-475@28
# CA-D-466@27
# CA-D-565@28
# CA-D-716@4

"""Private derivation of a single admitted Atom's Markdown Carrier path.

The caller supplies model-admitted properties and a verified containing Carrier;
this module does not select a Status, admit containment, or perform effects.
CA-D-651 leaves nonzero numeric Tier tokens to other registered grammar; this helper
only implements the ordinary grammar that omits them. External Project Goal
and Scope Unit Declaration grammars are not implemented here (CA-D-651).
"""
from __future__ import annotations

from .timing import trace

from dataclasses import dataclass
from pathlib import Path
import re

from carrier_aliases import carrier_read_view
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier
from project_selection import ProjectSelection
from scope_unit_declarations import read_scope_unit_declarations

from .common import InputError, logical_container
from .carrier import logical_view
from .placement_model import active_placement
from .source import query_reader, select_context, select_source


class PlacementError(ValueError):
    """Placement is unsafe, ambiguous, or not covered by the selected rules."""


@dataclass(frozen=True)
class ContainerCarrier:
    path: Path
    status: str

    def __fspath__(self):
        return str(self.path)


def _token(value: str) -> str:
    if not isinstance(value, str) or not re.fullmatch(r"[A-Za-z0-9]+(?:[ _-][A-Za-z0-9]+)*", value):
        raise PlacementError("Unsupported structured filename token")
    return re.sub(r"[ _-]+", "_", value).upper()


def _slug(summary: str) -> str:
    # Refuse cases whose transliteration is not specified by CA-D-282.
    if not isinstance(summary, str) or not summary.isascii() or not summary.isprintable():
        raise PlacementError("Unsupported Summary serialization")
    slug = re.sub(r"[^A-Za-z0-9]+", "-", summary).strip("-").lower()
    if not slug:
        raise PlacementError("Unsupported Summary serialization")
    return slug


def _inside(path: Path, root: Path) -> Path:
    if not path.is_absolute() or ".." in path.parts or not path.is_relative_to(root):
        raise PlacementError("Carrier context is outside the selected Project")
    # Existing symlinks must not redirect a derived destination.
    if path.resolve(strict=False) != path:
        raise PlacementError("Carrier context traverses a symlink")
    return path


@trace('placement.resolve_container')
def resolve_container(selection, view, atom_id, seen=frozenset(), *, model=None):
    if atom_id in seen or len(seen) >= 32:
        raise InputError('container', 'Containing Atom chain is cyclic or too deep.')
    container = logical_container({}, view)
    if 'scope_unit' in container:
        return container['scope_unit'], None
    ref = container['atom']
    if '@' in ref:
        raise InputError('container', 'Containing Atom must use a Current reference.')
    parent = select_context(selection, ref) if query_reader() is not None else select_source(selection, ref)
    parent_view = logical_view(parent.metadata, model)
    role, form = view.get('role'), view.get('form')
    if not _admitted_parent(role, form, parent_view, parent.status):
        raise InputError('container', 'Containing Atom Role or Form is unsupported.')
    scope, grandparent = resolve_container(selection, parent_view, parent.atom_id, seen | {atom_id}, model=model)
    expected = expected_status_directory(selection, role, parent.status, scope, grandparent)
    if parent.path.parent != expected:
        raise InputError('container', 'Containing Atom location disagrees with its declaration.')
    directory = parent.path.with_suffix('')
    shared_backlog = role == 'Plan' and active_placement().placement('Plan', 'Backlog')[0] == 'role'
    if (directory.resolve(strict=False) != directory
            or (not directory.is_dir() and not (shared_backlog and not directory.exists()))):
        raise InputError('container', 'Containing Atom directory is missing or unsafe.')
    return scope, ContainerCarrier(directory, parent.status) if role == 'Plan' else directory


def _admitted_parent(role, form, parent, status):
    if parent.get('role') != role or status.casefold() in {'draft', 'archived'}:
        return False
    if role == 'Plan':
        return True
    parent_form = {'Step': 'Workflow', 'Substep': 'Step', 'Sub-step': 'Step'}.get(form)
    return role == 'Operations' and parent_form is not None and parent.get('form') == parent_form


@trace('placement.scope_authority')
def _role_root(selection, role, scope_unit):
    reader = query_reader()
    if reader is None:
        selection._revalidate_boundary()
    declarations = (reader.lifecycle_declarations() if reader is not None else
                    read_scope_unit_declarations(selection.root, selection.control_relative))
    if declarations.digest != selection.declaration_digest:
        raise PlacementError("Project declarations are stale")
    prefix = selection.settings["artifacts"]["identity"]["project_prefix"]
    rows = [row for row in selection.structure["scope_units"] if scope_unit is not None and
            (scope_unit in (row["scope_unit_name"], row["scope_unit_id"]) or
             (row["parent"] == "PROJECT" and scope_unit == f"{prefix}-SU-00"))]
    if len(rows) != 1:
        raise PlacementError("Scope Unit is missing or ambiguous")
    authority = _inside(selection.root / rows[0]["authority_path"], selection.root)
    role_root = _inside(authority / active_placement().role_folder(role), selection.root)
    return rows[0], role_root


def _scope_binding(selection, atom_id, version, role, scope_unit, parent):
    prefix = selection.settings['artifacts']['identity']['project_prefix']
    if not isinstance(atom_id, str) or not re.fullmatch(re.escape(prefix) + r"-[A-Z]-[0-9]+", atom_id):
        raise PlacementError("Invalid canonical Atom ID")
    if type(version) is not int or version < 1:
        raise PlacementError("Invalid Version or unsupported Role")
    row, role_root = _role_root(selection, role, scope_unit)
    if parent is not None:
        if role not in ("Plan", "Operations"):
            raise PlacementError("Unsupported containing Carrier")
        parent_path = _inside(Path(parent), role_root)
        shared_backlog = (role == 'Plan' and isinstance(parent, ContainerCarrier)
                          and active_placement().placement('Plan', 'Backlog')[0] == 'role')
        if parent_path == role_root or (not parent_path.is_dir() and not (shared_backlog and not parent_path.exists())):
            raise PlacementError("Containing Carrier must be an existing directory")
        parent = ContainerCarrier(parent_path, parent.status) if isinstance(parent, ContainerCarrier) else parent_path
    return row, role_root, parent


def _status_directory(role_root, role, status, parent):
    base, folder = active_placement().placement(role, status)
    if (role == 'Plan' and status.casefold() == 'backlog' and base == 'role'
            and isinstance(parent, ContainerCarrier) and parent.status.casefold() == 'backlog'):
        return parent.path
    return (role_root if base == 'role' else Path(parent) if parent is not None else role_root) / folder


def shared_plan_backlog_directory(selection, scope):
    _, role_root = _role_root(selection, 'Plan', scope)
    base, folder = active_placement().placement('Plan', 'Backlog')
    return _inside(role_root / folder, selection.root) if base == 'role' else None


def expected_status_directory(selection, role, status, scope, parent):
    _, role_root = _role_root(selection, role, scope)
    if parent is not None:
        _inside(Path(parent), role_root)
    return _inside(_status_directory(role_root, role, status, parent), selection.root)


def archived_owner(selection, path, role):
    """Locate an exact Archived revision in a declared Scope Unit's Role area."""
    placement = active_placement()
    role_dir = placement.role_folder(role)
    base, _ = placement.placement(role, 'Archived')
    if base != 'role':
        raise InputError('target', 'Archived placement is not Role-owned.')
    for row in selection.structure["scope_units"]:
        directory = selection.root / row["authority_path"] / role_dir
        if path.parent in {directory / folder for folder in placement.archive_folders(role)}:
            return row["scope_unit_name"]
    raise InputError('target', 'Archived Atom is outside a shared Role archive.')


def _predecessor_status(source, atom_id, version):
    if not source.is_file():
        raise PlacementError("Exact predecessor Carrier is missing")
    reader = query_reader()
    raw = reader.lifecycle_read(source) if reader is not None else source.read_bytes()
    view = carrier_read_view(parse_carrier(raw, source).metadata)
    old_status = view.get("status")
    if (view.get("atom_id") != atom_id or type(view.get("version")) is not int or view.get("version") != version or
            not isinstance(old_status, str) or not re.fullmatch(r"[A-Za-z]+", old_status) or
            old_status.casefold() in {"draft", "archived"}):
        raise PlacementError("Predecessor identity, Version or Current Status is invalid")
    return old_status.casefold()


def _archive_destination(root, role_root, parent, role, atom_id, version, source_path):
    if source_path is None:
        raise PlacementError("Archival requires the exact source Carrier")
    source = _inside(Path(source_path), role_root)
    old_state = _predecessor_status(source, atom_id, version)
    model = active_placement()
    if source.parent != _status_directory(role_root, role, old_state, parent):
        raise PlacementError("Predecessor Status does not match its location")
    # Preserve the actual old components, without normalizing legacy names.
    match = re.fullmatch(r"((?:[1-9][0-9]*-)?)" + re.escape(atom_id) + r"(?!@)(.*)\.md", source.name)
    if not match:
        raise PlacementError("Unsupported predecessor filename")
    stem = match.group(1) + atom_id + "@" + str(version) + match.group(2)
    archive_base, archive_folder = model.placement(role, 'Archived')
    if archive_base != 'role':
        raise PlacementError('Archived placement is not Role-owned')
    return _inside(role_root / archive_folder / (stem + ".md"), root)


def _plan_placement(marker, effective_label, target_scope, work_sequence):
    if work_sequence is not None and (type(work_sequence) is not int or work_sequence < 1):
        raise PlacementError("Invalid Work Sequence Number")
    stem = (f"{work_sequence}-" if work_sequence is not None else "") + marker
    if effective_label:
        stem += "-" + _token(effective_label)
    if target_scope is not None:
        raise PlacementError("Plan target token is unsupported")
    return stem


def _ordinary_placement(marker, effective_label, target_scope, work_sequence, row, tier):
    if work_sequence is not None:
        raise PlacementError("Work Sequence Number applies only to Plan")
    stem = marker
    if row["parent"] != "PROJECT":
        stem += "-" + _token(row["scope_unit_name"])
    if tier == 0:
        stem += "-SCOPE_CONTRACT"
    if effective_label:
        stem += "-" + _token(effective_label)
    if target_scope:
        stem += "-" + _token(target_scope)
    return stem


def derive_filename(*, atom_id, version, status, role, summary, row, form=None,
                    label=None, tier=None, target_scope=None, work_sequence=None):
    """Serialize the supported Current/Draft filename grammar without I/O."""
    if type(version) is not int or version < 1 or not isinstance(atom_id, str):
        raise PlacementError("Invalid Atom identity or Version")
    if tier is not None and (type(tier) is not int or tier < 0):
        raise PlacementError("Invalid Tier")
    state = status.casefold() if isinstance(status, str) else None
    marker = atom_id + (f"@{version}-draft" if state == "draft" else "")
    effective_label = form if label is None or label == "" else label
    if role == "Plan":
        stem = _plan_placement(marker, effective_label, target_scope, work_sequence)
    else:
        stem = _ordinary_placement(marker, effective_label, target_scope, work_sequence, row, tier)
    return stem + "--" + _slug(summary) + ".md"


@trace('placement.derive_destination')
def derive_destination(selection: ProjectSelection, *, atom_id: str, version: int,
                       status: str | None, role: str, summary: str, scope_unit: str,
                       form: str | None = None, label: str | None = None,
                       tier: int | None = None, target_scope: str | None = None,
                       parent: Path | None = None, source_path: Path | None = None,
                       work_sequence: int | None = None, archived_update: bool = False) -> Path:
    """Derive a project-bound path; parent is an already verified local container.

    source_path is required for archival and preserves the exact predecessor's
    filename components. For Plan, parent identifies the declared immediate
    containing Plan's directory. For Operations, it identifies an admitted
    Workflow/Step grouping directory. Other parent groupings are unsupported.
    """
    if not isinstance(selection, ProjectSelection):
        raise PlacementError("Project selection is required")
    try:
        row, role_root, parent = _scope_binding(selection, atom_id, version, role, scope_unit, parent)
        if status is not None and (not isinstance(status, str) or not re.fullmatch(r"[A-Za-z]+", status)):
            raise PlacementError("Invalid admitted Status")
        state = status.casefold() if status else None
        if state == "archived" and not archived_update:
            return _archive_destination(selection.root, role_root, parent, role, atom_id, version, source_path)
        if archived_update and (state != "archived" or parent is not None or source_path is not None):
            raise PlacementError("Archived update requires a scope-owned Carrier")
        if source_path is not None:
            raise PlacementError("Source path applies only to exact predecessor archival")
        if tier is not None and (type(tier) is not int or tier < 0):
            raise PlacementError("Invalid Tier")
        name = derive_filename(atom_id=atom_id, version=version, status=status, role=role,
                               summary=summary, row=row, form=form, label=label, tier=tier,
                               target_scope=target_scope, work_sequence=work_sequence)
        if archived_update:
            name = name.replace(atom_id, f"{atom_id}@{version}", 1)
        directory = _status_directory(role_root, role, status, parent)
        return _inside(directory / name, selection.root)
    except PlacementError:
        raise
    except (KeyError, TypeError, ValueError, OSError) as error:
        raise PlacementError("Cannot derive placement from the selected Project") from error
