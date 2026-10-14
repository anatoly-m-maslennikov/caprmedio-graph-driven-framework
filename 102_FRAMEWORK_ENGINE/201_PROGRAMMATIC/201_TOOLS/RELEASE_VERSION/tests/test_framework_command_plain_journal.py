"""Retained command facts and actual Sessions do not need Journal proof."""

import unittest
from unittest.mock import patch

import test_framework_installation_command as fixture_module

command = fixture_module.command_module


class FrameworkCommandPlainJournalTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixture_module.FrameworkInstallationCommandTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.result = command.run_framework_installation_command(self.fixture._request())
        self.addCleanup(self.result.action_session.close)

    def reopen(self):
        return command.reopen_framework_installation_command_start(
            self.fixture.root,
            self.result.command_receipt,
            action_package=self.fixture.package,
            operators_registry_ref=self.fixture.control.relative_to(self.fixture.root)
            / "operators_registry.toml",
        )

    def remove_start_log(self):
        for path in (self.fixture.control / "_journal").glob("*.ndjson"):
            path.unlink()

    def test_no_start_journal_returns_only_the_retained_run_locator(self):
        self.remove_start_log()
        with patch.object(command.work_journal, "read_records", side_effect=AssertionError):
            locator = self.reopen()
            actual = command._direct_result_context(self.result)
        self.assertIsInstance(locator, str)
        self.assertEqual(locator, self.result.action_start["run_id"])
        self.assertEqual(actual[2], locator)
        self.assertEqual(
            self.result.action_session.read_recorded_action_start(locator),
            self.result.action_provenance,
        )

    def test_journal_contents_do_not_control_command_reopening(self):
        self.remove_start_log()
        log = self.fixture.control / "_journal" / "observations.ndjson"
        log.write_bytes(b"not JSON\n")
        self.assertEqual(self.reopen(), self.result.action_start["run_id"])
        self.assertEqual(log.read_bytes(), b"not JSON\n")

    def test_registry_currentness_is_still_required(self):
        registry = self.fixture.control / "operators_registry.toml"
        with registry.open("ab") as stream:
            stream.write(b"\n# changed registry\n")
        with self.assertRaises(command.FrameworkInstallationCommandError) as raised:
            self.reopen()
        self.assertEqual(raised.exception.code, "installation-command-operator-invalid")

    def test_missing_operator_is_still_refused(self):
        registry = self.fixture.control / "operators_registry.toml"
        registry.write_text(registry.read_text().replace("Fixture Operator", "Other Operator"))
        with self.assertRaises(command.FrameworkInstallationCommandError):
            self.reopen()

    def test_stale_package_owned_source_is_still_refused(self):
        source = self.fixture.package.root / fixture_module.INSTALLATION_ATOM_RELATIVE
        with source.open("ab") as stream:
            stream.write(b"\nchanged source\n")
        with self.assertRaises(command.FrameworkInstallationCommandError) as raised:
            self.reopen()
        self.assertEqual(raised.exception.code, "installation-command-start-invalid")

    def test_retained_command_digest_is_still_required(self):
        self.result.command_receipt_path.write_bytes(b"{}")
        with self.assertRaises(command.FrameworkInstallationCommandError) as raised:
            self.reopen()
        self.assertEqual(raised.exception.code, "installation-command-receipt-digest-mismatch")

    def test_run_locator_cannot_replace_the_actual_live_session(self):
        self.remove_start_log()
        self.result.action_session.actual.clear()
        with self.assertRaises(command.FrameworkInstallationCommandError):
            command._direct_result_context(self.result)


if __name__ == "__main__":
    unittest.main()
