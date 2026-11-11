"""Synthetic placement policy for disposable lifecycle tests, not production authority."""
from functools import wraps

from ATOM_LIFECYCLE.placement_model import bind_placement, load_placement


def fixture_rules(*, operations_folder='09_operations', resolved_folder='resolved'):
    roles = {'Concern': '01_concern', 'Plan': '03_plan', 'Requirement': '04_requirement',
             'Operations': operations_folder, 'Method': '05_method', 'Decision': '06_decision'}
    records = []
    for role in roles:
        base = 'container' if role in {'Plan', 'Operations'} else 'role'
        for status, folder, owner in [('*', '<lowercase status>', 'container'), ('Active', '', base),
                                      ('Draft', 'draft', 'role'),
                                      ('Archived', 'archived', 'role'),
                                      ('Resolved', resolved_folder, base), ('Done', 'done', base),
                                      ('Canceled', 'canceled', base), ('Backlog', '001_backlog', base)]:
            records.append({'role': role, 'status': status, 'base': owner, 'folder': folder, 'source': 'CA-D-1'})
    return load_placement({'sources': [{'atom_id': 'CA-D-1', 'version': 1, 'sha256': 'a' * 64,
                                         'source_path': 'synthetic/CA-D-1.md'}],
                           'role_folders': [{'role': role, 'folder': folder, 'source': 'CA-D-1'}
                                            for role, folder in roles.items()],
                           'placements': records,
                           'archive_aliases': [{'role': role, 'folder': 'archive', 'source': 'CA-D-1'}
                                               for role in roles]})


def with_fixture_placement(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        with bind_placement(fixture_rules()):
            return function(*args, **kwargs)
    return wrapped
