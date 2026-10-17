"""Admission fixtures must remain independent of live authority and manifests."""

from __future__ import annotations

import builtins
import os
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parent
PROJECT = TOOLS.parents[2]
sys.path.insert(0, str(HERE))

import test_proposed_relation_admission as relations  # noqa: E402
import test_status_bundle_publication_independent as statuses  # noqa: E402


class RelationFixtureIsolationTests(unittest.TestCase):
    def setUp(self) -> None:
        original_open = builtins.open
        live_control = PROJECT / ".caprmedio_caprmedio"
        manifests = TOOLS / "VALIDATE_ATOMS/validate_atoms_workers"

        def guarded_open(file, *args, **kwargs):
            if isinstance(file, (str, os.PathLike)):
                path = Path(file).absolute()
                self.assertFalse(path.is_relative_to(live_control), f"live authority read: {path}")
                self.assertFalse(
                    path.parent == manifests and path.suffix == ".json",
                    f"mutable manifest read: {path}",
                )
            return original_open(file, *args, **kwargs)

        self.guarded_open = guarded_open

    def test_relation_admission_uses_only_frozen_authority(self) -> None:
        original_entry = relations.proposed_carrier._entry
        fixture = relations.ProposedRelationAdmissionTest(methodName="runTest")
        try:
            with (
                patch("builtins.open", self.guarded_open),
                patch("io.open", self.guarded_open),
            ):
                fixture.setUp()
            fixture.test_standard_evaluation_requires_and_admits_one_exact_active_target()
        finally:
            fixture.tearDown()
            fixture.doCleanups()
        self.assertIs(relations.proposed_carrier._entry, original_entry)

    def test_status_publication_uses_only_frozen_authority(self) -> None:
        original_entry = relations.proposed_carrier._entry
        fixture = statuses.IndependentStatusBundlePublicationTests(methodName="runTest")
        try:
            with (
                patch("builtins.open", self.guarded_open),
                patch("io.open", self.guarded_open),
            ):
                fixture.setUp()
            fixture.test_noop_preserves_all_bytes_paths_and_has_no_revision_or_history()
        finally:
            fixture.tearDown()
            fixture.doCleanups()
        self.assertIs(relations.proposed_carrier._entry, original_entry)


if __name__ == "__main__":
    unittest.main()
