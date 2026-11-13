# CA-O-10009@2
# CA-R-1521@32
# CA-D-461@33
# CA-D-475@28
"""Read-only selection of latest Atoms in a matching Carrier tree."""
from __future__ import annotations

import os
from pathlib import Path
import re
import stat

from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext
from VALIDATE_ATOMS.validate_atoms_workers.parsing import CarrierError
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS

from .carrier import logical_view
from .common import InputError, logical_container
from .source import (SourceSelectionError, _read_candidate, query_candidates, query_reader,
                     select_current_sources, select_source)
from .placement import ContainerCarrier, _admitted_parent, _role_root, _status_directory, resolve_container
from .placement_model import active_placement


def _fail(message):
    raise InputError('target', message)


def _walk_error(error):
    raise error


def _atom_paths(selection, directory):
    prefix = selection.settings['artifacts']['identity']['project_prefix']
    atom_name = re.compile(r'^(?:[1-9][0-9]*-)?(' + re.escape(prefix) + r'-[A-Z]-[0-9]+)(?=[@.-])')
    atom_prefix = re.compile(r'^(?:[1-9][0-9]*-)?' + re.escape(prefix) + r'-[A-Z]-')
    reader = ReadContext(roots=[str(selection.root)], limits=dict(CEILINGS))
    if query_reader() is not None:
        indexed = query_candidates(selection, under=directory)
        return sorted((path, atom_id) for atom_id, paths in indexed.items() for path in paths
                      if path.is_relative_to(directory)), reader
    paths = []
    count = 0
    for root, dirs, files in os.walk(directory, followlinks=False, onerror=_walk_error):
        for name in dirs + files:
            reader.checkpoint()
            count += 1
            if count > reader.limits['max_candidates']:
                _fail('Carrier tree entry limit exceeded')
            path = Path(root) / name
            mode = path.lstat().st_mode
            if not (stat.S_ISDIR(mode) or stat.S_ISREG(mode)):
                _fail('Unsafe asset in Carrier companion directory')
            if name in files and name.endswith('.md') and atom_prefix.match(name):
                match = atom_name.match(name)
                if not match:
                    _fail('Malformed Atom Markdown in Carrier tree')
                paths.append((path, match.group(1)))
    return sorted(paths), reader


def _retained_version(path, atom_id):
    marker = re.match(r'(?:[1-9][0-9]*-)?' + re.escape(atom_id) + r'@([1-9][0-9]*)(-draft)?(?=-|\.)', path.name)
    suffix = re.search(r'@([1-9][0-9]*)\.md$', path.name)
    if marker:
        if marker.group(2) or suffix:
            _fail('Carrier tree contains a Draft or malformed revision')
        return marker.group(1)
    if suffix:
        return suffix.group(1)
    if '@' in path.name:
        _fail('Carrier tree contains malformed revision Markdown')
    return None


def _select_pins(selection, parent_pin, model, paths, reader):
    pins = {parent_pin.atom_id: parent_pin}
    retained = set()
    current = {}
    parent_role = logical_view(parent_pin.metadata, model).get('role')
    for path, atom_id in paths:
        version = _retained_version(path, atom_id)
        if version is not None:
            ref = f'{atom_id}@{version}'
            if (ref in retained or _read_candidate(
                    reader, path, ref, atom_id, version, None, retained_history=True) is None):
                _fail('Carrier tree contains duplicate or invalid retained history')
            retained.add(ref)
            continue
        if atom_id in current or atom_id == parent_pin.atom_id:
            _fail('Carrier tree contains duplicate or misplaced Current Atom Markdown')
        current[atom_id] = path
    for atom_id, pin in select_current_sources(selection, list(current)).items():
        if pin.path != current[atom_id]:
            _fail('Carrier tree contains duplicate or misplaced Current Atom Markdown')
        view = logical_view(pin.metadata, model)
        if view.get('role') != parent_role:
            _fail('Carrier tree contains unsupported Atom Markdown')
        pins[atom_id] = pin
    revisions = (ref.rsplit('@', 1) for ref in retained)
    if any(atom_id in pins and int(version) >= pins[atom_id].version for atom_id, version in revisions):
        _fail('Retained revision is not older than the Current Atom')
    if reader.currentness()['state'] != 'unchanged':
        _fail('Carrier tree changed during selection')
    return pins


def _ordered_pins(parent_pin, pins, model, role_root):
    children = {atom_id: [] for atom_id in pins}
    for atom_id, pin in pins.items():
        if atom_id == parent_pin.atom_id:
            continue
        view = logical_view(pin.metadata, model)
        owner = logical_container({}, view).get('atom')
        if owner not in pins or owner == atom_id:
            _fail('Atom containment does not match its companion directory')
        parent = pins[owner]
        parent_view = logical_view(parent.metadata, model)
        role = view.get('role')
        if not _admitted_parent(role, view.get('form'), parent_view, parent.status):
            _fail('Atom Role or Form is unsupported for its container')
        container = ContainerCarrier(parent.path.with_suffix(''), parent.status)
        directory = _status_directory(role_root, role, pin.status, container)
        if pin.path.parent != directory:
            _fail('Atom placement does not match its declared container and Status')
        children[owner].append(atom_id)
    ordered = []
    visiting = set()

    def visit(atom_id):
        if atom_id in visiting:
            _fail('Atom containment is cyclic')
        visiting.add(atom_id)
        for child in sorted(children[atom_id]):
            visit(child)
        ordered.append(pins[atom_id])

    visit(parent_pin.atom_id)
    if len(ordered) != len(pins):
        _fail('Carrier tree contains disconnected Atoms')
    return tuple(ordered)


def _shared_paths(selection, directory, prefix, reader):
    if query_reader() is not None:
        for atom_id, paths in query_candidates(selection, under=directory).items():
            for path in paths:
                if path.parent == directory and _retained_version(path, atom_id) is None:
                    yield path, atom_id
        return
    pattern = re.compile(r'^(?:[1-9][0-9]*-)?(' + re.escape(prefix) + r'-[A-Z]-[0-9]+)(?=[@.-])')
    atom_prefix = re.compile(r'^(?:[1-9][0-9]*-)?' + re.escape(prefix) + r'-[A-Z]-')
    with os.scandir(directory) as entries:
        for count, entry in enumerate(entries, 1):
            reader.checkpoint()
            if count > reader.limits['max_candidates']:
                _fail('Shared Backlog entry limit exceeded')
            if entry.is_symlink():
                _fail('Unsafe asset in shared Backlog directory')
            if not (entry.is_file(follow_symlinks=False) or entry.is_dir(follow_symlinks=False)):
                _fail('Unsafe asset in shared Backlog directory')
            if not entry.is_file(follow_symlinks=False) or not entry.name.endswith('.md'):
                continue
            match = pattern.match(entry.name)
            if not match:
                if atom_prefix.match(entry.name):
                    _fail('Malformed Atom Markdown in shared Backlog directory')
                continue
            path, atom_id = Path(entry.path), match.group(1)
            if _retained_version(path, atom_id) is None:
                yield path, atom_id


def _shared_candidates(selection, directory, model):
    if directory is None:
        return {}, None
    if directory.is_symlink():
        _fail('Shared Backlog directory is unsafe')
    if not directory.exists():
        return {}, None
    if not directory.is_dir() or directory.resolve() != directory:
        _fail('Shared Backlog directory is unsafe')
    prefix = selection.settings['artifacts']['identity']['project_prefix']
    reader = ReadContext(roots=[str(selection.root)], limits=dict(CEILINGS))
    candidates = {}
    for path, atom_id in _shared_paths(selection, directory, prefix, reader):
        pin = _read_candidate(reader, path, atom_id, atom_id, None, None)
        if pin is None:
            _fail('Shared Backlog contains a projection')
        view = logical_view(pin.metadata, model)
        container = view.get('container')
        if not isinstance(container, dict) or 'atom' not in container:
            continue
        if view.get('role') != 'Plan' or pin.status.casefold() != 'backlog':
            _fail('Shared Backlog contains misplaced Current Atom Markdown')
        owner = logical_container({}, view).get('atom')
        candidates.setdefault(owner, []).append(pin)
    return candidates, reader


def _companion_pins(selection, pin, model):
    directory = pin.path.with_suffix('')
    if directory.is_symlink():
        _fail('Carrier companion directory is unsafe')
    if not directory.exists():
        return {pin.atom_id: pin}
    if not directory.is_dir() or directory.resolve() != directory:
        _fail('Carrier companion directory is unsafe')
    paths, reader = _atom_paths(selection, directory)
    return _select_pins(selection, pin, model, paths, reader)


def _indexed_plan_descendants(selection, pins, model):
    """Use derived containment instead of reading every Plan in the shared Backlog."""
    seeds = set(pins)
    while seeds:
        refs = query_reader().lifecycle_descendants(tuple(sorted(seeds)), 'CONTAINS')
        if not seeds <= refs:
            _fail('Plan containment is unavailable in the query index')
        # Drafts and Archived revisions can be graph descendants but are not
        # Current Status targets; their shared Role folders do not move.
        missing = sorted(ref for ref in refs - pins.keys() if '@' not in ref)
        seeds = set()
        for selected in select_current_sources(selection, missing).values():
            if selected.atom_id in pins:
                continue
            nested = _companion_pins(selection, selected, model)
            for atom_id, pin in nested.items():
                if atom_id in pins and pins[atom_id].path != pin.path:
                    _fail('Carrier tree contains duplicate Current Atom')
                pins[atom_id] = pin
            seeds.update(nested.keys() - refs)
    return pins


def select_archive_cascade(selection, parent_pin, model):
    """Return verified Current pins in child-first order, including parent.

    Retained Archived revisions and ordinary assets are not Status targets.
    """
    parent_view = logical_view(parent_pin.metadata, model)
    role = parent_view.get('role')
    if (role not in {'Plan', 'Operations'} or parent_pin.status.casefold() in {'draft', 'archived'}
            or (role == 'Operations' and parent_view.get('form') not in {'Workflow', 'Step'})):
        _fail('A Current Plan, Workflow or Step is required for an archive cascade')
    try:
        pins = _companion_pins(selection, parent_pin, model)
        role_root = None
        if role == 'Plan':
            scope, _ = resolve_container(selection, parent_view, parent_pin.atom_id, model=model)
            _, role_root = _role_root(selection, role, scope)
            if query_reader() is not None:
                return _ordered_pins(parent_pin, _indexed_plan_descendants(selection, pins, model), model, role_root)
            base, folder = active_placement().placement(role, 'Backlog')
            shared, reader = _shared_candidates(selection, role_root / folder if base == 'role' else None, model)
            pending = list(pins)
            visited = set()
            while pending:
                owner = pending.pop()
                if owner in visited:
                    continue
                visited.add(owner)
                for candidate in shared.get(owner, ()):
                    selected = select_source(selection, candidate.atom_id)
                    if selected.path != candidate.path or selected.sha256 != candidate.sha256 or selected.atom_id in pins:
                        _fail('Shared Backlog contains duplicate or changed Current Atom')
                    nested = _companion_pins(selection, selected, model)
                    if pins.keys() & nested.keys():
                        _fail('Carrier tree contains duplicate Current Atom')
                    pins.update(nested)
                    pending.extend(nested)
            if reader is not None and reader.currentness()['state'] != 'unchanged':
                _fail('Shared Backlog changed during selection')
        return _ordered_pins(parent_pin, pins, model, role_root)
    except (OSError, RuntimeError, SourceSelectionError, CarrierError) as error:
        raise InputError('target', 'Carrier tree source selection is unsafe or ambiguous') from error


def has_contained_atoms(selection, pin, model):
    return len(select_archive_cascade(selection, pin, model)) > 1


def has_shared_plan_children(selection, pin, model):
    return (pin.status.casefold() not in {'draft', 'archived'}
            and logical_view(pin.metadata, model).get('role') == 'Plan'
            and active_placement().placement('Plan', 'Backlog')[0] == 'role'
            and has_contained_atoms(selection, pin, model))
