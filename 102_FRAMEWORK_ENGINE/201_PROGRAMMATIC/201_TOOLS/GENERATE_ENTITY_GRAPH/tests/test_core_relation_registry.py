"""Focused checks for the closed, source-pinned Core Relation registry."""

from __future__ import annotations

import hashlib
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
TOOL_DIRECTORY = Path(__file__).resolve().parents[1]
WORKSPACE = TOOL_DIRECTORY.parents[3]
ACTUAL_CORE = (
    WORKSPACE
    / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL"
)
if str(TOOL_DIRECTORY) not in sys.path:
    sys.path.insert(0, str(TOOL_DIRECTORY))

import core_relation_registry as registry  # noqa: E402
import generate_entity_graph as graph  # noqa: E402


class CoreRelationRegistryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.repository = Path(self.temporary.name) / "repository"
        self.control = self.repository / ".caprmedio_caprmedio"
        self.authority = (
            self.control
            / "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL"
        )
        self.authority.mkdir(parents=True)
        (self.control / "caprmedio_project_settings.toml").write_text(
            "[paths]\n"
            "control_root = '.caprmedio_caprmedio'\n"
            "projection_root = '.caprmedio_caprmedio/_projection'\n",
            encoding="utf-8",
        )
        (self.control / "project_structure.toml").write_text(
            "[[scope_units]]\n"
            "scope_unit_name = 'CORE_META_MODEL'\n"
            "authority_path = '.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL'\n"
            "authority_mode = 'strict'\n",
            encoding="utf-8",
        )
        for _, (_, _, _, suffix) in registry._REQUIRED_AUTHORITIES.items():
            source = ACTUAL_CORE / suffix
            destination = self.authority / suffix
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def inputs(self):
        carriers, diagnostics = graph.discover_atoms(self.repository, self.authority)
        self.assertEqual([], diagnostics)
        return (
            carriers,
            graph.source_frontier_for(self.repository, self.authority),
            {"atom_ids": [], "scope_unit_names": ["CORE_META_MODEL"]},
        )

    def prepare(self):
        carriers, frontier, selection = self.inputs()
        return registry.prepare_core_relation_registry(
            self.repository, carriers, frontier, selection
        )

    @staticmethod
    def relation(records, graph_kind: str, canonical_name: str):
        return next(
            item
            for item in records
            if item["kind"]
            == {
                "graph_kind": graph_kind,
                "canonical_name": canonical_name,
            }
        )

    def test_actual_current_registered_core_frontier_compiles_three_closed_records(self) -> None:
        carriers, diagnostics = graph.discover_atoms(WORKSPACE, ACTUAL_CORE)
        self.assertFalse([item for item in diagnostics if item.get("severity") == "error"])
        frontier = graph.source_frontier_for(WORKSPACE, ACTUAL_CORE)
        result = registry.prepare_core_relation_registry(
            WORKSPACE,
            carriers,
            frontier,
            {"atom_ids": [], "scope_unit_names": ["CORE_META_MODEL"]},
        )

        self.assertEqual((), result.diagnostics)
        self.assertEqual(
            [
                ("entities", "IS_ALLOWED_VALUE_OF"),
                ("entities", "IS_BORNE_BY"),
                ("terms", "NARROWER_THAN"),
            ],
            [(row["kind"]["graph_kind"], row["kind"]["canonical_name"]) for row in result.records],
        )

    def test_records_have_complete_reviewed_metadata_exact_digests_and_contribution_refs(
        self,
    ) -> None:
        result = self.prepare()
        records = result.records
        self.assertEqual((), result.diagnostics)
        self.assertEqual(3, len(records))
        self.assertNotIn("BEARS", {row["kind"]["canonical_name"] for row in records})

        borne = self.relation(records, "entities", "IS_BORNE_BY")
        allowed = self.relation(records, "entities", "IS_ALLOWED_VALUE_OF")
        narrower = self.relation(records, "terms", "NARROWER_THAN")
        self.assertEqual("Dependent Entity", borne["metadata"]["source_class"])
        self.assertEqual("Entity", borne["metadata"]["target_class"])
        self.assertEqual(
            {"outgoing": "exactly_one", "incoming": "unconstrained"},
            borne["metadata"]["cardinality"],
        )
        self.assertEqual(
            {"kind": "declared", "graph_kind": "entities", "canonical_name": "BEARS"},
            borne["metadata"]["inverse"],
        )
        self.assertEqual("nontransitive", borne["metadata"]["transitivity"])
        self.assertEqual("Value occurrence", allowed["metadata"]["source_class"])
        self.assertEqual({"kind": "reverse_navigation"}, allowed["metadata"]["inverse"])
        self.assertEqual(
            {"outgoing": "unconstrained", "incoming": "unconstrained"},
            allowed["metadata"]["cardinality"],
        )
        self.assertIn(
            "without_assignment_or_cardinality_effect", allowed["metadata"]["exclusive_purpose"]
        )
        self.assertEqual(
            "zero_or_more_direct_parents", narrower["metadata"]["cardinality"]["outgoing"]
        )
        self.assertEqual("acyclic_definition_implication", narrower["metadata"]["authority_effect"])
        self.assertEqual(
            "semantic_transitivity_without_implicit_edge_materialization",
            narrower["metadata"]["transitivity"],
        )
        self.assertIn("CA-R-1347", {ref["atom_id"] for ref in narrower["authority_inputs"]})

        for record in records:
            self.assertEqual(
                {
                    "kind",
                    "metadata",
                    "authority_inputs",
                    "evaluator",
                    "checks",
                    "registry_record_sha256",
                },
                set(record),
            )
            self.assertEqual(registry._METADATA_FIELDS, set(record["metadata"]))
            digest_input = dict(record)
            digest = digest_input.pop("registry_record_sha256")
            self.assertEqual(
                hashlib.sha256(registry.canonical_bytes(digest_input)).hexdigest(), digest
            )
            self.assertEqual(
                registry._source_refs(record["authority_inputs"]),
                record["authority_inputs"],
            )
            self.assertEqual(
                [row["code"] for row in record["checks"]],
                sorted(row["code"] for row in record["checks"]),
            )
            for source in [
                *record["authority_inputs"],
                *(ref for check in record["checks"] for ref in check["source_refs"]),
            ]:
                contribution = source["contribution"]
                self.assertIn(contribution["kind"], {"primary_content", "canonical_atom_property"})
                self.assertGreaterEqual(contribution["start_line"], 1)
                self.assertGreaterEqual(contribution["end_line"], contribution["start_line"])
                raw = (
                    (self.repository / source["carrier_path"])
                    .read_bytes()
                    .splitlines(keepends=True)
                )
                span = b"".join(raw[contribution["start_line"] - 1 : contribution["end_line"]])
                self.assertEqual(hashlib.sha256(span).hexdigest(), contribution["text_sha256"])

    def test_kind_status_is_proven_by_details_not_transferred_from_atom_lifecycle(self) -> None:
        result = self.prepare()
        for record in result.records:
            self.assertEqual("Active", record["metadata"]["status"])
            self.assertTrue(all("status" not in ref for ref in record["authority_inputs"]))
            status_check = next(
                item
                for item in record["checks"]
                if item["code"] == "explicit-relation-kind-status-current"
            )
            self.assertEqual(1, len(status_check["source_refs"]))
            source = status_check["source_refs"][0]
            self.assertEqual("canonical_atom_property", source["contribution"]["kind"])
            self.assertEqual("Details", source["contribution"]["section"])

    def test_changed_authority_or_stale_frontier_fails_closed_without_records(self) -> None:
        carriers, frontier, selection = self.inputs()
        changed = next(item for item in carriers if item.atom_id == "CA-R-1260")
        path = self.repository / changed.carrier_path
        path.write_bytes(path.read_bytes() + b"\n<!-- changed authority -->\n")

        stale = registry.prepare_core_relation_registry(
            self.repository, carriers, frontier, selection
        )
        self.assertEqual((), stale.records)
        self.assertIn(
            stale.diagnostics[0]["code"],
            {"registry-frontier-stale", "registry-carriers-unverified"},
        )

        fresh_carriers, fresh_frontier, fresh_selection = self.inputs()
        changed_profile = registry.prepare_core_relation_registry(
            self.repository,
            fresh_carriers,
            fresh_frontier,
            fresh_selection,
        )
        self.assertEqual((), changed_profile.records)
        self.assertEqual("registry-authority-unsupported", changed_profile.diagnostics[0]["code"])

    def test_path_alias_and_foreign_core_path_fail_closed(self) -> None:
        real = self.authority.with_name("actual-core")
        self.authority.rename(real)
        self.authority.symlink_to(real, target_is_directory=True)
        carriers, frontier, selection = self.inputs()
        aliased = registry.prepare_core_relation_registry(
            self.repository, carriers, frontier, selection
        )
        self.assertEqual((), aliased.records)
        self.assertEqual("registry-profile-unavailable", aliased.diagnostics[0]["code"])

        self.temporary.cleanup()
        self.setUp()
        structure = self.control / "project_structure.toml"
        structure.write_text(
            structure.read_text(encoding="utf-8").replace(
                "001_CORE_META_MODEL",
                "101_STALE_PUBLIC_COPY",
                1,
            ),
            encoding="utf-8",
        )
        carriers, frontier, selection = self.inputs()
        foreign = registry.prepare_core_relation_registry(
            self.repository, carriers, frontier, selection
        )
        self.assertEqual((), foreign.records)
        self.assertEqual("registry-core-authority-path-unsupported", foreign.diagnostics[0]["code"])

    def test_loaded_code_drift_and_untrusted_bundle_fail_closed(self) -> None:
        carriers, frontier, selection = self.inputs()
        original_read = Path.read_bytes
        changed_code = registry._IMPLEMENTATION_PATH.read_bytes() + b"\n# drift\n"

        def current_bytes(path: Path) -> bytes:
            return changed_code if path == registry._IMPLEMENTATION_PATH else original_read(path)

        with patch.object(Path, "read_bytes", autospec=True, side_effect=current_bytes):
            drifted = registry.prepare_core_relation_registry(
                self.repository, carriers, frontier, selection
            )
        self.assertEqual((), drifted.records)
        self.assertEqual("registry-profile-stale", drifted.diagnostics[0]["code"])

        trusted = self.prepare()
        rejected = registry.verified_core_relation_registry({}, self.repository, *self.inputs())
        self.assertEqual((), rejected.records)
        self.assertEqual("registry-untrusted", rejected.diagnostics[0]["code"])
        self.assertEqual(3, len(trusted.records))

    def test_bundle_is_immutable_and_rechecked_before_use(self) -> None:
        result = self.prepare()
        changed_view = result.records[0]
        changed_view["metadata"]["status"] = "Canceled"
        self.assertEqual("Active", result.records[0]["metadata"]["status"])
        carriers, frontier, selection = self.inputs()
        self.assertEqual(
            result.records,
            registry.verified_core_relation_registry(
                result,
                self.repository,
                carriers,
                frontier,
                selection,
            ).records,
        )


if __name__ == "__main__":
    unittest.main()
