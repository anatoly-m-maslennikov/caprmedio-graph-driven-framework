# CA-E-675@4
# CA-E-676@3
# CA-E-677@6

from __future__ import annotations

from contextlib import redirect_stderr
from io import StringIO
from pathlib import Path
import sys
import tempfile
import time
import unittest


APP_ROOT = Path(__file__).resolve().parents[2]
TOOLS_ROOT = APP_ROOT.parent / "FEATURE_TOOLS"
sys.path[:0] = [str(APP_ROOT), str(TOOLS_ROOT), str(TOOLS_ROOT / "VALIDATE_ATOMS"), str(Path(__file__).parent)]

from APP_WORKBENCH.service import WorkbenchService  # noqa: E402
from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
from smalltest_support import extension_directory, source_path, write_atom, write_settings  # noqa: E402


class WorkbenchFunctionalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "project"
        self.root.mkdir()
        control = write_settings(self.root)
        self.declarations = write_scope_unit_declarations(
            self.root,
            ({"scope_unit_name": "ENGINE", "scope_unit_type": "Ordered", "scope_unit_label": "LAYER", "local_order": 1},),
            control_root=control,
        )
        self.service = WorkbenchService(self.root, extension_directory=extension_directory(APP_ROOT.parents[2]))
        self.addCleanup(self.service.close)

    def atom(self, name: str, atom_id: str, *, status: str = "Active", role: str = "04_requirement", **kwargs) -> Path:
        return write_atom(source_path(self.declarations, "ENGINE", role, name), atom_id, status=status, **kwargs)

    def refresh(self) -> None:
        self.service.run("SELECT 1")
        self.service._refresh()

    def test_real_yaml_commonmark_schema_and_native_sql_run_check(self) -> None:
        self.atom("first.md", "CA-R-501", body="# Parent Heading\nintro\n\n## Child Property\nchild\n", extra="nested:\n  level: kept\n")
        result = self.service.run("SELECT id, status_group, json_array_length(content_properties_json), json_extract_string(header_json, '$.nested.level') FROM atoms WHERE id = 'CA-R-501'")
        self.assertEqual([["CA-R-501", "Current", 2, "kept"]], result["rows"])
        self.assertEqual({"valid": True, "row_count": 1, "column_count": 1}, self.service.check("SELECT id FROM atoms WHERE id = 'CA-R-501'"))

    def test_background_scan_indexes_new_sources_without_a_manual_refresh(self) -> None:
        self.service.run("SELECT 1")
        self.atom("later.md", "CA-R-599")
        deadline = time.monotonic() + 10
        while time.monotonic() < deadline:
            rows = self.service.run("SELECT id FROM atoms WHERE id = 'CA-R-599'")["rows"]
            if rows:
                self.assertEqual([["CA-R-599"]], rows)
                return
            time.sleep(0.05)
        self.fail("background scan did not index the new source")

    def test_create_edit_move_delete_and_bad_source_do_not_leave_stale_rows(self) -> None:
        source = self.atom("created.md", "CA-R-502")
        self.refresh()
        self.assertEqual([["CA-R-502"]], self.service.run("SELECT id FROM atoms WHERE id = 'CA-R-502'")["rows"])
        write_atom(source, "CA-R-502", version=2, body="# Summary\n\nEdited.\n")
        self.refresh()
        self.assertEqual([[2, "# Summary\n\nEdited.\n"]], self.service.run("SELECT version, content_markdown FROM atoms WHERE id = 'CA-R-502'")["rows"])
        moved = source.with_name("moved.md")
        source.rename(moved)
        self.refresh()
        self.assertEqual([[moved.relative_to(self.root).as_posix()]], self.service.run("SELECT source_path FROM atoms WHERE id = 'CA-R-502'")["rows"])
        moved.unlink()
        self.refresh()
        self.assertEqual([[0]], self.service.run("SELECT count(*) FROM atoms WHERE id = 'CA-R-502'")["rows"])
        bad = self.atom("bad.md", "CA-R-503", extra="atom_id: CA-R-504\n")
        stderr = StringIO()
        with redirect_stderr(stderr):
            self.refresh()
        self.assertIn(bad.relative_to(self.root).as_posix(), stderr.getvalue())
        self.assertEqual([[0]], self.service.run("SELECT count(*) FROM atoms WHERE source_path LIKE '%bad.md'")["rows"])

    def test_draft_is_included_archive_is_excluded_and_inverses_change_counterpart_hash(self) -> None:
        declarations = (
            ("inverse.md", "CA-R-510", "IS_CONTAINED_BY", "## Claim\n```CFEL\nRelation//IS_CONTAINED_BY ((HAS_INVERSE)) Relation//CONTAINS;\n```\n"),
            ("reverse.md", "CA-R-511", "CONTAINS", "## Claim\n```CFEL\nRelation//CONTAINS <((HAS_INVERSE)) Relation//IS_CONTAINED_BY;\n```\n"),
        )
        for name, atom_id, relation, body in declarations:
            self.atom(name, atom_id, body=body, subjects=f"{{active: 'CAPRMEDIO_MODEL <+ CFEL <+ Relation//{relation}'}}")
        scope_id = self.declarations["ENGINE"]["scope_id"]
        self.atom("scope-owned.md", "CA-R-518", relations=f"{{IS_CONTAINED_BY: {{scope_unit: {scope_id}}}}}")
        self.atom("parent.md", "CA-P-512")
        child = self.atom("child.md", "CA-P-513", relations="{is_contained_by: [CA-P-512]}")
        self.atom("draft.md", "CA-R-514", status="Draft", version=2, role="04_requirement/draft")
        self.atom("archived.md", "CA-R-515", status="Archived")
        self.atom("done.md", "CA-R-516", status="Done")
        self.atom("canceled.md", "CA-R-517", status="Canceled")
        self.refresh()
        self.assertEqual([["ENGINE", "CA-R-518"]], self.service.run(
            "FROM GRAPH_TABLE (caprmedio MATCH (a:Reference)-[e:CONTAINS]->(b:Reference) "
            "COLUMNS (a.ref AS owner, b.ref AS child)) WHERE child = 'CA-R-518'"
        )["rows"])
        self.assertEqual([["Active"], ["Canceled"], ["Done"]], self.service.run(
            "SELECT status FROM atoms WHERE id IN ('CA-P-512', 'CA-R-516', 'CA-R-517') ORDER BY status"
        )["rows"])
        self.assertEqual([["CA-R-514@2-draft"]], self.service.run("SELECT ref FROM atoms WHERE id = 'CA-R-514'")["rows"])
        self.assertEqual([[0]], self.service.run("SELECT count(*) FROM atoms WHERE id = 'CA-R-515'")["rows"])
        before = self.service.run("SELECT hash FROM atoms WHERE id = 'CA-P-512'")["rows"][0][0]
        self.assertEqual([["CA-P-512", "CA-P-513", True]], self.service.run(
            "FROM GRAPH_TABLE (caprmedio MATCH (a:Reference)-[e:CONTAINS]->(b:Reference) "
            "COLUMNS (a.ref AS source_ref, b.ref AS target_ref, e.derived AS derived)) WHERE source_ref = 'CA-P-512'"
        )["rows"])
        write_atom(child, "CA-P-513")
        self.refresh()
        self.assertNotEqual(before, self.service.run("SELECT hash FROM atoms WHERE id = 'CA-P-512'")["rows"][0][0])


if __name__ == "__main__":
    unittest.main()
