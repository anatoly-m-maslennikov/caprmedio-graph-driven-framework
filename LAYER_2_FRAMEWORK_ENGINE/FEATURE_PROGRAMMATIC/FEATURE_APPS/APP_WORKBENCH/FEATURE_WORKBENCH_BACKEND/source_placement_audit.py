"""Pure, best-effort carrier placement expectations from cached source rows."""
from pathlib import Path, PurePosixPath
import sys

from .markdown_content import content_lines, direct_markdown, source_markdown

TOOLS = Path(__file__).resolve().parents[3] / 'FEATURE_TOOLS'
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from carrier_aliases import carrier_read_view  # noqa: E402
from ATOM_LIFECYCLE.placement import derive_filename, PlacementError, _admitted_parent  # noqa: E402


def expected_carrier(row, scopes, get_current, placement):
    """Return (filename, directory), or None for fields with unsupported grammar.

    scopes maps Scope Unit names/IDs to declaration dicts containing authority_path,
    scope_unit_name and parent. get_current(ref) returns a cached Current Atom row.
    Returned directory is relative to the Project root. No carrier files are read.
    """
    return _expected(row, scopes, get_current, placement, frozenset())


def _scope_of(row, scopes, parents, seen):
    while True:
        container = carrier_read_view(row['header_json']).get('container')
        if not isinstance(container, dict):
            return None
        scope = scopes.get(container.get('scope_unit'))
        if scope is not None:
            return scope
        ref = container.get('atom')
        if not isinstance(ref, str) or ref in seen:
            return None
        row = parents(ref)
        if row is None:
            return None
        seen = seen | {ref}


def _parent_context(container, role, form, scopes, parents, placement, seen):
    scope = scopes.get(container.get('scope_unit'))
    if scope is not None:
        return scope, None, None
    ref = container.get('atom')
    if not isinstance(ref, str) or ref in seen:
        return None, None, None
    parent = parents(ref)
    if parent is None:
        return None, None, None
    view = carrier_read_view(parent['header_json'])
    view['role'] = parent.get('role') or view.get('role')
    view['form'] = parent.get('form') or view.get('form')
    if not _admitted_parent(role, form, view, parent.get('status', '')):
        return None, None, None
    name, path = _expected(parent, scopes, parents, placement, seen | {ref})
    if name is None or path is None:
        return None, None, None
    return _scope_of(parent, scopes, parents, seen | {ref}), PurePosixPath(path) / Path(name).stem, parent


def _expected_name(row, view, scope, status, role, form):
    # Archive filenames retain predecessor bytes, and have no reconstructible grammar.
    special = str(form).casefold().replace('_', ' ') in {'scope unit declaration', 'scope delegation'}
    if str(status).casefold() == 'archived' or special:
        return None
    records = row.get('content_properties_json') or []
    summary = next((r for r in records if r.get('property_path') == ['summary']), None)
    if summary is None:
        return None
    body = source_markdown(row)
    text = direct_markdown(summary, records, content_lines(body) if body is not None else None)
    if not isinstance(text, str):
        return None
    try:
        return derive_filename(
            atom_id=row.get('id') or view.get('atom_id'),
            version=row.get('version') or view.get('version'), status=status, role=role,
            summary=text.strip(), row=scope, form=form, label=view.get('label'),
            tier=row.get('tier'), target_scope=row.get('claim_target_scope_unit'),
            work_sequence=view.get('work_sequence_number'),
        )
    except (KeyError, TypeError, ValueError, PlacementError):
        return None


def _expected(row, scopes, parents, placement, seen):
    try:
        view = carrier_read_view(row['header_json'])
        role = row.get('role') or view.get('role')
        role = {'plan': 'Plan', 'operations': 'Operations'}.get(str(role).casefold(), role)
        status = row.get('status') or view.get('status')
        if row.get('status_group') in ('Draft', 'Archived'):
            status = row['status_group']
        form = row.get('form') or view.get('form')
        container = view.get('container')
        if not isinstance(container, dict):
            return None, None
        scope, parent_dir, parent = _parent_context(container, role, form, scopes, parents, placement, seen)
        if scope is None:
            return None, None
        root = PurePosixPath(scope['authority_path']) / placement.role_folder(role)
        base, folder = placement.placement(role, status)
        directory = (root if base == 'role' or parent_dir is None else parent_dir) / folder
        if (role == 'Plan' and str(status).casefold() == 'backlog' and base == 'role'
                and parent_dir is not None and str(parent.get('status', '')).casefold() == 'backlog'):
            directory = parent_dir
        return _expected_name(row, view, scope, status, role, form), directory.as_posix()
    except (KeyError, TypeError, ValueError, PlacementError):
        return None, None


def affected_descendants(previous_state, next_state, changed_paths):
    """Return carrier paths below changed Atoms or Scope Unit declarations.

    Traverse each graph separately, retaining old and new paths through moves and
    deletes. An edge is (source kind, source ref, relation, target kind, target
    ref, derived); refs maps Current Atom references to their carrier paths.
    """
    changed = set(changed_paths)
    result = set()
    for state in (previous_state, next_state):
        if state is not None:
            result.update(_state_descendants(state, changed))
    return result


def _state_descendants(state, changed):
    pending = []
    for path in changed:
        row = state.raw_by_path.get(path)
        if row and isinstance(ref := row.get('ref'), str):
            pending.append(('Atom', ref))
    pending.extend(('Scope Unit', name) for name, row in state.scope_rows.items()
                   if row.get('declaration_source_path') in changed)
    result, visited = set(), set()
    while pending:
        endpoint = pending.pop()
        if endpoint in visited:
            continue
        visited.add(endpoint)
        for edge in state.outgoing.get(endpoint, ()):
            if edge[2] != 'CONTAINS':
                continue
            child = (edge[3], edge[4])
            pending.append(child)
            if child[0] == 'Atom':
                path = state.refs.get(child[1])
                if path is not None:
                    result.add(path)
    return result
