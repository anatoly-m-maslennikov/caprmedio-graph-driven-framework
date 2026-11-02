"""Install CAPRMEDIO host runtime or Project setup; dry-run unless --apply."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))


def _parser():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="scope", required=True)
    runtime = commands.add_parser("runtime", help="Configure one shared host runtime")
    runtime.add_argument("--harness", choices=("codex",))
    runtime.add_argument("--projects-root", type=Path)
    runtime.add_argument("--host-settings", type=Path)
    runtime.add_argument("--runtime-root", type=Path)
    runtime.add_argument("--http-port", type=int)
    runtime.add_argument("--max-loaded-projects", type=int)
    runtime.add_argument("--image", help="Admitted sha256 image; --apply also starts Docker")
    runtime.add_argument("--apply", action="store_true")
    project = commands.add_parser("project", help="Configure one Project, never the host")
    project.add_argument("--project-root", type=Path, required=True)
    project.add_argument(
        "--prefix", help="Required for a new Project; never changes an existing ID"
    )
    project.add_argument(
        "--source-root", type=Path, help="Framework source containing the ca Skill"
    )
    project.add_argument("--apply", action="store_true")
    return parser


def _dispatch(args):
    values = vars(args).copy()
    scope = values.pop("scope")
    if scope == "runtime":
        from INSTALL_TOOLS.runtime_installation import install_runtime

        return install_runtime(**values)
    from INSTALL_TOOLS.project_installation import install_project

    return install_project(**values)


def cli(argv=None):
    args = _parser().parse_args(argv)
    try:
        result = _dispatch(args)
        container = result.get("container", {})
        ok = not (
            args.apply and args.scope == "runtime" and args.image and not container.get("ready")
        )
        response = {"ok": bool(ok), "mode": "apply" if args.apply else "dry-run", "result": result}
    except (ValueError, OSError) as error:
        response = {"ok": False, "error": type(error).__name__, "message": str(error)}
    print(json.dumps(response, sort_keys=True))
    return 0 if response["ok"] else 2


if __name__ == "__main__":
    from runtime_process_boundary import run_process

    raise SystemExit(run_process(cli, operation="INSTALL_TOOLS/install"))
