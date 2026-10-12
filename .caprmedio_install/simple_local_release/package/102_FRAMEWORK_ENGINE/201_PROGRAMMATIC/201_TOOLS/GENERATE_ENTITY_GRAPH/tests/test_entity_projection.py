"""Focused contract tests for the pure native-ownership projection."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from dataclasses import dataclass
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "entity_projection.py"
SPEC = importlib.util.spec_from_file_location("entity_projection", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
projection = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = projection
SPEC.loader.exec_module(projection)
sys.path.insert(0, str(SCRIPT.parent))
import generate_entity_graph  # noqa: E402
import graph_fact_context  # noqa: E402


@dataclass(frozen=True)
class Carrier:
    atom_id: str
    version: int
    carrier_path: str
    sha256: str

    def evidence(self) -> dict[str, object]:
        return {"atom_id": self.atom_id, "atom_revision": self.version, "carrier_path": self.carrier_path, "carrier_sha256": self.sha256}


@dataclass(frozen=True)
class Relation:
    atom_id: str
    atom_revision: int
    carrier_path: str
    carrier_sha256: str
    subject_path: str
    kind: str


class EntityProjectionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.first = Carrier("CA-A-001", 2, "atoms/one.md", "a" * 64)
        self.second = Carrier("CA-A-002", 7, "atoms/two.md", "b" * 64)
        self.metadata = {
            "CA-A-001": {"author": "Ada", "content_role": "Requirement", "status": "Active", "version": 2},
            "CA-A-002": {"author": "Benoit", "content_role": "Plan", "status": "Draft", "version": 7},
        }

    def build(self) -> dict[str, object]:
        return projection.build_entity_projection(
            [self.second, self.first],
            [
                Relation("CA-A-001", 2, "atoms/one.md", "a" * 64, "Domain/Thing", "GOVERNS"),
                Relation("CA-A-002", 7, "atoms/two.md", "b" * 64, "Domain/Thing", "GOVERNS"),
                Relation("CA-A-001", 2, "atoms/one.md", "a" * 64, "External/Prerequisite", "DEPENDS_ON"),
            ],
            self.metadata,
            [{"scope_unit_name": "TOOLS", "parent": "FRAMEWORK"}],
        )

    def test_governing_subjects_are_unresolved_candidates_and_authors_stay_local(self) -> None:
        result = self.build()

        self.assertEqual([], result["entities"])
        self.assertEqual(["Domain/Thing", "Domain/Thing"], [row["candidate_identity"] for row in result["entity_candidates"]])
        self.assertEqual({"unresolved"}, {row["disposition"] for row in result["entity_candidates"]})
        self.assertEqual(3, len(result["atom_incidence"]))
        self.assertEqual(["CA-A-001", "CA-A-002"], [row["atom_id"] for row in result["source_atoms"]])
        self.assertEqual("Ada", result["source_atoms"][0]["metadata"]["author"])
        serialized_entities = str(result["entities"]) + str(result["entity_candidates"]) + str(result["atom_incidence"]) + str(result["external_references"])
        self.assertNotIn("Ada", serialized_entities)
        self.assertNotIn("Benoit", serialized_entities)

    def test_incidence_preserves_exact_source_hash_and_depends_on_does_not_invent_native_edge(self) -> None:
        result = self.build()

        dependency = next(row for row in result["atom_incidence"] if row["relation"] == "DEPENDS_ON")
        self.assertEqual({"sourceAtomID": "CA-A-001", "atom_revision": 2, "carrier_path": "atoms/one.md", "carrier_sha256": "a" * 64}, dependency["source"])
        self.assertEqual([], result["native_relations"])
        self.assertEqual(["External/Prerequisite"], [row["subject_path"] for row in result["external_references"]])
        self.assertEqual([], result["native_properties"])
        self.assertEqual("not-covered", result["coverage"]["properties"]["status"])
        self.assertEqual("unknown", result["coverage"]["entity_admission"]["status"])

    def test_untrusted_mapping_cannot_admit_native_facts(self) -> None:
        with self.assertRaisesRegex(ValueError, "graph_fact_context"):
            projection.build_entity_projection(
                [self.first], [], self.metadata, [],
                graph_fact_context={"admitted_facts": [{"fact_class": "entity_admission"}]},
            )

    def test_duplicate_carrier_identity_is_rejected_without_selecting_a_winner(self) -> None:
        duplicate = Carrier("CA-A-001", 3, "atoms/duplicate.md", "c" * 64)

        with self.assertRaisesRegex(ValueError, "carrier identities must be unique"):
            projection.build_entity_projection([self.first, duplicate], [], self.metadata, [])

    def test_verified_complete_empty_context_keeps_native_collections_empty_and_complete(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            repository = Path(temporary) / "repository"
            selected = repository / "selected"
            selected.mkdir(parents=True)
            (selected / "CA-R-001.md").write_text(
                "---\n"
                "atom_id: CA-R-001\ncontent_role: Requirement\ncurrent_scope_unit: TOOLS\n"
                "claim_target_scope_unit: TOOLS\nstatus: Active\nauthor: Test Author\nversion: 1\n"
                'updated_at: "2026-10-09 00:00:00 +0000"\nsubjects:\n  governs: Entity\n'
                "  depends_on: []\nrelations: {}\n---\n# Summary\nSynthetic source.\n\n"
                "## Scope\nTOOLS.\n\n## Claim\nEntity MEANS an identity.\n\n## Details\nFixture.\n",
                encoding="utf-8",
            )
            carriers, diagnostics = generate_entity_graph.discover_atoms(repository, selected)
            self.assertEqual([], diagnostics)
            frontier = generate_entity_graph.source_frontier_for(repository, selected)
            context = graph_fact_context.prepare_fact_context(
                repository, "entities", carriers,
                {"atom_ids": [], "scope_unit_names": []}, frontier, carriers,
            )

            result = projection.build_entity_projection(carriers, [], {}, [], context)

        self.assertEqual([], result["entities"])
        self.assertEqual([], result["native_properties"])
        self.assertEqual([], result["native_relations"])
        self.assertEqual("complete", result["coverage"]["entity_admission"]["status"])
        self.assertEqual("complete", result["coverage"]["properties"]["status"])
        self.assertEqual("complete", result["coverage"]["native_relations"]["status"])


if __name__ == "__main__":
    unittest.main()
