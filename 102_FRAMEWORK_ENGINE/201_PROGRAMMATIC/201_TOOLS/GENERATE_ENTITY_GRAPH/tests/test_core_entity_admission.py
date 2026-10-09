"""Real grammar and registered-source boundaries for Core Operations facts."""

from __future__ import annotations

import hashlib
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
from unittest.mock import patch


TOOL_DIRECTORY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOL_DIRECTORY))
import core_entity_admission as core  # noqa: E402
import generate_entity_graph as graph  # noqa: E402
import graph_fact_context as facts  # noqa: E402

TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp/tests/test_core_entity_admission"
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
REAL_CORE = TOOL_DIRECTORY.parents[3] / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL"


def operation_atom(atom_id: str, name: str, atom_type: str = "Action", *, operation: str | None = None) -> str:
    declaration = operation or f"{name} **means** the {'reusable ' if atom_type == 'Workflow' else ''}{atom_type} that consumes its required input, checks its precondition, returns its result and reports a failure without effects."
    return "\n".join((
        "---", f"atom_id: {atom_id}", "content_role: Operations", f"type: {atom_type}",
        "current_scope_unit: CORE_META_MODEL", "claim_target_scope_unit: CORE_META_MODEL",
        "local_tier: Standard", "global_tier: 11", "status: Active", "author: Test Author",
        "version: 1", 'updated_at: "2026-10-09 00:00:00 +0000"', "subjects:",
        f'  governs: "{name}"', "  depends_on: []", "relations: {}", "---", "# Summary", "",
        name, "", "## Operation", "", declaration, "", "### Inputs and results", "",
        "Required input, declared precondition, returned result, effects and failure remain one operational contribution.",
        "", "## Details", "", "Supporting information only.", "",
    ))


class CoreEntityAdmissionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.repository = Path(self.temporary.name) / "repository"
        self.control = self.repository / ".control"
        self.folder = self.control / "core"
        self.folder.mkdir(parents=True)
        (self.control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".control"\nprojection_root = ".control/_projection"\n', encoding="utf-8",
        )
        self.structure = self.control / "project_structure.toml"
        self.structure.write_text(
            '[[scope_units]]\nscope_unit_name = "CORE_META_MODEL"\nauthority_path = ".control/core"\n', encoding="utf-8",
        )
        for suffix, revision, digest, role in core._REQUIRED_AUTHORITIES.values():
            raw = (REAL_CORE / suffix).read_bytes()
            self.assertEqual(digest, hashlib.sha256(raw).hexdigest())
            destination = self.folder / suffix
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(raw)
        self.action = self.folder / "09_operations/CA-O-8001.md"
        self.workflow = self.folder / "09_operations/CA-O-8002.md"
        self.action.parent.mkdir(exist_ok=True)
        self.action.write_text(operation_atom("CA-O-8001", "Alpha Action"), encoding="utf-8", newline="")
        self.workflow.write_text(operation_atom("CA-O-8002", "Beta Workflow", "Workflow"), encoding="utf-8", newline="")
        self.sibling = self.folder / "09_operations/CA-O-8003.md"
        self.sibling.write_text(operation_atom("CA-O-8003", "Unselected Action"), encoding="utf-8", newline="")

    def inputs(self, ids: list[str] | None = None):
        carriers, diagnostics = graph.discover_atoms(self.repository, self.folder)
        self.assertEqual([], diagnostics)
        frontier = graph.source_frontier_for(self.repository, self.folder)
        selection = {"atom_ids": ["CA-O-8001", "CA-O-8002"] if ids is None else ids, "scope_unit_names": []}
        return carriers, frontier, selection

    def profile(self, ids: list[str] | None = None):
        carriers, frontier, selection = self.inputs(ids)
        return core.prepare_core_entity_profile(self.repository, carriers, frontier, selection), carriers

    def checked(self, profile, carriers, atom_id="CA-O-8001"):
        carrier = next(item for item in carriers if item.atom_id == atom_id)
        return core.checked_operations_source(self.repository, carrier, profile)

    def test_raw_factory_recognizes_only_actual_selected_atom_identity_and_type(self) -> None:
        profile, carriers = self.profile()
        sources = [self.checked(profile, carriers, atom_id) for atom_id in ("CA-O-8001", "CA-O-8002")]
        result = core.review_core_entity_candidates(sources, profile)
        identities = [row["payload"]["entity_identity"] for row in result["candidates"] if row["fact_class"] == "entity_admission"]
        self.assertEqual(["CA-O-8001", "CA-O-8002"], sorted(identities))
        properties = [row["payload"] for row in result["candidates"] if row["fact_class"] == "entity_property"]
        self.assertEqual({("CA-O-8001", "Action"), ("CA-O-8002", "Workflow")},
                         {(row["entity_identity"], row["value"]["data"]) for row in properties})
        self.assertTrue(all(row["property_identity"] == "Atom/Type" and row["value"]["type"] == "string" for row in properties))
        self.assertNotIn("Alpha Action", str([row["payload"] for row in result["candidates"]]))
        self.assertNotIn("status", str([row["payload"] for row in result["candidates"]]))
        self.assertEqual([], result["admitted_facts"])
        self.assertTrue(all(row["disposition"] == "unresolved" for row in result["admission_decisions"]))
        self.assertTrue(all(row["admitted_count"] == 0 for row in result["coverage"]))
        self.assertTrue(all(row["disposition"] == row["selected_result"] == "unknown" for row in result["coverage"]))
        self.assertEqual({"provider", "candidates", "admission_decisions", "admitted_facts", "coverage", "diagnostics"}, set(result))
        self.assertEqual({"id", "version", "profile_sha256"}, set(result["provider"]))
        self.assertEqual(profile.profile_sha256, result["provider"]["profile_sha256"])
        for decision in result["admission_decisions"]:
            self.assertEqual(20, len(decision["authority_inputs"]))
            self.assertTrue(all("contribution" in ref for ref in decision["authority_inputs"]))
            self.assertEqual(sorted(decision["authority_inputs"], key=facts._source_key), decision["authority_inputs"])
            identity_details = [ref for ref in decision["authority_inputs"] if ref["atom_id"] == "CA-E-246" and ref["contribution"].get("section") == "Details"]
            self.assertEqual(1, len(identity_details))
            semantic_check = next(check for check in decision["checks"] if check["code"] == "semantic-profile-unperformed")
            self.assertEqual("unresolved", semantic_check["disposition"])
            self.assertEqual(sorted(semantic_check["source_refs"], key=facts._source_key), semantic_check["source_refs"])
            without_digest = dict(decision)
            digest = without_digest.pop("decision_sha256")
            self.assertEqual(hashlib.sha256(facts.canonical_bytes(without_digest)).hexdigest(), digest)

    def test_exact_operation_and_type_contributions_and_immutable_profile(self) -> None:
        profile, carriers = self.profile()
        source = self.checked(profile, carriers).as_dict()
        raw = self.action.read_bytes()
        lines = raw.splitlines(keepends=True)
        for key in ("operation_source", "type_source"):
            ref = source[key]
            contribution = ref["contribution"]
            span = b"".join(lines[contribution["start_line"] - 1:contribution["end_line"]])
            self.assertEqual(hashlib.sha256(span).hexdigest(), contribution["text_sha256"])
            self.assertEqual("CA-O-8001", ref["atom_id"])
        self.assertEqual("Operation", source["operation_source"]["contribution"]["section"])
        self.assertEqual("type", source["type_source"]["contribution"]["property_path"])
        self.assertEqual(source["type_source"]["contribution"]["start_line"], source["type_source"]["contribution"]["end_line"])
        self.assertIn(b"### Inputs and results", b"".join(lines[source["operation_source"]["contribution"]["start_line"] - 1:source["operation_source"]["contribution"]["end_line"]]))
        data = profile.as_dict()
        data["selection"]["atom_ids"].clear()
        self.assertEqual(["CA-O-8001", "CA-O-8002"], profile.as_dict()["selection"]["atom_ids"])
        with self.assertRaises((AttributeError, TypeError)):
            profile.profile_sha256 = "replacement"

    def test_unselected_sibling_is_bound_but_cannot_be_admitted(self) -> None:
        profile, carriers = self.profile()
        with self.assertRaises(core.CoreEntityAdmissionError) as failure:
            self.checked(profile, carriers, "CA-O-8003")
        self.assertEqual("core-source-unselected", failure.exception.code)
        source = self.checked(profile, carriers)
        self.sibling.write_bytes(self.sibling.read_bytes() + b"\nChanged unselected sibling.\n")
        with self.assertRaises(ValueError):
            core.review_core_entity_candidates([source], profile)

    def test_actual_owner_scope_not_claim_target_or_folder_hint(self) -> None:
        self.action.write_text(operation_atom("CA-O-8001", "Alpha Action").replace(
            "claim_target_scope_unit: CORE_META_MODEL", "claim_target_scope_unit: SOME_OTHER_TARGET",
        ), encoding="utf-8")
        profile, carriers = self.profile()
        self.assertEqual("CA-O-8001", self.checked(profile, carriers).as_dict()["atom_id"])
        self.action.write_text(operation_atom("CA-O-8001", "Alpha Action").replace(
            "current_scope_unit: CORE_META_MODEL", "current_scope_unit: FOREIGN_SCOPE",
        ), encoding="utf-8")
        with self.assertRaises(core.CoreEntityAdmissionError) as failure:
            self.profile()
        self.assertEqual("core-owner-foreign", failure.exception.code)

    def test_foreign_folder_cannot_reuse_valid_core_authority_bytes(self) -> None:
        foreign = self.control / "foreign"
        for path in self.folder.rglob("*.md"):
            destination = foreign / path.relative_to(self.folder)
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(path.read_bytes())
        carriers, _ = graph.discover_atoms(self.repository, foreign)
        frontier = graph.source_frontier_for(self.repository, foreign)
        with self.assertRaises(core.CoreEntityAdmissionError) as failure:
            core.prepare_core_entity_profile(self.repository, carriers, frontier, {"atom_ids": ["CA-O-8001"]})
        self.assertEqual("core-folder-foreign", failure.exception.code)

    def test_frontier_structure_selection_and_missing_authority_fail_closed(self) -> None:
        carriers, frontier, selection = self.inputs()
        for invalid_frontier in ({"sealed": "frontier"}, {key: value for key, value in frontier.items() if key != "project_structure"}):
            with self.assertRaises(ValueError):
                core.prepare_core_entity_profile(self.repository, carriers, invalid_frontier, selection)
        for invalid_selection in ({"atom_ids": ["CA-O-9999"]}, {"atom_ids": ["CA-O-8002", "CA-O-8001"]}, {"atom_ids": ["CA-O-8001"], "passed": True}):
            with self.assertRaises(ValueError):
                core.prepare_core_entity_profile(self.repository, carriers, frontier, invalid_selection)
        self.structure.write_bytes(self.structure.read_bytes() + b"\n# changed structure\n")
        with self.assertRaises(ValueError):
            core.prepare_core_entity_profile(self.repository, carriers, frontier, selection)
        required = self.folder / core._REQUIRED_AUTHORITIES["CA-R-1766"][0]
        required.unlink()
        with self.assertRaises(core.CoreEntityAdmissionError) as failure:
            self.profile()
        self.assertEqual("core-authority-missing", failure.exception.code)

    def test_changed_same_identity_authority_is_not_auto_supported(self) -> None:
        path = self.folder / core._REQUIRED_AUTHORITIES["CA-D-276"][0]
        path.write_bytes(path.read_bytes() + b"\n<!-- changed authority -->\n")
        with self.assertRaises(core.CoreEntityAdmissionError) as failure:
            self.profile()
        self.assertEqual("core-authority-unsupported", failure.exception.code)

    def test_unsupported_types_plain_or_fenced_prose_and_missing_type_do_not_admit(self) -> None:
        variants = (
            operation_atom("CA-O-8001", "Alpha Action", "Step"),
            operation_atom("CA-O-8001", "Alpha Action", operation="This source is merely described."),
            operation_atom("CA-O-8001", "Alpha Action", operation="```markdown\nAlpha Action **means** an example.\n```"),
            operation_atom("CA-O-8001", "Alpha Action", operation="> Alpha Action **means** a quoted example."),
            operation_atom("CA-O-8001", "Alpha Action", operation="Alpha Action MEANS named behavior."),
            operation_atom("CA-O-8001", "Alpha Action").replace("type: Action\n", ""),
            operation_atom("CA-O-8001", "Alpha Action").replace("status: Active", "status: active"),
        )
        for text in variants:
            with self.subTest(source=text):
                self.action.write_text(text, encoding="utf-8")
                profile, carriers = self.profile()
                with self.assertRaises(ValueError):
                    self.checked(profile, carriers)

    def test_definition_type_must_match_one_named_primary_profile(self) -> None:
        variants = (
            "Alpha Action **means** the Workflow that consumes its required input.",
            "Alpha Action **means** the reusable Workflow whose entry is one Step.",
            "Alpha Action **means** the Action/Workflow that consumes its required input.",
            "Alpha Action **means** the Action **and** Workflow that consumes its required input.",
            "Alpha Action **means** an Action that consumes its required input.",
            "Alpha Action **means** the Action that consumes input.\n\nAlpha Action **means** the Action that returns a result.",
            "Alpha Action **means** the Action that consumes input.\n\nOther Workflow **means** the Workflow whose entry is one Step.",
        )
        for declaration in variants:
            with self.subTest(declaration=declaration):
                self.action.write_text(operation_atom("CA-O-8001", "Alpha Action", operation=declaration), encoding="utf-8")
                profile, carriers = self.profile()
                with self.assertRaises(core.CoreEntityAdmissionError) as failure:
                    self.checked(profile, carriers)
                self.assertEqual("core-operation-unresolved", failure.exception.code)
                # Unsupported source does not mint any checked input or fact.
                self.assertEqual([], core.review_core_entity_candidates([], profile)["admitted_facts"])

        self.action.write_text(operation_atom("CA-O-8001", "Alpha Action"), encoding="utf-8")
        self.workflow.write_text(operation_atom("CA-O-8002", "Beta Workflow", "Workflow",
                                              operation="Beta Workflow **means** the reusable Workflow whose entry is one Step."), encoding="utf-8")
        profile, carriers = self.profile()
        sources = [self.checked(profile, carriers, atom_id) for atom_id in ("CA-O-8001", "CA-O-8002")]
        result = core.review_core_entity_candidates(sources, profile)
        for decision in result["admission_decisions"]:
            consistency = next(check for check in decision["checks"] if check["code"] == "named-operational-definition-type-consistency")
            self.assertEqual("pass", consistency["disposition"])
            self.assertEqual({"primary_content", "canonical_atom_property"},
                             {ref["contribution"]["kind"] for ref in consistency["source_refs"]})
            self.assertEqual(sorted(consistency["source_refs"], key=facts._source_key), consistency["source_refs"])

    def test_operation_properties_require_exact_heading_layout(self) -> None:
        canonical = operation_atom("CA-O-8001", "Alpha Action")
        variants = (
            canonical.replace("# Summary\n", "# Overview\n"),
            canonical.replace("# Summary\n", "# Summary\n\n# Summary\n"),
            canonical.replace("## Operation\n", "## Claim\n"),
            canonical.replace("## Operation\n", "### Operation\n"),
            canonical.replace("## Details\n", "## Detail\n"),
            canonical.replace("## Details\n", "## Details\n\n## Details\n"),
            canonical.replace("## Operation\n", "## Details\n\n## Operation\n").replace("Supporting information only.", ""),
            canonical.replace("## Details\n", "## Extra\n\n## Details\n"),
            canonical.replace("version: 1\n", "version: 1\noperation: duplicate body property\n"),
        )
        for raw in variants:
            with self.subTest(source=raw):
                self.action.write_text(raw, encoding="utf-8")
                profile, carriers = self.profile()
                with self.assertRaises(core.CoreEntityAdmissionError) as failure:
                    self.checked(profile, carriers)
                self.assertEqual("core-operation-unresolved", failure.exception.code)

        # Lower support headings and fenced examples cannot create Property
        # boundaries or a second primary definition.
        supported = canonical.replace("Required input, declared precondition", "```markdown\n# Summary\n## Operation\nOther Workflow **means** the Workflow whose entry is one Step.\n```\n\n#### Lower support\n\nRequired input, declared precondition")
        self.action.write_text(supported, encoding="utf-8")
        profile, carriers = self.profile()
        result = core.review_core_entity_candidates([self.checked(profile, carriers)], profile)
        self.assertEqual(2, len(result["candidates"]))
        self.assertEqual([], result["admitted_facts"])
        self.assertTrue(all(any(check["code"] == "canonical-operations-property-layout" and check["disposition"] == "pass"
                                for check in decision["checks"]) for decision in result["admission_decisions"]))

    def test_bare_workflow_without_step_graph_and_direction_is_not_admitted(self) -> None:
        self.workflow.write_text(operation_atom("CA-O-8002", "Beta Workflow", "Workflow",
                                               operation="Beta Workflow **means** the Workflow that does some work."), encoding="utf-8")
        profile, carriers = self.profile(["CA-O-8002"])
        source = self.checked(profile, carriers, "CA-O-8002")
        result = core.review_core_entity_candidates([source], profile)
        self.assertEqual(2, len(result["candidates"]))
        self.assertEqual([], result["admitted_facts"])
        for decision in result["admission_decisions"]:
            self.assertEqual("unresolved", decision["disposition"])
            check = next(check for check in decision["checks"] if check["code"] == "semantic-profile-unperformed")
            self.assertEqual("unresolved", check["disposition"])
            refs = {ref["atom_id"] for ref in check["source_refs"]}
            self.assertTrue({"CA-R-1563", "CA-R-1508", "CA-M-314", "CA-O-8002"} <= refs)
        self.assertTrue(all(row["disposition"] == "unknown" and row["admitted_count"] == 0 for row in result["coverage"]))

    def test_forgery_old_descriptors_constructors_duplicates_and_stale_source_are_rejected(self) -> None:
        profile, carriers = self.profile()
        source = self.checked(profile, carriers)
        self.assertFalse(hasattr(core, "_prepare_descriptor_profile"))
        self.assertFalse(hasattr(core, "AuthoritySource"))
        self.assertFalse(hasattr(core, "SourceRef"))
        with self.assertRaises(core.CoreEntityAdmissionError):
            core.CoreEntityProfile(b"{}", self.repository, tuple())
        with self.assertRaises(core.CoreEntityAdmissionError):
            core.CheckedCarrierSource(b"{}", "x" * 64)
        with self.assertRaises(ValueError):
            core.checked_operations_source(self.repository, source.as_dict(), profile)
        with self.assertRaises(ValueError):
            core.review_core_entity_candidates([source.as_dict()], profile)
        with self.assertRaises(ValueError):
            core.review_core_entity_candidates([source], profile.as_dict())
        with self.assertRaises(core.CoreEntityAdmissionError) as failure:
            core.review_core_entity_candidates([source, source], profile)
        self.assertEqual("core-source-duplicate", failure.exception.code)
        self.action.write_bytes(self.action.read_bytes() + b"\nchanged source\n")
        with self.assertRaises(ValueError):
            self.checked(profile, carriers)

    def test_loaded_profile_code_cannot_claim_changed_disk_bytes(self) -> None:
        profile, carriers = self.profile()
        source = self.checked(profile, carriers)
        original = Path.read_bytes
        changed = core._IMPLEMENTATION_PATH.read_bytes() + b"\n# changed after load\n"
        with patch.object(Path, "read_bytes", autospec=True, side_effect=lambda path: changed if path == core._IMPLEMENTATION_PATH else original(path)):
            with self.assertRaises(core.CoreEntityAdmissionError) as failure:
                core.review_core_entity_candidates([source], profile)
            self.assertEqual("profile-stale", failure.exception.code)

    def test_current_crlf_sources_keep_exact_operation_and_type_bytes(self) -> None:
        carriers, frontier, selection = self.inputs()
        self.action.write_bytes(self.action.read_bytes().replace(b"\n", b"\r\n"))
        carriers = [replace(carrier, sha256=hashlib.sha256(self.action.read_bytes()).hexdigest())
                    if carrier.atom_id == "CA-O-8001" else carrier for carrier in carriers]
        frontier["carriers"] = [carrier.evidence() for carrier in carriers]
        frontier["source_frontier_sha256"] = graph.frontier_digest(carriers)
        profile = core.prepare_core_entity_profile(self.repository, carriers, frontier, selection)
        source = self.checked(profile, carriers).as_dict()
        lines = self.action.read_bytes().splitlines(keepends=True)
        for key in ("operation_source", "type_source"):
            contribution = source[key]["contribution"]
            span = b"".join(lines[contribution["start_line"] - 1:contribution["end_line"]])
            self.assertTrue(span.endswith(b"\r\n"))
            self.assertEqual(hashlib.sha256(span).hexdigest(), contribution["text_sha256"])

    def test_sources_are_bound_to_exact_repository_profile_and_selection(self) -> None:
        profile, carriers = self.profile(["CA-O-8001"])
        source = self.checked(profile, carriers)
        other, _ = self.profile(["CA-O-8001", "CA-O-8002"])
        with self.assertRaises(core.CoreEntityAdmissionError) as failure:
            core.review_core_entity_candidates([source], other)
        self.assertEqual("core-source-untrusted", failure.exception.code)
        with self.assertRaises(core.CoreEntityAdmissionError) as failure:
            core.checked_operations_source(self.repository.parent, carriers[0], profile)
        self.assertEqual("core-profile-foreign", failure.exception.code)
        with self.assertRaises(ValueError):
            core.prepare_core_entity_profile(self.repository, [carrier.evidence() for carrier in carriers],
                                             profile.as_dict()["source_frontier"], profile.as_dict()["selection"])


if __name__ == "__main__":
    unittest.main()
