"""Focused source-readback tests for plain replacement Journal append."""

from __future__ import annotations

import hashlib
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
if str(APP) not in sys.path:
    sys.path.insert(0, str(APP))

from selected_replacement_journal import ReplacementJournalError, record_selected_replacement  # noqa: E402


class SelectedReplacementJournalTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        (self.root / ".git").mkdir()
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            "[paths]\n"
            'control_root = ".caprmedio_caprmedio"\n'
            'journal_root = ".caprmedio_caprmedio/_journal"\n',
            encoding="utf-8",
        )
        self.result_path = self.root / "archive/replacement.md"
        self.result_path.parent.mkdir()
        self.result_path.write_bytes(b"replacement carrier")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def event(self, path: str = "archive/replacement.md") -> dict[str, object]:
        return {
            "replacement_identity": ["any", "ordinary", "row"],
            "result": {
                "path": path,
                "sha256": hashlib.sha256((self.root / path).read_bytes()).hexdigest(),
            },
        }

    def test_appends_unvalidated_row_and_returns_location(self) -> None:
        event = self.event()

        recorded = record_selected_replacement(
            self.root,
            canonical_event=event,
            author="user",
            local_date="2026-10-14",
            timezone="UTC",
        )

        self.assertEqual("completed", recorded["state"])
        self.assertEqual(event, recorded["event"])
        self.assertEqual(1, len(recorded["locations"]))
        self.assertTrue((self.root / recorded["locations"][0]["carrier"]).is_file())

    def test_unsafe_or_drifted_effect_does_not_append_or_retry(self) -> None:
        unsafe = {"result": {"path": "../outside", "sha256": "0" * 64}}
        with self.assertRaises(ReplacementJournalError):
            record_selected_replacement(
                self.root,
                canonical_event=unsafe,
                author="user",
                local_date="2026-10-14",
                timezone="UTC",
            )

        event = self.event()
        self.result_path.write_bytes(b"drift")
        with self.assertRaises(ReplacementJournalError):
            record_selected_replacement(
                self.root,
                canonical_event=event,
                author="user",
                local_date="2026-10-14",
                timezone="UTC",
            )
        with patch(
            "selected_replacement_journal.append_sealed_events", side_effect=OSError("full")
        ):
            with self.assertRaises(OSError):
                record_selected_replacement(
                    self.root,
                    canonical_event=self.event(),
                    author="user",
                    local_date="2026-10-14",
                    timezone="UTC",
                )
