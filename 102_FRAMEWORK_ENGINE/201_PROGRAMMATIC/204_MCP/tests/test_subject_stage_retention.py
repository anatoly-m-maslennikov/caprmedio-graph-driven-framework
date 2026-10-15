"""Every unique staged intent retains its same session-bound whole-manifest pin."""

from pathlib import Path
import sys
from types import SimpleNamespace
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import hot_reload  # noqa: E402


class SubjectStageRetentionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.gateway = object.__new__(hot_reload.Gateway)
        self.gateway.subject_stages = {}
        self.connection = object()
        self.context = SimpleNamespace(session=SimpleNamespace(_connection=self.connection))

    def retain(self, preview: object) -> None:
        response = SimpleNamespace(
            is_error=False,
            structured_content={
                "operation": "stage_subjects",
                "errors": [],
                "preview": preview,
                "staging": {"manifest_path": "batch/manifest.json", "manifest_sha256": "f" * 64},
            },
        )
        self.gateway._retain_subject_stage(self.context, response)

    def test_multiple_intents_retain_exact_whole_manifest_and_connection(self) -> None:
        intents = ["a" * 64, "b" * 64]
        self.retain(
            {"count": 2, "atoms": [{"subject_intent_sha256": intent} for intent in intents]}
        )
        self.assertEqual(len(self.gateway.subject_stages), 2)
        for intent in intents:
            connection, manifest = self.gateway.subject_stages[(id(self.connection), intent)]
            self.assertIs(connection, self.connection)
            self.assertEqual(manifest, {"path": "batch/manifest.json", "digest": "f" * 64})
            self.assertNotIn((id(object()), intent), self.gateway.subject_stages)

    def test_malformed_counts_atoms_and_intents_do_not_partially_retain(self) -> None:
        first = {"subject_intent_sha256": "a" * 64}
        for preview in (
            {"count": 0, "atoms": []},
            {"count": True, "atoms": [first]},
            {"count": "1", "atoms": [first]},
            {"count": 2, "atoms": [first]},
            {"count": 2, "atoms": [first, {}]},
            {"count": 2, "atoms": [first, None]},
            {"count": 2, "atoms": [first, {"subject_intent_sha256": {}}]},
            {"count": 2, "atoms": [first, first]},
        ):
            with self.subTest(preview=preview):
                self.retain(preview)
                self.assertEqual(self.gateway.subject_stages, {})


if __name__ == "__main__":
    unittest.main()
