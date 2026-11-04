# CA-E-675@4
# CA-E-677@6

from __future__ import annotations

from contextlib import redirect_stderr
from io import StringIO
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


APP_ROOT = Path(__file__).resolve().parents[2]
TOOLS_ROOT = APP_ROOT.parent / "FEATURE_TOOLS"
sys.path[:0] = [str(APP_ROOT), str(TOOLS_ROOT), str(TOOLS_ROOT / "VALIDATE_ATOMS")]

from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
from scope_unit_declarations import ScopeDeclarationError  # noqa: E402
from APP_WORKBENCH import source_reader as source_reader_module  # noqa: E402
from APP_WORKBENCH.source_reader import SourceReader  # noqa: E402


ATOM_COLUMNS = (
    "source_path", "status_group", "id", "ref", "version", "status",
    "current_scope_unit", "claim_target_scope_unit", "role", "form", "tier",
    "updated_at", "header_json", "content_markdown", "content_properties_json",
    "relation_edges_json", "hash",
)
SCOPE_COLUMNS = (
    "name", "scope_unit_id", "parent_name", "declared_label", "ordered",
    "order_number", "declaration_source_path", "declaration_version",
    "relation_edges_json", "hash",
)
ROLES = (
    "01_concern", "02_analysis", "03_plan", "04_requirement", "05_method",
    "06_evaluation", "07_delivery", "09_operations",
)


class SourceReaderTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "project"
        self.root.mkdir()
        self.control = self.root / ".caprmedio_caprmedio"
        self.control.mkdir()
        (self.control / "caprmedio_project_settings.toml").write_text(
            '[project]\nname = "fixture"\n'
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n',
            encoding="utf-8",
        )
        self.declarations = write_scope_unit_declarations(
            self.root,
            (
                {
                    "scope_unit_name": "MAIN",
                    "scope_unit_type": "Ordered",
                    "scope_unit_label": "LAYER",
                    "local_order": 1,
                },
                {"scope_unit_name": "CHILD", "parent": "MAIN", "scope_unit_label": "FEATURE"},
            ),
            control_root=self.control,
        )
        # The no-argument path is the canonical Project Settings resolution.
        self.reader = SourceReader(self.root)

    def _path(self, scope: str, role: str, filename: str, *parts: str) -> Path:
        path = Path(self.declarations[scope]["authority_path"]) / role
        if parts:
            path = path.joinpath(*parts)
        path.mkdir(parents=True, exist_ok=True)
        return path / filename

    def _write_atom(
        self,
        scope: str,
        role: str,
        filename: str,
        *,
        atom_id: str,
        status: str = "Active",
        version: int = 1,
        body: str = "# Summary\n\nFixture source.\n",
        parts: tuple[str, ...] = (),
    ) -> Path:
        path = self._path(scope, role, filename, *parts)
        path.write_text(
            "---\n"
            f'atom_id: "{atom_id}"\n'
            'role: "Requirement"\n'
            'form: "Definition"\n'
            f'status: "{status}"\n'
            f"version: {version}\n"
            'updated_at: "2026-11-04 00:00:00 +0000"\n'
            "subjects: {}\n"
            "relations: {}\n"
            "---\n"
            + body,
            encoding="utf-8",
        )
        return path

    def _capture(self) -> tuple[list[dict], list[dict], str]:
        stderr = StringIO()
        with redirect_stderr(stderr):
            atoms, scopes = self.reader.capture()
        return atoms, scopes, stderr.getvalue()

    def _snapshot_files(self) -> dict[Path, bytes]:
        return {
            path: path.read_bytes()
            for path in self.root.rglob("*")
            if path.is_file()
        }

    def test_real_root_child_inventory_includes_canonical_roles_and_declarations(self) -> None:
        for index, role in enumerate(ROLES, start=1):
            self._write_atom(
                "fixture", role, f"root-{index}.md", atom_id=f"CA-R-{100 + index}"
            )
        self._write_atom("CHILD", "04_requirement", "child.md", atom_id="CA-R-120")

        atoms, scopes, stderr = self._capture()

        self.assertEqual(stderr, "")
        self.assertEqual({row["name"] for row in scopes}, {"fixture", "MAIN", "CHILD"})
        self.assertEqual(len(scopes), len(self.declarations))
        self.assertTrue(
            {
                Path(row["declaration_path"]).relative_to(self.root).as_posix()
                for row in self.declarations.values()
            }
            <= {row["source_path"] for row in atoms}
        )
        role_paths = {
            Path(row["source_path"]).parts[-2]
            for row in atoms
            if Path(row["source_path"]).parts[-2] in ROLES
        }
        self.assertEqual(role_paths, set(ROLES))
        self.assertEqual(tuple(atoms[0]), ATOM_COLUMNS)
        self.assertTrue(all(tuple(row) == ATOM_COLUMNS for row in atoms))
        self.assertTrue(all(row["relation_edges_json"] == [] and row["hash"] is None for row in atoms))
        self.assertTrue(all(tuple(row) == SCOPE_COLUMNS for row in scopes))
        self.assertTrue(all(row["relation_edges_json"] == [] and row["hash"] is None for row in scopes))

    def test_status_groups_refs_and_archive_locations(self) -> None:
        sources = {
            "CA-R-201": self._write_atom(
                "MAIN", "01_concern", "active.md", atom_id="CA-R-201", status="Active"
            ),
            "CA-R-202": self._write_atom(
                "MAIN", "02_analysis", "done.md", atom_id="CA-R-202", status="Done"
            ),
            "CA-R-203": self._write_atom(
                "MAIN", "03_plan", "canceled.md", atom_id="CA-R-203", status="Canceled"
            ),
            "CA-R-204@7-draft": self._write_atom(
                "MAIN", "04_requirement", "draft.md", atom_id="CA-R-204@7-draft",
                status="Draft", version=7, parts=("DRAFT",),
            ),
        }
        archived = (
            self._write_atom("MAIN", "05_method", "archived-folder.md", atom_id="CA-R-205", parts=("ARCHIVE",)),
            self._write_atom("MAIN", "06_evaluation", "archived-nested.md", atom_id="CA-R-206", parts=("nested", "Archived")),
            self._write_atom("MAIN", "07_delivery", "archived-status.md", atom_id="CA-R-207", status="archived"),
        )

        atoms, _scopes, stderr = self._capture()
        rows = {row["ref"]: row for row in atoms}

        self.assertEqual(stderr, "")
        self.assertEqual({ref: rows[ref]["status_group"] for ref in sources}, {
            "CA-R-201": "Current",
            "CA-R-202": "Current",
            "CA-R-203": "Current",
            "CA-R-204@7-draft": "Draft",
        })
        self.assertEqual(set(rows), set(sources) | {row["ref"] for row in atoms if row["form"] == "Scope Unit Declaration"})
        self.assertEqual(
            {row["source_path"] for row in atoms} & {
                path.relative_to(self.root).as_posix() for path in archived
            },
            set(),
        )

    def test_generic_and_legacy_filename_markers_are_candidates(self) -> None:
        legacy_concern = self._path("fixture", "01_concern", "CAPRMEDIO-CONC-004--legacy.md")
        legacy_concern.write_text(
            "---\natom_id: CAPRMEDIO-CONC-004\nversion: 1\n---\n# Legacy concern\n",
            encoding="utf-8",
        )
        legacy_analysis = self._path("fixture", "02_analysis", "CAPRMEDIO-ANRP-003--legacy.md")
        legacy_analysis.write_text(
            "---\natom_id: CAPRMEDIO-ANRP-003\nversion: 2\n---\n# Legacy analysis\n",
            encoding="utf-8",
        )
        draft = self._path("fixture", "04_requirement", "CAPRMEDIO-REQU-DRAFT--legacy.md", "drafts")
        draft.write_text("---\nversion: 1\n---\n# Legacy draft\n", encoding="utf-8")

        atoms, _scopes, stderr = self._capture()
        paths = {row["source_path"] for row in atoms}

        self.assertEqual(stderr, "")
        self.assertIn(legacy_concern.relative_to(self.root).as_posix(), paths)
        self.assertIn(legacy_analysis.relative_to(self.root).as_posix(), paths)
        self.assertIn(draft.relative_to(self.root).as_posix(), paths)

    def test_unrepresentable_convenience_integer_keeps_the_full_header_value(self) -> None:
        value = 2**100
        source = self._write_atom("MAIN", "04_requirement", "wide.md", atom_id="CA-R-900", version=value)
        source.write_text(source.read_text().replace("subjects: {}", f"tier: {value}\nsubjects: {{}}"))
        atoms, _scopes, stderr = self._capture()
        row = next(row for row in atoms if row["id"] == "CA-R-900")
        self.assertEqual("", stderr)
        self.assertIsNone(row["version"])
        self.assertIsNone(row["tier"])
        self.assertEqual(value, row["header_json"]["version"])
        self.assertEqual(value, row["header_json"]["tier"])

    def test_crlf_body_and_legacy_header_aliases_are_preserved(self) -> None:
        path = self._path("CHILD", "05_method", "aliases.md")
        body = "## Summary\r\n\r\nOriginal CRLF body.\r\n"
        raw = (
            "---\r\n"
            'atom_id: "CA-R-301"\r\n'
            'content_role: "Requirement"\r\n'
            'type: "Method"\r\n'
            'status: "Active"\r\n'
            "version: 4\r\n"
            'updated_at: "2026-11-04 00:00:00 +0000"\r\n'
            "subjects: {}\r\n"
            "relations: {}\r\n"
            "---\r\n"
            + body
        ).encode()
        path.write_bytes(raw)
        before = path.read_bytes()

        atoms, _scopes, stderr = self._capture()
        row = next(row for row in atoms if row["id"] == "CA-R-301")

        self.assertEqual(stderr, "")
        self.assertEqual(row["role"], "Requirement")
        self.assertEqual(row["form"], "Method")
        self.assertEqual(row["content_markdown"], body)
        self.assertEqual(row["header_json"]["content_role"], "Requirement")
        self.assertEqual(row["header_json"]["type"], "Method")
        self.assertNotIn("role", row["header_json"])
        self.assertNotIn("form", row["header_json"])
        self.assertEqual(path.read_bytes(), before)

        legacy = self._path("CHILD", "05_method", "legacy-carrier.md")
        legacy.write_text(
            "---\nrole: Requirement\nform: Definition\nstatus: Active\nversion: 1\n"
            "updated_at: \"2026-11-04 00:00:00 +0000\"\n---\n# Summary\nLegacy.\n",
            encoding="utf-8",
        )
        atoms, _scopes, stderr = self._capture()
        legacy_row = next(row for row in atoms if row["source_path"] == legacy.relative_to(self.root).as_posix())
        self.assertEqual(stderr, "")
        self.assertIsNone(legacy_row["id"])
        self.assertIsNone(legacy_row["ref"])

    def test_invalid_sources_are_excluded_and_unchanged_failures_are_not_retried(self) -> None:
        valid = self._write_atom("MAIN", "01_concern", "valid.md", atom_id="CA-R-401")
        invalid = self._path("MAIN", "04_requirement", "CA-R-402-bad.md")
        invalid.write_text(
            "---\natom_id: CA-R-402\natom_id: CA-R-403\nrole: Requirement\n"
            "form: Definition\nstatus: Active\nversion: 1\n---\n# Summary\nBad\n",
            encoding="utf-8",
        )

        atoms, _scopes, first_stderr = self._capture()
        self.assertIn(valid.relative_to(self.root).as_posix(), {row["source_path"] for row in atoms})
        self.assertNotIn(invalid.relative_to(self.root).as_posix(), {row["source_path"] for row in atoms})
        self.assertIn("duplicate", first_stderr.lower())
        self.assertIn(invalid.relative_to(self.root).as_posix(), first_stderr)
        self.assertEqual(self.reader.excluded_count, 1)

        atoms_again, _scopes_again, second_stderr = self._capture()
        self.assertEqual({row["source_path"] for row in atoms_again}, {row["source_path"] for row in atoms})
        self.assertEqual(second_stderr, "")
        self.assertEqual(self.reader.excluded_count, 1)

    def test_editing_a_failed_source_makes_it_new_input(self) -> None:
        path = self._path("MAIN", "02_analysis", "repair.md")
        path.write_text(
            "---\natom_id: CA-R-410\natom_id: CA-R-411\nrole: Requirement\n"
            "form: Definition\nstatus: Active\nversion: 1\n---\n# Summary\nBad\n",
            encoding="utf-8",
        )
        atoms, _scopes, _stderr = self._capture()
        self.assertNotIn("CA-R-410", {row["id"] for row in atoms})
        self.assertEqual(self.reader.excluded_count, 1)

        path.write_text(
            "---\natom_id: CA-R-410\nrole: Requirement\nform: Definition\n"
            "status: Active\nversion: 2\nupdated_at: \"2026-11-04 00:00:00 +0000\"\n"
            "subjects: {}\nrelations: {}\n---\n# Summary\nRepaired.\n",
            encoding="utf-8",
        )
        atoms, _scopes, stderr = self._capture()

        self.assertEqual(stderr, "")
        self.assertEqual(next(row["version"] for row in atoms if row["id"] == "CA-R-410"), 2)
        self.assertEqual(self.reader.excluded_count, 0)

    def test_unchanged_success_reuses_row_but_changed_invalid_source_drops_it(self) -> None:
        path = self._write_atom("MAIN", "02_analysis", "cached.md", atom_id="CA-R-411")
        with patch.object(
            source_reader_module,
            "parse_carrier",
            wraps=source_reader_module.parse_carrier,
        ) as parse:
            atoms, _scopes, stderr = self._capture()
            first_calls = parse.call_count
            self.assertEqual(stderr, "")
            self.assertGreater(first_calls, 0)

            atoms_again, _scopes_again, stderr_again = self._capture()
            self.assertEqual(stderr_again, "")
            self.assertEqual(parse.call_count, first_calls)
            self.assertIn(path.relative_to(self.root).as_posix(), {row["source_path"] for row in atoms_again})

            path.write_text(
                "---\natom_id: CA-R-411\natom_id: CA-R-412\nrole: Requirement\n"
                "form: Definition\nstatus: Active\nversion: 2\n---\n# Summary\nBad\n",
                encoding="utf-8",
            )
            changed_atoms, _scopes_changed, changed_stderr = self._capture()
            self.assertNotIn(path.relative_to(self.root).as_posix(), {row["source_path"] for row in changed_atoms})
            self.assertIn(path.relative_to(self.root).as_posix(), changed_stderr)
            self.assertEqual(parse.call_count, first_calls + 1)
            self.assertEqual(self.reader.excluded_count, 1)

            path.write_text(
                "---\natom_id: CA-R-411\nrole: Requirement\nform: Definition\n"
                "status: Active\nversion: 3\n---\n# Summary\nRepaired.\n",
                encoding="utf-8",
            )
            repaired_atoms, _scopes_repaired, repaired_stderr = self._capture()

            self.assertEqual(parse.call_count, first_calls + 2)
        self.assertEqual(repaired_stderr, "")
        self.assertEqual(next(row["version"] for row in repaired_atoms if row["id"] == "CA-R-411"), 3)
        self.assertEqual(self.reader.excluded_count, 0)

    def test_unrepresentable_source_and_nonregular_source_only_exclude_themselves(self) -> None:
        valid = self._write_atom("CHILD", "06_evaluation", "valid.md", atom_id="CA-R-420")
        unsupported = self._path("CHILD", "06_evaluation", "unsupported.md")
        unsupported.write_text(
            "---\natom_id: CA-R-421\nrole: Requirement\nform: Definition\n"
            "status: Active\nversion: 1\nunsupported: !!set\n  ? value\n---\n"
            "# Summary\nUnsupported JSON value.\n",
            encoding="utf-8",
        )
        nonregular = self._path("CHILD", "06_evaluation", "CA-E-422-directory.md")
        nonregular.mkdir()

        atoms, _scopes, stderr = self._capture()

        self.assertIn(valid.relative_to(self.root).as_posix(), {row["source_path"] for row in atoms})
        self.assertNotIn(unsupported.relative_to(self.root).as_posix(), {row["source_path"] for row in atoms})
        self.assertNotIn(nonregular.relative_to(self.root).as_posix(), {row["source_path"] for row in atoms})
        self.assertIn(unsupported.relative_to(self.root).as_posix(), stderr)
        self.assertIn(nonregular.relative_to(self.root).as_posix(), stderr)

    def test_plain_review_markdown_is_ignored_without_a_diagnostic(self) -> None:
        for name in ("README.md", "REPORT.md"):
            path = self._path("MAIN", "02_analysis", name, "draft")
            path.write_text("This is review prose, not an Atom carrier.\n", encoding="utf-8")
        copied_atom = self._write_atom(
            "MAIN",
            "02_analysis",
            "CA-R-499-proof-copy.md",
            atom_id="CA-R-499",
            parts=("draft", "frozen-inputs"),
        )

        atoms, _scopes, stderr = self._capture()

        self.assertEqual(stderr, "")
        self.assertNotIn("README.md", {row["source_path"] for row in atoms})
        self.assertNotIn("REPORT.md", {row["source_path"] for row in atoms})
        self.assertNotIn(copied_atom.relative_to(self.root).as_posix(), {row["source_path"] for row in atoms})
        self.assertEqual(self.reader.excluded_count, 0)

    def test_unterminated_plain_review_markdown_is_ignored_without_a_diagnostic(self) -> None:
        path = self._path("MAIN", "02_analysis", "README.md", "draft")
        path.write_text("---\nReview prose.\nrole: prose\n", encoding="utf-8")

        atoms, _scopes, stderr = self._capture()

        self.assertEqual(stderr, "")
        self.assertNotIn(path.relative_to(self.root).as_posix(), {row["source_path"] for row in atoms})
        self.assertEqual(self.reader.excluded_count, 0)

    def test_lifecycle_group_uses_paths_relative_to_the_selected_project(self) -> None:
        for parent_name in ("archive", "archived", "draft", "drafts"):
            root = self.root.parent / parent_name / "project"
            root.mkdir(parents=True)
            control = root / ".caprmedio_caprmedio"
            control.mkdir()
            (control / "caprmedio_project_settings.toml").write_text(
                '[project]\nname = "fixture"\n'
                '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n',
                encoding="utf-8",
            )
            declarations = write_scope_unit_declarations(
                root,
                ({
                    "scope_unit_name": "MAIN",
                    "scope_unit_type": "Ordered",
                    "scope_unit_label": "LAYER",
                    "local_order": 1,
                },),
                control_root=control,
            )
            source = Path(declarations["MAIN"]["authority_path"]) / "04_requirement" / "current.md"
            source.parent.mkdir(parents=True, exist_ok=True)
            source.write_text(
                "---\natom_id: CA-R-701\nrole: Requirement\nform: Definition\n"
                "status: Active\nversion: 1\n---\n# Current\n",
                encoding="utf-8",
            )

            atoms, _scopes = SourceReader(root, control).capture()

            row = next(row for row in atoms if row["id"] == "CA-R-701")
            self.assertEqual(row["status_group"], "Current")

    def test_mixed_frontmatter_line_endings_preserve_the_exact_body(self) -> None:
        path = self._path("MAIN", "04_requirement", "mixed.md")
        body = b"# Summary\r\n\r\nMixed body.\r\n"
        path.write_bytes(
            b"---\r\n"
            b"atom_id: CA-R-702\n"
            b"role: Requirement\r\n"
            b"form: Definition\n"
            b"status: Active\r\n"
            b"version: 1\n"
            b"---\r\n"
            + body
        )

        atoms, _scopes, stderr = self._capture()

        self.assertEqual(stderr, "")
        row = next(row for row in atoms if row["id"] == "CA-R-702")
        self.assertEqual(row["content_markdown"], body.decode("utf-8"))

    def test_unreadable_role_mismatched_filename_is_ignored(self) -> None:
        proof_copy = self._write_atom(
            "MAIN", "02_analysis", "CA-R-703-proof-copy.md", atom_id="CA-R-703"
        )
        original_read = source_reader_module.ReadContext.read

        def fail_proof_copy(context, path, **kwargs):
            if Path(path) == proof_copy:
                raise OSError("proof copy unavailable")
            return original_read(context, path, **kwargs)

        stderr = StringIO()
        with patch.object(source_reader_module.ReadContext, "read", new=fail_proof_copy), redirect_stderr(stderr):
            atoms, _scopes = self.reader.capture()

        self.assertEqual(stderr.getvalue(), "")
        self.assertNotIn(proof_copy.relative_to(self.root).as_posix(), {row["source_path"] for row in atoms})
        self.assertEqual(self.reader.excluded_count, 0)

    def test_broken_scope_declaration_reports_and_raises(self) -> None:
        declaration = Path(self.declarations["MAIN"]["declaration_path"])
        declaration.write_text(
            declaration.read_text(encoding="utf-8").replace(
                'atom_id: "CA-R-990001"',
                'atom_id: "CA-R-990001"\natom_id: "CA-R-990099"',
            ),
            encoding="utf-8",
        )

        stderr = StringIO()
        with redirect_stderr(stderr), self.assertRaises(ScopeDeclarationError):
            self.reader.capture()

        self.assertIn(str(self.root), stderr.getvalue())
        self.assertEqual(self.reader.excluded_count, 0)

    def test_explicit_control_root_supports_fixtures_without_project_settings(self) -> None:
        source = self._write_atom("MAIN", "04_requirement", "explicit.md", atom_id="CA-R-501")
        (self.control / "caprmedio_project_settings.toml").unlink()

        reader = SourceReader(self.root, self.control)
        atoms, scopes = reader.capture()

        self.assertIn(source.relative_to(self.root).as_posix(), {row["source_path"] for row in atoms})
        self.assertEqual(len(scopes), len(self.declarations))

    def test_move_remove_and_capture_do_not_write_sources(self) -> None:
        source = self._write_atom("MAIN", "07_delivery", "moving.md", atom_id="CA-R-430")
        before = self._snapshot_files()
        atoms, _scopes, stderr = self._capture()
        self.assertEqual(stderr, "")
        self.assertIn("CA-R-430", {row["id"] for row in atoms})
        self.assertEqual(self._snapshot_files(), before)

        destination = self._path("MAIN", "09_operations", "moved.md")
        source.rename(destination)
        atoms, _scopes, stderr = self._capture()
        paths = {row["source_path"] for row in atoms}
        self.assertEqual(stderr, "")
        self.assertIn(destination.relative_to(self.root).as_posix(), paths)
        self.assertNotIn(source.relative_to(self.root).as_posix(), paths)

        destination.unlink()
        atoms, _scopes, stderr = self._capture()
        self.assertEqual(stderr, "")
        self.assertNotIn("CA-R-430", {row["id"] for row in atoms})
        self.assertEqual(
            {path: content for path, content in self._snapshot_files().items() if path != destination},
            {path: content for path, content in before.items() if path != source},
        )


if __name__ == "__main__":
    unittest.main()
