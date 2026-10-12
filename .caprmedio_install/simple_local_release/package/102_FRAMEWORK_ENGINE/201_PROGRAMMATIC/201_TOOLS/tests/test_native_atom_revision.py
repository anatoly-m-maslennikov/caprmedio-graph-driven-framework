"""Native Framework Settings revisions use the selected Project control only."""

from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path


TOOLS_ROOT = Path(__file__).resolve().parents[1]
TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

import native_atom_revision as revisions


class NativeAtomRevisionTests(unittest.TestCase):
    def setUp(self) -> None:
        # Retain the fixture: framework directories can be made immutable by
        # the bounded reader on macOS, which prevents reliable cleanup.
        self.root = Path(tempfile.mkdtemp(dir=TEST_TEMP_ROOT)).resolve() / "non-git-project"
        self.root.mkdir()
        self.control = self.root / ".caprmedio_alpha"
        self.control.mkdir()
        (self.control / "caprmedio_project_settings.toml").write_text(
            "[project]\nname = \"fixture\"\n\n"
            "[paths]\ncontrol_root = \".caprmedio_alpha\"\n"
            "journal_root = \".caprmedio_alpha/_journal\"\n",
            encoding="utf-8",
        )
        (self.control / "project_structure.toml").write_text(
            "schema_version = 1\nscope_units = []\n", encoding="utf-8"
        )
        self.canonical = self.control / revisions.FRAMEWORK_SETTINGS_RELATIVE
        self.canonical.parent.mkdir()
        self.canonical.write_bytes(b"canonical settings\n")
        self.legacy = self.root / "caprmedio_framework_settings.toml"
        self.legacy.write_bytes(b"legacy settings must not be current\n")
        self.generation_legacy = (
            self.control
            / "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
            "000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/"
            "caprmedio_framework_settings.toml"
        )
        self.generation_legacy.parent.mkdir(parents=True)
        self.generation_legacy.write_bytes(b"nested legacy settings must not be current\n")

    @property
    def atom(self) -> revisions.NativeAtom:
        return revisions.NATIVE_ATOMS["framework-settings"]

    def _record(self, version: int, output: str, digest: str) -> dict[str, object]:
        return {
            "event": "completed",
            "kind": "artifact_revision",
            "operation": "register_framework_settings_revision",
            "governed_subjects": [self.atom.artifact_id],
            "produced_outputs": [output],
            "details": {
                "version": str(version),
                "updated_at": f"2026-10-0{version} 01:02:03",
                "sha256": digest,
            },
        }

    def _write_records(self, *records: dict[str, object]) -> None:
        journal = self.control / "_journal"
        journal.mkdir()
        (journal / "src-work-journal-2026-10-01.ndjson").write_text(
            "".join(json.dumps(record) + "\n" for record in records), encoding="utf-8"
        )

    def test_non_git_fixture_uses_selected_control_canonical_address(self) -> None:
        self.assertFalse((self.root / ".git").exists())
        self.assertEqual(
            revisions.carrier_address(self.root, self.atom),
            Path(".caprmedio_alpha/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml"),
        )
        self.assertEqual(
            revisions.carrier_digest(self.root, self.atom),
            hashlib.sha256(self.canonical.read_bytes()).hexdigest(),
        )

    def test_legacy_root_carrier_is_ignored_as_current_authority(self) -> None:
        digest = hashlib.sha256(self.canonical.read_bytes()).hexdigest()
        self._write_records(self._record(1, revisions.carrier_address(self.root, self.atom).as_posix(), digest))
        self.assertEqual(
            revisions.current_reference(self.root, "framework-settings"),
            "CAPRMEDIO-FRAMEWORK-SETTINGS@1,2026-10-01 01:02:03",
        )

    def test_nested_generation_carrier_is_ignored_as_current_authority(self) -> None:
        self.assertNotEqual(self.canonical.read_bytes(), self.generation_legacy.read_bytes())
        self.assertEqual(
            revisions.carrier_digest(self.root, self.atom),
            hashlib.sha256(self.canonical.read_bytes()).hexdigest(),
        )

    def test_canonical_carrier_symlink_is_refused(self) -> None:
        self.canonical.unlink()
        self.canonical.symlink_to(self.generation_legacy)
        with self.assertRaisesRegex(OSError, "Symlink"):
            revisions.carrier_digest(self.root, self.atom)

    def test_historical_journal_addresses_preserve_sequence_without_current_authority(self) -> None:
        canonical_address = revisions.carrier_address(self.root, self.atom).as_posix()
        digest = hashlib.sha256(self.canonical.read_bytes()).hexdigest()
        self._write_records(
            self._record(1, "caprmadio_framework_settings.toml", "a" * 64),
            self._record(2, "caprmedio_framework_settings.toml", "b" * 64),
            self._record(3, canonical_address, digest),
        )
        self.assertEqual([row["version"] for row in revisions.revision_records(self.root, self.atom)], [1, 2, 3])
        self.assertEqual(
            revisions.current_reference(self.root, "framework-settings"),
            "CAPRMEDIO-FRAMEWORK-SETTINGS@3,2026-10-03 01:02:03",
        )

    def test_framework_settings_compatibility_module_has_no_git_bootstrap(self) -> None:
        source = (TOOLS_ROOT / "framework_settings_revision.py").read_text(encoding="utf-8")
        self.assertNotIn("next(parent for parent", source)


if __name__ == "__main__":
    unittest.main()
