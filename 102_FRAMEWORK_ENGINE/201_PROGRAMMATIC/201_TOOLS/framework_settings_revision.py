#!/usr/bin/env python3
"""Compatibility entry point for Framework Settings Atom revisions."""

from __future__ import annotations



import sys
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve()
TOOLS_ROOT = SCRIPT_PATH.parent
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from native_atom_revision import cli, current_reference as native_current_reference  # noqa: E402


def current_reference(root: Path) -> str:
    return native_current_reference(root, "framework-settings")


def _image_main():
    return cli(["framework-settings", *sys.argv[1:]])


if __name__ == "__main__":
    # Direct script execution needs the shared process boundary available from the tools root.
    import sys
    from pathlib import Path
    _TOOLS_ROOT = next(p for p in Path(__file__).resolve().parents if p.name in {"201_TOOLS", "TOOLS"})
    if str(_TOOLS_ROOT) not in sys.path:
        sys.path.insert(0, str(_TOOLS_ROOT))
    from runtime_process_boundary import run_process
    raise SystemExit(run_process(_image_main, operation="framework_settings_revision"))
