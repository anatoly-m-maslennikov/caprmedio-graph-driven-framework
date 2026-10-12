"""Direct Project-owned public release.

The selected MCP route supplies a bound Project root, run id, and one complete
content draft. This module deliberately has no selector, admission, or recovery API.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import tomllib
from typing import Any, Callable, Mapping


class PublicReleaseError(ValueError):
    """A direct public release input or command could not continue."""


def run_public_release(
    project_root: Path | str,
    *,
    run_id: str,
    content_draft: Mapping[str, object] | None = None,
    runner: Callable[[tuple[str, ...], Path], Any] | None = None,
) -> dict[str, object]:
    """Test, bump, document, push, upsert the PR, and link its real URL."""

    prompt = (
        "Provide content_draft as one object with exactly description and summary. "
        "description is the full Markdown PR body with non-empty ## New and ## Fixed sections; "
        "summary is a non-empty list of concise Version History bullets."
    )
    if content_draft is None:
        return {
            "outcome": "input_required",
            "run_id": run_id,
            "project_root": str(Path(project_root)),
            "prompt": prompt,
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

    step = "content_draft"

    def command(argv: tuple[str, ...], *, allow_dirty_status: bool = False) -> Any:
        result = runner(argv, root) if runner is not None else subprocess.run(
            argv, cwd=root, text=True, capture_output=True, check=False,
        )
        returncode = getattr(result, "returncode", None)
        if not isinstance(returncode, int) or (returncode != 0 and not allow_dirty_status):
            raise PublicReleaseError(f"public-release-command-failed: {' '.join(argv[:2])}")
        return result

    def git_all(before: str) -> None:
        command((
            "git", "add", "-A", "--", ".", ":(exclude,glob)**/.env", ":(exclude,glob)**/.env*",
            ":(exclude,glob)**/*.env",
        ))
        staged = command(("git", "diff", "--cached", "--quiet"), allow_dirty_status=True)
        if staged.returncode == 1:
            command(("git", "commit", "-m", f"chore(release): checkpoint before public {before}"))
        elif staged.returncode != 0:
            raise PublicReleaseError("public-release-git-status-failed")

    try:
        if not isinstance(content_draft, Mapping) or set(content_draft) != {"description", "summary"}:
            raise PublicReleaseError("content_draft must contain exactly description and summary")
        description = content_draft["description"]
        summary = content_draft["summary"]
        if not isinstance(description, str) or not description.strip():
            raise PublicReleaseError("content_draft.description must be non-empty Markdown")
        description = description.strip() + "\n"
        _, new_heading, after_new = description.partition("## New\n")
        new_section, fixed_heading, fixed_section = after_new.partition("\n## Fixed\n")
        if (not new_heading or not fixed_heading
                or not any(line.startswith("- ") and line[2:].strip() for line in new_section.splitlines())
                or not any(line.startswith("- ") and line[2:].strip() for line in fixed_section.splitlines())):
            raise PublicReleaseError("content_draft.description needs non-empty ## New and ## Fixed sections")
        if not isinstance(summary, list) or not summary or any(
            not isinstance(item, str) or not item.strip() or "\n" in item or len(item) > 240 for item in summary
        ):
            raise PublicReleaseError("content_draft.summary must be concise non-empty bullets")

        version_path = root / "version.toml"
        try:
            version_text = version_path.read_text(encoding="utf-8")
            old_version = tomllib.loads(version_text)["framework"]["version"]
        except (FileNotFoundError, KeyError, TypeError, tomllib.TOMLDecodeError) as error:
            raise PublicReleaseError("version.toml must declare [framework].version") from error
        match = re.fullmatch(
            r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(?:\.(0|[1-9][0-9]*))?",
            old_version,
        ) if isinstance(old_version, str) else None
        if match is None:
            raise PublicReleaseError("public release requires a numeric framework version")
        version = f"{match.group(1)}.{match.group(2)}.{int(match.group(3)) + 1}"
        branch = command(("git", "branch", "--show-current"))
        if getattr(branch, "stdout", "").strip() != "amm/dev":
            raise PublicReleaseError("public-release-requires-amm-dev")

        step = "tests"
        git_all(step)
        command((
            "uv", "run", "--locked", "--no-sync", "--no-env-file", "--group", "rmed-workflow-mcp",
            "--group", "workflow-orchestrator", "python", "-B", "-m", "unittest",
            "PROJECT_TOOLS/tests/test_simple_local_release.py",
            "PROJECT_TOOLS/tests/test_simple_public_release.py",
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/tests/test_simple_local_release_route.py",
        ))

        step = "bump_version"
        git_all(step)
        version_path.write_text(version_text.replace(f'"{old_version}"', f'"{version}"', 1), encoding="utf-8")

        step = "write_docs"
        git_all(step)
        readme = root / "README.md"
        history = root / "VERSION_HISTORY.md"
        marker = f"<!-- public-release:{run_id} -->"
        latest_marker = "<!-- latest-public-release -->"
        if not readme.is_file() or not history.is_file():
            raise PublicReleaseError("public-release-documents-missing")
        if marker in history.read_text(encoding="utf-8"):
            raise PublicReleaseError("public-release-run-id-already-recorded")
        latest = f"{latest_marker}\nLatest public release: **{version}**. See [Version History](VERSION_HISTORY.md)."
        readme_text = readme.read_text(encoding="utf-8")
        if latest_marker in readme_text:
            readme_text, changed = re.subn(
                r"(?m)^<!-- latest-public-release -->\nLatest public release: \*\*[^*\n]+\*\*\. See \[Version History\]\(VERSION_HISTORY\.md\)\.$",
                latest, readme_text,
            )
            if changed != 1:
                raise PublicReleaseError("public-release-readme-block-invalid")
        else:
            readme_text = readme_text.rstrip() + f"\n\n{latest}\n"
        readme.write_text(readme_text, encoding="utf-8")
        history.write_text(
            history.read_text(encoding="utf-8").rstrip()
            + f"\n\n{marker}\n## {version}\n"
            + "\n".join(f"- {item.strip()}" for item in summary)
            + "\n",
            encoding="utf-8",
        )

        step = "push"
        git_all(step)
        command(("git", "push", "origin", "amm/dev"))

        step = "upsert_pr"
        git_all(step)
        discovered = command((
            "gh", "pr", "list", "--head", "amm/dev", "--base", "main", "--state", "open", "--json", "url", "--limit", "2",
        ))
        try:
            matches = json.loads(getattr(discovered, "stdout", ""))
        except (TypeError, json.JSONDecodeError) as error:
            raise PublicReleaseError("public-release-pr-discovery-invalid") from error
        title = f"CAPRMEDIO {version} public release"
        if not isinstance(matches, list) or len(matches) > 1:
            raise PublicReleaseError("public-release-pr-discovery-invalid")
        if matches:
            pr_url = matches[0].get("url") if isinstance(matches[0], Mapping) else None
            if not isinstance(pr_url, str) or re.fullmatch(r"https://github\.com/[^/\s]+/[^/\s]+/pull/[1-9][0-9]*", pr_url) is None:
                raise PublicReleaseError("public-release-pr-discovery-invalid")
            command(("gh", "pr", "edit", pr_url, "--title", title, "--body", description))
        else:
            created = command(("gh", "pr", "create", "--head", "amm/dev", "--base", "main", "--title", title, "--body", description))
            pr_url = getattr(created, "stdout", "").strip()
            if not isinstance(pr_url, str) or re.fullmatch(r"https://github\.com/[^/\s]+/[^/\s]+/pull/[1-9][0-9]*", pr_url) is None:
                raise PublicReleaseError("public-release-pr-create-invalid")

        step = "link_history"
        git_all(step)
        entry = f"{marker}\n## {version}"
        history_text = history.read_text(encoding="utf-8")
        if history_text.count(entry) != 1:
            raise PublicReleaseError("public-release-history-entry-missing")
        history.write_text(history_text.replace(entry, f"{entry} [PR]({pr_url})", 1), encoding="utf-8")

        step = "final_commit_push"
        git_all(step)
        command(("git", "push", "origin", "amm/dev"))
    except Exception as error:
        report = root / ".caprmedio_tmp" / "public_release" / run_id / "issue.md"
        report.parent.mkdir(parents=True, exist_ok=True)
        report.write_text(f"# Public release issue\n\n- Run: `{run_id}`\n- Step: `{step}`\n- Error: {error}\n", encoding="utf-8")
        return {
            "outcome": "failed", "run_id": run_id, "project_root": str(root), "failed_step": step,
            "report_path": report.relative_to(root).as_posix(), "error": str(error),
        }
    return {
        "outcome": "completed", "run_id": run_id, "project_root": str(root), "version": version,
        "pr_url": pr_url, "failed_step": None, "report_path": None,
    }
