"""Focused checks that Journal rows do not decide selected Action state."""

from __future__ import annotations

from pathlib import Path
import sys
import unittest


APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parents[1] / "201_TOOLS"
for location in (APP, TOOLS, APP / "tests"):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from selected_action_observation import observe_selected_action  # noqa: E402
import test_selected_action_observation as fixture_module  # noqa: E402


class PlainJournalLoggingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = fixture_module.SelectedActionObservationTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.temporary.cleanup)

    def test_bound_progress_is_terminal_without_accepted_journal_receipt(self) -> None:
        action_id, folder, _execution = self.fixture._run("plain-log")
        result_ref = self.fixture._progress(action_id, folder)

        observed = observe_selected_action(self.fixture.root, action_id)

        self.assertEqual(("terminal", "completed"), (observed["disposition"], observed["outcome"]))
        self.assertEqual(result_ref, observed["result_ref"])
        self.assertNotIn("journal_confirmation", observed)


if __name__ == "__main__":
    unittest.main()
