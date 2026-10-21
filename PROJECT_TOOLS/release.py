"""Run the existing Project release workflows directly from the host."""

from __future__ import annotations

import argparse
from contextlib import redirect_stdout
from functools import partial
import json
from pathlib import Path
import re
import sys

from pydantic import BaseModel, ConfigDict

sys.dont_write_bytecode = True
REPOSITORY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY))
sys.path.insert(0, str(REPOSITORY / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS"))

from PROJECT_TOOLS.PUBLIC_RELEASE.public_release import run_public_release  # noqa: E402
from PROJECT_TOOLS.PUBLIC_RELEASE.public_release_materials import validate_draft  # noqa: E402
from PROJECT_TOOLS.RELEASE_VERSION.local_release import run_local_release  # noqa: E402
from PROJECT_TOOLS.release_events import run_recorded_release  # noqa: E402


class ContentDraft(BaseModel):
    """The existing closed draft contract, validated before release effects."""

    model_config = ConfigDict(strict=True, extra="forbid")
    description: str
    summary: list[str]


def _arguments(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="operation", required=True)
    for operation in ("local", "public"):
        command = commands.add_parser(operation)
        command.add_argument("--project-root", type=Path, default=REPOSITORY)
        command.add_argument("--run-id", required=True)
        if operation == "public":
            command.add_argument(
                "--content-draft", type=Path, help="UTF-8 JSON description/summary object"
            )
        else:
            command.add_argument(
                "--test-module",
                action="append",
                dest="test_modules",
                metavar="PATH",
                help="repeatable relative source test module for focused validation",
            )
    return parser.parse_args(argv)


def _read_draft(path: Path | None) -> dict[str, object] | None:
    if path is None:
        return None
    if path.is_symlink() or not path.is_file():
        raise ValueError("content-draft-file-invalid")
    with path.open("rb") as source:
        payload = source.read(1_048_577)
    if len(payload) > 1_048_576:
        raise ValueError("content-draft-file-too-large")
    validated = ContentDraft.model_validate_json(payload.decode("utf-8")).model_dump()
    validate_draft(validated)
    return validated


def _invoke(arguments: argparse.Namespace) -> dict[str, object]:
    root = arguments.project_root.resolve(strict=True)
    if arguments.project_root.is_symlink() or not root.is_dir() or root == Path(root.anchor):
        raise ValueError("release-project-root-invalid")
    pattern = (
        r"[A-Za-z0-9][A-Za-z0-9._:-]*"
        if arguments.operation == "public"
        else r"[A-Za-z0-9][A-Za-z0-9._-]*"
    )
    if re.fullmatch(pattern, arguments.run_id) is None:
        raise ValueError("release-run-id-invalid")
    if arguments.operation == "local":
        if arguments.test_modules is None:
            invoke = partial(run_local_release, root, run_id=arguments.run_id)
        else:
            invoke = partial(
                run_local_release,
                root,
                run_id=arguments.run_id,
                test_modules=tuple(arguments.test_modules),
            )
        operation = "release_version"
    else:
        draft = _read_draft(arguments.content_draft)
        if draft is None:
            return run_public_release(root, run_id=arguments.run_id)
        invoke = partial(run_public_release, root, run_id=arguments.run_id, content_draft=draft)
        operation = "public.release"
    return run_recorded_release(root, operation, arguments.run_id, invoke)


def main(argv: list[str] | None = None) -> int:
    arguments = _arguments(argv)
    try:
        with redirect_stdout(sys.stderr):
            result = _invoke(arguments)
    except KeyboardInterrupt:
        result = {
            "outcome": "failed",
            "failed_step": "invocation",
            "error_type": "KeyboardInterrupt",
        }
    except (OSError, ValueError, RuntimeError) as error:
        result = {
            "outcome": "failed",
            "failed_step": "invocation",
            "error_type": type(error).__name__,
        }
    print(json.dumps(result, ensure_ascii=False))
    if result.get("error_type") == "KeyboardInterrupt":
        return 130
    return 0 if result.get("outcome") == "completed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
