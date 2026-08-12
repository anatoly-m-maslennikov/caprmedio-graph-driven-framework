"""Verify the explicit root-to-installed CAPRMADIO synchronization script."""

from __future__ import annotations

import contextlib
import io
import unittest
from pathlib import Path
from unittest.mock import patch

from dset_toolchain.methodology_sync import MethodologyDrift
from scripts import sync_caprmadio


class SyncCaprmadioScriptTests(unittest.TestCase):
    """Verify preview, apply, and fail-closed synchronization behavior."""

    def test_preview_reports_drift_without_writing(self) -> None:
        drift = (MethodologyDrift("carrier.md", "changed"),)
        with (
            patch.object(sync_caprmadio, "methodology_drift", return_value=drift),
            patch.object(sync_caprmadio, "sync_methodology") as sync,
        ):
            self.assertEqual(sync_caprmadio.synchronize(Path(".")), drift)
        sync.assert_not_called()

    def test_apply_uses_canonical_engine_and_requires_zero_residual_drift(
        self,
    ) -> None:
        initial = (MethodologyDrift("carrier.md", "missing"),)
        with (
            patch.object(
                sync_caprmadio,
                "methodology_drift",
                side_effect=(initial, ()),
            ),
            patch.object(
                sync_caprmadio,
                "_refresh_bootstrap_bundle",
                return_value=False,
            ),
            patch.object(sync_caprmadio, "sync_methodology") as sync,
        ):
            self.assertEqual(
                sync_caprmadio.synchronize(Path("."), apply=True),
                initial,
            )
        sync.assert_called_once_with(Path(".").resolve(), execute=True)

    def test_apply_fails_when_drift_remains(self) -> None:
        residual = (MethodologyDrift("carrier.md", "changed"),)
        with (
            patch.object(
                sync_caprmadio,
                "methodology_drift",
                side_effect=(residual, residual),
            ),
            patch.object(
                sync_caprmadio,
                "_refresh_bootstrap_bundle",
                return_value=False,
            ),
            patch.object(sync_caprmadio, "sync_methodology"),
            self.assertRaisesRegex(RuntimeError, "carrier.md"),
        ):
            sync_caprmadio.synchronize(Path("."), apply=True)

    def test_apply_resynchronizes_a_changed_bootstrap_bundle(self) -> None:
        with (
            patch.object(
                sync_caprmadio,
                "methodology_drift",
                side_effect=((), ()),
            ),
            patch.object(
                sync_caprmadio,
                "_refresh_bootstrap_bundle",
                return_value=True,
            ),
            patch.object(sync_caprmadio, "sync_methodology") as sync,
        ):
            drift = sync_caprmadio.synchronize(Path("."), apply=True)
        self.assertEqual(
            drift,
            (MethodologyDrift("bootstrap_bundle.json", "changed"),),
        )
        self.assertEqual(sync.call_count, 2)

    def test_main_prints_stable_preview(self) -> None:
        drift = (MethodologyDrift("carrier.md", "changed"),)
        output = io.StringIO()
        with (
            patch.object(sync_caprmadio, "synchronize", return_value=drift),
            contextlib.redirect_stdout(output),
        ):
            self.assertEqual(sync_caprmadio.main(["."]), 0)
        self.assertEqual(output.getvalue(), "PREVIEW carriers=1\nCHANGED carrier.md\n")


if __name__ == "__main__":
    unittest.main()
