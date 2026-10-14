"""Concrete Git, PR and subprocess boundary for one public release."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
import subprocess
import sys

sys.path.insert(
    0, str(Path(__file__).resolve().parents[2] / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS")
)
from artifact_metadata import project_identity
from public_release_materials import PublicReleaseError, repository_identity, validate_pr_url

Runner = Callable[[tuple[str, ...], Path], subprocess.CompletedProcess[str]]
Command = Callable[..., subprocess.CompletedProcess[str]]


def _command(
    root: Path, runner: Runner | None, argv: tuple[str, ...], *, allow_dirty_status: bool = False
) -> subprocess.CompletedProcess[str]:
    result = (
        runner(argv, root)
        if runner is not None
        else subprocess.run(
            argv,
            cwd=root,
            text=True,
            capture_output=True,
            check=False,
            timeout=3600 if argv[:2] == ("uv", "run") else 120,
        )
    )
    if not isinstance(result.returncode, int) or (
        result.returncode != 0 and not allow_dirty_status
    ):
        detail = ""
        if argv[:2] == ("uv", "run"):
            detail = "\n".join(
                f"{stream}:\n{getattr(result, stream)[-4000:]}" for stream in ("stdout", "stderr")
            )
        raise PublicReleaseError(f"public-release-command-failed: {' '.join(argv[:2])}: {detail}")
    return result


def _checkpoint(command: Command, before: str) -> None:
    command(
        (
            "git",
            "add",
            "-A",
            "--",
            ".",
            ":(exclude,glob)**/.env",
            ":(exclude,glob)**/.env*",
            ":(exclude,glob)**/*.env",
        )
    )
    staged = command(("git", "diff", "--cached", "--quiet"), allow_dirty_status=True)
    if staged.returncode == 1:
        command(("git", "commit", "-m", f"chore(release): checkpoint before public {before}"))
    elif staged.returncode != 0:
        raise PublicReleaseError("public-release-git-status-failed")


def _repository(root: Path, command: Command) -> str:
    if command(("git", "branch", "--show-current")).stdout.strip() != "amm/dev":
        raise PublicReleaseError("public-release-requires-amm-dev")
    slug = project_identity(root)["project"]["repository_slug"]
    repository = repository_identity(
        command(("git", "remote", "get-url", "--all", "origin")).stdout, slug
    )
    push_repository = repository_identity(
        command(("git", "remote", "get-url", "--push", "--all", "origin")).stdout, slug
    )
    if push_repository != repository:
        raise PublicReleaseError("public-release-remote-mismatch")
    return repository


def _upsert_pr(
    command: Command, repository: str, version: str, description: str, pr_url: str | None
) -> str:
    title = f"CAPRMEDIO {version} public release"
    if pr_url:
        command(("gh", "pr", "ready", pr_url, "--undo", "--repo", repository))
        command(
            (
                "gh",
                "pr",
                "edit",
                pr_url,
                "--repo",
                repository,
                "--title",
                title,
                "--body",
                description,
            )
        )
        return pr_url
    created = command(
        (
            "gh",
            "pr",
            "create",
            "--repo",
            repository,
            "--draft",
            "--head",
            "amm/dev",
            "--base",
            "main",
            "--title",
            title,
            "--body",
            description,
        )
    )
    return validate_pr_url(created.stdout.strip(), repository)
