"""Verify the complete fail-closed CAPRMADIO identity migration."""

from __future__ import annotations

import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
MIGRATION_SCRIPT = (
    REPOSITORY_ROOT
    / "15_layer_implementation"
    / "tools"
    / "migrations"
    / "migrate_to_caprmadio.py"
)
SOURCE_UPPER = "CAR" + "MADIO"
SOURCE_TITLE = SOURCE_UPPER.lower().title()
SOURCE_LOWER = SOURCE_UPPER.lower()
TARGET_UPPER = "CAPRMADIO"
TARGET_TITLE = TARGET_UPPER.lower().title()
TARGET_LOWER = TARGET_UPPER.lower()


class CaprmadioIdentityMigrationTests(unittest.TestCase):
    """Exercise preview, apply, preservation, and idempotent check."""

    def test_complete_identity_migration_preserves_runtime_and_modes(self) -> None:
        with tempfile.TemporaryDirectory(
            prefix="caprmadio-migration-", dir="/tmp"
        ) as temporary:
            root = Path(temporary)
            self._initialize_fixture(root)

            preview = self._run(root)
            digest_match = re.search(r"^plan-digest: ([0-9a-f]{64})$", preview, re.M)
            self.assertIsNotNone(digest_match)
            digest = digest_match.group(1)

            applied = self._run(root, "--apply", "--expect-plan-digest", digest)
            self.assertIn("identity migration applied", applied)
            self.assertIn("identity migration check: PASS", self._run(root, "--check"))

            governed = root / f".{TARGET_LOWER}"
            runtime = root / f".{TARGET_LOWER}_runtime"
            migrated = governed / f"000_{TARGET_UPPER}_METHODOLOGY" / "identity.md"
            executable = root / "scripts" / f"sync_{TARGET_LOWER}.py"
            binary = governed / f"{TARGET_LOWER}.bin"
            self.assertEqual(
                migrated.read_text(),
                f"{TARGET_UPPER} {TARGET_TITLE} {TARGET_LOWER}\n",
            )
            self.assertEqual(binary.read_bytes(), b"\x00\x01\x02")
            self.assertEqual(executable.stat().st_mode & 0o777, 0o755)
            self.assertEqual((runtime / "sentinel.txt").read_text(), "preserved\n")
            self.assertFalse((root / f".{SOURCE_LOWER}").exists())
            self.assertFalse((root / f".{SOURCE_LOWER}_runtime").exists())

    def _initialize_fixture(self, root: Path) -> None:
        subprocess.run(["git", "init", "-q", str(root)], check=True)
        governed = root / f".{SOURCE_LOWER}"
        methodology = governed / f"000_{SOURCE_UPPER}_METHODOLOGY"
        methodology.mkdir(parents=True)
        (methodology / "identity.md").write_text(
            f"{SOURCE_UPPER} {SOURCE_TITLE} {SOURCE_LOWER}\n"
        )
        (governed / f"{SOURCE_LOWER}.bin").write_bytes(b"\x00\x01\x02")
        runtime = root / f".{SOURCE_LOWER}_runtime"
        runtime.mkdir()
        (runtime / "sentinel.txt").write_text("preserved\n")
        scripts = root / "scripts"
        scripts.mkdir()
        executable = scripts / f"sync_{SOURCE_LOWER}.py"
        executable.write_text(f"#!/usr/bin/env python3\n# {SOURCE_UPPER}\n")
        executable.chmod(0o755)
        subprocess.run(
            ["git", "add", methodology, governed / f"{SOURCE_LOWER}.bin", executable],
            cwd=root,
            check=True,
        )

    def _run(self, root: Path, *arguments: str) -> str:
        completed = subprocess.run(
            [sys.executable, MIGRATION_SCRIPT, root, *arguments],
            cwd=REPOSITORY_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        if completed.returncode:
            self.fail(
                f"migration exited {completed.returncode}: "
                f"stdout={completed.stdout!r}, stderr={completed.stderr!r}"
            )
        return completed.stdout


if __name__ == "__main__":
    unittest.main()
