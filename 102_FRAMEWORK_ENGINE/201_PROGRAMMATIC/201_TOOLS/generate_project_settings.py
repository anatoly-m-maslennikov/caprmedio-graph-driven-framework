#!/usr/bin/env python3
"""Retired compatibility entry point for the former settings Projection.

Use the selected installed ``GENERATE_PROJECT_GRAPH_STATE`` Tool instead. It
generates the Project Scope Unit Graph and Sources Projections and never writes
the retired Project Settings outputs.
"""

from __future__ import annotations




def main() -> None:
    raise SystemExit(
        "generate_project_settings.py is retired; use the installed "
        "GENERATE_PROJECT_GRAPH_STATE Tool"
    )


def _image_main():
    return main()


if __name__ == "__main__":
    # Direct script execution needs the shared process boundary available from the tools root.
    import sys
    from pathlib import Path
    _TOOLS_ROOT = next(p for p in Path(__file__).resolve().parents if p.name in {"201_TOOLS", "TOOLS"})
    if str(_TOOLS_ROOT) not in sys.path:
        sys.path.insert(0, str(_TOOLS_ROOT))
    from runtime_process_boundary import run_process
    raise SystemExit(run_process(_image_main, operation="generate_project_settings"))
