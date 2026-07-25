#!/usr/bin/env python3
"""Historical preservation verifier for a META/GOV atomic migration replay.

Invocation: ``python dset_verify_meta_gov_migration.py [ROOT] [--expected-count N]``.
ROOT defaults to the repository containing this completed tool. It compares the
current atomic files in ``.dset/101_layer_meta`` and ``.dset/102_layer_gov``
with that root's ``HEAD`` versions, checking paths, IDs, protected relations,
original body prefixes, YAML carrier format, and frontmatter retention. The
default expected count is 319. It writes nothing, exits 0 on success and 1 on
any preservation failure. This bounded tool is outside active imports and CLI.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True

REPO = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO))

from dset_toolchain.frontmatter import parse  # noqa: E402

ROOT_PREFIXES = (
    ".dset/101_layer_meta/",
    ".dset/102_layer_gov/",
)
VOCAB = {
    "layer:meta": {
        "artifact-model",
        "assurance",
        "authority",
        "external-boundary",
        "governance-surface",
        "interaction",
        "lifecycle",
        "profile",
        "scope",
        "self-hosting",
        "topology",
    },
    "layer:gov": {
        "artifact-catalog",
        "assurance",
        "carrier-format",
        "external-boundary",
        "interaction",
        "layout",
        "lifecycle",
        "methodology",
        "priority",
        "provenance",
        "relation-model",
        "runtime",
        "settings",
        "subject-scope",
    },
}
RETAINED = {
    "artifact_type",
    "artifact_subtype",
    "artifact_id",
    "scope_path",
    "subject_scopes",
    "priority",
    "llm_session_ids",
    "relation_kind",
    "endpoints",
    "relations",
}


def run(*args: str) -> str:
    return subprocess.run(
        args,
        cwd=REPO,
        check=True,
        text=True,
        capture_output=True,
    ).stdout


def head_paths() -> list[str]:
    paths = run("git", "ls-tree", "-r", "--name-only", "HEAD").splitlines()
    return sorted(
        path
        for path in paths
        if path.endswith(".md") and path.startswith(ROOT_PREFIXES)
    )


def current_paths() -> list[str]:
    return sorted(
        str(path.relative_to(REPO))
        for prefix in ROOT_PREFIXES
        for path in (REPO / prefix).rglob("*.md")
    )


def head_text(path: str) -> str:
    return run("git", "show", f"HEAD:{path}")


def frontmatter_payload(text: str) -> str:
    return text.split("---", 2)[1]


def raw_blocks(raw: str) -> dict[str, str]:
    lines = raw.splitlines(keepends=True)
    starts = [
        index
        for index, line in enumerate(lines)
        if line and not line[0].isspace() and re.match(r"^[A-Za-z0-9_-]+:", line)
    ]
    result: dict[str, str] = {}
    for offset, start in enumerate(starts):
        end = starts[offset + 1] if offset + 1 < len(starts) else len(lines)
        key = lines[start].split(":", 1)[0].strip()
        result[key] = "".join(lines[start:end])
    return result


def relation_signature(metadata: dict[str, Any]) -> tuple[Any, Any, Any]:
    return (
        metadata.get("relation_kind"),
        metadata.get("endpoints"),
        metadata.get("relations"),
    )


def main() -> int:
    """Verify preservation invariants for the selected historical replay root."""
    global REPO
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=REPO)
    parser.add_argument("--expected-count", type=int, default=319)
    arguments = parser.parse_args()
    REPO = arguments.root.resolve()
    before_paths = head_paths()
    after_paths = current_paths()
    issues = _path_issues(before_paths, after_paths, arguments.expected_count)
    before_ids, after_ids = _verify_paths(after_paths, issues)
    _verify_id_sets(before_ids, after_ids, issues)
    return _report(issues, len(after_paths))


def _path_issues(before: list[str], after: list[str], expected: int) -> list[str]:
    issues: list[str] = []
    if before != after:
        issues.append("atomic path set changed")
    if len(after) != expected:
        issues.append(f"expected {expected} atoms, found {len(after)}")
    return issues


def _verify_paths(paths: list[str], issues: list[str]) -> tuple[set[str], set[str]]:
    before_ids: set[str] = set()
    after_ids: set[str] = set()
    for path in paths:
        _verify_path(path, issues, before_ids, after_ids)
    return before_ids, after_ids


def _verify_path(
    path: str, issues: list[str], before_ids: set[str], after_ids: set[str]
) -> None:
    before_text = head_text(path)
    after_text = (REPO / path).read_text(encoding="utf-8")
    before = parse(before_text)
    after = parse(after_text)
    if before is None or after is None:
        issues.append(f"{path}: missing frontmatter")
        return
    before_meta, before_body, _ = before
    after_meta, after_body, after_format = after

    artifact_id = str(after_meta.get("artifact_id", ""))
    before_ids.add(str(before_meta.get("artifact_id", "")))
    after_ids.add(artifact_id)

    _verify_protected(
        path, before_meta, after_meta, before_body, after_body, after_format, issues
    )

    expected_scope = "layer:meta" if path.startswith(ROOT_PREFIXES[0]) else "layer:gov"
    if after_meta.get("scope_path") != expected_scope:
        issues.append(f"{path}: invalid scope_path")

    _verify_subjects(path, after_meta, expected_scope, issues)
    _verify_payload(path, before_text, after_text, after_body, issues)


def _verify_protected(
    path: str,
    before: dict[str, Any],
    after: dict[str, Any],
    before_body: str,
    after_body: str,
    fmt: str,
    issues: list[str],
) -> None:
    for key in (
        "artifact_type",
        "artifact_subtype",
        "artifact_id",
        "priority",
        "llm_session_ids",
    ):
        if before.get(key) != after.get(key):
            issues.append(f"{path}: protected property changed: {key}")
    if relation_signature(before) != relation_signature(after):
        issues.append(f"{path}: relations or endpoints changed")
    if not after_body.startswith(before_body):
        issues.append(f"{path}: original body is not an exact prefix")
    if fmt != "yaml":
        issues.append(f"{path}: frontmatter is not YAML")


def _verify_subjects(
    path: str, metadata: dict[str, Any], scope: str, issues: list[str]
) -> None:
    subjects, artifact_type = (
        metadata.get("subject_scopes"),
        str(metadata.get("artifact_type", "")),
    )
    if artifact_type == "evidence_record":
        if subjects not in (None, []):
            issues.append(f"{path}: Evidence Record subject scope must be omitted")
    elif not isinstance(subjects, list) or not subjects:
        issues.append(f"{path}: subject_scopes required")
    elif artifact_type != "analysis_report" and len(subjects) != 1:
        issues.append(f"{path}: exactly one subject scope required")
    elif len(subjects) != len(set(subjects)):
        issues.append(f"{path}: duplicate subject scope")
    elif any(subject not in VOCAB[scope] for subject in subjects):
        issues.append(f"{path}: unregistered subject scope")


def _verify_payload(
    path: str, before: str, after: str, body: str, issues: list[str]
) -> None:

    payload = frontmatter_payload(after)
    if '"' in payload or "'" in payload:
        issues.append(f"{path}: quoted frontmatter value")
    if re.search(r":\s*(?:\[\]|\{\}|\[|\{)", payload):
        issues.append(f"{path}: inline collection")
    removed = {
        key: value
        for key, value in raw_blocks(frontmatter_payload(before)).items()
        if key not in RETAINED
    }
    if (
        removed
        and "## Historical frontmatter metadata\n\n```yaml\n"
        + "".join(removed.values())
        + "```"
        not in body
    ):
        issues.append(f"{path}: removed metadata not retained exactly")


def _verify_id_sets(
    before_ids: set[str], after_ids: set[str], issues: list[str]
) -> None:
    if before_ids != after_ids or "" in before_ids or "" in after_ids:
        issues.append("artifact ID set changed or contains an empty ID")


def _report(issues: list[str], count: int) -> int:
    if issues:
        print("\n".join(issues))
        return 1
    print(f"migration-verification-ok: {count} atoms, IDs/relations/bodies preserved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
