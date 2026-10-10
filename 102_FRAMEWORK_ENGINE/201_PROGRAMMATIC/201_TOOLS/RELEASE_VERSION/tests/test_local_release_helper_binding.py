"""Focused binding coverage for Project-local O164 destructive helpers."""

from __future__ import annotations

import tempfile
import sys
import unittest
from pathlib import Path


RELEASE_ROOT = Path(__file__).resolve().parents[1]
if str(RELEASE_ROOT) not in sys.path:
    sys.path.insert(0, str(RELEASE_ROOT))

from release_actions import (  # noqa: E402
    _freeze_local_release_helper_binding,
    _load_bound_local_release_helpers,
)
from release_contract import ReleaseContractError  # noqa: E402


class LocalReleaseHelperBindingTests(unittest.TestCase):
    def _project(self) -> Path:
        root = Path(tempfile.mkdtemp(prefix="caprmedio-local-helper-", dir="/private/tmp"))
        helpers = root / "PROJECT_TOOLS/RELEASE_VERSION"
        helpers.mkdir(parents=True)
        (helpers / "local_release.py").write_text('VALUE = "frozen"\n', encoding="utf-8")
        (helpers / "native_hooks.py").write_text(
            "def bind_local_release_core(module):\n"
            "    global CORE\n"
            "    CORE = module\n\n"
            "def create_selected_local_bindings(project_root, *, run, context):\n"
            "    return CORE.VALUE\n",
            encoding="utf-8",
        )
        return root

    def test_exact_pre_gate_bytes_are_used_and_later_drift_refuses(self) -> None:
        root = self._project()
        binding = _freeze_local_release_helper_binding(root)

        hooks = _load_bound_local_release_helpers(root, binding)
        self.assertEqual(hooks.create_selected_local_bindings(root, run=object(), context=object()), "frozen")

        (root / "PROJECT_TOOLS/RELEASE_VERSION/local_release.py").write_text('VALUE = "changed"\n', encoding="utf-8")
        # Already-loaded hook code holds the injected frozen sibling; it does
        # not perform a later filesystem import.
        self.assertEqual(hooks.create_selected_local_bindings(root, run=object(), context=object()), "frozen")
        with self.assertRaises(ReleaseContractError) as stale:
            _load_bound_local_release_helpers(root, binding)
        self.assertEqual(stale.exception.code, "local-release-helper-stale")

    def test_missing_helper_refuses_before_loading(self) -> None:
        root = self._project()
        (root / "PROJECT_TOOLS/RELEASE_VERSION/native_hooks.py").unlink()
        with self.assertRaises(ReleaseContractError) as missing:
            _freeze_local_release_helper_binding(root)
        self.assertEqual(missing.exception.code, "local-release-helper-unavailable")


if __name__ == "__main__":
    unittest.main()
