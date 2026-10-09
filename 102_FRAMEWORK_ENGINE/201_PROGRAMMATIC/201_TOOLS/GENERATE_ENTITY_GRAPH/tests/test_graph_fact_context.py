"""TDD contract tests for the source-pinned derived graph fact context."""

from __future__ import annotations

import hashlib
import importlib.util
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
from unittest.mock import patch


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
TOOL_DIRECTORY = Path(__file__).resolve().parents[1]
GRAPH_SPEC = importlib.util.spec_from_file_location("graph_fact_context_graph_builder", TOOL_DIRECTORY / "generate_entity_graph.py")
assert GRAPH_SPEC is not None and GRAPH_SPEC.loader is not None
graph_builder = importlib.util.module_from_spec(GRAPH_SPEC)
sys.modules[GRAPH_SPEC.name] = graph_builder
GRAPH_SPEC.loader.exec_module(graph_builder)

# This module is intentionally absent at the TDD baseline.
sys.path.insert(0, str(TOOL_DIRECTORY))
import graph_fact_context  # type: ignore[import-not-found]  # noqa: E402


def current_atom(atom_id: str, claim: str, *, eol: str = "\n") -> str:
    return eol.join((
        "---",
        f"atom_id: {atom_id}",
        "content_role: Requirement",
        "current_scope_unit: TOOLS",
        "claim_target_scope_unit: TOOLS",
        "status: Active",
        "author: Test Author",
        "version: 1",
        'updated_at: "2026-10-09 00:00:00 +0000"',
        "subjects:",
        "  governs: Entity",
        "  depends_on: []",
        "relations:",
        "  relates_to: []",
        "---",
        "# Summary",
        "A current synthetic source.",
        "",
        "## Scope",
        "TOOLS.",
        "",
        "## Claim",
        claim,
        "",
        "## Details",
        "Bounded test-only details.",
        "",
    ))


class GraphFactContextTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.repository = Path(self.temporary.name) / "repository"
        self.selected = self.repository / "selected"
        self.selected.mkdir(parents=True)
        self.source = self.selected / "CA-R-001.md"
        self.source.write_text(
            current_atom("CA-R-001", "Entity MEANS a canonical graph identity."),
            encoding="utf-8", newline="",
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def inputs(self, *, atom_ids: list[str] | None = None) -> tuple[list[object], dict[str, object], dict[str, object]]:
        carriers, diagnostics = graph_builder.discover_atoms(self.repository, self.selected)
        self.assertEqual([], diagnostics)
        frontier = graph_builder.source_frontier_for(self.repository, self.selected)
        selection = {"atom_ids": ["CA-R-001"] if atom_ids is None else atom_ids, "scope_unit_names": []}
        return carriers, frontier, selection

    def prepare(self, *, atom_ids: list[str] | None = None, graph_kind: str = "entities"):
        carriers, frontier, selection = self.inputs(atom_ids=atom_ids)
        return graph_fact_context.prepare_fact_context(
            self.repository, graph_kind, carriers, selection, frontier, carriers,
        )

    def details_authorities(self) -> list[object]:
        """Use the actual pinned assignment bytes, never a passed test flag."""
        core = TOOL_DIRECTORY.parents[3] / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL"
        destinations = self.repository / "authority"
        destinations.mkdir(exist_ok=True)
        sources = (
            core / "07_delivery/CA-D-478-CORE_META_MODEL-CORE-DELIVERY--store-every-atom-property-in-one-internal-location.md",
            core / "07_delivery/CA-D-479-CORE_META_MODEL-DELIVERY--use-stable-headings-for-atom-body-properties.md",
            core / "04_requirement/CA-R-1624-CORE_META_MODEL-CORE-REQUIREMENT--keep-details-within-the-primary-contribution.md",
        )
        for source in sources:
            (destinations / source.name).write_bytes(source.read_bytes())
        carriers, diagnostics = graph_builder.discover_atoms(self.repository, destinations)
        self.assertEqual([], diagnostics)
        return carriers

    def test_canonical_bytes_are_exact_and_reject_noncanonical_values(self) -> None:
        self.assertEqual(
            b'{"a":"\xce\xbb","z":[1,true,null]}',
            graph_fact_context.canonical_bytes({"z": [1, True, None], "a": "λ"}),
        )
        for invalid in ({"value": 1.0}, {"value": "\ud800"}):
            with self.subTest(invalid=repr(invalid)):
                with self.assertRaises(Exception):
                    graph_fact_context.canonical_bytes(invalid)

    def test_lowercase_concern_lifecycle_is_retained_not_promoted_to_admission(self) -> None:
        self.source.write_text(current_atom("CA-C-001", "A concern is not a Definition.")
                               .replace("content_role: Requirement", "content_role: Concern")
                               .replace("status: Active", "status: active"), encoding="utf-8")
        carriers, frontier, selection = self.inputs(atom_ids=["CA-C-001"])
        context = graph_fact_context.prepare_fact_context(
            self.repository, "terms", carriers, selection, frontier, carriers).as_dict()
        self.assertEqual("active", frontier["carriers"][0]["status"])
        self.assertEqual([], context["admitted_facts"])
        self.assertTrue(all(row["disposition"] == "unknown" for row in context["coverage"]))
        self.assertIn("status-model-unresolved", {row["code"] for row in context["diagnostics"]})

    def test_context_is_immutable_detached_and_self_hashes_exact_canonical_bytes(self) -> None:
        context = self.prepare()
        first = context.as_dict()
        self.assertEqual(
            {
                "schema_version", "context_kind", "graph_kind", "source_binding", "provider",
                "authority_sources", "relation_registry", "coverage", "candidates", "admission_decisions",
                "admitted_facts", "derivations", "diagnostics", "context_sha256",
            },
            set(first),
        )
        expected = dict(first)
        digest = expected.pop("context_sha256")

        self.assertEqual(hashlib.sha256(graph_fact_context.canonical_bytes(expected)).hexdigest(), digest)
        self.assertEqual(graph_fact_context.canonical_bytes(first), graph_fact_context.canonical_bytes(context.as_dict()))
        first["coverage"].append({"caller": "mutation"})
        self.assertNotIn({"caller": "mutation"}, context.as_dict()["coverage"])
        with self.assertRaises((AttributeError, TypeError)):
            context.context_sha256 = "caller-replacement"

    def test_primary_claim_source_reference_uses_inclusive_original_eol_span_and_detects_drift(self) -> None:
        context = self.prepare().as_dict()
        sources = context["authority_sources"]
        claim_source = next(item for item in sources if item["contribution"].get("section") == "Claim")
        contribution = claim_source["contribution"]
        raw = self.source.read_bytes()
        lines = raw.splitlines(keepends=True)
        span = b"".join(lines[contribution["start_line"] - 1 : contribution["end_line"]])
        self.assertEqual(hashlib.sha256(span).hexdigest(), contribution["text_sha256"])
        self.assertTrue(span.endswith(b"\n"))

        carriers, frontier, selection = self.inputs()
        self.source.write_text(
            current_atom("CA-R-001", "Entity MEANS a canonical graph identity.", eol="\r\n"),
            encoding="utf-8", newline="",
        )
        with self.assertRaises(Exception):
            graph_fact_context.prepare_fact_context(
                self.repository, "entities", carriers, selection, frontier, carriers,
            )

    def test_governs_metadata_dependencies_and_matching_prose_never_admit_native_facts_without_profiles(self) -> None:
        context = self.prepare().as_dict()

        self.assertEqual([], context["admitted_facts"])
        self.assertEqual([], context["derivations"])
        self.assertTrue(any(row["disposition"] == "unresolved" for row in context["admission_decisions"]))

    def test_generic_matching_prose_is_not_a_candidate_or_native_fact(self) -> None:
        self.source.write_text(
            current_atom("CA-R-001", "Entity is governed and related to Entity."),
            encoding="utf-8", newline="",
        )
        context = self.prepare().as_dict()

        self.assertEqual([], context["admitted_facts"])
        self.assertEqual([], context["candidates"])
        self.assertEqual([], context["admission_decisions"])

    def test_unsupported_coverage_is_unknown_never_evidentiary_empty(self) -> None:
        context = self.prepare().as_dict()

        self.assertEqual({"entity_admission", "entity_property", "relation"}, {row["fact_class"] for row in context["coverage"]})
        for row in context["coverage"]:
            self.assertEqual("unknown", row["disposition"])
            self.assertEqual("unknown", row["selected_result"])

    def test_explicit_empty_selection_with_a_current_sealed_frontier_is_complete_empty_and_writes_no_journal(self) -> None:
        before = sorted(path.relative_to(self.repository).as_posix() for path in self.repository.rglob("*"))
        context = self.prepare(atom_ids=[]).as_dict()
        after = sorted(path.relative_to(self.repository).as_posix() for path in self.repository.rglob("*"))

        self.assertEqual(before, after)
        self.assertEqual([], context["admitted_facts"])
        for row in context["coverage"]:
            self.assertEqual("complete", row["disposition"])
            self.assertEqual("empty", row["selected_result"])
            self.assertEqual(0, row["admitted_count"])

    def test_context_evidence_is_the_closed_copy_of_context_identity_provider_binding_and_coverage(self) -> None:
        context = self.prepare()
        evidence = graph_fact_context.context_evidence(context)

        self.assertEqual({"context_sha256", "provider", "source_binding", "coverage"}, set(evidence))
        self.assertEqual(context.context_sha256, evidence["context_sha256"])
        self.assertEqual(context.as_dict()["coverage"], evidence["coverage"])

    def test_terms_context_has_its_own_required_unknown_coverage(self) -> None:
        context = self.prepare(graph_kind="terms").as_dict()

        self.assertEqual({"definition", "relation"}, {row["fact_class"] for row in context["coverage"]})
        self.assertTrue(all(row["selected_result"] == "unknown" for row in context["coverage"]))

    def test_crlf_claim_span_hashes_the_original_bytes(self) -> None:
        carriers, _, selection = self.inputs()
        self.source.write_text(
            current_atom("CA-R-001", "Entity MEANS a canonical graph identity.", eol="\r\n"),
            encoding="utf-8", newline="",
        )
        crlf_carrier = replace(carriers[0], sha256=hashlib.sha256(self.source.read_bytes()).hexdigest())
        crlf_frontier = {
            "selected_folder": "selected",
            "carriers": [crlf_carrier.evidence()],
            "source_frontier_sha256": graph_builder.frontier_digest([crlf_carrier]),
        }
        context = graph_fact_context.prepare_fact_context(
            self.repository, "entities", [crlf_carrier], selection, crlf_frontier, [crlf_carrier],
        ).as_dict()
        source = next(item for item in context["authority_sources"] if item["contribution"].get("section") == "Claim")
        contribution = source["contribution"]
        lines = self.source.read_bytes().splitlines(keepends=True)
        span = b"".join(lines[contribution["start_line"] - 1 : contribution["end_line"]])

        self.assertTrue(span.endswith(b"\r\n"))
        self.assertEqual(hashlib.sha256(span).hexdigest(), contribution["text_sha256"])

    def test_rejects_duplicate_id_malformed_unsorted_or_unknown_selection(self) -> None:
        duplicate = self.selected / "duplicate.md"
        duplicate.write_text(
            current_atom("CA-R-001", "Entity MEANS a second canonical graph identity."),
            encoding="utf-8", newline="",
        )
        carriers, frontier, selection = self.inputs()
        with self.assertRaises(Exception):
            graph_fact_context.prepare_fact_context(self.repository, "entities", carriers, selection, frontier, carriers)

        duplicate.unlink()
        (self.selected / "CA-R-002.md").write_text(
            current_atom("CA-R-002", "Second MEANS a canonical graph identity."), encoding="utf-8", newline="",
        )
        carriers, frontier, selection = self.inputs()
        for invalid in (
            {"atom_ids": ["CA-R-999"], "scope_unit_names": []},
            {"atom_ids": ["CA-R-001", "CA-R-001"], "scope_unit_names": []},
            {"atom_ids": ["CA-R-002", "CA-R-001"], "scope_unit_names": []},
            {"atom_ids": "CA-R-001", "scope_unit_names": []},
            {"atom_ids": ["CA-R-001"], "scope_unit_names": [], "caller_admission": True},
        ):
            with self.subTest(invalid=invalid):
                with self.assertRaises(Exception):
                    graph_fact_context.prepare_fact_context(self.repository, "entities", carriers, invalid, frontier, carriers)

    def test_rejects_forged_context_mapping_and_escaping_carrier_path(self) -> None:
        context = self.prepare()
        with self.assertRaises(Exception):
            graph_fact_context.context_evidence(context.as_dict())

        carriers, frontier, selection = self.inputs()
        escaping = replace(carriers[0], carrier_path="../outside/CA-R-001.md")
        with self.assertRaises(Exception):
            graph_fact_context.prepare_fact_context(
                self.repository, "entities", [escaping], selection, frontier, [escaping],
            )

        alias_path = self.selected / "alias.md"
        alias_path.symlink_to(self.source)
        alias = replace(carriers[0], carrier_path="selected/alias.md")
        with self.assertRaises(graph_fact_context.FactContextError) as failure:
            graph_fact_context.prepare_fact_context(
                self.repository, "entities", [alias], selection, frontier, [alias],
            )
        self.assertEqual("context-path-ambiguous", failure.exception.code)

    def test_loaded_implementation_cannot_claim_changed_disk_profile_bytes(self) -> None:
        carriers, frontier, selection = self.inputs()
        context = self.prepare()
        module_path = graph_fact_context._IMPLEMENTATION_PATH
        original_read = Path.read_bytes
        original_source = self.source.read_bytes()
        changed_implementation = module_path.read_bytes() + b"\n# changed after module load\n"

        def current_bytes(path: Path) -> bytes:
            return changed_implementation if path == module_path else original_read(path)

        with patch.object(Path, "read_bytes", autospec=True, side_effect=current_bytes):
            self.assertEqual(original_source, self.source.read_bytes())
            with self.assertRaises(graph_fact_context.FactContextError) as failure:
                graph_fact_context.prepare_fact_context(
                    self.repository, "entities", carriers, selection, frontier, carriers,
                )
            self.assertEqual("profile-stale", failure.exception.code)
            with self.assertRaises(graph_fact_context.FactContextError) as recheck_failure:
                graph_fact_context.verified_context(
                    context, self.repository, "entities", carriers, selection, frontier, carriers,
                )
            self.assertEqual("profile-stale", recheck_failure.exception.code)

        self.assertEqual(original_source, self.source.read_bytes())
        self.assertEqual(context.context_sha256, self.prepare().context_sha256)

    def test_bound_details_evidence_preserves_whole_lf_and_crlf_section_without_widening_claim(self) -> None:
        authorities = self.details_authorities()
        base_carriers, _, selection = self.inputs()
        support = "\n".join((
            "### relation admission", "", "- Status: the test relation is Active.", "",
            "```markdown", "## Claim", "# Summary", "```", "",
            "### nested support", "Supporting information only.",
        ))
        for eol in ("\n", "\r\n"):
            with self.subTest(eol=repr(eol)):
                text = current_atom("CA-R-001", "Entity MEANS a canonical graph identity.").replace(
                    "Bounded test-only details.", support,
                ).replace("\n", eol)
                self.source.write_text(text, encoding="utf-8", newline="")
                raw = self.source.read_bytes()
                carrier = replace(base_carriers[0], sha256=hashlib.sha256(raw).hexdigest())
                frontier = {"selected_folder": "selected", "carriers": [carrier.evidence()],
                            "source_frontier_sha256": graph_builder.frontier_digest([carrier])}
                context = graph_fact_context.prepare_fact_context(
                    self.repository, "entities", [carrier], selection, frontier, [carrier, *authorities],
                ).as_dict()
                rows = [row for row in context["authority_sources"] if row["atom_id"] == "CA-R-001"]
                details = next(row for row in rows if row["contribution"].get("section") == "Details")
                claim = next(row for row in rows if row["contribution"].get("section") == "Claim")
                self.assertEqual("canonical_atom_property", details["contribution"]["kind"])
                self.assertNotIn("property_path", details["contribution"])
                lines = raw.splitlines(keepends=True)
                heading = next(index for index, line in enumerate(lines) if line.rstrip(b"\r\n") == b"## Details")
                contribution = details["contribution"]
                self.assertEqual(heading + 2, contribution["start_line"])
                self.assertEqual(len(lines), contribution["end_line"])
                span = b"".join(lines[contribution["start_line"] - 1:contribution["end_line"]])
                self.assertIn(b"### relation admission", span)
                self.assertIn(b"## Claim", span)
                self.assertTrue(span.endswith(eol.encode()))
                self.assertEqual(hashlib.sha256(span).hexdigest(), contribution["text_sha256"])
                self.assertEqual(heading, claim["contribution"]["end_line"])
                self.assertEqual(details, graph_fact_context.raw_section_property_evidence(
                    self.repository, carrier, authority_sources=authorities,
                ))
                self.assertEqual([], context["admitted_facts"])
                self.assertTrue(all(row["disposition"] == "unknown" for row in context["coverage"]))
                expected_sources = sorted(context["authority_sources"], key=graph_fact_context._source_key)
                self.assertEqual(expected_sources, context["authority_sources"])
                self.assertEqual(len(expected_sources), len({graph_fact_context.canonical_bytes(row) for row in expected_sources}))
                self.assertEqual(hashlib.sha256(graph_fact_context.canonical_bytes(expected_sources)).hexdigest(),
                                 context["source_binding"]["authority_frontier_sha256"])

    def test_details_requires_all_current_reviewed_assignment_authorities(self) -> None:
        carriers, frontier, selection = self.inputs()
        authorities = self.details_authorities()
        for incomplete in ([], [carrier for carrier in authorities if carrier.atom_id != "CA-R-1624"]):
            with self.subTest(ids=[carrier.atom_id for carrier in incomplete]):
                self.assertIsNone(graph_fact_context.raw_section_property_evidence(
                    self.repository, carriers[0], authority_sources=incomplete,
                ))
                context = graph_fact_context.prepare_fact_context(
                    self.repository, "entities", carriers, selection, frontier, [*carriers, *incomplete],
                ).as_dict()
                self.assertFalse(any(row["contribution"].get("section") == "Details" for row in context["authority_sources"]))
                self.assertTrue(any(row["code"] == "details-assignment-profile-unavailable" for row in context["diagnostics"]))

        changed_authority = next(carrier for carrier in authorities if carrier.atom_id == "CA-D-479")
        path = self.repository / changed_authority.carrier_path
        path.write_bytes(path.read_bytes() + b"\n<!-- unsupported authority revision bytes -->\n")
        with self.assertRaises(graph_fact_context.FactContextError) as failure:
            graph_fact_context.raw_section_property_evidence(self.repository, carriers[0], authority_sources=authorities)
        self.assertEqual("context-source-stale", failure.exception.code)
        refreshed, _ = graph_builder.discover_atoms(self.repository, path.parent)
        self.assertIsNone(graph_fact_context.raw_section_property_evidence(
            self.repository, carriers[0], authority_sources=refreshed,
        ))

    def test_details_rejects_unassigned_or_ambiguous_layout_and_duplicate_frontmatter_value(self) -> None:
        authorities = self.details_authorities()
        original = current_atom("CA-R-001", "Entity MEANS a canonical graph identity.")
        variants = (
            original.replace("## Details", "## Notes"),
            original + "\n## Details\nAnother value.\n",
            original.replace("## Details", "## Details\nValue.\n\n## Other section"),
            original.replace("version: 1", "version: 1\ndetails: duplicate value"),
            original.replace("content_role: Requirement", "content_role: Plan"),
            original.replace("# Summary", "# A title"),
        )
        for text in variants:
            with self.subTest(layout=text):
                self.source.write_text(text, encoding="utf-8", newline="")
                carriers, _, _ = self.inputs()
                self.assertIsNone(graph_fact_context.raw_section_property_evidence(
                    self.repository, carriers[0], authority_sources=authorities,
                ))
        with self.assertRaises(graph_fact_context.FactContextError) as failure:
            graph_fact_context.raw_section_property_evidence(
                self.repository, carriers[0], section="Notes", authority_sources=authorities,
            )
        self.assertEqual("context-section-unsupported", failure.exception.code)

    def test_operations_details_uses_separate_assigned_section_not_a_claim_alias(self) -> None:
        authorities = self.details_authorities()
        text = current_atom("CA-R-001", "Entity MEANS named operational behavior.").replace(
            "content_role: Requirement", "content_role: Operations",
        ).replace("## Scope\nTOOLS.\n\n", "").replace("## Claim", "## Operation")
        self.source.write_text(text, encoding="utf-8", newline="")
        carriers, frontier, selection = self.inputs()
        context = graph_fact_context.prepare_fact_context(
            self.repository, "entities", carriers, selection, frontier, [*carriers, *authorities],
        ).as_dict()
        rows = [row for row in context["authority_sources"] if row["atom_id"] == "CA-R-001"]
        self.assertEqual({("primary_content", "Operation"), ("canonical_atom_property", "Details")},
                         {(row["contribution"]["kind"], row["contribution"]["section"]) for row in rows})
        self.assertEqual([], context["admitted_facts"])

    def test_rejects_authority_carrier_stale_bytes_separately_from_the_current_selected_source(self) -> None:
        authority_path = self.selected / "CA-R-002.md"
        authority_path.write_text(
            current_atom("CA-R-002", "Authority MEANS a bounded definition."), encoding="utf-8", newline="",
        )
        carriers, _, selection = self.inputs()
        old_authority = next(carrier for carrier in carriers if carrier.atom_id == "CA-R-002")
        authority_path.write_text(
            current_atom("CA-R-002", "Authority MEANS changed bytes."), encoding="utf-8", newline="",
        )
        current_carriers, diagnostics = graph_builder.discover_atoms(self.repository, self.selected)
        self.assertEqual([], diagnostics)
        current_frontier = graph_builder.source_frontier_for(self.repository, self.selected)

        with self.assertRaises(Exception):
            graph_fact_context.prepare_fact_context(
                self.repository, "entities", current_carriers, selection, current_frontier, [old_authority],
            )


if __name__ == "__main__":
    unittest.main()
