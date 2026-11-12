from pathlib import Path
import sys
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'tests'))
from test_incremental_indexing import APP_ROOT  # noqa: F401,E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.source_placement_audit import expected_carrier, affected_descendants
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.markdown_content import parse_content


class Rules:
    def role_folder(self, role):
        return {'Requirement': '04_requirement', 'Plan': '03_plan'}[role]

    def placement(self, role, status):
        return ('role', {'Draft': 'draft', 'Archived': 'archive', 'Active': ''}[status])


def sample(status='Active'):
    body = '## Summary\n\nA short summary\n'
    return {'id': 'CA-R-1', 'version': 2, 'status': status, 'status_group': status,
            'role': 'Requirement', 'form': 'Rule', 'tier': 1,
            'header_json': {'container': {'scope_unit': 'ENGINE'}},
            'content_markdown': body, 'content_properties_json': parse_content(body)}


def test_current_draft_and_archive():
    scopes = {'ENGINE': {'scope_unit_name': 'ENGINE', 'parent': 'PROJECT', 'authority_path': 'engine'}}
    assert expected_carrier(sample(), scopes, {}.get, Rules()) == ('CA-R-1-RULE--a-short-summary.md', 'engine/04_requirement')
    assert expected_carrier(sample('Draft'), scopes, {}.get, Rules()) == ('CA-R-1@2-draft-RULE--a-short-summary.md', 'engine/04_requirement/draft')
    assert expected_carrier(sample('Archived'), scopes, {}.get, Rules()) == (None, 'engine/04_requirement/archive')


def test_unsupported_summary_keeps_directory():
    row = sample()
    row['content_markdown'] = '## Summary\n\nNot supported!\n'
    row['content_properties_json'] = parse_content(row['content_markdown'])
    scopes = {'ENGINE': {'scope_unit_name': 'ENGINE', 'parent': 'PROJECT', 'authority_path': 'engine'}}
    assert expected_carrier(row, scopes, {}.get, Rules()) == (None, 'engine/04_requirement')


def test_nested_parent_lookup():
    scopes = {'ENGINE': {'scope_unit_name': 'ENGINE', 'parent': 'PROJECT', 'authority_path': 'engine'}}
    parent = sample()
    parent.update(id='CA-P-1', role='Plan', form='Epic')
    child = sample()
    child.update(id='CA-P-2', role='Plan', form='Task')
    child['header_json'] = {'container': {'atom': 'CA-P-1'}}
    class LocalRules(Rules):
        def placement(self, role, status):
            return ('container', '')
    assert expected_carrier(child, scopes, {'CA-P-1': parent}.get, LocalRules()) == (
        'CA-P-2-TASK--a-short-summary.md', 'engine/03_plan/CA-P-1-EPIC--a-short-summary')
    assert expected_carrier(child, scopes, {}.get, LocalRules()) == (None, None)


def test_descendants_include_previous_and_next_paths_and_scope_declarations():
    def state(parent_path, child_path, grandchild_path):
        return SimpleNamespace(raw_by_path={parent_path: {'ref': 'P'}},
            refs={'C': child_path, 'G': grandchild_path},
            scope_rows={'ENGINE': {'declaration_source_path': 'scope.md'}},
            outgoing={('Scope Unit', 'ENGINE'): {('Scope Unit', 'ENGINE', 'CONTAINS', 'Atom', 'P', True)},
                      ('Atom', 'P'): {('Atom', 'P', 'CONTAINS', 'Atom', 'C', True)},
                      ('Atom', 'C'): {('Atom', 'C', 'CONTAINS', 'Atom', 'G', True)},
                      ('Atom', 'G'): {('Atom', 'G', 'CONTAINS', 'Atom', 'C', True)}})
    before = state('old-parent', 'old-child', 'old-grandchild')
    after = state('new-parent', 'new-child', 'new-grandchild')
    assert affected_descendants(before, after, {'old-parent', 'new-parent'}) == {
        'old-child', 'old-grandchild', 'new-child', 'new-grandchild'}
    assert affected_descendants(before, None, {'scope.md'}) == {'old-child', 'old-grandchild'}
