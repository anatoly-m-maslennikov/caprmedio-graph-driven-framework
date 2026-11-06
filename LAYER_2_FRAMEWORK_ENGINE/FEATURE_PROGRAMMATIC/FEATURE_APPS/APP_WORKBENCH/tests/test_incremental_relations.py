# CA-E-677@14
from __future__ import annotations

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.incremental_relations import materialize_delta  # noqa: E402
from APP_WORKBENCH.tests.test_relations import atom, declarations  # noqa: E402


class IncrementalRelationTests(unittest.TestCase):
    def test_change_updates_source_and_inverse_neighbours_only(self):
        old = atom("CA-P-1")
        new = atom("CA-P-3")
        task = atom("CA-P-2", relation={"is_contained_by": ["CA-P-1"]})
        rows, _scopes, _registered, _inverse, state, delta = materialize_delta(declarations() + [old, task, new], [])
        self.assertIsNone(delta)
        changed = atom("CA-P-2", relation={"is_contained_by": ["CA-P-3"]})
        rows, _scopes, _registered, _inverse, state, delta = materialize_delta(
            declarations() + [old, changed, new], [], state, {"CA-P-2.md": changed},
        )
        self.assertEqual({"CA-P-1.md", "CA-P-2.md", "CA-P-3.md"}, set(delta.old_atoms))
        self.assertEqual(set(delta.old_atoms), set(delta.new_atoms))
        by_ref = {row["ref"]: row for row in rows}
        self.assertEqual([], by_ref["CA-P-1"]["relation_edges_json"])
        self.assertEqual("CONTAINS", by_ref["CA-P-3"]["relation_edges_json"][0]["relation_type"])

    def test_delete_returns_old_row_and_prunes_state(self):
        source = atom("CA-P-1")
        rows, _scopes, _registered, _inverse, state, _delta = materialize_delta(declarations() + [source], [])
        rows, _scopes, _registered, _inverse, state, delta = materialize_delta(
            declarations(), [], state, {"CA-P-1.md": None},
        )
        self.assertIn("CA-P-1.md", delta.old_atoms)
        self.assertNotIn("CA-P-1.md", delta.new_atoms)
        self.assertNotIn("CA-P-1.md", state.raw_by_path)
        self.assertNotIn("CA-P-1", [row["ref"] for row in rows])

    def test_relation_registry_change_uses_full_boundary(self):
        source = atom("CA-P-1")
        metadata = declarations()
        _rows, _scopes, _registered, _inverse, state, _delta = materialize_delta(metadata + [source], [])
        changed = dict(metadata[0], content_markdown="## Claim\n", header_json={"relations": {}})
        _rows, _scopes, _registered, _inverse, _state, delta = materialize_delta(
            [changed, metadata[1], source], [], state, {changed["source_path"]: changed},
        )
        self.assertIsNone(delta)

    def test_registry_source_prose_change_keeps_incremental_delta(self):
        metadata = declarations()
        source = atom("CA-P-1")
        _rows, _scopes, _registered, _inverse, state, _delta = materialize_delta(metadata + [source], [])
        changed = dict(metadata[0], content_markdown=metadata[0]["content_markdown"] + "\nProse only.\n")
        _rows, _scopes, _registered, _inverse, _state, delta = materialize_delta(
            [changed, metadata[1], source], [], state, {changed["source_path"]: changed},
        )
        self.assertIsNotNone(delta)

    def test_ordinary_change_parses_only_the_changed_source(self):
        import APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.incremental_relations as incremental

        first = atom("CA-P-1")
        second = atom("CA-P-2")
        original = incremental._atom_facts
        calls = 0

        def counted(*args):
            nonlocal calls
            calls += 1
            return original(*args)

        incremental._atom_facts = counted
        try:
            _rows, _scopes, _registered, _inverse, state, _delta = materialize_delta(
                declarations() + [first, second], [],
            )
            first_changed = dict(first, content_markdown="## Claim\nChanged.\n")
            materialize_delta(
                declarations() + [first_changed, second], [], state, {"CA-P-1.md": first_changed},
            )
        finally:
            incremental._atom_facts = original
        self.assertEqual(5, calls)

    def test_duplicate_reference_changes_use_full_membership_boundary(self):
        first = atom("CA-R-X")
        second = dict(atom("CA-R-X"), source_path="second.md")
        _rows, _scopes, _registered, _inverse, state, _delta = materialize_delta([first, second], [])
        self.assertEqual(frozenset({"CA-R-X.md", "second.md"}), state.excluded_paths)

        still_duplicate = dict(first, content_markdown="## Claim\nChanged.\n")
        rows, _scopes, _registered, _inverse, state, delta = materialize_delta(
            [still_duplicate, second], [], state, {"CA-R-X.md": still_duplicate},
        )
        self.assertIsNone(delta)
        self.assertEqual([], rows)

        third = dict(atom("CA-R-X"), source_path="third.md")
        rows, _scopes, _registered, _inverse, state, delta = materialize_delta(
            [still_duplicate, second, third], [], state, {"third.md": third},
        )
        self.assertIsNone(delta)
        self.assertEqual([], rows)

        renamed = dict(still_duplicate, id="CA-R-Y", ref="CA-R-Y")
        rows, _scopes, _registered, _inverse, _state, delta = materialize_delta(
            [renamed, second], [], state, {"CA-R-X.md": renamed},
        )
        self.assertIsNone(delta)
        self.assertEqual({"CA-R-X", "CA-R-Y"}, {row["ref"] for row in rows})

    def test_draft_without_reference_is_materialized_by_an_ordinary_delta(self):
        draft = dict(atom("draft"), id=None, ref=None, status_group="Draft")
        rows, _scopes, _registered, _inverse, state, _delta = materialize_delta([draft], [])
        self.assertEqual(1, len(rows))
        changed = dict(draft, content_markdown="## Claim\nChanged draft.\n")
        rows, _scopes, _registered, _inverse, _state, delta = materialize_delta(
            [changed], [], state, {"draft.md": changed},
        )
        self.assertIn("draft.md", delta.old_atoms)
        self.assertIn("draft.md", delta.new_atoms)
        self.assertEqual("Changed draft.", rows[0]["content_markdown"].splitlines()[-1])

    def test_unrelated_outgoing_sets_keep_their_identity(self):
        first = atom("CA-P-1")
        second = atom("CA-P-2", relation={"is_contained_by": ["CA-P-1"]})
        third = atom("CA-P-3")
        fourth = atom("CA-P-4", relation={"is_contained_by": ["CA-P-3"]})
        _rows, _scopes, _registered, _inverse, state, _delta = materialize_delta(
            declarations() + [first, second, third, fourth], [],
        )
        untouched = state.outgoing[("Atom", "CA-P-3")]
        changed = atom("CA-P-2")
        _rows, _scopes, _registered, _inverse, next_state, _delta = materialize_delta(
            declarations() + [first, changed, third, fourth], [], state, {"CA-P-2.md": changed},
        )
        self.assertIs(untouched, next_state.outgoing[("Atom", "CA-P-3")])

    def test_rename_with_same_reference_stays_incremental(self):
        source = atom("CA-P-1")
        _rows, _scopes, _registered, _inverse, state, _delta = materialize_delta([source], [])
        moved = dict(source, source_path="moved.md")
        rows, _scopes, _registered, _inverse, state, delta = materialize_delta(
            [moved], [], state, {"CA-P-1.md": None, "moved.md": moved},
        )
        self.assertIsNotNone(delta)
        self.assertIn("CA-P-1.md", delta.old_atoms)
        self.assertIn("moved.md", delta.new_atoms)
        self.assertEqual(["moved.md"], list(state.atom_order))
        self.assertEqual(["moved.md"], [row["source_path"] for row in rows])

    def test_new_duplicate_forces_full_but_ignored_delete_does_not(self):
        first = atom("CA-P-1")
        _rows, _scopes, _registered, _inverse, state, _delta = materialize_delta([first], [])
        second = dict(atom("CA-P-2"), source_path="second.md")
        third = dict(atom("CA-P-2"), source_path="third.md")
        rows, _scopes, _registered, _inverse, state, delta = materialize_delta(
            [first, second, third], [], state, {"second.md": second, "third.md": third},
        )
        self.assertIsNone(delta)
        self.assertEqual(["CA-P-1"], [row["ref"] for row in rows])

        changed = dict(first, content_markdown="## Claim\nChanged.\n")
        rows, _scopes, _registered, _inverse, _state, delta = materialize_delta(
            [changed], [], state, {"ignored.md": None, "CA-P-1.md": changed},
        )
        self.assertIsNotNone(delta)
        self.assertEqual("Changed.", rows[0]["content_markdown"].splitlines()[-1])


if __name__ == "__main__":
    unittest.main()
