"""Focused source-readback tests for plain creation Journal append."""

from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
if str(APP) not in sys.path:
    sys.path.insert(0, str(APP))

from selected_creation_journal import CreationJournalError, record_selected_creation  # noqa: E402


class SelectedCreationJournalTest(unittest.TestCase):
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
        self.created = self.root / "atoms/CA-M-301.md"
        self.created.parent.mkdir()
        self.created.write_bytes(b"observed carrier")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def event(self) -> dict[str, object]:
        return {
            "arbitrary": "caller event rows remain ordinary Journal data",
            "result": {
                "path": "atoms/CA-M-301.md",
                "sha256": hashlib.sha256(self.created.read_bytes()).hexdigest(),
            },
        }

    def test_appends_unvalidated_row_and_returns_location(self) -> None:
        event = self.event()

        recorded = record_selected_creation(
            self.root,
            canonical_event=event,
            author="user",
            local_date="2026-10-14",
            timezone="UTC",
        )

        self.assertEqual("completed", recorded["state"])
        self.assertEqual(event, recorded["event"])
        self.assertEqual(1, len(recorded["locations"]))
        carrier = self.root / recorded["locations"][0]["carrier"]
        self.assertEqual(event, json.loads(carrier.read_text()))

    def test_drift_or_append_failure_does_not_become_pending_state(self) -> None:
        event = self.event()
        self.created.write_bytes(b"drift")
        with self.assertRaises(CreationJournalError):
            record_selected_creation(
                self.root,
                canonical_event=event,
                author="user",
                local_date="2026-10-14",
                timezone="UTC",
            )

        event = self.event()
        with patch("selected_creation_journal.append_sealed_events", side_effect=OSError("full")):
            with self.assertRaises(OSError):
                record_selected_creation(
                    self.root,
                    canonical_event=event,
                    author="user",
                    local_date="2026-10-14",
                    timezone="UTC",
                )
