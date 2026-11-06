# CA-E-677@12
# CA-E-780@4
"""Case-colliding Relation definitions stay out of the native graph."""

from __future__ import annotations

from contextlib import redirect_stderr
from io import StringIO
from pathlib import Path
import sys
import unittest


APP_ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(APP_ROOT), str(Path(__file__).parent)]

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.markdown_content import parse_content  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.query_store import QueryStore  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.relations import materialize, relation_registry  # noqa: E402
from smalltest_support import extension_directory  # noqa: E402


def atom(reference: str, *, subjects: str | None = None, relations: dict[str, list[str]] | None = None) -> dict:
    header = {"relations": relations or {}}
    if subjects is not None:
        header["subjects"] = {"active": subjects}
    body = "# Claim\n\nOne claim.\n"
    return {
        "source_path": f"definitions/{reference}.md",
        "status_group": "Current",
        "id": reference,
        "ref": reference,
        "version": 1,
        "status": "Active",
        "current_scope_unit": None,
        "claim_target_scope_unit": None,
        "role": "Requirement",
        "form": "Relation Definition" if subjects is not None else "Definition",
        "tier": 1,
        "updated_at": None,
        "header_json": header,
        "content_markdown": body,
        "content_properties_json": parse_content(body, tolerate_duplicate_siblings=True),
        "relation_edges_json": [],
        "hash": None,
    }


class RelationRegistryCollisionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.store = QueryStore(extension_directory=extension_directory(APP_ROOT.parents[2]))

    def tearDown(self) -> None:
        self.store.close()

    def test_case_collisions_are_warned_omitted_and_do_not_break_duckpgq(self) -> None:
        definitions = [
            atom("CA-R-1", subjects="Subject/Graph/Relation//DEPENDS_ON"),
            atom("CA-R-2", subjects="Subject/Graph/Relation//depends_on"),
            atom("CA-R-3", subjects="Subject/Graph/Relation//CONTAINS"),
        ]
        source = atom(
            "CA-R-4", relations={"DEPENDS_ON": ["CA-R-5"], "CONTAINS": ["CA-R-5"]},
        )
        errors = StringIO()
        with redirect_stderr(errors):
            registered, inverse = relation_registry(definitions + [source, atom("CA-R-5")])

        self.assertEqual({"CONTAINS"}, registered)
        self.assertEqual({}, inverse)
        self.assertIn("DEPENDS_ON, depends_on", errors.getvalue())
        self.assertIn("definitions/CA-R-1.md", errors.getvalue())
        self.assertIn("definitions/CA-R-2.md", errors.getvalue())
        self.assertEqual({"DEPENDS_ON": ["CA-R-5"], "CONTAINS": ["CA-R-5"]}, source["header_json"]["relations"])

        with redirect_stderr(StringIO()):
            rows, scopes = materialize(definitions + [source, atom("CA-R-5")], [])
        self.assertEqual(["CONTAINS"], [edge["relation_type"] for edge in rows[3]["relation_edges_json"]])

        self.store.replace(rows, scopes, relation_types=registered)
        result = self.store.run(
            "FROM GRAPH_TABLE (caprmedio "
            "MATCH (source:Reference)-[edge:CONTAINS]->(target:Reference) "
            "COLUMNS (source.ref AS source_ref, target.ref AS target_ref))"
        )
        self.assertEqual([["CA-R-4", "CA-R-5"]], result["rows"])


if __name__ == "__main__":
    unittest.main()
