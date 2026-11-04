# CA-E-676@6
# CA-E-677@7

"""Native graph relation projection tests."""

from __future__ import annotations

from pathlib import Path
import sys
import unittest


APP_ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(APP_ROOT), str(Path(__file__).parent)]

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.graph_store import graph_relations  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.query_store import QueryStore  # noqa: E402
from smalltest_support import extension_directory  # noqa: E402


class GraphRelationsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.store = QueryStore(extension_directory=extension_directory(APP_ROOT.parents[2]))
        self.addCleanup(self.store.close)

    @staticmethod
    def atom(ref: str, edges: list[dict]) -> dict:
        return {
            "source_path": f"{ref}.md", "status_group": "Current", "id": ref,
            "ref": ref, "version": 1, "status": "Active",
            "current_scope_unit": None, "claim_target_scope_unit": None,
            "role": "Requirement", "form": "Declaration", "tier": 1,
            "updated_at": None, "header_json": {}, "content_markdown": "",
            "content_properties_json": [], "relation_edges_json": edges,
            "hash": ref,
        }

    @staticmethod
    def scope(name: str, edges: list[dict]) -> dict:
        return {
            "name": name, "scope_unit_id": None, "parent_name": None,
            "declared_label": None, "ordered": False, "order_number": None,
            "declaration_source_path": f"{name}.md", "declaration_version": 1,
            "relation_edges_json": edges, "hash": name,
        }

    @staticmethod
    def edge(source_kind: str, source_ref: str, target_kind: str, target_ref: str,
             relation_type: str, derived: bool = False) -> dict:
        return {
            "source_kind": source_kind, "source_ref": source_ref,
            "target_kind": target_kind, "target_ref": target_ref,
            "relation_type": relation_type, "derived": derived,
        }

    def test_reads_outgoing_native_edges_with_typed_references(self) -> None:
        self.store.replace(
            [
                self.atom("A", [self.edge("Atom", "A", "Atom", "B", "CONTAINS")]),
                self.atom("B", [self.edge("Atom", "B", "Scope Unit", "A", "CONTAINS", True)]),
            ],
            [self.scope("A", [self.edge("Scope Unit", "A", "Atom", "A", "DEPENDS_ON")])],
        )

        self.assertEqual(
            {
                ("Atom", "A"): {"CONTAINS": [{"kind": "Atom", "reference": "B", "derived": False}]},
                ("Atom", "B"): {"CONTAINS": [{"kind": "Scope Unit", "reference": "A", "derived": True}]},
                ("Scope Unit", "A"): {"DEPENDS_ON": [{"kind": "Atom", "reference": "A", "derived": False}]},
            },
            graph_relations(self.store._connection, has_edges=True),
        )

    def test_returns_empty_when_the_native_graph_has_no_edges(self) -> None:
        self.store.replace([self.atom("A", [])], [self.scope("A", [])])
        self.assertEqual({}, graph_relations(self.store._connection, has_edges=True))
        self.assertEqual({}, graph_relations(self.store._connection, has_edges=False))


if __name__ == "__main__":
    unittest.main()
