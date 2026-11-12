# CA-E-675@6
# CA-E-676@10
# CA-E-677@12
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
sys.path[:0] = [str(APP_ROOT), str(TOOLS_ROOT), str(TOOLS_ROOT / "tests"),
                str(TOOLS_ROOT / "VALIDATE_ATOMS"), str(Path(__file__).parent)]

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service import WorkbenchService  # noqa: E402
from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
from lifecycle_placement_test_support import fixture_rules  # noqa: E402
from smalltest_support import built_assets, extension_directory, source_path, write_atom, write_settings  # noqa: E402


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
        self.nested_atom(
            "content-model.md", "CA-R-500", form="Declaration",
            body=(
                "## Claim\n\n### Formal Claim\n\n```CFEL\n"
                "Atom.Content.Summary{::1}:: {::1};\n"
                "Atom/(.Header.Role in RMED).Content.Claim{::1}:: []{::0};\n"
                "Atom/(.Header.Role in RMED).Content.Claim.*[string, in (Formal Claim, Prose Claim)]{::1..2};\n"
                "Atom/(.Header.Role in RMED).Content.Claim.Formal Claim:: {::1};\n"
                "Atom/(.Header.Role in RMED).Content.Claim.Prose Claim:: {::1};\n"
                "```\n"
            ),
        )
        self.service = WorkbenchService(self.root, extension_directory=extension_directory(APP_ROOT.parents[2]),
                                        archive_placement=fixture_rules(), **built_assets(self.root))
        self.addCleanup(self.service.close)

    def atom(self, name: str, atom_id: str, *, status: str = "Active", role: str = "04_requirement", **kwargs) -> Path:
        return write_atom(source_path(self.declarations, "ENGINE", role, name), atom_id, status=status, **kwargs)

    def nested_atom(
        self, name: str, atom_id: str, *, body: str, form: str = "Definition", extra: str = "",
    ) -> Path:
        path = source_path(self.declarations, "ENGINE", "04_requirement", name)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "---\n"
            "identity:\n"
            f'  atom_id: "{atom_id}"\n'
            "state:\n"
            '  status: "Active"\n'
            "  version: 1\n"
            '  updated_at: "2026-11-04 00:00:00 +0000"\n'
            "context:\n"
            '  role: "Requirement"\n'
            f'  form: "{form}"\n'
            "  tier: 1\n"
            "relations: {}\n"
            + extra
            + "---\n"
            + body,
            encoding="utf-8",
        )
        return path

    def refresh(self) -> None:
        self.service.run("SELECT 1", result_delivery="inline")
        self.service._refresh()

    def test_real_yaml_commonmark_schema_and_native_sql_run_check(self) -> None:
        self.nested_atom(
            "first.md", "CA-R-501",
            body=("## Summary\nShort requirement.\n\n## Claim\n"
                  "### Formal claim\nAtom.id[string]{1}\n\n"
                  "### Prose claim\nAn Atom has one ID.\n"),
            extra="nested:\n  level: kept\n",
        )
        result = self.service.run(
            "SELECT \"header.identity.atom_id\", \"header.state.status\", \"header.state.version\", "
            "\"header.context.role\", \"header.context.form\", \"header.context.tier\", status_group, "
            '"content.summary", "content.claim.formal_claim", "content.claim.prose_claim" FROM atoms '
            "WHERE \"header.identity.atom_id\" = 'CA-R-501'",
            result_delivery="inline",
        )
        self.assertEqual(
            [[
                "CA-R-501", "Active", 1, "Requirement", "Definition", 1, "Current",
                "Short requirement.", "Atom.id[string]{1}", "An Atom has one ID.",
            ]],
            result["rows"],
        )
        self.assertNotIn("sql", result)
        self.assertNotIn("sql", self.service.page(result["query_id"], 0, result_delivery="inline"))
        checked = self.service.check(
            "SELECT \"header.identity.atom_id\" FROM atoms WHERE \"header.identity.atom_id\" = 'CA-R-501'"
        )
        self.assertEqual(
            {
                "valid": True, "row_count": 1, "column_count": 1,
                "columns": [{"name": "header.identity.atom_id", "type": "VARCHAR", "has_values": True}],
            },
            checked,
        )
        self.assertEqual({"items": []}, self.service.saved_list())

    def test_background_scan_indexes_new_sources_without_a_manual_refresh(self) -> None:
        self.service.run("SELECT 1", result_delivery="inline")
        self.atom("later.md", "CA-R-599")
        deadline = time.monotonic() + 10
        while time.monotonic() < deadline:
            rows = self.service.run(
                "SELECT \"header.atom_id\" FROM atoms WHERE \"header.atom_id\" = 'CA-R-599'",
                result_delivery="inline",
            )["rows"]
            if rows:
                self.assertEqual([["CA-R-599"]], rows)
                return
            time.sleep(0.05)
        self.fail("background scan did not index the new source")

    def test_create_edit_move_delete_and_bad_source_do_not_leave_stale_rows(self) -> None:
        source = self.atom("created.md", "CA-R-502")
        self.refresh()
        self.assertEqual(
            [["CA-R-502"]],
            self.service.run(
                "SELECT \"header.atom_id\" FROM atoms WHERE \"header.atom_id\" = 'CA-R-502'",
                result_delivery="inline",
            )["rows"],
        )
        write_atom(source, "CA-R-502", version=2, body="# Summary\n\nEdited.\n")
        self.refresh()
        self.assertEqual(
            [[2, "Edited."]],
            self.service.run(
                'SELECT \"header.version\", "content.summary" FROM atoms '
                "WHERE \"header.atom_id\" = 'CA-R-502'",
                result_delivery="inline",
            )["rows"],
        )
        moved = source.with_name("CA-R-moved.md")
        source.rename(moved)
        self.refresh()
        self.assertEqual(
            [[moved.parent.relative_to(self.root).as_posix(), "CA-R-moved.md"]],
            self.service.run(
                'SELECT "relative_path", filename FROM atoms WHERE \"header.atom_id\" = \'CA-R-502\'',
                result_delivery="inline",
            )["rows"],
        )
        moved.unlink()
        self.refresh()
        self.assertEqual(
            [[0]],
            self.service.run("SELECT count(*) FROM atoms WHERE \"header.atom_id\" = 'CA-R-502'", result_delivery="inline")["rows"],
        )
        bad = self.atom("bad.md", "CA-R-503", extra="atom_id: CA-R-504\n")
        stderr = StringIO()
        with redirect_stderr(stderr):
            self.refresh()
        self.assertIn(bad.relative_to(self.root).as_posix(), stderr.getvalue())
        self.assertEqual([[0]], self.service.run("SELECT count(*) FROM atoms WHERE filename = 'CA-R-bad.md'", result_delivery="inline")["rows"])

    def test_draft_and_loaded_archive_and_inverses_change_counterpart_hash(self) -> None:
        declarations = (
            ("inverse.md", "CA-R-510", "IS_CONTAINED_BY", "## Claim\n\n### Formal Claim\n\n```CFEL\nRelation//IS_CONTAINED_BY ((HAS_INVERSE)) Relation//CONTAINS;\n```\n"),
            ("reverse.md", "CA-R-511", "CONTAINS", "## Claim\n\n### Formal Claim\n\n```CFEL\nRelation//CONTAINS <((HAS_INVERSE)) Relation//IS_CONTAINED_BY;\n```\n"),
        )
        for name, atom_id, relation, body in declarations:
            self.atom(name, atom_id, body=body, subjects=f"{{active: 'CAPRMEDIO_MODEL <+ CFEL <+ Relation//{relation}'}}")
        self.service.close()
        self.service = WorkbenchService(self.root, extension_directory=extension_directory(APP_ROOT.parents[2]),
                                        archive_placement=fixture_rules(), **built_assets(self.root))
        self.addCleanup(self.service.close)
        scope_id = self.declarations["ENGINE"]["scope_id"]
        self.atom("scope-owned.md", "CA-R-518", relations=f"{{IS_CONTAINED_BY: {{scope_unit: {scope_id}}}}}")
        self.atom("parent.md", "CA-P-512")
        child = self.atom("child.md", "CA-P-513", relations="{is_contained_by: [CA-P-512]}")
        self.atom("draft.md", "CA-R-514", status="Draft", version=2, role="04_requirement/draft")
        self.atom("CA-R-515@1-archived.md", "CA-R-515", status="Archived", role="04_requirement/archive")
        self.atom("done.md", "CA-R-516", status="Done")
        self.atom("canceled.md", "CA-R-517", status="Canceled")
        self.refresh()
        self.service.load_archives([{"scope_unit": "ENGINE", "role": "Requirement"}])
        self.assertEqual([["ENGINE", "CA-R-518"]], self.service.run(
            "SELECT * FROM GRAPH_TABLE (caprmedio MATCH (a:Reference)-[e:CONTAINS]->(b:Reference) "
            "COLUMNS (a.ref AS owner, b.ref AS child)) WHERE child = 'CA-R-518'",
            result_delivery="inline",
        )["rows"])
        self.assertEqual([["Active"], ["Canceled"], ["Done"]], self.service.run(
            "SELECT \"header.status\" FROM atoms WHERE \"header.atom_id\" "
            "IN ('CA-P-512', 'CA-R-516', 'CA-R-517') ORDER BY \"header.status\"",
            result_delivery="inline",
        )["rows"])
        self.assertEqual(
            [["CA-R-514@2-draft"]],
            self.service.run("SELECT reference FROM atoms WHERE \"header.atom_id\" = 'CA-R-514'", result_delivery="inline")["rows"],
        )
        self.assertEqual([["CA-R-515@1", "Archived"]], self.service.run(
            "SELECT reference, status_group FROM atoms WHERE \"header.atom_id\" = 'CA-R-515'",
            result_delivery="inline",
        )["rows"])
        before = self.service.run("SELECT hash FROM atoms WHERE \"header.atom_id\" = 'CA-P-512'", result_delivery="inline")["rows"][0][0]
        self.assertEqual([["CA-P-512", "CA-P-513", True]], self.service.run(
            "SELECT * FROM GRAPH_TABLE (caprmedio MATCH (a:Reference)-[e:CONTAINS]->(b:Reference) "
            "COLUMNS (a.ref AS source_ref, b.ref AS target_ref, e.derived AS derived)) WHERE source_ref = 'CA-P-512'",
            result_delivery="inline",
        )["rows"])
        write_atom(child, "CA-P-513")
        self.refresh()
        self.assertNotEqual(
            before,
            self.service.run("SELECT hash FROM atoms WHERE \"header.atom_id\" = 'CA-P-512'", result_delivery="inline")["rows"][0][0],
        )


if __name__ == "__main__":
    unittest.main()
