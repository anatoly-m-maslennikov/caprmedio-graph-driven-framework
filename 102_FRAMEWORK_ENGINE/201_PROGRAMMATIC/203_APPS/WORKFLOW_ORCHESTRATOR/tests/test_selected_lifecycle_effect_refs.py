"""Functional checks for lifecycle effect-reference selection."""

from __future__ import annotations

import hashlib
from pathlib import Path
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
PROJECT_ROOT = APP.parents[3]
if str(APP) not in sys.path:
    sys.path.insert(0, str(APP))

from selected_lifecycle_result import effect_refs, try_append_record  # noqa: E402


class SelectedLifecycleEffectReferenceTests(unittest.TestCase):
    def test_only_changed_effects_are_references(self) -> None:
        result = {
            "effects": [
                {"state": "unchanged", "carrier": {"path": "unchanged.md"}},
                {"state": "unknown", "carrier": {"path": "unknown.md"}},
                {"carrier": {"path": "missing-state.md"}},
                "string-entry.md",
                None,
                17,
                {"state": "changed", "carrier": {"path": "actual-effect.md"}},
            ]
        }
        self.assertEqual(["actual-effect.md"], effect_refs(PROJECT_ROOT, result))

    def test_prior_revision_is_retained(self) -> None:
        content = b"prior\n"
        digest = hashlib.sha256(content).hexdigest()
        with tempfile.TemporaryDirectory(dir=PROJECT_ROOT / ".caprmedio_tmp") as raw:
            root = Path(raw)
            (root / "previous.md").write_bytes(content)
            result = {
                "effects": [{"state": "changed", "carrier": {"path": "current.md"}}],
                "history": {
                    "prior_revision": {
                        "filename": "previous.md",
                        "version": 1,
                        "path": "previous.md",
                        "digest": digest,
                    }
                },
            }
            self.assertEqual(["current.md", "previous.md"], effect_refs(root, result))

    def test_observed_path_is_retained_after_recording(self) -> None:
        content = b"after\n"
        digest = hashlib.sha256(content).hexdigest()
        with tempfile.TemporaryDirectory(dir=PROJECT_ROOT / ".caprmedio_tmp") as raw:
            root = Path(raw)
            (root / "after.md").write_bytes(content)
            result = {
                "outcome": "applied",
                "effects": [{"state": "changed", "carrier": {"path": "changed.md"}}],
                "observed": {
                    "filename": "after.md",
                    "version": 2,
                    "path": "after.md",
                    "digest": digest,
                },
            }
            session = SimpleNamespace()
            with (
                patch(
                    "selected_lifecycle_result.journal_context",
                    return_value=("test", "2026-10-22", "UTC", "2026-10-22T00:00:00+00:00"),
                ),
                patch(
                    "selected_lifecycle_journal.record_lifecycle_change",
                    return_value={"state": "admitted"},
                ),
            ):
                refs, _recording, error = try_append_record(
                    root,
                    session,
                    {"atom_id": "CA-O-030"},
                    {"before_result": {"path": "before.md", "version": 1, "sha256": "x"}},
                    {"path": "before.md", "version": 1},
                    result,
                    "child-1",
                    "request-1",
                    "PROGRAMMATIC",
                    effect_refs(root, result),
                )
            self.assertIsNone(error)
            self.assertEqual(["after.md", "changed.md"], refs)


if __name__ == "__main__":
    unittest.main()
