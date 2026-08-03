#!/usr/bin/env python3
"""Migrate META Subject scopes and generate their deterministic Catalog.

Usage:
    python 15_layer_implementation/tools/carmadio_meta_scope.py migrate
    python 15_layer_implementation/tools/carmadio_meta_scope.py migrate \
        --apply --expect-plan-digest SHA256
    python 15_layer_implementation/tools/carmadio_meta_scope.py project
    python 15_layer_implementation/tools/carmadio_meta_scope.py project --write
    python 15_layer_implementation/tools/carmadio_meta_scope.py project --check

Both commands default to a dry, read-only preview. ``migrate`` replaces only a
validated legacy ``subject_scopes`` block with one canonical ``subject_scope``
line. ``project`` renders the active META Atom Catalog. Writes stage under the
script-owned ``.carmadio_runtime/carmadio-meta-scope`` folder, verify complete
bytes before replacement, and roll back every touched carrier on failure.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from dset_toolchain.frontmatter import FrontmatterError  # noqa: E402
from dset_toolchain.frontmatter import parse as parse_frontmatter  # noqa: E402
from dset_toolchain.frontmatter import render as render_frontmatter  # noqa: E402

META_RELATIVE = Path(".carmadio/101_layer_meta")
CATALOG_RELATIVE = META_RELATIVE / (
    "CARMADIO-META-CATL-001-requirement--active-atoms-by-subject-scope.md"
)
RUNTIME_RELATIVE = Path(".carmadio_runtime/carmadio-meta-scope")
EXCLUDED_PARTS = frozenset({"archive", "drafts"})
PROJECTION_TYPES = frozenset({"catalog", "hub", "map"})
CANONICAL_SCOPES = (
    "principles",
    "artifact-model",
    "scope-topology",
    "authority",
    "assurance",
    "lifecycle-traceability",
    "development-flow",
    "framework-boundary",
)
LEGACY_SCOPE_MAP = {
    "artifact-model": "artifact-model",
    "assurance": "assurance",
    "authority": "authority",
    "candidate-promotion": "development-flow",
    "delivery-planning": "development-flow",
    "external-boundary": "scope-topology",
    "framework-identity": "principles",
    "governance-surface": "framework-boundary",
    "interaction": "development-flow",
    "lifecycle": "lifecycle-traceability",
    "product-framing": "development-flow",
    "profile": "scope-topology",
    "provenance": "lifecycle-traceability",
    "release-finalization": "development-flow",
    "release-reconciliation": "development-flow",
    "scope": "scope-topology",
    "self-hosting": "framework-boundary",
    "topology": "scope-topology",
}
SCOPE_OVERRIDES = {
    "CARMADIO-ANALYSIS-META-001": "lifecycle-traceability",
    "CARMADIO-CONTRACT-META-001": "framework-boundary",
    "CARMADIO-REQUIREMENT-META-004": "assurance",
    "CARMADIO-REQUIREMENT-META-011": "framework-boundary",
    "CARMADIO-REQUIREMENT-META-053": "lifecycle-traceability",
    "CARMADIO-REQUIREMENT-META-075": "lifecycle-traceability",
    "CARMADIO-REQUIREMENT-META-077": "lifecycle-traceability",
    "CARMADIO-REQUIREMENT-META-090": "authority",
    "CARMADIO-REQUIREMENT-META-092": "assurance",
    "CARMADIO-REQUIREMENT-META-113": "lifecycle-traceability",
    "CARMADIO-REQUIREMENT-META-114": "principles",
    "CARMADIO-REQUIREMENT-META-115": "principles",
    "CARMADIO-REQUIREMENT-META-116": "principles",
    "CARMADIO-REQUIREMENT-META-117": "principles",
    "CARMADIO-REQUIREMENT-META-118": "principles",
}
CATALOG_ID = "CARMADIO-META-CATL-001"
GENERATOR_ID = "carmadio-meta-scope"
GENERATOR_VERSION = 1


class MetaScopeError(RuntimeError):
    """META Subject-scope migration or Projection generation failed safely."""


@dataclass(frozen=True)
class Atom:
    """One validated active META Atom and its exact carrier bytes."""

    artifact_id: str
    subject_scope: str
    title: str
    path: Path
    content: bytes


@dataclass(frozen=True)
class Change:
    """One exact carrier replacement with a stable preimage."""

    path: Path
    before: bytes
    after: bytes


def _metadata(path: Path, content: bytes) -> tuple[dict[str, Any], str]:
    """Parse one YAML-frontmatter Markdown carrier."""
    try:
        parsed = parse_frontmatter(content.decode("utf-8"))
    except (UnicodeError, FrontmatterError) as error:
        raise MetaScopeError(f"invalid Markdown properties: {path}: {error}") from error
    if parsed is None:
        raise MetaScopeError(f"missing Markdown properties: {path}")
    metadata, body, format_name = parsed
    if format_name != "yaml":
        raise MetaScopeError(f"META carrier does not use YAML properties: {path}")
    return metadata, body


def _active_markdown_paths(root: Path) -> tuple[Path, ...]:
    """Return active META Markdown paths without assuming their role folder."""
    meta_root = root / META_RELATIVE
    if not meta_root.is_dir():
        raise MetaScopeError(f"META root does not exist: {meta_root}")
    paths = []
    for path in meta_root.rglob("*.md"):
        relative = path.relative_to(meta_root)
        if path == root / CATALOG_RELATIVE:
            continue
        if EXCLUDED_PARTS.intersection(relative.parts):
            continue
        if path.is_symlink() or not path.is_file():
            raise MetaScopeError(f"active META carrier is not a regular file: {path}")
        paths.append(path)
    return tuple(sorted(paths))


def _artifact_identity(path: Path, metadata: dict[str, Any]) -> tuple[str, str]:
    """Return a validated Atom identity and artifact type."""
    artifact_id = metadata.get("artifact_id")
    artifact_type = metadata.get("artifact_type")
    if not isinstance(artifact_id, str) or not artifact_id:
        raise MetaScopeError(f"missing or invalid artifact_id: {path}")
    if not isinstance(artifact_type, str) or not artifact_type:
        raise MetaScopeError(f"missing or invalid artifact_type: {path}")
    return artifact_id, artifact_type


def _legacy_scope(path: Path, metadata: dict[str, Any]) -> str:
    """Resolve one legacy plural scope without accepting ambiguity."""
    values = metadata.get("subject_scopes")
    if not isinstance(values, list) or len(values) != 1:
        raise MetaScopeError(f"legacy subject_scopes must contain one value: {path}")
    value = values[0]
    if not isinstance(value, str) or value not in LEGACY_SCOPE_MAP:
        raise MetaScopeError(f"unknown legacy Subject scope in {path}: {value!r}")
    return value


def _target_scope(artifact_id: str, legacy_scope: str) -> str:
    """Map one validated legacy classification to its canonical scope."""
    target = SCOPE_OVERRIDES.get(artifact_id, LEGACY_SCOPE_MAP[legacy_scope])
    if target not in CANONICAL_SCOPES:
        raise MetaScopeError(f"migration produced unknown Subject scope: {target}")
    return target


def _replace_legacy_scope(
    path: Path, content: bytes, metadata: dict[str, Any], artifact_id: str
) -> bytes:
    """Replace only the exact legacy property bytes after semantic validation."""
    if "subject_scope" in metadata:
        raise MetaScopeError(f"carrier has singular and plural Subject scope: {path}")
    legacy = _legacy_scope(path, metadata)
    target = _target_scope(artifact_id, legacy)
    old = f"subject_scopes:\n  - {legacy}\n"
    text = content.decode("utf-8")
    if text.count(old) != 1:
        raise MetaScopeError(f"unexpected legacy Subject-scope carrier shape: {path}")
    updated = text.replace(old, f"subject_scope: {target}\n", 1).encode("utf-8")
    _verify_scope_recode(path, metadata, updated, target)
    return updated


def _verify_scope_recode(
    path: Path, before: dict[str, Any], content: bytes, target: str
) -> None:
    """Prove that the singular scope property is the only metadata change."""
    after, _ = _metadata(path, content)
    expected = {
        ("subject_scope" if key == "subject_scopes" else key): (
            target if key == "subject_scopes" else value
        )
        for key, value in before.items()
    }
    if after != expected:
        raise MetaScopeError(f"Subject-scope recoding changed other metadata: {path}")


def _replace_singular_scope(
    path: Path, content: bytes, metadata: dict[str, Any], target: str
) -> bytes:
    """Correct one explicitly classified singular scope without broader edits."""
    current = _scope_value(path, metadata)
    old = f"subject_scope: {current}\n"
    text = content.decode("utf-8")
    if text.count(old) != 1:
        raise MetaScopeError(f"unexpected singular Subject-scope carrier shape: {path}")
    updated = text.replace(old, f"subject_scope: {target}\n", 1).encode("utf-8")
    after, _ = _metadata(path, updated)
    expected = {**metadata, "subject_scope": target}
    if after != expected:
        raise MetaScopeError(f"Subject-scope correction changed other metadata: {path}")
    return updated


def _scope_value(path: Path, metadata: dict[str, Any]) -> str:
    """Return one canonical singular Subject scope or fail closed."""
    if "subject_scopes" in metadata:
        raise MetaScopeError(f"legacy plural subject_scopes remains: {path}")
    value = metadata.get("subject_scope")
    if not isinstance(value, str) or value not in CANONICAL_SCOPES:
        raise MetaScopeError(f"missing or unknown subject_scope in {path}: {value!r}")
    return value


def _migration_changes(root: Path) -> tuple[Change, ...]:
    """Build the complete migration plan before changing any carrier."""
    changes = []
    seen = set()
    for path in _active_markdown_paths(root):
        content = path.read_bytes()
        metadata, _ = _metadata(path, content)
        artifact_id, artifact_type = _artifact_identity(path, metadata)
        if artifact_type in PROJECTION_TYPES:
            continue
        if artifact_id in seen:
            raise MetaScopeError(f"duplicate active META artifact_id: {artifact_id}")
        seen.add(artifact_id)
        if "subject_scopes" in metadata:
            after = _replace_legacy_scope(path, content, metadata, artifact_id)
            changes.append(Change(path, content, after))
        else:
            current = _scope_value(path, metadata)
            override = SCOPE_OVERRIDES.get(artifact_id)
            if override is not None and current != override:
                after = _replace_singular_scope(path, content, metadata, override)
                changes.append(Change(path, content, after))
    return tuple(changes)


def _plan_digest(root: Path, changes: tuple[Change, ...]) -> str:
    """Bind apply to exact paths, preimages, and replacement bytes."""
    records = [
        {
            "path": item.path.relative_to(root).as_posix(),
            "before": hashlib.sha256(item.before).hexdigest(),
            "after": hashlib.sha256(item.after).hexdigest(),
        }
        for item in changes
    ]
    encoded = json.dumps(records, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _print_plan(root: Path, changes: tuple[Change, ...]) -> str:
    """Render the stable migration preview and return its digest."""
    digest = _plan_digest(root, changes)
    print(f"changes: {len(changes)}")
    print(f"plan-digest: {digest}")
    for item in changes:
        print(f"UPDATE {item.path.relative_to(root).as_posix()}")
    return digest


def _runtime_root(root: Path) -> Path:
    """Create the script-owned transaction directory without collision."""
    runtime = root / RUNTIME_RELATIVE
    if runtime.exists():
        raise MetaScopeError(f"runtime transaction folder already exists: {runtime}")
    runtime.mkdir(parents=True)
    return runtime


def _stage_changes(runtime: Path, changes: tuple[Change, ...]) -> list[Path]:
    """Write and verify every replacement before touching a source carrier."""
    staged = []
    for index, item in enumerate(changes):
        path = runtime / f"{index:04d}.stage"
        path.write_bytes(item.after)
        if path.read_bytes() != item.after:
            raise MetaScopeError(f"staged byte verification failed: {item.path}")
        staged.append(path)
    return staged


def _restore_changes(
    runtime: Path, applied: list[Change], originals: dict[Path, bytes]
) -> None:
    """Restore every replaced carrier atomically in reverse order."""
    for index, item in enumerate(reversed(applied)):
        staged = runtime / f"rollback-{index:04d}.stage"
        staged.write_bytes(originals[item.path])
        os.replace(staged, item.path)


def _apply_changes(root: Path, changes: tuple[Change, ...]) -> None:
    """Apply a fully staged plan and roll back on any failure."""
    if not changes:
        return
    runtime = _runtime_root(root)
    originals = {item.path: item.before for item in changes}
    applied: list[Change] = []
    try:
        staged = _stage_changes(runtime, changes)
        for item in changes:
            if item.path.read_bytes() != item.before:
                raise MetaScopeError(f"carrier changed after preview: {item.path}")
        for item, stage in zip(changes, staged, strict=True):
            os.replace(stage, item.path)
            applied.append(item)
        _collect_atoms(root)
    except Exception:
        _restore_changes(runtime, applied, originals)
        raise
    finally:
        shutil.rmtree(runtime, ignore_errors=True)


def _title(path: Path, body: str) -> str:
    """Extract exactly one source title from the Markdown body."""
    titles = [line[2:].strip() for line in body.splitlines() if line.startswith("# ")]
    if len(titles) != 1 or not titles[0]:
        raise MetaScopeError(f"expected exactly one level-one title: {path}")
    return titles[0]


def _collect_atoms(root: Path) -> tuple[Atom, ...]:
    """Collect every active META Atom and validate catalog coordinates."""
    atoms = []
    seen = set()
    for path in _active_markdown_paths(root):
        content = path.read_bytes()
        metadata, body = _metadata(path, content)
        artifact_id, artifact_type = _artifact_identity(path, metadata)
        if artifact_type in PROJECTION_TYPES:
            continue
        if artifact_id in seen:
            raise MetaScopeError(f"duplicate active META artifact_id: {artifact_id}")
        seen.add(artifact_id)
        atoms.append(
            Atom(
                artifact_id,
                _scope_value(path, metadata),
                _title(path, body),
                path,
                content,
            )
        )
    order = {scope: index for index, scope in enumerate(CANONICAL_SCOPES)}
    return tuple(
        sorted(atoms, key=lambda item: (order[item.subject_scope], item.artifact_id))
    )


def _frontier_digest(atoms: tuple[Atom, ...]) -> str:
    """Digest the ordered source IDs and exact carrier digests."""
    digest = hashlib.sha256()
    for atom in atoms:
        digest.update(atom.artifact_id.encode("utf-8"))
        digest.update(b"\0")
        digest.update(hashlib.sha256(atom.content).hexdigest().encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def _catalog_body(atoms: tuple[Atom, ...]) -> str:
    """Render stable scope headings with source IDs and titles only."""
    grouped: dict[str, list[Atom]] = {scope: [] for scope in CANONICAL_SCOPES}
    for atom in atoms:
        grouped[atom.subject_scope].append(atom)
    lines = ["# META Active Atom Catalog by Subject Scope", ""]
    for scope in CANONICAL_SCOPES:
        lines.extend((f"## `{scope}` ({len(grouped[scope])})", ""))
        lines.extend(
            f"- `{atom.artifact_id}` — {atom.title}" for atom in grouped[scope]
        )
        lines.append("")
    return "\n".join(lines)


def _catalog_bytes(atoms: tuple[Atom, ...]) -> bytes:
    """Render the complete GitHub-previewable Catalog carrier."""
    metadata = {
        "artifact_type": "catalog",
        "artifact_subtype": "requirement",
        "artifact_id": CATALOG_ID,
        "scope_path": "layer:meta",
        "subject_scope": "artifact-model",
        "generator": GENERATOR_ID,
        "generator_version": GENERATOR_VERSION,
        "source_count": len(atoms),
        "source_frontier_sha256": _frontier_digest(atoms),
        "relations": [
            {
                "type": "child_of",
                "targets": ["CARMADIO-REQUIREMENT-META-125"],
            }
        ],
    }
    return render_frontmatter(metadata, _catalog_body(atoms), format="yaml").encode(
        "utf-8"
    )


def _write_catalog(root: Path, expected: bytes) -> None:
    """Replace the Catalog atomically after staging its complete bytes."""
    target = root / CATALOG_RELATIVE
    runtime = _runtime_root(root)
    try:
        stage = runtime / "catalog.stage"
        stage.write_bytes(expected)
        _metadata(stage, stage.read_bytes())
        target.parent.mkdir(parents=True, exist_ok=True)
        os.replace(stage, target)
    finally:
        shutil.rmtree(runtime, ignore_errors=True)


def _run_migrate(root: Path, apply: bool, expected_digest: str | None) -> int:
    """Preview or apply the exact plural-to-singular migration plan."""
    changes = _migration_changes(root)
    digest = _print_plan(root, changes)
    if not apply:
        return 0
    if not expected_digest or expected_digest != digest:
        raise MetaScopeError("--apply requires the exact preview plan digest")
    _apply_changes(root, changes)
    if _migration_changes(root):
        raise MetaScopeError("migration did not converge to an empty plan")
    print("migration applied and verified")
    return 0


def _run_project(root: Path, write: bool, check: bool) -> int:
    """Preview, write, or verify the deterministic Catalog Projection."""
    atoms = _collect_atoms(root)
    expected = _catalog_bytes(atoms)
    target = root / CATALOG_RELATIVE
    current = target.read_bytes() if target.is_file() else None
    print(f"source-count: {len(atoms)}")
    print(f"output-sha256: {hashlib.sha256(expected).hexdigest()}")
    if check:
        if current != expected:
            raise MetaScopeError(f"Catalog Projection is missing or stale: {target}")
        print("Catalog Projection is current")
        return 0
    if write and current != expected:
        _write_catalog(root, expected)
        print(f"wrote {target.relative_to(root).as_posix()}")
    elif write:
        print("Catalog Projection already current")
    else:
        print("change-required: " + ("yes" if current != expected else "no"))
    return 0


def _parser() -> argparse.ArgumentParser:
    """Build the documented command-line contract."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPOSITORY_ROOT)
    parser.add_argument("--debug", action="store_true")
    commands = parser.add_subparsers(dest="command", required=True)
    migrate = commands.add_parser("migrate")
    migrate.add_argument("--apply", action="store_true")
    migrate.add_argument("--expect-plan-digest")
    project = commands.add_parser("project")
    mode = project.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    return parser


def main() -> int:
    """Run one bounded operation with verbose failure reporting."""
    args = _parser().parse_args()
    root = args.repo_root.resolve()
    try:
        if args.command == "migrate":
            return _run_migrate(root, args.apply, args.expect_plan_digest)
        return _run_project(root, args.write, args.check)
    except (MetaScopeError, OSError) as error:
        if args.debug:
            raise
        print(f"carmadio-meta-scope: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
