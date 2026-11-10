# CA-E-821@1
"""Exercise Atom audits through the shared query backend."""

from pathlib import Path
from dataclasses import replace
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tests"))
from test_incremental_indexing import IncrementalIndexingTests
from smalltest_support import source_path, write_atom
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND import audit_tables
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.content_schema import compile_content_schema
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.markdown_content import parse_content


class AtomAuditTests(IncrementalIndexingTests):
    def test_missing_declared_column_is_reported_from_compiled_rules(self):
        declaration = {"role": "Requirement", "form": "Declaration", "status_group": "Current",
                       "content_markdown": "## Claim\n\n```CFEL\n# model\n"
                       "Atom.Content.Summary:: {::1};\nAtom.Content.Details:: {::1};\n```\n"}
        body = "## Summary\n\nPresent.\n\n## Details\n\nMissing.\n"
        row = {"ref": "CA-R-851", "role": "Requirement", "form": "Rule",
               "content_markdown": body, "content_properties_json": parse_content(body, tolerate_duplicate_siblings=True)}
        complete = compile_content_schema([declaration, row])
        incomplete = replace(complete, columns=tuple(c for c in complete.columns if c.name != "content.details"))
        issues = audit_tables._content_issues(Path("source/CA-R-851.md"), row, incomplete,
                                              {"content.summary": "Present."}, {})
        self.assertEqual("content.details", issues[0][4])

    def test_empty_source_and_presentation_headings_are_not_missing_content(self):
        declaration = {"role": "Requirement", "form": "Declaration", "status_group": "Current",
                       "content_markdown": "## Claim\n\n```CFEL\n# model\n"
                       "Atom.Content.Details:: {::0..1};\n```\n"}
        body = "## Details\n\n### Presentation only\n\nKeep as prose.\n"
        row = {"ref": "CA-R-851", "role": "Requirement", "form": "Rule",
               "content_markdown": body, "content_properties_json": parse_content(body, tolerate_duplicate_siblings=True)}
        schema = compile_content_schema([declaration, row])
        present = schema.values(row)["content.details"]
        self.assertIn("### Presentation only", present)
        self.assertEqual([], audit_tables._content_issues(Path("source/CA-R-851.md"), row, schema,
                                                          {"content.details": present}, {}))
        row["content_markdown"] = "## Details\n\n"
        row["content_properties_json"] = parse_content(row["content_markdown"], tolerate_duplicate_siblings=True)
        self.assertEqual([], audit_tables._content_issues(Path("source/CA-R-851.md"), row, schema,
                                                          {"content.details": None}, {}))

    def test_reports_declared_content_missing_from_the_query_projection(self):
        model = source_path(self.declarations, "ENGINE", "04_requirement", "CA-R-850.md")
        source = source_path(self.declarations, "ENGINE", "04_requirement", "CA-R-851.md")
        draft = source_path(self.declarations, "ENGINE", "04_requirement", "draft/CA-R-852@2-draft.md")
        write_atom(model, "CA-R-850", body="## Claim\n\n```CFEL\n# model\n"
                   "Atom.Content.Summary:: {::1};\nAtom.Content.Details:: {::0..1};\n```\n")
        model.write_text(model.read_text().replace('form: "Definition"', 'form: "Declaration"'))
        write_atom(source, "CA-R-851", body="## Summary\n\nPresent.\n\n## Details\n\nMissing.\n")
        write_atom(draft, "CA-R-852", status="Draft", version=2,
                   body="## Summary\n\nPresent.\n\n## Details\n\nMissing draft.\n")
        self.service._refresh([self.event(path, operation="create") for path in (model, source, draft)])
        original = {path: path.read_bytes() for path in (source, draft)}
        self.assertEqual([["Present.", "Missing."]], self.store.run(
            'SELECT "content.summary", "content.details" FROM atoms WHERE filename = \'CA-R-851.md\''
        )["rows"])
        self.store._connection.execute(
            'UPDATE atoms SET "content.details" = NULL '
            "WHERE filename = 'CA-R-851.md'"
        )
        self.store._connection.execute(
            'UPDATE atoms SET "content.details" = \'Miss\' WHERE filename = \'CA-R-852@2-draft.md\''
        )
        self.service._refresh([self.event(path) for path in (source, draft)])
        issues = self.store.run(
            "SELECT filename, issue_category, property FROM atom_content_issues "
            "WHERE filename LIKE 'CA-R-85%' ORDER BY filename"
        )["rows"]
        self.assertEqual([
            ["CA-R-851.md", "query_inaccessible_atom", "content.details"],
            ["CA-R-852@2-draft.md", "query_inaccessible_atom", "content.details"],
        ], issues)
        self.assertEqual(original, {path: path.read_bytes() for path in (source, draft)})
        self.service._refresh()
        self.assertEqual([[0]], self.store.run(
            "SELECT count(*) FROM atom_content_issues WHERE filename LIKE 'CA-R-85%'"
        )["rows"])

    def test_declared_role_conflicts_and_matching_carriers(self):
        role_dir = Path(self.declarations["ENGINE"]["authority_path"]) / "04_requirement"
        relative = role_dir.relative_to(self.root).as_posix()
        cases = [
            ("CA-R-810.md", "CA-P-810.md", "Active", 1),
            ("draft/CA-R-811@2-draft.md", "CA-P-811@2-draft.md", "Draft", 2),
            ("CA-R-812.md", "CA-R-812.md", "Active", 1),
            ("draft/CA-R-813@2-draft.md", "CA-R-813@2-draft.md", "Draft", 2),
        ]
        paths = []
        for index, (filename, declared_name, status, version) in enumerate(cases, 810):
            path = source_path(self.declarations, "ENGINE", "04_requirement", filename)
            destination = relative + ("/draft" if status == "Draft" else "")
            write_atom(path, f"CA-R-{index}", status=status, version=version,
                       extra=f'destination:\n  file:\n    name: "{declared_name}"\n    path: "{destination}"\n')
            paths.append(path)
        self.service._refresh([self.event(path, operation="create") for path in paths])
        result = self.store.run(
            "SELECT filename, issue_category FROM atom_declared_carrier_issues "
            "WHERE filename LIKE 'CA-R-81%' AND issue_category = 'declared_carrier_inconsistency' "
            "ORDER BY filename"
        )
        self.assertEqual([["CA-R-810.md", "declared_carrier_inconsistency"],
                          ["CA-R-811@2-draft.md", "declared_carrier_inconsistency"]], result["rows"])
        self.assertEqual(result["rows"], self.store.page(result["query_id"], 0)["rows"])
        clean = self.store.run(
            "SELECT count(*) FROM atom_physical_carrier_issues "
            "WHERE filename LIKE 'CA-R-812%' OR filename LIKE 'CA-R-813%'"
        )["rows"]
        self.assertEqual([[0]], clean)
        self.assertEqual([[0]], self.store.run("SELECT count(*) FROM atom_declared_carrier_issues WHERE filename LIKE 'CA-R-812%' OR filename LIKE 'CA-R-813%'")["rows"])

    def test_role_directory_mismatch_is_audited_until_removed(self):
        paths = [source_path(self.declarations, "ENGINE", "04_requirement", name) for name in
                 ("CA-P-900.md", "draft/CA-P-901@2-draft.md")]
        for index, path in enumerate(paths):
            write_atom(path, f"CA-P-{900 + index}", status="Draft" if index else "Active", version=2 if index else 1)
        self.service._refresh([self.event(path, operation="create") for path in paths])
        self.assertEqual([[2]], self.store.run("SELECT count(*) FROM atom_content_issues WHERE filename LIKE 'CA-P-90%'")["rows"])
        self.assertEqual([[0]], self.store.run("SELECT count(*) FROM atoms WHERE filename LIKE 'CA-P-90%'")["rows"])
        repaired = paths[0].with_name("CA-R-900.md")
        paths[0].unlink()
        write_atom(repaired, "CA-R-900")
        paths[1].unlink()
        self.service._refresh([self.event(None, old=path, operation="remove") for path in paths]
                              + [self.event(repaired, operation="create")])
        self.assertEqual([[0]], self.store.run("SELECT count(*) FROM atom_content_issues WHERE filename LIKE 'CA-P-90%'")["rows"])
        self.assertEqual([[1]], self.store.run("SELECT count(*) FROM atoms WHERE filename='CA-R-900.md'")["rows"])

    def test_declared_filename_conflicts_with_header_identity_or_role(self):
        paths = [source_path(self.declarations, "ENGINE", "04_requirement", f"CA-R-{n}.md") for n in (890, 891)]
        for path in paths:
            relative = path.parent.relative_to(self.root).as_posix()
            write_atom(path, f"CA-R-{path.stem[-3:]}", extra=f'destination:\n  file:\n    name: "{path.name}"\n    path: "{relative}"\n')
        paths[0].write_text(paths[0].read_text().replace('name: "CA-R-890.md"', 'name: "CA-R-2.md"'))
        paths[1].write_text(paths[1].read_text().replace('role: "Requirement"', 'role: "Method"'))
        self.service._refresh([self.event(path, operation="create") for path in paths])
        self.assertEqual([["CA-R-890.md"], ["CA-R-891.md"]], self.store.run(
            "SELECT DISTINCT filename FROM atom_declared_carrier_issues WHERE filename LIKE 'CA-R-89%' ORDER BY filename"
        )["rows"])

    def test_declared_path_conflicts_are_distinct_from_physical_mismatches(self):
        cases = [("CA-R-820.md", "Active", 1), ("draft/CA-R-821@2-draft.md", "Draft", 2)]
        paths = []
        for index, (filename, status, version) in enumerate(cases, 820):
            path = source_path(self.declarations, "ENGINE", "04_requirement", filename)
            write_atom(
                path, f"CA-R-{index}", status=status, version=version,
                extra=f'container:\n  scope_unit: "TEST-SU-1"\n'
                f'destination:\n  file:\n    name: "{path.name}"\n    path: "outside"\n',
            )
            paths.append(path)
        before = {path: path.read_bytes() for path in paths}
        self.service._refresh([self.event(path, operation="create") for path in paths])
        for table, category in (
            ("atom_declared_carrier_issues", "declared_carrier_inconsistency"),
            ("atom_physical_carrier_issues", "physical_carrier_mismatch"),
        ):
            rows = self.store.run(
                f"SELECT filename, property, issue_category FROM {table} "
                "WHERE filename LIKE 'CA-R-82%' AND property = 'file.path' ORDER BY filename"
            )["rows"]
            self.assertEqual([[paths[0].name, "file.path", category],
                              [paths[1].name, "file.path", category]], rows)
        self.assertEqual(before, {path: path.read_bytes() for path in paths})

    def test_schema_has_only_the_declared_audit_columns(self):
        schema = self.store.schema()["tables"]
        for table in audit_tables.TABLES:
            self.assertEqual(list(audit_tables.COLUMNS), [column["name"] for column in schema[table]])

    def test_invalid_new_carrier_updates_only_its_audit_rows(self):
        path = source_path(self.declarations, "ENGINE", "04_requirement", "CA-R-899.md")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("---\natom_id: [invalid\n---\n")
        with patch.object(audit_tables, "issues_for_source", wraps=audit_tables.issues_for_source) as inspected:
            self.service._refresh([self.event(path, operation="create")])
        self.assertEqual(1, inspected.call_count)
        self.assertEqual([[1]], self.store.run(
            "SELECT count(*) FROM atom_content_issues WHERE filename='CA-R-899.md'"
        )["rows"])
        write_atom(path, "CA-R-899")
        self.service._refresh([self.event(path)])
        self.assertEqual([[0]], self.store.run(
            "SELECT count(*) FROM atom_content_issues WHERE filename='CA-R-899.md'"
        )["rows"])

    def test_value_only_update_preserves_unrelated_audit_rows(self):
        paths = [
            source_path(self.declarations, "ENGINE", "04_requirement", f"CA-R-{index}.md")
            for index in (830, 831)
        ]
        for index, path in zip((830, 831), paths):
            write_atom(path, f"CA-R-{index}", extra='destination:\n  file:\n    name: "wrong.md"\n    path: "wrong"\n')
        self.service._refresh([self.event(path, operation="create") for path in paths])
        before = self.store.run(
            "SELECT issue_category, property, observed, expected, diagnostic FROM atom_physical_carrier_issues "
            "WHERE filename='CA-R-831.md' ORDER BY property"
        )["rows"]
        write_atom(paths[0], "CA-R-830", version=2,
                   extra='destination:\n  file:\n    name: "wrong.md"\n    path: "wrong"\n')
        with patch.object(audit_tables, "issues_for_source", wraps=audit_tables.issues_for_source) as inspected:
            self.service._refresh([self.event(paths[0])])
        self.assertEqual(1, inspected.call_count)
        self.assertEqual(before, self.store.run(
            "SELECT issue_category, property, observed, expected, diagnostic FROM atom_physical_carrier_issues "
            "WHERE filename='CA-R-831.md' ORDER BY property"
        )["rows"])

    def test_audit_tables_report_current_draft_and_clear_stale_issues(self):
        role_dir = Path(self.declarations["ENGINE"]["authority_path"]) / "04_requirement"
        current = source_path(self.declarations, "ENGINE", "04_requirement", "CA-R-800.md")
        draft = source_path(self.declarations, "ENGINE", "04_requirement", "draft/CA-R-801@2-draft.md")
        broken = source_path(self.declarations, "ENGINE", "04_requirement", "CA-R-802.md")
        broken_draft = source_path(self.declarations, "ENGINE", "04_requirement", "draft/CA-R-803@2-draft.md")
        relative = role_dir.relative_to(self.root).as_posix()
        write_atom(current, "CA-R-800", extra=f'destination:\n  file:\n    name: "wrong.md"\n    path: "{relative}"\n')
        write_atom(draft, "CA-R-801", status="Draft", version=2,
                   extra=f'destination:\n  file:\n    name: "wrong-draft.md"\n    path: "{relative}/draft"\n')
        for path in (broken, broken_draft):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("---\natom_id: [not valid\n---\n## Summary\n\nInvalid.\n")
        self.service._refresh([self.event(p, operation="create") for p in (current, draft, broken, broken_draft)])
        self.assertEqual(2, self.store.run("SELECT count(*) FROM atom_content_issues WHERE filename LIKE 'CA-R-80%'")["rows"][0][0])
        self.assertEqual(2, self.store.run("SELECT count(*) FROM atom_physical_carrier_issues WHERE property = 'file.name' AND filename LIKE 'CA-R-80%'")["rows"][0][0])
        self.assertEqual(0, self.store.run("SELECT count(*) FROM atoms WHERE filename LIKE 'CA-R-802%' OR filename LIKE 'CA-R-803%'")["rows"][0][0])

        for path in (current, draft, broken, broken_draft):
            path.unlink()
        self.service._refresh([self.event(None, old=p, operation="remove") for p in (current, draft, broken, broken_draft)])
        for table in ("atom_content_issues", "atom_declared_carrier_issues", "atom_physical_carrier_issues"):
            self.assertEqual(0, self.store.run(f"SELECT count(*) FROM {table} WHERE filename LIKE 'CA-R-80%'")["rows"][0][0])


if __name__ == "__main__":
    unittest.main()
