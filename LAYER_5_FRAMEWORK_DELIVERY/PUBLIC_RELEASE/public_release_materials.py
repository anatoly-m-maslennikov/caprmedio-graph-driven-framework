# CA-M-366@20

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
    readme: str, history: str, version: str, run_id: str, summary: list[str], pr_url: str
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
    heading, separator, rest = history.partition("\n")
    if not separator or not heading.startswith("# "):
        raise PublicReleaseError("public-release-history-heading-invalid")
    entry = f"{marker}\n## {version} [PR]({pr_url})\n" + "\n".join(f"- {item.strip()}" for item in summary) + "\n\n"
    pattern = re.compile(r"(?m)^(?:<!-- public-release:[^\n]+ -->\n)?## (?:Version )?(\d+(?:\.\d+)+)(?=\s|$)[^\n]*\n")
    matches = list(pattern.finditer(rest))
    prefix = rest[:matches[0].start()] if matches else rest
    entries = [
        (tuple(map(int, match.group(1).split("."))), rest[match.start():matches[i + 1].start() if i + 1 < len(matches) else len(rest)])
        for i, match in enumerate(matches)
    ]
    new_key = tuple(map(int, version.split(".")))
    if any(key >= new_key for key, _ in entries):
        raise PublicReleaseError("public-release-version-not-newest")
    entries.append((new_key, entry))
    entries.sort(key=lambda item: item[0], reverse=True)
    result = heading + "\n" + prefix
    for _, value in entries:
        if not result.endswith("\n\n"):
            result += "\n" if result.endswith("\n") else "\n\n"
        result += value
    return readme, result
