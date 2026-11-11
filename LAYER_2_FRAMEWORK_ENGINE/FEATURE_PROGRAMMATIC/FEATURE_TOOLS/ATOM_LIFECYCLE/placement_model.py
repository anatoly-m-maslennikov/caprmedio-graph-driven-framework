# CA-R-3049@5
# CA-R-1539@25
# CA-R-1608@23
# CA-R-2696@3
# CA-D-296@33
# CA-D-475@28
# CA-D-466@27
# CA-D-565@28
# CA-D-716@4
# CA-D-717@1

"""Immutable compiled placement bindings for lifecycle operations."""
from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import dataclass
from pathlib import PurePosixPath
from types import MappingProxyType
import re

from carrier_aliases import canonical_role_name, named_value_token
from ATOM_LIFECYCLE.status_model import _STATUS_ORDER

_STATEMENT = re.compile(
    r'^Atom(?P<selectors>(?:/\(\s*\.Header\.(?:Context\.Role|State\.Status)\s*:=\s*[^()]+\))*)'
    r'\.Header\.Destination\.File\.Path\s*==\s*PATH_TEMPLATE\("(?P<path>[^"\r\n]+)"\)$')
_SELECTOR = re.compile(r'/\(\s*\.Header\.(Context\.Role|State\.Status)\s*:=\s*([^()]+?)\s*\)')
_CURRENT_GROUP = re.compile(
    r'^Atom/\(\s*\.Header\.State\.Status\s*>\|\s*Status Group\s*=\s*Current\s*\)'
    r'\.Header\.Destination\.File\.Path\s*==\s*PATH_TEMPLATE\("<container>/(?P<folder><lowercase status>|<status folder>)"\)$')


def _name(value):
    token = named_value_token(canonical_role_name(value)) if isinstance(value, str) else None
    if not token:
        raise ValueError('Invalid placement Role or Status name')
    return token.casefold()


def _folder(value, *, empty=False):
    if not isinstance(value, str) or (not value and not empty):
        raise ValueError('Invalid placement folder')
    if not value:
        return value
    path = PurePosixPath(value)
    if (path.is_absolute() or '\\' in value or any(part in ('', '.', '..') for part in value.split('/'))
            or str(path) != value or '\x00' in value):
        raise ValueError('Unsafe placement folder')
    return value


@dataclass(frozen=True)
class PlacementRules:
    role_folders: object
    _placements: object
    _archive_aliases: object
    sources: tuple

    def role_folder(self, role):
        try:
            return self.role_folders[_name(role)]
        except KeyError as error:
            raise ValueError('No declared Role folder') from error

    def placement(self, role, status):
        key = (_name(role), _name(status))
        try:
            return self._placements[key]
        except KeyError:
            if key[1] in {'draft', 'archived', 'active'}:
                raise ValueError('Required explicit Status placement is missing') from None
            try:
                base, folder = self._placements[(key[0], '*')]
                return base, key[1] if folder == '<lowercase status>' else folder
            except KeyError as error:
                raise ValueError('No declared Role and Status placement') from error

    def archive_folders(self, role):
        base, folder = self.placement(role, 'Archived')
        if base != 'role' or not folder:
            raise ValueError('Archived placement must be Role-owned')
        return (folder, *self._archive_aliases.get(_name(role), ()))


def load_placement(payload):  # noqa: C901
    if not isinstance(payload, dict) or set(payload) != {'sources', 'role_folders', 'placements', 'archive_aliases'}:
        raise ValueError('Invalid placement asset')
    sources = payload['sources']
    if not isinstance(sources, list) or not sources:
        raise ValueError('Placement requires pinned sources')
    ids = set()
    pins = []
    for pin in sources:
        if (not isinstance(pin, dict) or set(pin) != {'atom_id', 'version', 'sha256', 'source_path'}
                or not isinstance(pin['atom_id'], str) or not re.fullmatch(r'[A-Za-z0-9]+-[RD]-[1-9][0-9]*', pin['atom_id'])
                or type(pin['version']) is not int or pin['version'] < 1
                or not isinstance(pin['sha256'], str) or not re.fullmatch(r'[0-9a-f]{64}', pin['sha256'])):
            raise ValueError('Invalid placement source pin')
        _folder(pin['source_path'])
        if pin['atom_id'] in ids:
            raise ValueError('Duplicate placement source pin')
        ids.add(pin['atom_id'])
        pins.append(MappingProxyType(dict(pin)))
    folders = {}
    entries = payload['role_folders']
    if not isinstance(entries, list) or not entries:
        raise ValueError('Placement requires Role folders')
    for entry in entries:
        if not isinstance(entry, dict) or set(entry) != {'role', 'folder', 'source'} or entry['source'] not in ids:
            raise ValueError('Invalid Role folder binding')
        role = _name(entry['role'])
        folder = _folder(entry['folder'])
        if '/' in folder or role in folders or folder in folders.values():
            raise ValueError('Duplicate or invalid Role folder binding')
        folders[role] = folder
    placements = {}
    records = payload['placements']
    if not isinstance(records, list) or not records:
        raise ValueError('Placement requires Status bindings')
    for record in records:
        if (not isinstance(record, dict) or set(record) != {'role', 'status', 'base', 'folder', 'source'}
                or record['source'] not in ids or record['base'] not in {'role', 'container'}):
            raise ValueError('Invalid Status placement binding')
        role = _name(record['role'])
        status = '*' if record['status'] == '*' else _name(record['status'])
        key = (role, status)
        if role not in folders or key in placements:
            raise ValueError('Ambiguous Status placement binding')
        folder = record['folder']
        if folder == '<lowercase status>':
            if status != '*' or record['base'] != 'container':
                raise ValueError('Invalid Status-derived folder')
        else:
            _folder(folder, empty=True)
        placements[key] = (record['base'], folder)
    for role in folders:
        if any((role, status) not in placements for status in ('draft', 'archived', 'active')):
            raise ValueError('Incomplete Role placement bindings')
    aliases = {}
    records = payload['archive_aliases']
    if not isinstance(records, list):
        raise ValueError('Invalid archive aliases')
    for record in records:
        if not isinstance(record, dict) or set(record) != {'role', 'folder', 'source'} or record['source'] not in ids:
            raise ValueError('Invalid archive alias')
        role = _name(record['role'])
        folder = _folder(record['folder'])
        if role not in folders or folder in aliases.get(role, []):
            raise ValueError('Duplicate or unknown archive alias')
        aliases.setdefault(role, []).append(folder)
    for role, values in aliases.items():
        target = placements.get((role, 'archived')) or placements.get((role, '*'))
        if target is None or target[0] != 'role' or target[1] in values:
            raise ValueError('Archive alias conflicts with declared placement')
    return PlacementRules(MappingProxyType(folders), MappingProxyType(placements),
                          MappingProxyType({role: tuple(values) for role, values in aliases.items()}), tuple(pins))


def compile_placement(rows, requirement_rows=(), declared_roles=None, required_statuses=None):  # noqa: C901
    """Compile the bounded explicit Delivery path statements from staged sources."""
    from FEATURE_WORKBENCH_BACKEND.declaration_cfel import formal_claim_blocks, model_statements
    from role_directory_rules import compile_role_folders

    folders, rules, sources = {}, {}, {}
    order_statements = [(statement, row['id']) for row in requirement_rows
                        for block in formal_claim_blocks(row['_content_bytes'].decode('utf-8'))
                        for statement in model_statements(block)]
    role_folders = compile_role_folders(order_statements)
    status_folders, status_numbers = {}, set()
    for statement, source in order_statements:
        if 'Status Order Number' not in statement:
            continue
        match = _STATUS_ORDER.fullmatch(statement)
        if match is None:
            raise ValueError(f'{source}: unsupported Status Order Number declaration')
        status = _name(match['status'].strip().strip('"'))
        order = int(match['order'])
        if status in status_folders or order in status_numbers or order > 999:
            raise ValueError(f'{source}: ambiguous Status order binding')
        status_folders[status] = (f'{order:03d}_{status}', source)
        status_numbers.add(order)
    generic_source = None
    for row in rows:
        for block in formal_claim_blocks(row['_content_bytes'].decode('utf-8')):
            for statement in model_statements(block):
                if statement == 'Atom.Header.Destination.File.Path == PATH_TEMPLATE("<owning scope unit>/<role folder>/<placement>")':
                    if generic_source is not None:
                        raise ValueError('Duplicate generic Role placement template')
                    generic_source = row['id']
                    sources[generic_source] = row
                    continue
                if statement.startswith('Atom.Header.Destination.File.Path') and 'PATH_TEMPLATE' in statement:
                    raise ValueError(f"{row['id']}: unsupported generic Role placement template")
                if not statement.startswith('Atom/') or '.Header.Destination.File.Path' not in statement:
                    continue
                source = row['id']
                if current := _CURRENT_GROUP.fullmatch(statement):
                    key, value = (None, '*'), ('container', current['folder'])
                else:
                    match = _STATEMENT.fullmatch(statement)
                    if not match:
                        raise ValueError(f'{source}: unsupported placement statement')
                    selectors = _SELECTOR.findall(match['selectors'])
                    if len(dict(selectors)) != len(selectors):
                        raise ValueError(f'{source}: duplicate placement selector')
                    selectors = dict(selectors)
                    role = selectors.get('Context.Role')
                    status = selectors.get('State.Status')
                    path = match['path']
                    if role and not status and path.startswith('<owning scope unit>/') and path.endswith('/<placement>'):
                        folder = path[len('<owning scope unit>/'):-len('/<placement>')]
                        normalized_role = _name(role)
                        if normalized_role in folders:
                            raise ValueError(f'{source}: duplicate Role folder')
                        folders[normalized_role] = {'role': role, 'folder': folder, 'source': source}
                        sources[source] = row
                        continue
                    if path.startswith('<owning scope unit>/<role folder>/'):
                        value = ('role', path[len('<owning scope unit>/<role folder>/'):])
                    elif path == '<container>':
                        value = ('container', '')
                    elif path.startswith('<container>/'):
                        value = ('container', path[len('<container>/'):])
                    else:
                        raise ValueError(f'{source}: unsupported placement path')
                    if not status:
                        raise ValueError(f'{source}: Status selector required')
                    key = (_name(role) if role else None, _name(status))
                if key in rules:
                    raise ValueError(f'{source}: duplicate placement binding')
                rules[key] = (*value, source)
                sources[source] = row
    if generic_source is not None:
        if folders:
            raise ValueError('Conflicting generic and explicit Role folder declarations')
        if not role_folders or (declared_roles is not None and
                {_name(role) for role in role_folders} != {_name(role) for role in declared_roles}):
            raise ValueError('Role order declarations are incomplete')
        by_id = {row['id']: row for row in requirement_rows}
        for role, (folder, source) in role_folders.items():
            folders[_name(role)] = {'role': role, 'folder': folder, 'source': source}
            sources[source] = by_id[source]
    elif role_folders:
        raise ValueError('Generic Role placement template is missing')
    if not sources:
        return None
    if not folders:
        raise ValueError('Placement Role folder declarations are missing')
    records = []
    by_id = {row['id']: row for row in requirement_rows}
    for role, entry in folders.items():
        statuses = {status for selected_role, status in rules if selected_role in (None, role)}
        expected = {_name(status) for status in required_statuses.get(role, ())} if required_statuses is not None else set()
        if (None, '*') in rules and rules[(None, '*')][1] == '<status folder>':
            if not expected:
                raise ValueError(f"{entry['role']}: Current Status domain is missing")
            statuses.remove('*')
            statuses.update(expected - {'draft', 'archived'})
        if required_statuses is not None and '*' not in statuses:
            if not expected or not expected.issubset(statuses):
                raise ValueError(f"{entry['role']}: incomplete Status placement declarations")
        for status in sorted(statuses):
            binding = rules.get((role, status), rules.get((None, status)))
            if binding is None and status not in {'draft', 'archived'}:
                binding = rules.get((None, '*'))
            if binding is None:
                raise ValueError(f"{entry['role']}: Status placement is missing")
            base, folder, source = binding
            if folder == '<status folder>':
                if status not in status_folders:
                    raise ValueError(f"{entry['role']}: Status order is missing for {status}")
                folder, order_source = status_folders[status]
                sources[order_source] = by_id[order_source]
            records.append({'role': entry['role'], 'status': status, 'base': base, 'folder': folder, 'source': source})
    payload = {'sources': [{'atom_id': row['id'], 'version': row['version'], 'sha256': row['_sha256'],
                            'source_path': row['source_path']} for row in sources.values()],
               'role_folders': list(folders.values()), 'placements': records, 'archive_aliases': []}
    load_placement(payload)
    return payload


_CURRENT = ContextVar('lifecycle_placement', default=None)


@contextmanager
def bind_placement(rules):
    if not isinstance(rules, PlacementRules):
        raise ValueError('Compiled placement rules required')
    token = _CURRENT.set(rules)
    try:
        yield rules
    finally:
        _CURRENT.reset(token)


def active_placement():
    rules = _CURRENT.get()
    if rules is None:
        raise ValueError('Lifecycle placement rules are not bound')
    return rules
