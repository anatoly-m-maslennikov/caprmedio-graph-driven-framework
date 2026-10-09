"""Focused checks for the bounded Requirement Core Term profile."""

from __future__ import annotations

import hashlib
import importlib.util
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
TOOL_DIRECTORY = Path(__file__).resolve().parents[1]
if str(TOOL_DIRECTORY) not in sys.path:
    sys.path.insert(0, str(TOOL_DIRECTORY))
GRAPH_SPEC = importlib.util.spec_from_file_location("core_term_graph_builder", TOOL_DIRECTORY / "generate_entity_graph.py")
assert GRAPH_SPEC and GRAPH_SPEC.loader
graph = importlib.util.module_from_spec(GRAPH_SPEC)
sys.modules[GRAPH_SPEC.name] = graph
GRAPH_SPEC.loader.exec_module(graph)

SPEC = importlib.util.spec_from_file_location("core_term_admission", TOOL_DIRECTORY / "core_term_admission.py")
assert SPEC and SPEC.loader
core = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = core
SPEC.loader.exec_module(core)


WORKSPACE = TOOL_DIRECTORY.parents[3]
ACTUAL_CORE = WORKSPACE / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL"


def requirement(atom_id: str, *, target: str = "Entity", scope: str | None = "Core declaration only.",
                claim: str | None = None, status: str = "Active", extra_frontmatter: str = "") -> str:
    scope_section = "" if scope is None else f"## Scope\n\n{scope}\n\n"
    claim = claim or f"the Term {target.rsplit('/', 1)[-1]} **means** a declared Core-model meaning."
    return (
        "---\n"
        f"atom_id: {atom_id}\n"
        "version: 1\n"
        "content_role: Requirement\n"
        "current_scope_unit: CORE_META_MODEL\n"
        "claim_target_scope_unit: CORE_META_MODEL\n"
        f"status: {status}\n"
        f"{extra_frontmatter}"
        "subjects:\n"
        f"  governs: \"{target}\"\n"
        "  depends_on: []\n"
        "relations: {}\n"
        "---\n"
        "# Summary\n\nSynthetic requirement.\n\n"
        f"{scope_section}"
        f"## Claim\n\n{claim}\n\n"
        "## Details\n\nSupporting declaration context.\n"
    )


class CoreTermAdmissionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.repository = Path(self.temporary.name) / "repository"
        self.authority_root = self.repository / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL"
        self.authority_root.mkdir(parents=True)
        control = self.repository / ".caprmedio_caprmedio"
        (control / "caprmedio_project_settings.toml").write_text(
            "[paths]\ncontrol_root = '.caprmedio_caprmedio'\nprojection_root = '.caprmedio_caprmedio/_projection'\n",
            encoding="utf-8",
        )
        (control / "project_structure.toml").write_text(
            "[[scope_units]]\n"
            "scope_unit_name = 'CORE_META_MODEL'\n"
            "authority_path = '.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL'\n"
            "authority_mode = 'strict'\n",
            encoding="utf-8",
        )
        for _, (_, _, _, suffix) in core._REQUIRED_AUTHORITIES.items():
            source = ACTUAL_CORE / suffix
            destination = self.authority_root / suffix
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(source.read_bytes())
        self.write("04_requirement/CA-R-900.md", requirement("CA-R-900"))

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write(self, relative: str, content: str) -> Path:
        path = self.authority_root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="")
        return path

    def inputs(self, atom_ids: list[str] | None = None):
        carriers, diagnostics = graph.discover_atoms(self.repository, self.authority_root)
        self.assertEqual([], diagnostics)
        frontier = graph.source_frontier_for(self.repository, self.authority_root)
        return carriers, frontier, {"atom_ids": atom_ids or ["CA-R-900"], "scope_unit_names": ["CORE_META_MODEL"]}

    def profile(self, atom_ids: list[str] | None = None):
        carriers, frontier, selection = self.inputs(atom_ids)
        return core.prepare_core_term_profile(self.repository, carriers, frontier, selection), carriers

    @staticmethod
    def carrier(carriers, atom_id: str):
        return next(item for item in carriers if item.atom_id == atom_id)

    def test_admits_single_requirement_term_with_actual_source_pins_and_raw_scope(self) -> None:
        profile, carriers = self.profile()
        checked = core.checked_requirement_source(self.repository, self.carrier(carriers, "CA-R-900"), profile)

        result = core.review_core_term_candidates([checked], profile)

        self.assertEqual("declared_core_model", result["native_graph_context"])
        self.assertTrue(profile.frontier_complete)
        self.assertEqual("complete", result["coverage"][0]["disposition"])
        self.assertEqual("nonempty", result["coverage"][0]["selected_result"])
        self.assertEqual("relation", result["coverage"][1]["fact_class"])
        self.assertEqual("unknown", result["coverage"][1]["disposition"])
        coverage_keys = {"fact_class", "disposition", "selected_result", "candidate_count", "admitted_count", "source_refs"}
        self.assertEqual(coverage_keys, set(result["coverage"][0]))
        self.assertEqual(coverage_keys, set(result["coverage"][1]))
        self.assertEqual(
            [{"term_identity": "Entity", "subject_path": "Entity"}],
            [row["payload"] for row in result["admitted_facts"]],
        )
        fact = result["admitted_facts"][0]
        self.assertEqual("definition", fact["fact_class"])
        self.assertEqual({"fact_id", "candidate_id", "fact_class", "payload", "decision_sha256"}, set(fact))
        self.assertEqual({"term_identity", "subject_path"}, set(fact["payload"]))
        self.assertNotIn("meaning", fact["payload"])
        candidate = result["candidates"][0]
        self.assertEqual({"candidate_id", "fact_class", "payload", "recognizer", "source_ref"}, set(candidate))
        self.assertEqual({"id", "version", "profile_sha256"}, set(candidate["recognizer"]))
        decision = result["admission_decisions"][0]
        self.assertEqual({"id", "version", "profile_sha256"}, set(decision["evaluator"]))
        self.assertEqual(len(core._REQUIRED_AUTHORITIES) + 3, len(decision["authority_inputs"]))
        self.assertIn("CA-D-478", {ref["atom_id"] for ref in decision["authority_inputs"]})
        self.assertIn("CA-D-479", {ref["atom_id"] for ref in decision["authority_inputs"]})
        self.assertIn("CA-R-126", {ref["atom_id"] for ref in decision["authority_inputs"]})
        self.assertTrue({"CA-R-1318", "CA-R-1319", "CA-R-1335"}.issubset(
            {ref["atom_id"] for ref in decision["authority_inputs"]},
        ))
        authority_keys = [core._source_key(ref) for ref in decision["authority_inputs"]]
        self.assertEqual(sorted(set(authority_keys)), authority_keys)
        self.assertTrue(all(len(key) == 9 for key in authority_keys))
        self.assertEqual(
            [
                (
                    ref["atom_id"], ref["atom_revision"], ref["carrier_path"],
                    ref["contribution"]["kind"],
                    ref["contribution"].get("section", ref["contribution"].get("property_path", "")),
                    ref["contribution"].get("canonical_target_reference", ""),
                    ref["contribution"]["start_line"], ref["contribution"]["end_line"],
                    ref["contribution"]["text_sha256"],
                )
                for ref in decision["authority_inputs"]
            ],
            authority_keys,
        )
        self.assertTrue(any(ref["contribution"].get("section") == "Scope" for ref in decision["authority_inputs"]))
        term_system_check = next(
            row for row in decision["checks"]
            if row["code"] == "term-definition-governed-term-terms-graph-authority-bound"
        )
        self.assertEqual(
            {"CA-R-1318", "CA-R-1319", "CA-R-1335"},
            {ref["atom_id"] for ref in term_system_check["source_refs"]},
        )
        scope = checked.scope_source
        assert scope is not None
        lines = (self.repository / scope.carrier_path).read_bytes().splitlines(keepends=True)
        self.assertEqual(
            hashlib.sha256(b"".join(lines[scope.contribution["start_line"] - 1:scope.contribution["end_line"]])).hexdigest(),
            scope.contribution["text_sha256"],
        )
        for reference in decision["authority_inputs"]:
            contribution = reference["contribution"]
            raw_lines = (self.repository / reference["carrier_path"]).read_bytes().splitlines(keepends=True)
            self.assertEqual(
                hashlib.sha256(b"".join(raw_lines[contribution["start_line"] - 1:contribution["end_line"]])).hexdigest(),
                contribution["text_sha256"],
            )

    def test_missing_or_duplicate_scope_is_unresolved_not_complete(self) -> None:
        for scope, extra in ((None, ""), ("Core declaration only.", "scope: copied illegally\n")):
            with self.subTest(scope=scope, extra=extra):
                self.write("04_requirement/CA-R-900.md", requirement("CA-R-900", scope=scope, extra_frontmatter=extra))
                profile, carriers = self.profile()
                checked = core.checked_requirement_source(self.repository, self.carrier(carriers, "CA-R-900"), profile)
                result = core.review_core_term_candidates([checked], profile)
                self.assertEqual([], result["admitted_facts"])
                self.assertEqual("unknown", result["coverage"][0]["disposition"])
                self.assertEqual("unknown", result["coverage"][0]["selected_result"])

    def test_structural_scope_copy_is_unresolved_but_meaningful_scope_remains_admissible(self) -> None:
        for scope in ("CORE_META_MODEL", "`CORE_META_MODEL`."):
            with self.subTest(scope=scope):
                self.write("04_requirement/CA-R-900.md", requirement("CA-R-900", scope=scope))
                profile, carriers = self.profile()
                checked = core.checked_requirement_source(self.repository, self.carrier(carriers, "CA-R-900"), profile)
                self.assertIn("scope-structural-copy", checked.unresolved_codes)
                result = core.review_core_term_candidates([checked], profile)
                self.assertEqual([], result["admitted_facts"])

        self.write("04_requirement/CA-R-900.md", requirement("CA-R-900", scope="Core declaration only."))
        profile, carriers = self.profile()
        checked = core.checked_requirement_source(self.repository, self.carrier(carriers, "CA-R-900"), profile)
        self.assertNotIn("scope-structural-copy", checked.unresolved_codes)
        self.assertEqual(1, len(core.review_core_term_candidates([checked], profile)["admitted_facts"]))

    def test_any_complete_frontier_terminal_collision_is_unresolved_not_duplicate_definition(self) -> None:
        baseline, _ = self.profile()
        self.write("04_requirement/CA-R-901.md", requirement("CA-R-901", target="Other/Entity"))
        profile, carriers = self.profile()
        self.assertNotEqual(baseline.profile_sha256, profile.profile_sha256)
        checked = core.checked_requirement_source(self.repository, self.carrier(carriers, "CA-R-900"), profile)

        result = core.review_core_term_candidates([checked], profile)

        self.assertEqual([], result["admitted_facts"])
        self.assertEqual("unknown", result["coverage"][0]["disposition"])
        decision = result["admission_decisions"][0]
        cardinality = next(row for row in decision["checks"] if row["code"] == "complete-frontier-terminal-cardinality")
        self.assertEqual("unresolved", cardinality["disposition"])
        self.assertNotIn("duplicate", " ".join(row["code"] for row in result["diagnostics"]))

    def test_stale_data_and_wrong_registered_root_fail_closed(self) -> None:
        profile, carriers = self.profile()
        carrier = self.carrier(carriers, "CA-R-900")
        path = self.repository / carrier.carrier_path
        path.write_bytes(path.read_bytes() + b"\n<!-- changed -->\n")
        with self.assertRaises(core.CoreTermAdmissionError):
            core.checked_requirement_source(self.repository, carrier, profile)
        fresh_carriers, _, _ = self.inputs()
        with self.assertRaises(core.CoreTermAdmissionError):
            core.checked_requirement_source(self.repository, self.carrier(fresh_carriers, "CA-R-900"), profile)
        with tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT) as empty:
            with self.assertRaises(core.CoreTermAdmissionError):
                core.prepare_core_term_profile(Path(empty), [], {}, {"atom_ids": [], "scope_unit_names": ["CORE_META_MODEL"]})

    def test_nonliteral_layout_is_unresolved_and_forged_carrier_metadata_fails_closed(self) -> None:
        self.write("04_requirement/CA-R-900.md", requirement("CA-R-900").replace("## Scope", "##  Scope"))
        profile, carriers = self.profile()
        checked = core.checked_requirement_source(self.repository, self.carrier(carriers, "CA-R-900"), profile)
        self.assertIn("registered-body-layout-unresolved", checked.unresolved_codes)

        self.write("04_requirement/CA-R-900.md", requirement("CA-R-900"))
        profile, carriers = self.profile()
        forged = replace(self.carrier(carriers, "CA-R-900"), frontmatter="forged")
        with self.assertRaises(core.CoreTermAdmissionError):
            core.checked_requirement_source(self.repository, forged, profile)

    def test_escaped_governs_scalar_is_unresolved_without_raw_path_admission(self) -> None:
        self.write(
            "04_requirement/CA-R-900.md",
            requirement("CA-R-900", target=r"Qualifier\u002fLabel", claim="the Label **means** a declared Core-model meaning."),
        )
        profile, carriers = self.profile()
        checked = core.checked_requirement_source(self.repository, self.carrier(carriers, "CA-R-900"), profile)
        self.assertIn("governs-noncanonical-scalar", checked.unresolved_codes)
        self.assertIsNone(checked.subject_path)
        self.assertIsNone(checked.term_identity)
        self.assertEqual([], core.review_core_term_candidates([checked], profile)["candidates"])

    def test_unhandled_selected_role_and_claim_grammar_leave_coverage_unknown(self) -> None:
        self.write(
            "05_method/CA-M-900.md",
            requirement("CA-M-900").replace("content_role: Requirement", "content_role: Method"),
        )
        profile, carriers = self.profile(["CA-M-900", "CA-R-900"])
        method = core.checked_requirement_source(self.repository, self.carrier(carriers, "CA-M-900"), profile)
        self.assertIn("unhandled-content-role", method.unresolved_codes)
        checked = core.checked_requirement_source(self.repository, self.carrier(carriers, "CA-R-900"), profile)
        result = core.review_core_term_candidates([checked], profile)
        self.assertEqual("unknown", result["coverage"][0]["disposition"])
        self.assertTrue(any(row["code"] == "selected-source-unreviewed" for row in result["diagnostics"]))

    def test_unsupported_role_never_gets_a_fabricated_claim_reference(self) -> None:
        operation = requirement("CA-O-900").replace("content_role: Requirement", "content_role: Operations")
        operation = operation.replace("## Scope\n\nCore declaration only.\n\n", "").replace("## Claim", "## Operation")
        self.write("09_operations/CA-O-900.md", operation)
        profile, carriers = self.profile(["CA-O-900", "CA-R-900"])
        checked = core.checked_requirement_source(self.repository, self.carrier(carriers, "CA-O-900"), profile)
        self.assertIsNone(checked.claim_source)
        self.assertIsNone(checked.scope_source)
        self.assertIsNotNone(checked.governs_source)
        self.assertIsNone(checked.term_identity)

        result = core.review_core_term_candidates([checked], profile)
        self.assertEqual([], result["candidates"])
        diagnostic = next(row for row in result["diagnostics"] if row["details"].get("atom_id") == "CA-O-900")
        self.assertTrue(all(ref["contribution"].get("section") != "Claim" for ref in diagnostic["source_refs"]))


if __name__ == "__main__":
    unittest.main()
