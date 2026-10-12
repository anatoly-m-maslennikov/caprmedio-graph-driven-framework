"""Current O164 revision gate coverage without a copied revision pin."""

from __future__ import annotations

import copy
from dataclasses import replace
import sys
import tempfile
import unittest
from pathlib import Path
import re


RELEASE_ROOT = Path(__file__).resolve().parents[1]
if str(RELEASE_ROOT) not in sys.path:
    sys.path.insert(0, str(RELEASE_ROOT))

from release_actions import (  # noqa: E402
    ReleaseActionRun,
    SelectedReleaseActionContext,
    _fingerprint,
    _selection,
)
from release_contract import ReleaseContractError  # noqa: E402
from release_contract import canonical_json  # noqa: E402
from release_checkpoint import (  # noqa: E402
    NATIVE_PORTABLE_RELEASE_ACTION_CHECKPOINT_SCHEMA,
    dump_release_checkpoint,
    release_action_checkpoint_sha256,
    restore_release_action_checkpoint,
)
import test_portable_release_actions as portable_actions  # noqa: E402


class _Request:
    def __init__(self, project_root: str) -> None:
        self.project_root = project_root

    def model_dump(self, **_kwargs):
        return {
            "project_root": self.project_root,
            "operation": "apply",
            "failed_recording_ref": None,
        }


class CurrentReleaseRevisionGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = str(Path(self.temporary.name).resolve())
        self.request = _Request(self.root)
        self.run = ReleaseActionRun(
            self.root, "workflow", _fingerprint(self.request), self.request,
        )

    def context(self, version: int) -> SelectedReleaseActionContext:
        return SelectedReleaseActionContext(
            self.root, "workflow", "step", "action", "workflow", "step",
            "CA-O-170", "CA-O-165", self.run.frozen_parameters_sha256,
            workflow_version=version,
        )

    def test_current_admitted_revision_is_not_a_copied_pin(self) -> None:
        source = RELEASE_ROOT.parents[3] / (
            ".caprmedio_caprmedio/09_operations/CA-O-164-WORKFLOW--release-a-selected-framework-version.md"
        )
        version = int(re.search(
            r"(?m)^version:\s*([1-9][0-9]*)\s*$", source.read_text(encoding="utf-8"),
        ).group(1))
        index, phase = _selection(self.request, self.context(version), self.run)
        self.assertEqual((index, phase), (0, "freeze"))

    def test_non_positive_or_non_integer_revision_is_refused(self) -> None:
        for version in (0, -1, True, "12"):
            with self.subTest(version=version):
                with self.assertRaises(ReleaseContractError):
                    _selection(self.request, self.context(version), self.run)


class CurrentNativeCheckpointRevisionTests(unittest.TestCase):
    @staticmethod
    def current_revision() -> int:
        source = RELEASE_ROOT.parents[3] / (
            ".caprmedio_caprmedio/09_operations/CA-O-164-WORKFLOW--release-a-selected-framework-version.md"
        )
        return int(re.search(
            r"(?m)^version:\s*([1-9][0-9]*)\s*$", source.read_text(encoding="utf-8"),
        ).group(1))

    def portable_run(self):
        fixture = portable_actions.PortableReleaseActionsTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        original_context = fixture.context
        revision = self.current_revision()
        fixture.context = lambda index: replace(original_context(index), workflow_version=revision)
        return fixture, revision

    @staticmethod
    def reseal(payload: dict) -> bytes:
        payload["sha256"] = release_action_checkpoint_sha256(payload)
        return canonical_json(payload)

    def test_first_freeze_checkpoint_round_trips_current_admitted_revision(self) -> None:
        fixture, revision = self.portable_run()
        (fixture.root / "catalog.toml").unlink()
        self.assertEqual(fixture.execute(0).outcome, "completed")
        checkpoint = fixture.checkpoints[-1]
        self.assertEqual(checkpoint["schema"], NATIVE_PORTABLE_RELEASE_ACTION_CHECKPOINT_SCHEMA)
        self.assertEqual(checkpoint["contexts"][0]["context"]["workflow_version"], revision)
        restored = restore_release_action_checkpoint(canonical_json(checkpoint))
        self.assertEqual(restored.contexts[0].workflow_version, revision)

    def test_checkpoint_refuses_nonpositive_mixed_or_foreign_frozen_context(self) -> None:
        fixture, revision = self.portable_run()
        (fixture.root / "catalog.toml").unlink()
        self.assertEqual(fixture.execute(0).outcome, "completed")
        fixture.bind_stage_session()
        self.assertEqual(fixture.execute(1).outcome, "completed")
        checkpoint = dump_release_checkpoint(fixture.run)
        cases = {
            "nonpositive-revision": lambda payload: payload["contexts"][0]["context"].update(workflow_version=0),
            "mixed-frozen-revisions": lambda payload: payload["contexts"][1]["context"].update(workflow_version=revision - 1),
            "foreign-frozen-lineage": lambda payload: payload["contexts"][0]["context"].update(
                frozen_parameters_sha256="0" * 64,
            ),
        }
        for name, change in cases.items():
            with self.subTest(name=name):
                altered = copy.deepcopy(checkpoint)
                change(altered)
                with self.assertRaises(ReleaseContractError):
                    restore_release_action_checkpoint(self.reseal(altered))


if __name__ == "__main__":
    unittest.main()
