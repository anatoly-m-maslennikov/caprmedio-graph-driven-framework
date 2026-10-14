"""Direct Project-owned public release, without selector or admission gates."""

from __future__ import annotations

from collections.abc import Mapping
from functools import partial
from pathlib import Path
import re
import sys
import tomllib

sys.path.insert(0, str(Path(__file__).resolve().parent))
from public_release_materials import (
    PublicReleaseError,
    finalize_history,
    matching_pr,
    next_public_version,
    prepare_documents,
    validate_draft,
)

from public_release_git import Command, Runner, _checkpoint, _command, _repository, _upsert_pr


def _prepare_materials(root: Path, run_id: str, summary: list[str], pr_url: str | None) -> str:
    version_path, readme, history = (
        root / name for name in ("version.toml", "README.md", "VERSION_HISTORY.md")
    )
    if any(path.is_symlink() or not path.is_file() for path in (version_path, readme, history)):
        raise PublicReleaseError("public-release-documents-missing-or-unsafe")
    version_text = version_path.read_text(encoding="utf-8")
    try:
        old_version = tomllib.loads(version_text)["framework"]["version"]
    except (KeyError, TypeError, tomllib.TOMLDecodeError) as error:
        raise PublicReleaseError("version.toml must declare [framework].version") from error
    version = next_public_version(old_version)
    readme_text, history_text = prepare_documents(
        readme.read_text(encoding="utf-8"),
        history.read_text(encoding="utf-8"),
        version,
        run_id,
        summary,
        pr_url,
    )
    version_path.write_text(
        version_text.replace(f'"{old_version}"', f'"{version}"', 1), encoding="utf-8"
    )
    readme.write_text(readme_text, encoding="utf-8")
    history.write_text(history_text, encoding="utf-8")
    return version


def _test_materials(root: Path, command: Command) -> None:
    observations = (
        ("git", "rev-parse", "HEAD"),
        ("git", "status", "--porcelain", "--untracked-files=all"),
    )
    before = tuple(command(argv).stdout for argv in observations)
    command(
        (
            "uv",
            "run",
            "--project",
            str(root),
            "--locked",
            "--no-sync",
            "--python",
            "3.14",
            "--managed-python",
            "--no-env-file",
            "--all-groups",
            "python",
            "-B",
            str(Path(__file__).resolve().parents[1] / "run_full_test_suite.py"),
            "--project-root",
            str(root),
        )
    )
    if tuple(command(argv).stdout for argv in observations) != before:
        raise PublicReleaseError("public-release-tested-source-changed")


def _finalize_history(root: Path, command: Command, version: str, run_id: str, pr_url: str) -> None:
    path = root / "VERSION_HISTORY.md"
    history = path.read_text(encoding="utf-8")
    linked = finalize_history(history, version, run_id, pr_url)
    if linked != history:
        path.write_text(linked, encoding="utf-8")
        _checkpoint(command, "final_commit_push")
        command(("git", "push", "origin", "amm/dev"))
    else:
        _checkpoint(command, "completion")


def _release(
    root: Path, run_id: str, draft: Mapping[str, object], command: Command
) -> dict[str, object]:
    step = "content_draft"
    try:
        description, summary = validate_draft(draft)
        repository = _repository(root, command)
        step = "discover_pr"
        _checkpoint(command, step)
        discovered = command(
            (
                "gh",
                "pr",
                "list",
                "--repo",
                repository,
                "--head",
                "amm/dev",
                "--base",
                "main",
                "--state",
                "open",
                "--json",
                "url,state,headRefName,baseRefName",
                "--limit",
                "2",
            )
        )
        pr_url = matching_pr(discovered.stdout, repository)
        _checkpoint(command, "content_draft")
        step = "write_docs"
        _checkpoint(command, step)
        version = _prepare_materials(root, run_id, summary, pr_url)
        step = "tests"
        _checkpoint(command, step)
        _test_materials(root, command)
        step = "push"
        command(("git", "push", "origin", "amm/dev"))
        step = "upsert_pr"
        pr_url = _upsert_pr(command, repository, version, description, pr_url)
        step = "link_history"
        _checkpoint(command, step)
        _finalize_history(root, command, version, run_id, pr_url)
    except Exception as error:
        return _report_failure(root, run_id, step, error)
    return {
        "outcome": "completed",
        "run_id": run_id,
        "project_root": str(root),
        "version": version,
        "pr_url": pr_url,
        "failed_step": None,
        "report_path": None,
    }


def _report_failure(root: Path, run_id: str, step: str, error: Exception) -> dict[str, object]:
    report = root / ".caprmedio_tmp" / "public_release" / run_id / "issue.md"
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(
        f"# Public release issue\n\n- Run: `{run_id}`\n- Step: `{step}`\n- Error: {error}\n",
        encoding="utf-8",
    )
    return {
        "outcome": "failed",
        "run_id": run_id,
        "project_root": str(root),
        "failed_step": step,
        "report_path": report.relative_to(root).as_posix(),
        "error": str(error),
    }


def run_public_release(
    project_root: Path | str,
    *,
    run_id: str,
    content_draft: Mapping[str, object] | None = None,
    runner: Runner | None = None,
) -> dict[str, object]:
    """Discover the selected PR, prepare and test materials, then publish Draft."""
    if content_draft is None:
        return {
            "outcome": "input_required",
            "run_id": run_id,
            "project_root": str(Path(project_root)),
            "prompt": "Provide content_draft as one object with exactly description and summary. description is the full Markdown PR body with non-empty ## New and ## Fixed sections; summary is a non-empty list of concise Version History bullets.",
            "content_draft_schema": {
                "description": "Markdown with ## New and ## Fixed",
                "summary": ["concise Version History bullet"],
            },
        }
    if not isinstance(run_id, str) or re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._:-]*", run_id) is None:
        raise PublicReleaseError("public-release-run-id-invalid")
    try:
        root = Path(project_root).resolve(strict=True)
    except OSError as error:
        raise PublicReleaseError("public-release-project-root-invalid") from error
    if not root.is_dir() or root == Path(root.anchor):
        raise PublicReleaseError("public-release-project-root-invalid")
    return _release(root, run_id, content_draft, partial(_command, root, runner))
