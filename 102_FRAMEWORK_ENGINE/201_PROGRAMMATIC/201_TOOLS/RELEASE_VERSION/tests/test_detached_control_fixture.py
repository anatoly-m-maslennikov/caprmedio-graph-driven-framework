"""Disposable fixture seeding from the Unit driver's existing sealed controls."""

from __future__ import annotations

import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = RELEASE_ROOT.parents[3]
for path in (RELEASE_ROOT, RELEASE_ROOT / "tests", REPOSITORY / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from full_suite_golden.control_fixture import copy_control_closure  # noqa: E402
from release_source_admission import derive_release_execution_source_snapshot  # noqa: E402
from release_suite_reference_context import (  # noqa: E402
    ReleaseSuiteReferenceContextError,
    capture_context,
    copy_verified_bytes,
    revalidate_context,
)
from selected_routes import PROJECT_SETTINGS_REF  # noqa: E402


class DetachedControlFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = Path(tempfile.mkdtemp(prefix="detached-control-fixture-")).resolve(strict=True)
        self.repository = self.temporary / "sealed-workspace"
        self.root = self.temporary / "disposable-test-project"
        self.repository.mkdir()
        self.root.mkdir()
        self.bindings = {
            "candidate_snapshot_manifest_sha256": "a" * 64,
            "compiled_candidate_root": ".caprmedio_tmp/release_candidates/fixture/compiled",
            "selected_n_identity": "detached-fixture-N",
            "selected_n_image_context": "sha256:" + "b" * 64,
        }
        context_source = self.temporary / "complete-control-fixture"
        context_source.mkdir()
        copy_control_closure(REPOSITORY, context_source)
        self.context = capture_context(context_source, self.bindings)
        copy_verified_bytes(self.context, self.repository)
        tool = Path("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/release_version.py")
        (self.repository / tool).parent.mkdir(parents=True)
        shutil.copyfile(REPOSITORY / tool, self.repository / tool)
        (self.repository / tool).chmod((REPOSITORY / tool).stat().st_mode & 0o777)
        self.envelope = {
            "schema_version": 2,
            "reference_rows": [row.as_dict() for row in self.context.reference_rows],
        }
        self.binding_path = self.repository / ".caprmedio_release/source_bindings.json"
        self.binding_path.parent.mkdir()
        self.write_envelope()

    def write_envelope(self) -> None:
        self.binding_path.write_text(json.dumps(self.envelope), encoding="utf-8")

    def seed(self) -> None:
        with patch.dict("os.environ", {"CAPRMEDIO_RELEASE_SOURCE_BINDINGS": str(self.binding_path)}):
            copy_control_closure(self.repository, self.root)

    def test_seeds_complete_fixture_without_mutating_partial_workspace(self) -> None:
        with self.assertRaises(ValueError):
            derive_release_execution_source_snapshot(self.repository)
        before = {path.relative_to(self.repository) for path in self.repository.rglob("*")}
        self.seed()
        self.assertEqual(before, {path.relative_to(self.repository) for path in self.repository.rglob("*")})
        self.assertFalse((self.root / ".caprmedio_caprmedio/_projection/release_execution_snapshot.json").exists())
        fixture_context = capture_context(self.root, self.bindings)
        revalidate_context(self.root, fixture_context, self.bindings)
        (self.root / PROJECT_SETTINGS_REF).write_bytes((self.root / PROJECT_SETTINGS_REF).read_bytes() + b"\n# changed\n")
        with self.assertRaises(ReleaseSuiteReferenceContextError):
            revalidate_context(self.root, fixture_context, self.bindings)

    def test_explicit_detached_context_never_falls_back_when_bindings_are_missing(self) -> None:
        self.binding_path.unlink()
        with self.assertRaises(RuntimeError), patch(
            "full_suite_golden.control_fixture.derive_release_execution_source_snapshot",
            side_effect=AssertionError("must not discover live sources"),
        ):
            self.seed()
        self.assertEqual(list(self.root.iterdir()), [])

    def test_stale_and_unsafe_reference_rows_are_refused_before_copy(self) -> None:
        self.envelope["reference_rows"][0]["sha256"] = "0" * 64
        self.write_envelope()
        with self.assertRaises(ReleaseSuiteReferenceContextError):
            self.seed()
        self.assertEqual(list(self.root.iterdir()), [])
        self.envelope["reference_rows"] = [{"source_path": "../escape.md", "sha256": "0" * 64, "mode": 0o644}]
        self.write_envelope()
        with self.assertRaises(ReleaseSuiteReferenceContextError):
            self.seed()
        self.assertEqual(list(self.root.iterdir()), [])

    def test_missing_required_definition_is_not_replaced_from_live_sources(self) -> None:
        authority = next(row for row in self.envelope["reference_rows"] if "CA-D-572-PROJECT_TOOLS" in row["source_path"])
        self.envelope["reference_rows"].remove(authority)
        self.write_envelope()
        with self.assertRaises(ValueError):
            self.seed()
        self.assertFalse((self.root / authority["source_path"]).exists())


if __name__ == "__main__":
    unittest.main()
