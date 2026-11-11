"""Declared Role folders drive Workbench filename audits."""
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / 'FEATURE_TOOLS'))

from role_directory_rules import compile_role_folders
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.audit_tables import _declared_filename_issue
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.content_schema import compile_content_schema
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.source_inventory import filename_role_matches
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.workbench_schema_asset import compile_schema, load_image_schema, schema_asset


class RoleFolderTests(unittest.TestCase):
    def test_formal_folders_round_trip_and_control_audit(self):
        claims = [
            ('Atom/(.Header.Context.Role := "Analysis and Advisory") >| (Role Order Number == 2)', 'source'),
            ('Atom/(.Header.Context.Role := Plan) >| (Role Order Number == 3)', 'source'),
        ]
        declared = compile_role_folders(claims)
        folders = tuple(sorted((role, value[0]) for role, value in declared.items()))
        with tempfile.TemporaryDirectory() as directory:
            asset = Path(directory) / 'schema.json'
            asset.write_bytes(schema_asset([], compile_schema([], compile_content_schema([]), role_folders=folders)))
            folders = load_image_schema(asset).role_folders
        self.assertTrue(filename_role_matches(Path('02_analysis_and_advisory/CA-A-1-record.md'), folders))
        self.assertFalse(filename_role_matches(Path('02_analysis_and_advisory/CA-P-1-record.md'), folders))
        self.assertFalse(filename_role_matches(Path('03_plan/02_analysis_and_advisory/CA-P-1-record.md'), folders))
        self.assertTrue(filename_role_matches(Path('02_analysis/CA-P-1-record.md'), folders))
        self.assertFalse(filename_role_matches(Path('02_analysis/CA-P-1-record.md')))
        issue = _declared_filename_issue('CA-P-1-record.md', '02_analysis_and_advisory', {'id': 'CA-P-1', 'role': 'Plan'}, folders)
        self.assertEqual('file.name', issue[0])


if __name__ == '__main__':
    unittest.main()
