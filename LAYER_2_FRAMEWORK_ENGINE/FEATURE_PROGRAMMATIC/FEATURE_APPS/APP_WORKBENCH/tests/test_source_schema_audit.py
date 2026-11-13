import unittest
# CA-E-821@2
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import sys

WORKBENCH = Path(__file__).resolve().parents[1]
TOOLS = WORKBENCH.parents[1] / 'FEATURE_TOOLS'
sys.path[:0] = [str(WORKBENCH), str(TOOLS)]

from ATOM_LIFECYCLE.candidate_schema import CandidateSchema
from ATOM_LIFECYCLE.content_constraints import compile_content_constraints, load_content_constraints
from ATOM_LIFECYCLE.header_constraints import compile_header_constraints, load_header_constraints
from ATOM_LIFECYCLE.role_form_schema import RoleFormSchema
from ATOM_LIFECYCLE.status_model import StatusModel
from FEATURE_WORKBENCH_BACKEND.content_schema import compile_content_schema
from FEATURE_WORKBENCH_BACKEND.header_columns import HeaderColumn, HeaderSchema
from FEATURE_WORKBENCH_BACKEND.markdown_content import parse_content
from FEATURE_WORKBENCH_BACKEND.source_schema_audit import SourceSchemaAudit


def auditor():
    formal = '''
Atom.Header.Role{::1} :: [string]{::1};
Atom.Header.Status{::1} :: [string]{::1};
Atom.Header.Version{::1} :: [int]{::1};
Atom/(.Header.Role: Concern).Header.Priority{::1} :: [string]{::1};
Atom/(.Header.Role: Concern).Header.Priority: High;
Atom.Content.Summary{::1} :: {::1};
Atom.Content.Claim{::1} :: []{::0};
Atom.Content.Claim.*[string, in (Formal Claim, Prose Claim)]{::1..2};
'''
    body = ('## Claim\n### Formal Claim\n```CFEL\n' + formal + '\n```\n').encode()
    declaration = {'id': 'CA-R-1', 'ref': 'CA-R-1', 'source_path': 'CA-R-1.md',
                   'version': 1, 'status_group': 'Current', 'role': 'Requirement',
                   'form': 'Declaration', '_content_bytes': body}
    content = compile_content_schema([declaration])
    header = HeaderSchema((HeaderColumn(('version',), 'header.version', 'BIGINT', True, 'version'),))
    roles = RoleFormSchema(frozenset({'Concern', 'Requirement'}), frozenset({'Problem', 'Declaration'}),
                           frozenset(), ())
    schema = CandidateSchema(SimpleNamespace(header=lambda _mode: header, content=content), roles,
                             load_header_constraints(compile_header_constraints([declaration]), {'CA-R-1'}),
                             load_content_constraints(compile_content_constraints([declaration]), {'CA-R-1'}))
    status = StatusModel(((None, None, 'Active'), (None, None, 'Archived')))
    return SourceSchemaAudit(schema, status)


def atom(header, body, group='Current'):
    return {'source_path': 'some/atom.md', 'status_group': group, 'header_json': header,
            'role': header.get('role'), 'form': header.get('form'), '_content_bytes': body.encode(),
            'content_properties_json': parse_content(body, tolerate_duplicate_siblings=True, compact=True)}



class Tests(unittest.TestCase):
    def test_valid_row_and_archived_row_are_both_audited_without_reparsing(self):
        audit = auditor()
        body = '## Summary\nExample\n## Claim\n### Prose Claim\nText\n'
        header = {'role': 'concern', 'form': 'problem', 'status': 'active', 'version': 1, 'priority': 'High'}
        current = atom(header, body)
        archived = atom({**header, 'status': 'archived', 'priority': 'Wrong'}, body, 'Archived')
        with patch('FEATURE_WORKBENCH_BACKEND.markdown_content.parse_content', side_effect=AssertionError('reparsed')):
            assert audit.issues(current) == []
            assert any(issue['field'] == 'priority' for issue in audit.issues(archived))


    def test_reports_multiple_header_and_content_violations(self):
        audit = auditor()
        row = atom({'role': 'concern', 'form': 'problem', 'status': 'bad', 'version': 'wrong'},
                   '## Summary\n## Claim\n### Unexpected\nText\n')
        issues = audit.issues(row)
        assert {'status', 'header.version', 'priority', 'content.summary', 'content.claim'} <= {
            issue['field'] for issue in issues}


    def test_reports_duplicate_declared_fields_in_archived_sources(self):
        audit = auditor()
        row = atom({'role': 'concern', 'form': 'problem', 'status': 'archived', 'version': 1, 'priority': 'High'},
                   '## Summary\nOne\n## Summary\nTwo\n## Claim\n### Prose Claim\nText\n', 'Archived')
        issues = audit.issues(row)
        assert any('duplicate declared content property: summary' in issue['message'] for issue in issues)


    def test_required_heading_and_direct_values_are_independent(self):
        audit = auditor()
        row = atom({'role': 'concern', 'form': 'problem', 'status': 'active', 'version': 1, 'priority': 'High'},
                   '## Summary\n## Claim\n### Prose Claim\nText\n')
        issues = audit.issues(row)
        assert any(issue['field'] == 'content.summary' and 'direct Markdown values' in issue['message'] for issue in issues)


    def test_null_is_not_a_valid_integer_even_when_property_is_present(self):
        audit = auditor()
        row = atom({'role': 'concern', 'form': 'problem', 'status': 'active', 'version': None, 'priority': 'High'},
                   '## Summary\nText\n## Claim\n### Prose Claim\nText\n')
        assert any(issue['field'] == 'header.version' for issue in audit.issues(row))


    def test_undeclared_form_is_reported(self):
        audit = auditor()
        row = atom({'role': 'concern', 'form': 'not_declared', 'status': 'active', 'version': 1, 'priority': 'High'},
                   '## Summary\nText\n## Claim\n### Prose Claim\nText\n')
        assert any(issue['field'] == 'form' for issue in audit.issues(row))
