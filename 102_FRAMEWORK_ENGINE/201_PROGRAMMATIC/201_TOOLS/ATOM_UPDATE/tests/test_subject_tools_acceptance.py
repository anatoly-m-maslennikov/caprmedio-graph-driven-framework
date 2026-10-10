"""Independent CA-P-1963 acceptance fixtures for grammar-aware Subject tools.

These tests intentionally build the expected occurrence ledger from literals.  They
do not import a graph builder or use a producer result to decide what a match is.
The fixture is disposable and lives below ``.caprmedio_tmp``; no authoritative
carrier in the repository is touched.
"""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import hashlib
import json
import sys
import subprocess
import tempfile
import unittest
from contextlib import ExitStack
from pathlib import Path
from unittest.mock import Mock, patch


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)

TOOLS = Path(__file__).resolve().parents[2]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import atom_operations as operations  # noqa: E402


class SubjectToolsAcceptanceTest(unittest.TestCase):
    """CA-E-301/304 checks over a complete, independently-authored fixture."""

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name)
        (self.root / ".git").mkdir()
        self.control = self.root / ".caprmedio_caprmedio"
        self.control.mkdir()
        self.methodology = self.control / "101_LAYER_1_FRAMEWORK_METHODOLOGY"
        self.engine = self.control / "102_LAYER_2_FRAMEWORK_ENGINE"
        self.requirements = self.methodology / "04_requirement"
        self.methods = self.methodology / "05_method"
        self.evaluations = self.methodology / "06_evaluation"
        self.deliveries = self.methodology / "07_delivery"
        self.concerns = self.methodology / "01_concern"
        self.analysis = self.methodology / "02_analysis"
        self.plans = self.methodology / "03_plan"
        self.backlog_planning = self.plans / "031_planning"
        self.methodology_operations = self.methodology / "09_operations"
        self.operations = self.engine / "09_operations"
        for directory in (
            self.requirements, self.methods, self.evaluations, self.deliveries,
            self.concerns, self.analysis, self.plans, self.backlog_planning,
            self.methodology_operations, self.operations,
        ):
            directory.mkdir(parents=True, exist_ok=True)

        # The settings and Structure are a real Project-shaped boundary, rather
        # than a mock graph input.  registered_tools is deliberately carried in
        # the fixture so a caller cannot accidentally test an unowned scope.
        (self.control / "caprmedio_project_settings.toml").write_text(
            '[project]\nname = "subject-tool-acceptance"\n'
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n'
            'projection_root = ".caprmedio_caprmedio/_projection"\n'
            '[artifact_timestamps]\ntimezone = "UTC"\n',
            encoding="utf-8",
        )
        (self.control / "project_structure.toml").write_text(
            "schema_version = 1\n\n"
            '[[scope_units]]\n'
            'scope_unit_name = "FRAMEWORK_METHODOLOGY"\n'
            'authority_path = ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY"\n'
            'parent = "caprmedio"\n'
            'registered_tools = ["ATOM_SEARCH", "ATOM_UPDATE"]\n\n'
            '[[scope_units]]\n'
            'scope_unit_name = "FRAMEWORK_ENGINE"\n'
            'authority_path = ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE"\n'
            'parent = "caprmedio"\n'
            'registered_tools = ["ATOM_SEARCH", "ATOM_UPDATE"]\n',
            encoding="utf-8",
        )
        (self.control / "operators_registry.toml").write_text(
            '[[operators]]\nname = "Fixture Operator"\nrole = "project owner"\n',
            encoding="utf-8",
        )

        self.paths: dict[str, Path] = {}
        self.paths["artifact"] = self._write_atom(
            self.requirements / "CA-R-1001-FRAMEWORK_METHODOLOGY-REQUIREMENT--artifact.md",
            "CA-R-1001", "Requirement", "FRAMEWORK_METHODOLOGY", "Artifact/Atom",
            ("Dependency/Only", "Shared"),
        )
        self.paths["method"] = self._write_atom(
            self.methods / "CA-M-1002-FRAMEWORK_METHODOLOGY-METHOD--dependency.md",
            "CA-M-1002", "Method", "FRAMEWORK_METHODOLOGY", "Governs/Only",
            ("Artifact/Atom/Status", "Dependency/Only"),
        )
        self.paths["engine"] = self._write_atom(
            self.operations / "CA-O-1003-FRAMEWORK_ENGINE-OPERATIONS--engine.md",
            "CA-O-1003", "Operations", "FRAMEWORK_ENGINE", "Dependency/Only",
            ("Engine/Only",),
        )
        self.paths["rmedo_requirement"] = self._write_atom(
            self.requirements / "CA-R-1018-FRAMEWORK_METHODOLOGY-REQUIREMENT--selected.md",
            "CA-R-1018", "Requirement", "FRAMEWORK_METHODOLOGY", "RMEDO/Selected",
            ("RMEDO/Dependency",),
        )
        self.paths["rmedo_method"] = self._write_atom(
            self.methods / "CA-M-1019-FRAMEWORK_METHODOLOGY-METHOD--selected.md",
            "CA-M-1019", "Method", "FRAMEWORK_METHODOLOGY", "RMEDO/Selected",
            ("RMEDO/Dependency",),
        )
        self.paths["rmedo_operations"] = self._write_atom(
            self.methodology_operations / "CA-O-1020-FRAMEWORK_METHODOLOGY-OPERATIONS--selected.md",
            "CA-O-1020", "Operations", "FRAMEWORK_METHODOLOGY", "RMEDO/Selected",
            ("RMEDO/Dependency",),
        )
        self.paths["evaluation"] = self._write_atom(
            self.evaluations / "CA-E-1013-FRAMEWORK_METHODOLOGY-EVALUATION--selected.md",
            "CA-E-1013", "Evaluation", "FRAMEWORK_METHODOLOGY", "RMEDO/Selected",
            ("RMEDO/Dependency",),
        )
        self.paths["delivery"] = self._write_atom(
            self.deliveries / "CA-D-1014-FRAMEWORK_METHODOLOGY-DELIVERY--selected.md",
            "CA-D-1014", "Delivery", "FRAMEWORK_METHODOLOGY", "RMEDO/Selected",
            ("RMEDO/Dependency",),
        )
        self.paths["concern"] = self._write_atom(
            self.concerns / "CA-C-1015-FRAMEWORK_METHODOLOGY-CONCERN--excluded.md",
            "CA-C-1015", "Concern", "FRAMEWORK_METHODOLOGY", "RMEDO/Selected",
            ("RMEDO/Dependency",),
        )
        self.paths["analysis"] = self._write_atom(
            self.analysis / "CA-A-1016-FRAMEWORK_METHODOLOGY-ANALYSIS--excluded.md",
            "CA-A-1016", "Analysis", "FRAMEWORK_METHODOLOGY", "RMEDO/Selected",
            ("RMEDO/Dependency",),
        )
        self.paths["plan"] = self._write_atom(
            self.plans / "CA-P-1017-FRAMEWORK_METHODOLOGY-PLAN--excluded.md",
            "CA-P-1017", "Plan", "FRAMEWORK_METHODOLOGY", "RMEDO/Selected",
            ("RMEDO/Dependency",),
        )
        self.paths["backlog_plan"] = self._write_atom(
            self.backlog_planning / "CA-P-1021-FRAMEWORK_METHODOLOGY-PLAN--backlog.md",
            "CA-P-1021", "Plan", "FRAMEWORK_METHODOLOGY", "Lifecycle/Backlog", (),
            status="Backlog", type_value="Plan",
        )
        self.paths["both"] = self._write_atom(
            self.requirements / "CA-R-1004-FRAMEWORK_METHODOLOGY-REQUIREMENT--same-both.md",
            "CA-R-1004", "Requirement", "FRAMEWORK_METHODOLOGY", "Shared", ("Shared",),
        )
        self.paths["body"] = self._write_atom(
            self.requirements / "CA-R-1005-FRAMEWORK_METHODOLOGY-REQUIREMENT--body-only.md",
            "CA-R-1005", "Requirement", "FRAMEWORK_METHODOLOGY", "Unrelated", (),
            body_extra="Body-only Artifact/Atom and Artifact:Atom:Status must never be Subject matches.",
        )
        self.paths["prefix"] = self._write_atom(
            self.requirements / "CA-R-1006-FRAMEWORK_METHODOLOGY-REQUIREMENT--prefix.md",
            "CA-R-1006", "Requirement", "FRAMEWORK_METHODOLOGY", "Artifact/Atom/Status",
            ("Artifact:Atom:Status", "Artifact/Atomology"),
        )
        self.paths["wrong_owner"] = self._write_atom(
            self.requirements / "CA-R-1007-FRAMEWORK_METHODOLOGY-REQUIREMENT--owner-mismatch.md",
            "CA-R-1007", "Requirement", "FRAMEWORK_ENGINE", "Owner/Mismatch", (),
        )

        archive = self.requirements / "archive"
        self.paths["archived"] = self._write_atom(
            archive / "CA-R-1008-FRAMEWORK_METHODOLOGY-REQUIREMENT--archived.md",
            "CA-R-1008", "Requirement", "FRAMEWORK_METHODOLOGY", "Artifact/Atom", (),
            status="Archived",
        )
        self.paths["nested"] = self._write_raw(
            self.requirements / "CA-R-1009-FRAMEWORK_METHODOLOGY-REQUIREMENT--nested.md",
            self._carrier_text(
                "CA-R-1009", "Requirement", "FRAMEWORK_METHODOLOGY",
                "subjects:\n  governs:\n    nested:\n      value: Artifact/Atom\n  depends_on: []",
                body_extra="Nested Subjects are invalid and must be diagnosed.",
            ),
        )
        self.paths["duplicate"] = self._write_raw(
            self.requirements / "CA-R-1010-FRAMEWORK_METHODOLOGY-REQUIREMENT--duplicate.md",
            self._carrier_text(
                "CA-R-1010", "Requirement", "FRAMEWORK_METHODOLOGY",
                'subjects:\n  governs: "Duplicate/Key"\n  depends_on:\n    - "Duplicate/Value"\n    - "Duplicate/Value"',
                body_extra="Duplicate dependency values are invalid.",
            ),
        )
        self.paths["duplicate_key"] = self._write_raw(
            self.requirements / "CA-R-1011-FRAMEWORK_METHODOLOGY-REQUIREMENT--duplicate-key.md",
            self._carrier_text(
                "CA-R-1011", "Requirement", "FRAMEWORK_METHODOLOGY",
                'subjects:\n  governs: "Artifact/Atom"\n  governs: "Artifact/Atom"\n  depends_on: []',
                body_extra="Duplicate YAML keys are invalid.",
            ),
        )
        drafts = self.requirements / "drafts"
        self._write_raw(
            drafts / "CA-R--FRAMEWORK_METHODOLOGY-REQUIREMENT--draft.md",
            self._carrier_text(
                None, "Requirement", "FRAMEWORK_METHODOLOGY",
                'subjects:\n  governs: "Artifact/Atom"\n  depends_on: []',
                status="Draft", body_extra="Drafts are outside the default Active lookup.",
            ),
        )
        self.paths["preview"] = self._write_atom(
            self.requirements / "CA-R-1012-FRAMEWORK_METHODOLOGY-REQUIREMENT--preview.md",
            "CA-R-1012", "Requirement", "FRAMEWORK_METHODOLOGY", "Preview/Old",
            ("Preview/Dependency", "Preview/Second"),
            newline="\r\n", unknown="unknown_fixture: \"оставить UTF-8\"",
            body_extra="Unicode body: Привет — preserve this exact CRLF text.\n",
        )
        # This candidate is a path hazard, not another valid occurrence.
        try:
            (self.requirements / "CA-R-1099-FRAMEWORK_METHODOLOGY-REQUIREMENT--symlink.md").symlink_to(
                self.paths["artifact"]
            )
        except (OSError, NotImplementedError):
            self.symlink_supported = False
        else:
            self.symlink_supported = True

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _write_atom(
        self, path: Path, atom_id: str, role: str, owner: str, governs: str,
        depends_on: tuple[str, ...], *, status: str = "Active", newline: str = "\n",
        unknown: str = 'unknown_fixture: "retain me"', body_extra: str = "",
        type_value: str | None = None,
    ) -> Path:
        dependency_yaml = "  depends_on: []" if not depends_on else (
            "  depends_on:\n" + "".join(f"    - {json.dumps(value)}\n" for value in depends_on).rstrip("\n")
        )
        subjects = f'  governs: {json.dumps(governs)}\n{dependency_yaml}'
        return self._write_raw(
            path,
            self._carrier_text(atom_id, role, owner, f"subjects:\n{subjects}", status=status,
                               unknown=unknown, body_extra=body_extra, type_value=type_value),
            newline=newline,
        )

    def _carrier_text(
        self, atom_id: str | None, role: str, owner: str, subjects: str, *,
        status: str = "Active", unknown: str = 'unknown_fixture: "retain me"',
        body_extra: str = "", type_value: str | None = None,
    ) -> str:
        identity = f"atom_id: {atom_id}\n" if atom_id else ""
        atom_type = f"type: {type_value}\n" if type_value else ""
        return (
            "---\n" + identity + f"content_role: {role}\n" +
            atom_type +
            f"current_scope_unit: {owner}\nclaim_target_scope_unit: {owner}\n" +
            "local_tier: Standard\nglobal_tier: 2\n" +
            "author: Fixture Operator\n" + f"status: {status}\n" +
            "version: 1\nupdated_at: \"2026-10-01 00:00:00 +0000\"\n" +
            unknown + "\n" + subjects + "\nrelations: {}\n---\n" +
            "# Summary\n\nA literal complete fixture.\n\n## Scope\n\nThe fixture Scope Unit applies.\n\n"
            "## Claim\n\nThe fixture claim remains stable.\n\n## Details\n\n" + body_extra +
            "Preserve this Details body.\n"
        )

    @staticmethod
    def _write_raw(path: Path, text: str, *, newline: str = "\n") -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text.replace("\n", newline).encode("utf-8"))
        return path

    def _search_args(self, value: str, *, field: str | None = "both", match: str | None = "exact",
                     lifecycle: str | None = None, under: str | None = None,
                     content_role: list[str] | None = None, scope_unit: str | None = None) -> argparse.Namespace:
        return argparse.Namespace(
            subject=value, subject_field=field, subject_match=match, content_role=content_role,
            scope_unit=scope_unit, under=under, lifecycle=lifecycle, atom=None, query=None,
            limit=None, view="metadata",
        )

    def _search(self, value: str, **kwargs: object) -> dict[str, object]:
        return operations.run_search(self.root, self._search_args(value, **kwargs))

    def _snapshot(self) -> dict[str, bytes]:
        return {
            path.relative_to(self.root).as_posix(): path.read_bytes()
            for path in self.root.rglob("*")
            if path.is_file() and not path.is_symlink()
        }

    def _assert_ledger(self, result: dict[str, object], expected: list[dict[str, object]]) -> None:
        occurrences = result.get("occurrences")
        self.assertIsInstance(occurrences, list)
        actual = []
        for row in occurrences:
            self.assertIsInstance(row, dict)
            actual.append({key: row.get(key) for key in (
                "atom_id", "version", "status", "owner", "current_scope_unit", "relative_path",
                "sha256", "updated_at", "field", "index", "value",
            )})
        self.assertEqual(expected, actual)
        self.assertEqual(len(expected), result.get("count"))
        for row in actual:
            source = self.root / str(row["relative_path"])
            self.assertTrue(source.is_file(), row)
            self.assertEqual(row["sha256"], hashlib.sha256(source.read_bytes()).hexdigest())
            self.assertEqual(row["current_scope_unit"], row["owner"])

    def _diagnostic_text(self, result: dict[str, object]) -> str:
        return json.dumps(result.get("diagnostics", []), ensure_ascii=False, sort_keys=True)

    def test_subject_search_is_directional_exact_and_prefix_with_literal_ledger(self) -> None:
        before = self._snapshot()
        exact_governs = self._search("Dependency/Only", field="governs")
        self._assert_ledger(exact_governs, [{
            "atom_id": "CA-O-1003", "version": 1, "status": "Active", "owner": "FRAMEWORK_ENGINE",
            "current_scope_unit": "FRAMEWORK_ENGINE", "relative_path": self.paths["engine"].relative_to(self.root).as_posix(),
            "sha256": hashlib.sha256(self.paths["engine"].read_bytes()).hexdigest(),
            "updated_at": "2026-10-01 00:00:00 +0000", "field": "governs", "index": None, "value": "Dependency/Only",
        }])

        exact_dependencies = self._search("Dependency/Only", field="depends_on")
        expected_dependencies = []
        for key, index in (("artifact", 0), ("method", 1)):
            path = self.paths[key]
            expected_dependencies.append({
                "atom_id": "CA-R-1001" if key == "artifact" else "CA-M-1002", "version": 1,
                "status": "Active", "owner": "FRAMEWORK_METHODOLOGY", "current_scope_unit": "FRAMEWORK_METHODOLOGY",
                "relative_path": path.relative_to(self.root).as_posix(),
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "updated_at": "2026-10-01 00:00:00 +0000", "field": "depends_on", "index": index,
                "value": "Dependency/Only",
            })
        self._assert_ledger(exact_dependencies, expected_dependencies)

        shared = self._search("Shared", field="both")
        shared_paths = [self.paths["artifact"], self.paths["both"]]
        shared_expected = []
        for path, atom_id, field, index in (
            (shared_paths[0], "CA-R-1001", "depends_on", 1),
            (shared_paths[1], "CA-R-1004", "depends_on", 0),
            (shared_paths[1], "CA-R-1004", "governs", None),
        ):
            shared_expected.append({
                "atom_id": atom_id, "version": 1, "status": "Active", "owner": "FRAMEWORK_METHODOLOGY",
                "current_scope_unit": "FRAMEWORK_METHODOLOGY", "relative_path": path.relative_to(self.root).as_posix(),
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "updated_at": "2026-10-01 00:00:00 +0000",
                "field": field, "index": index, "value": "Shared",
            })
        shared_expected.sort(key=lambda row: (
            str(row["relative_path"]), {"governs": 0, "depends_on": 1}[str(row["field"])],
            -1 if row["index"] is None else int(row["index"]),
        ))
        self._assert_ledger(shared, shared_expected)

        prefix = self._search("Artifact/Atom", field="both", match="prefix")
        paths = [self.paths["artifact"], self.paths["method"], self.paths["prefix"]]
        self.assertEqual(
            sorted(path.relative_to(self.root).as_posix() for path in paths),
            sorted({row["relative_path"] for row in prefix["occurrences"]}),
        )
        prefix_values = {(row["relative_path"], row["field"], row["index"], row["value"])
                         for row in prefix["occurrences"]}
        self.assertIn((paths[0].relative_to(self.root).as_posix(), "governs", None, "Artifact/Atom"), prefix_values)
        self.assertIn((paths[1].relative_to(self.root).as_posix(), "depends_on", 0, "Artifact/Atom/Status"), prefix_values)
        self.assertIn((paths[2].relative_to(self.root).as_posix(), "governs", None, "Artifact/Atom/Status"), prefix_values)
        self.assertNotIn("Artifact/Atomology", json.dumps(prefix, ensure_ascii=False))
        colon = self._search("Artifact:Atom", field="both", match="prefix")
        self.assertIn("Artifact:Atom:Status", json.dumps(colon, ensure_ascii=False))
        self.assertNotIn("Artifact/Atomology", json.dumps(colon, ensure_ascii=False))
        self.assertEqual(before, self._snapshot())

    def test_subject_search_filters_default_active_and_diagnostics_are_explicit(self) -> None:
        before = self._snapshot()
        default = self._search("Artifact/Atom", field="both")
        self.assertNotIn("CA-R-1008", {row["atom_id"] for row in default["occurrences"]})
        self.assertNotIn("CA-R-1009", {row["atom_id"] for row in default["occurrences"]})
        self.assertIn("CA-R-1009", self._diagnostic_text(default))
        self.assertIn("CA-R-1010", self._diagnostic_text(default))
        self.assertIn("CA-R-1011", self._diagnostic_text(default))
        self.assertIn("CA-R-1007", self._diagnostic_text(default))
        self.assertNotIn("CA-R-1005", {row["atom_id"] for row in default["occurrences"]})

        filtered = self._search(
            "Artifact/Atom", field="both", under=".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement",
            content_role=["Requirement"], scope_unit="FRAMEWORK_METHODOLOGY",
        )
        self.assertEqual({"CA-R-1001"}, {row["atom_id"] for row in filtered["occurrences"]})
        self.assertNotIn("CA-M-1002", json.dumps(filtered))
        self.assertEqual(before, self._snapshot())

    def test_subject_search_explicit_rmedo_selection_excludes_cap(self) -> None:
        selected_roles = ["Requirement", "Method", "Evaluation", "Delivery", "Operations"]
        selected = self._search("RMEDO/Selected", field="governs", content_role=selected_roles)
        selected_ids = {row["atom_id"] for row in selected["occurrences"]}
        self.assertEqual({"CA-R-1018", "CA-M-1019", "CA-E-1013", "CA-D-1014", "CA-O-1020"}, selected_ids)
        self.assertEqual(5, selected["count"])
        self.assertEqual(
            {"CA-R-1018", "CA-M-1019", "CA-E-1013", "CA-D-1014", "CA-O-1020"},
            {row["atom_id"] for row in selected["occurrences"]},
        )

        excluded = self._search(
            "RMEDO/Selected", field="governs", content_role=["Concern", "Analysis", "Plan"]
        )
        self.assertEqual(
            {"CA-C-1015", "CA-A-1016", "CA-P-1017"},
            {row["atom_id"] for row in excluded["occurrences"]},
        )
        self.assertFalse(
            {"CA-C-1015", "CA-A-1016", "CA-P-1017"}
            & {row["atom_id"] for row in selected["occurrences"]}
        )

    def test_default_active_lookup_excludes_non_active_plan_status(self) -> None:
        default = self._search("Lifecycle/Backlog", field="governs")
        self.assertNotIn("CA-P-1021", {row["atom_id"] for row in default["occurrences"]})

        all_lifecycles = self._search("Lifecycle/Backlog", field="governs", lifecycle="all")
        backlog_rows = [row for row in all_lifecycles["occurrences"] if row["atom_id"] == "CA-P-1021"]
        self.assertEqual(1, len(backlog_rows))
        self.assertEqual("Backlog", backlog_rows[0]["status"])

    def test_wrong_occurrence_result_fails_independent_comparison_and_invalid_requests_do_not_traverse(self) -> None:
        result = self._search("Dependency/Only", field="governs")
        corrupted = copy.deepcopy(result)
        corrupted["occurrences"][0]["value"] = "caller-invented"
        with self.assertRaises(AssertionError):
            self._assert_ledger(corrupted, [{
                "atom_id": "CA-O-1003", "version": 1, "status": "Active", "owner": "FRAMEWORK_ENGINE",
                "current_scope_unit": "FRAMEWORK_ENGINE", "relative_path": self.paths["engine"].relative_to(self.root).as_posix(),
                "sha256": hashlib.sha256(self.paths["engine"].read_bytes()).hexdigest(),
                "updated_at": "2026-10-01 00:00:00 +0000", "field": "governs", "index": None, "value": "Dependency/Only",
            }])
        before = self._snapshot()
        for kwargs in (
            {"field": "unsupported"}, {"match": "unsupported"}, {"lifecycle": "unsupported"},
            {"under": "../escape"}, {"content_role": ["UnknownRole"]}, {"scope_unit": "UnknownOwner"},
        ):
            with self.subTest(kwargs=kwargs), self.assertRaises(operations.ToolError):
                self._search("Artifact/Atom", **kwargs)
        self.assertEqual(before, self._snapshot())

    def _preview_item(self, **changes: object) -> dict[str, object]:
        path = self.paths["preview"]
        item: dict[str, object] = {
            "selector": path.relative_to(self.root).as_posix(),
            "expected": {
                "atom_id": "CA-R-1012", "version": 1,
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            },
            "subject_patches": [{
                "field": "governs", "old": "Preview/Old", "new": "Preview/New",
            }],
        }
        item.update(changes)
        return item

    def _validator_patch(self, stack: ExitStack, *, side_effect: object = None) -> list[Mock]:
        mocks: list[Mock] = []
        seen: set[tuple[int, str]] = set()
        modules = (operations,)
        try:
            import atom_subject_patch as subject_patch  # noqa: PLC0415
        except ImportError:
            subject_patch = None
        if subject_patch is not None:
            modules = (*modules, subject_patch)
        for module in modules:
            for name in ("_validate_complete_carrier", "validate_complete_carrier", "validate_proposed_carrier"):
                if not hasattr(module, name) or (id(module), name) in seen:
                    continue
                seen.add((id(module), name))
                mock = Mock(side_effect=side_effect)
                stack.enter_context(patch.object(module, name, mock))
                mocks.append(mock)
        if not mocks:
            self.fail("Subject patch module exposes no finite complete-carrier validator adapter to patch")
        return mocks

    def _preview(self, items: list[dict[str, object]], *, timestamp: str | None = "2026-10-11 00:00:00 +0000") -> dict[str, object]:
        import atom_subject_patch as subject_patch  # noqa: PLC0415
        with ExitStack() as stack:
            mocks = self._validator_patch(stack)
            result = subject_patch.preview_subject_patches(self.root, items, timestamp=timestamp)
            self.assertTrue(any(mock.called for mock in mocks), "complete validator adapter was not invoked")
            return result

    def test_subject_preview_preserves_utf8_crlf_unknown_frontmatter_and_body_without_writes(self) -> None:
        path = self.paths["preview"]
        before = self._snapshot()
        before_bytes = before[path.relative_to(self.root).as_posix()]
        before_text = before_bytes.decode("utf-8")
        item = self._preview_item()
        result = self._preview([item])
        self.assertEqual(before, self._snapshot())
        self.assertEqual(path.read_bytes(), before_bytes)
        self.assertEqual(1, result.get("count"))
        changes = result.get("atoms")
        self.assertIsInstance(changes, list)
        change = changes[0]
        self.assertEqual(1, change["before_version"])
        self.assertEqual(2, change["after_version"])
        self.assertEqual(item["expected"]["sha256"], change["before_sha256"])
        self.assertNotEqual(change["before_sha256"], change["after_sha256"])
        # Build the complete expected bytes independently.  Only the declared
        # Subject scalar and revision metadata slots may differ; this does not
        # reuse the producer's replacement list or proposed carrier.
        self.assertEqual(1, before_text.count('  governs: "Preview/Old"\r\n'))
        self.assertEqual(1, before_text.count("version: 1\r\n"))
        self.assertEqual(1, before_text.count('updated_at: "2026-10-01 00:00:00 +0000"\r\n'))
        expected_text = before_text.replace(
            '  governs: "Preview/Old"\r\n', '  governs: "Preview/New"\r\n', 1
        ).replace("version: 1\r\n", "version: 2\r\n", 1).replace(
            'updated_at: "2026-10-01 00:00:00 +0000"\r\n',
            'updated_at: "2026-10-11 00:00:00 +0000"\r\n', 1,
        )
        expected_bytes = expected_text.encode("utf-8")
        self.assertIsInstance(change["proposed_carrier"], str)
        proposed_bytes = change["proposed_carrier"].encode("utf-8")
        self.assertEqual(expected_bytes, proposed_bytes)
        self.assertEqual(change["after_sha256"], hashlib.sha256(expected_bytes).hexdigest())
        self.assertEqual(change["before_sha256"], hashlib.sha256(before_bytes).hexdigest())
        self.assertIn("Привет", expected_text)
        self.assertIn("unknown_fixture", expected_text)
        self.assertIn("Preserve this Details body.", expected_text)
        self.assertIn("\r\n", expected_text)
        self.assertEqual("2026-10-11 00:00:00 +0000", change["illustrative_updated_at"])
        self.assertFalse(change.get("noop", False))
        self.assertIn("preview_sha256", result)

    def test_subject_preview_rejects_stale_duplicate_and_unsafe_requests(self) -> None:
        path = self.paths["preview"]
        before = self._snapshot()
        stale_cases = [
            self._preview_item(expected={"atom_id": "CA-R-9999", "version": 1, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}),
            self._preview_item(expected={"atom_id": "CA-R-1012", "version": 9, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}),
            self._preview_item(expected={"atom_id": "CA-R-1012", "version": 1, "sha256": "0" * 64}),
            self._preview_item(subject_patches=[{"field": "governs", "old": "wrong", "new": "Preview/New"}]),
            self._preview_item(subject_patches=[{"field": "depends_on", "index": 0, "old": "Preview/Dependency", "new": "Preview/Second"},
                                                {"field": "depends_on", "index": 0, "old": "Preview/Dependency", "new": "Preview/Third"}]),
            self._preview_item(subject_patches=[{"field": "depends_on", "index": 0, "old": "Preview/Dependency", "new": "Preview/Second"},
                                                {"field": "depends_on", "index": 1, "old": "Preview/Second", "new": "Preview/Second"}]),
            self._preview_item(selector="../escape.md"),
            self._preview_item(selector=".caprmedio_caprmedio/_projection/fake.md"),
        ]
        for item in stale_cases:
            with self.subTest(item=item):
                with self.assertRaises(operations.ToolError):
                    self._preview([item])
                self.assertEqual(before, self._snapshot())

        duplicate_paths = [self._preview_item(), self._preview_item()]
        with self.assertRaises(operations.ToolError):
            self._preview(duplicate_paths)
        duplicate_occurrences = self._preview_item(subject_patches=[
            {"field": "governs", "old": "Preview/Old", "new": "Preview/New"},
            {"field": "governs", "old": "Preview/Old", "new": "Preview/Other"},
        ])
        with self.assertRaises(operations.ToolError):
            self._preview([duplicate_occurrences])
        self.assertEqual(before, self._snapshot())

    def test_noop_preview_and_subject_apply_are_write_free_and_generic_guard_remains(self) -> None:
        path = self.paths["preview"]
        before = self._snapshot()
        result = self._preview([self._preview_item(subject_patches=[{
            "field": "governs", "old": "Preview/Old", "new": "Preview/Old",
        }])])
        change = result["atoms"][0]
        self.assertTrue(change.get("noop"))
        self.assertEqual(change["before_version"], change["after_version"])
        self.assertEqual(change["before_sha256"], change["after_sha256"])
        self.assertEqual(before, self._snapshot())

        payload = {"atoms": [self._preview_item()]}
        input_path = self.root / "subject-update.json"
        input_path.write_text(json.dumps(payload), encoding="utf-8")
        before_with_input = self._snapshot()
        with self.assertRaises(operations.ToolError) as error:
            operations.run_update(self.root, argparse.Namespace(input=str(input_path), apply=True))
        self.assertEqual("subject-apply-not-admitted", error.exception.code)
        self.assertEqual(before_with_input, self._snapshot())

        generic = self.root / "generic-update.json"
        generic.write_text(json.dumps({"atoms": [{"selector": self.paths["artifact"].relative_to(self.root).as_posix(), "content": "# changed\n"}]}), encoding="utf-8")
        before_generic = self._snapshot()
        completed = subprocess.run(
            [sys.executable, str(TOOLS / "ATOM_UPDATE" / "atom_update.py"), "--repository", str(self.root),
             "run", "--input", str(generic), "--apply"],
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(2, completed.returncode, completed.stderr)
        envelope = json.loads(completed.stdout)
        self.assertFalse(envelope["ok"])
        self.assertEqual("standalone-apply-not-admitted", envelope["diagnostics"][0]["code"])
        self.assertEqual(before_generic, self._snapshot())

    def test_run_update_subject_wrapper_previews_and_refuses_mixed_modes_write_free(self) -> None:
        input_path = self.root / "subject-wrapper-update.json"
        subject_payload = {"atoms": [self._preview_item()]}
        input_path.write_text(json.dumps(subject_payload), encoding="utf-8")
        before = self._snapshot()
        with ExitStack() as stack:
            mocks = self._validator_patch(stack)
            result = operations.run_update(
                self.root, argparse.Namespace(input=str(input_path), apply=False)
            )
            self.assertTrue(any(mock.called for mock in mocks))
        self.assertEqual(1, result["count"])
        illustrative = result["illustrative_updated_at"]
        self.assertIsInstance(illustrative, str)
        self.assertRegex(illustrative, r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \+0000$")
        parsed_time = dt.datetime.strptime(illustrative, "%Y-%m-%d %H:%M:%S %z")
        self.assertEqual(dt.timedelta(0), parsed_time.utcoffset())
        self.assertEqual(illustrative, result["atoms"][0]["illustrative_updated_at"])
        self.assertEqual(before, self._snapshot())

        mixed_payload = {
            "atoms": [
                self._preview_item(),
                {
                    "selector": self.paths["artifact"].relative_to(self.root).as_posix(),
                    "content": "# generic replacement must not be mixed\n",
                },
            ]
        }
        input_path.write_text(json.dumps(mixed_payload), encoding="utf-8")
        before_mixed = self._snapshot()
        with self.assertRaises(operations.ToolError) as error:
            operations.run_update(
                self.root, argparse.Namespace(input=str(input_path), apply=False)
            )
        self.assertEqual("input-invalid", error.exception.code)
        self.assertIn("cannot be mixed", str(error.exception))
        self.assertEqual(before_mixed, self._snapshot())

    def test_complete_validator_refusal_is_propagated_and_not_claimed_as_authority_proof(self) -> None:
        import atom_subject_patch as subject_patch  # noqa: PLC0415
        before = self._snapshot()
        refusal = ValueError("finite complete-carrier authority unavailable")
        with ExitStack() as stack:
            mocks = self._validator_patch(stack, side_effect=refusal)
            with self.assertRaises(Exception) as error:
                subject_patch.preview_subject_patches(self.root, [self._preview_item()], timestamp="2026-10-11 00:00:00 +0000")
            self.assertTrue(any(mock.called for mock in mocks))
            self.assertIn("authority", str(error.exception).lower())
        self.assertEqual(before, self._snapshot())


if __name__ == "__main__":
    unittest.main()
