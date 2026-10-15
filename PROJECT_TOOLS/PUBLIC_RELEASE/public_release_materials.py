"""Pure input and material transformations for one direct public release."""

from __future__ import annotations

import json
import re
from collections.abc import Mapping


class PublicReleaseError(ValueError):
    """A direct public release input or command could not continue."""


def validate_draft(draft: Mapping[str, object]) -> tuple[str, list[str]]:
    if not isinstance(draft, Mapping) or set(draft) != {"description", "summary"}:
        raise PublicReleaseError("content_draft must contain exactly description and summary")
    description, summary = draft["description"], draft["summary"]
    if not isinstance(description, str) or not description.strip():
        raise PublicReleaseError("content_draft.description must be non-empty Markdown")
    description = description.strip() + "\n"
    _, new_heading, after_new = description.partition("## New\n")
    new_section, fixed_heading, fixed_section = after_new.partition("\n## Fixed\n")
    if (
        not new_heading
        or not fixed_heading
        or not all(
            any(line.startswith("- ") and line[2:].strip() for line in section.splitlines())
            for section in (new_section, fixed_section)
        )
    ):
        raise PublicReleaseError(
            "content_draft.description needs non-empty ## New and ## Fixed sections"
        )
    if (
        not isinstance(summary, list)
        or not summary
        or any(
            not isinstance(item, str) or not item.strip() or "\n" in item or len(item) > 240
            for item in summary
        )
    ):
        raise PublicReleaseError("content_draft.summary must be concise non-empty bullets")
    return description, summary


def next_public_version(old_version: object) -> str:
    match = (
        re.fullmatch(
            r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(?:\.(0|[1-9][0-9]*))?",
            old_version,
        )
        if isinstance(old_version, str)
        else None
    )
    if match is None:
        raise PublicReleaseError("public release requires a numeric framework version")
    return f"{match.group(1)}.{match.group(2)}.{int(match.group(3)) + 1}"


def repository_identity(remote_urls: str, repository_slug: object) -> str:
    urls = remote_urls.splitlines()
    if len(urls) != 1:
        raise PublicReleaseError("public-release-remote-invalid")
    match = re.fullmatch(
        r"(?:git@(?:githuba|github\.com):|ssh://git@(?:githuba|github\.com)/|https://github\.com/)"
        r"([A-Za-z0-9][A-Za-z0-9-]*)/([A-Za-z0-9_.-]+?)(?:\.git)?",
        urls[0],
    )
    if match is None or match.group(2) != repository_slug:
        raise PublicReleaseError("public-release-remote-invalid")
    return f"{match.group(1)}/{match.group(2)}"


def validate_pr_url(url: object, repository: str) -> str:
    if (
        not isinstance(url, str)
        or re.fullmatch(rf"https://github\.com/{re.escape(repository)}/pull/[1-9][0-9]*", url)
        is None
    ):
        raise PublicReleaseError("public-release-pr-url-invalid")
    return url


def matching_pr(output: str, repository: str) -> str | None:
    try:
        matches = json.loads(output)
    except (TypeError, json.JSONDecodeError) as error:
        raise PublicReleaseError("public-release-pr-discovery-invalid") from error
    if not isinstance(matches, list) or len(matches) > 1:
        raise PublicReleaseError("public-release-pr-discovery-invalid")
    if not matches:
        return None
    match = matches[0]
    if not isinstance(match, Mapping) or (
        match.get("state"),
        match.get("headRefName"),
        match.get("baseRefName"),
    ) != ("OPEN", "amm/dev", "main"):
        raise PublicReleaseError("public-release-pr-discovery-invalid")
    return validate_pr_url(match.get("url"), repository)


def prepare_documents(
    readme: str, history: str, version: str, run_id: str, summary: list[str], pr_url: str | None
) -> tuple[str, str]:
    marker = f"<!-- public-release:{run_id} -->"
    if marker in history:
        raise PublicReleaseError("public-release-run-id-already-recorded")
    latest_marker = "<!-- latest-public-release -->"
    latest = f"{latest_marker}\nLatest public release: **{version}**. See [Version History](VERSION_HISTORY.md)."
    if latest_marker in readme:
        readme, changed = re.subn(
            r"(?m)^<!-- latest-public-release -->\nLatest public release: \*\*[^*\n]+\*\*\. See \[Version History\]\(VERSION_HISTORY\.md\)\.$",
            latest,
            readme,
        )
        if changed != 1:
            raise PublicReleaseError("public-release-readme-block-invalid")
    else:
        readme = readme.rstrip() + f"\n\n{latest}\n"
    link = f" [PR]({pr_url})" if pr_url else ""
    history = history.rstrip() + f"\n\n{marker}\n## {version}{link}\n"
    return readme, history + "\n".join(f"- {item.strip()}" for item in summary) + "\n"


def finalize_history(history: str, version: str, run_id: str, pr_url: str) -> str:
    entry = f"<!-- public-release:{run_id} -->\n## {version}"
    linked_entry = f"{entry} [PR]({pr_url})"
    if history.count(entry) != 1:
        raise PublicReleaseError("public-release-history-entry-missing")
    if linked_entry in history:
        return history
    if entry + "\n" not in history:
        raise PublicReleaseError("public-release-history-entry-invalid")
    return history.replace(entry + "\n", linked_entry + "\n", 1)
