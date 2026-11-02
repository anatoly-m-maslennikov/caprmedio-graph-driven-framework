"""Configured timestamp formatting and revision scalar serialization."""

from __future__ import annotations

import datetime as dt
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path
from unittest import mock

import yaml


TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import artifact_metadata as metadata  # noqa: E402


class ArtifactMetadataTest(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.root = Path(self.directory.name)
        self.settings = self.root / metadata.SETTINGS_PATH
        self.settings.parent.mkdir()

    def tearDown(self) -> None:
        self.directory.cleanup()

    def _timezone(self, value: str | None) -> None:
        text = "" if value is None else f'[artifact_timestamps]\ntimezone = "{value}"\n'
        self.settings.write_text(text, encoding="utf-8")

    def test_utc_timestamp_carries_its_numeric_offset(self) -> None:
        self._timezone("UTC")
        moment = dt.datetime(2026, 10, 11, 12, 34, 56, tzinfo=dt.UTC)
        with mock.patch.object(metadata.dt, "datetime") as clock:
            clock.now.side_effect = lambda zone: moment.astimezone(zone)
            self.assertEqual("2026-10-11 12:34:56 +0000", metadata.current_timestamp(self.root))
            clock.now.assert_called_once_with(dt.UTC)

    def test_iana_timestamp_uses_the_offset_at_the_emitted_instant(self) -> None:
        self._timezone("America/New_York")
        cases = (
            (dt.datetime(2026, 1, 11, 12, 34, 56, tzinfo=dt.UTC), "2026-01-11 07:34:56 -0500"),
            (dt.datetime(2026, 7, 11, 12, 34, 56, tzinfo=dt.UTC), "2026-07-11 08:34:56 -0400"),
        )
        for moment, expected in cases:
            with self.subTest(moment=moment), mock.patch.object(metadata.dt, "datetime") as clock:
                clock.now.side_effect = lambda zone: moment.astimezone(zone)
                self.assertEqual(expected, metadata.current_timestamp(self.root))
                self.assertEqual("America/New_York", clock.now.call_args.args[0].key)

    def test_local_and_default_timestamp_keep_host_local_resolution(self) -> None:
        moment = dt.datetime(2026, 10, 11, 18, 4, 56, tzinfo=dt.timezone(dt.timedelta(hours=5, minutes=30)))
        for setting in ("local", None):
            self._timezone(setting)
            with self.subTest(setting=setting), mock.patch.object(metadata.dt, "datetime") as clock:
                clock.now.return_value.astimezone.return_value = moment
                self.assertEqual("2026-10-11 18:04:56 +0530", metadata.current_timestamp(self.root))
                clock.now.assert_called_once_with()
                clock.now.return_value.astimezone.assert_called_once_with()

    def test_selected_timezone_formatter_requires_no_canonical_settings_path(self) -> None:
        moment = dt.datetime(2026, 10, 11, 12, 34, 56, tzinfo=dt.UTC)
        self.assertFalse(self.settings.exists())
        with mock.patch.object(metadata.dt, "datetime") as clock:
            clock.now.side_effect = lambda zone: moment.astimezone(zone)
            self.assertEqual("2026-10-11 18:04:56 +0530", metadata.timestamp_for_timezone("Asia/Kolkata"))
            self.assertEqual("Asia/Kolkata", clock.now.call_args.args[0].key)

    def test_unknown_zone_and_malformed_settings_do_not_fall_back(self) -> None:
        self._timezone("Unknown/Not_A_Zone")
        with self.assertRaisesRegex(RuntimeError, "unknown artifact timestamp timezone"):
            metadata.current_timestamp(self.root)
        self.settings.write_text('[artifact_timestamps\ntimezone = "UTC"\n', encoding="utf-8")
        with self.assertRaises(tomllib.TOMLDecodeError):
            metadata.current_timestamp(self.root)

    def test_yaml_quotes_only_updated_at_property(self) -> None:
        timestamp = "2026-10-11 12:34:56 +0000"
        self.assertEqual(f'updated_at: "{timestamp}"', metadata.property_line("---", "updated_at", timestamp))
        self.assertEqual("version: 2", metadata.property_line("---", "version", 2))
        self.assertEqual("status: Active", metadata.property_line("---", "status", "Active"))

    def test_yaml_atom_and_projection_writes_keep_timestamp_a_quoted_string(self) -> None:
        timestamp = "2026-10-11 12:34:56 +0000"
        cases = (
            (metadata.update_atom("status: Active", "---", timestamp, new=True), 1),
            (metadata.update_atom("version: 2\nupdated_at: 2026-01-01 00:00:00", "---", timestamp, new=False), 3),
            (metadata.update_projection("artifact_form: PROJECTION", "---", timestamp), None),
            (metadata.update_projection('updated_at: "2026-01-01 00:00:00 +0000"', "---", timestamp), None),
        )
        for frontmatter, version in cases:
            with self.subTest(frontmatter=frontmatter):
                self.assertIn(f'updated_at: "{timestamp}"', frontmatter)
                parsed = yaml.safe_load(frontmatter)
                self.assertEqual(timestamp, parsed["updated_at"])
                self.assertIsInstance(parsed["updated_at"], str)
                self.assertEqual(version, parsed.get("version"))

    def test_toml_atom_and_projection_serialization_remains_quoted(self) -> None:
        timestamp = "2026-10-11 12:34:56 +0000"
        atom = metadata.update_atom('version = 2\nupdated_at = "2026-01-01 00:00:00"', "+++", timestamp, new=False)
        projection = metadata.update_projection('artifact_form = "PROJECTION"', "+++", timestamp)
        self.assertEqual(3, tomllib.loads(atom)["version"])
        for frontmatter in (atom, projection):
            with self.subTest(frontmatter=frontmatter):
                self.assertIn(f'updated_at = "{timestamp}"', frontmatter)
                self.assertEqual(timestamp, tomllib.loads(frontmatter)["updated_at"])


if __name__ == "__main__":
    unittest.main()
