#!/usr/bin/env python3
"""Move CAPRMADIO carriers into the recursive eight-role directory layout.

Usage:
    python migrate_caprmadio_role_layout.py
    python migrate_caprmadio_role_layout.py --apply --expect-plan-digest SHA256
    python migrate_caprmadio_role_layout.py --check

Preview is the default. Apply is bound to the exact preview digest, stages
byte-identical destinations under the script-owned runtime directory, rejects
unknown carriers and collisions, and restores every source if publication or
postcondition verification fails. The migration changes paths only; governed
carrier bytes and filenames are preserved.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
from contextlib import suppress
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import tomllib

sys.dont_write_bytecode = True

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from dset_toolchain.frontmatter import FrontmatterError  # noqa: E402
from dset_toolchain.frontmatter import parse as parse_frontmatter  # noqa: E402

CAPRMADIO_ROOT = Path(".caprmadio")
RUNTIME_ROOT = Path(".caprmadio_runtime/migrate-caprmadio-role-layout")
METHODOLOGY_SOURCE = "000_caprmadio_methodology"
METHODOLOGY_TARGET = "000_CAPRMADIO_METHODOLOGY"
PROJECT_SOURCE = "100_project"
VERSIONS_SOURCE = "150_versions"
ROOT_FILES = {
    "CAPRMADIO-CONTROL-HUB.md",
    "artifact_catalog.toml",
    "caprmadio_settings.toml",
}
ROLE_DIRECTORIES = (
    "01_CONCERN",
    "02_ANALYSIS",
    "03_REQUIREMENT",
    "04_METHOD",
    "05_ASSURANCE",
    "06_DELIVERY",
    "07_IMPLEMENTATION",
    "08_OPS",
)
ROLE_BY_TYPE = {
    "concern": "01_CONCERN",
    "external_problem": "01_CONCERN",
    "conflict": "01_CONCERN",
    "problem": "01_CONCERN",
    "question": "01_CONCERN",
    "analysis": "02_ANALYSIS",
    "analysis_report": "02_ANALYSIS",
    "external_analysis_report": "02_ANALYSIS",
    "conflict_analysis": "02_ANALYSIS",
    "requirement": "03_REQUIREMENT",
    "constraint": "03_REQUIREMENT",
    "contract": "03_REQUIREMENT",
    "specification": "03_REQUIREMENT",
    "reference": "03_REQUIREMENT",
    "method": "04_METHOD",
    "implementation_methodology": "04_METHOD",
    "integration_decision": "04_METHOD",
    "implementation_decision": "04_METHOD",
    "decision": "04_METHOD",
    "assurance": "05_ASSURANCE",
    "assurance_standard": "05_ASSURANCE",
    "review_protocol": "05_ASSURANCE",
    "test_case": "05_ASSURANCE",
    "evaluation_case": "05_ASSURANCE",
    "test_plan": "05_ASSURANCE",
    "evaluation_plan": "05_ASSURANCE",
    "delivery": "06_DELIVERY",
    "development_backlog": "06_DELIVERY",
    "implementation": "07_IMPLEMENTATION",
    "external_git_commit": "07_IMPLEMENTATION",
    "pull_request": "07_IMPLEMENTATION",
    "implementation_journal": "07_IMPLEMENTATION",
    "ops": "08_OPS",
    "external_evidence_record": "08_OPS",
    "verification_record": "08_OPS",
    "evidence_record": "08_OPS",
    "verification": "08_OPS",
}
ROLE_BY_FAMILY = {
    "question": "01_CONCERN",
    "problem": "01_CONCERN",
    "analysis": "02_ANALYSIS",
    "decision": "04_METHOD",
    "qa": "05_ASSURANCE",
    "evidence": "08_OPS",
    "verification": "08_OPS",
    "references": "03_REQUIREMENT",
}
PROJECTION_TYPES = {"catalog", "map", "hub"}
PROJECTION_ROLES = {
    "concern": "01_CONCERN",
    "analysis": "02_ANALYSIS",
    "requirement": "03_REQUIREMENT",
    "method": "04_METHOD",
    "assurance": "05_ASSURANCE",
    "delivery": "06_DELIVERY",
    "implementation": "07_IMPLEMENTATION",
    "ops": "08_OPS",
}
ROLE_BY_CONTENT_ROLE = {
    "inquiry": "01_CONCERN",
    "concern": "01_CONCERN",
    "rationale": "02_ANALYSIS",
    "analysis": "02_ANALYSIS",
    "definition": "03_REQUIREMENT",
    "requirement": "03_REQUIREMENT",
    "method": "04_METHOD",
    "assurance": "05_ASSURANCE",
    "delivery": "06_DELIVERY",
    "implementation": "07_IMPLEMENTATION",
    "observation": "08_OPS",
    "ops": "08_OPS",
}
DELIVERY_VERSION_SUBTYPES = {"version_scope", "roadmap", "release_plan"}
ASSURANCE_VERSION_SUBTYPES = {"readiness_record"}
OPS_VERSION_SUBTYPES = {"release_record"}
LIFECYCLE_DIRECTORIES = {"archive", "drafts"}


class RoleLayoutError(RuntimeError):
    """The role-layout migration cannot proceed safely."""


@dataclass(frozen=True)
class Move:
    """One byte-preserving carrier move."""

    source: Path
    target: Path
    sha256: str


@dataclass(frozen=True)
class Plan:
    """One complete deterministic migration plan."""

    moves: tuple[Move, ...]
    trash: tuple[tuple[Path, str], ...]
    rename_methodology: bool


def _digest(content: bytes) -> str:
    """Return one lowercase SHA-256 digest."""
    return hashlib.sha256(content).hexdigest()


def _regular_bytes(path: Path) -> bytes:
    """Read a regular non-symlink file or stop."""
    if path.is_symlink() or not path.is_file():
        raise RoleLayoutError(f"carrier is not a regular file: {path}")
    return path.read_bytes()


def _metadata(path: Path, content: bytes) -> dict[str, Any]:
    """Read supported Markdown or TOML metadata without changing bytes."""
    if path.suffix.lower() == ".md":
        try:
            parsed = parse_frontmatter(content.decode("utf-8"))
        except (UnicodeError, FrontmatterError) as error:
            message = f"invalid Markdown carrier: {path}: {error}"
            raise RoleLayoutError(message) from error
        return {} if parsed is None else parsed[0]
    if path.suffix.lower() == ".toml":
        try:
            return tomllib.loads(content.decode("utf-8"))
        except (UnicodeError, tomllib.TOMLDecodeError) as error:
            raise RoleLayoutError(f"invalid TOML carrier: {path}: {error}") from error
    return {}


def _role_for_version(subtype: str | None, path: Path) -> str:
    """Classify one legacy Version carrier by its direct subtype."""
    if subtype in DELIVERY_VERSION_SUBTYPES:
        return "06_DELIVERY"
    if subtype in ASSURANCE_VERSION_SUBTYPES:
        return "05_ASSURANCE"
    if subtype in OPS_VERSION_SUBTYPES:
        return "08_OPS"
    raise RoleLayoutError(f"unknown Version subtype in {path}: {subtype!r}")


def _role_for_plan(subtype: str | None, path: Path) -> str:
    """Classify one legacy Plan carrier without treating plan as a role."""
    if subtype in {"test_plan", "evaluation_plan", "verification_plan"}:
        return "05_ASSURANCE"
    if subtype in {"implementation_plan", "work_plan"}:
        return "04_METHOD"
    if subtype == "release_plan":
        return "06_DELIVERY"
    return _role_from_name(path)


def _role_for_projection(subtype: str | None, path: Path) -> str:
    """Derive a Projection's role from its mandatory direct subtype."""
    role = PROJECTION_ROLES.get(subtype or "")
    if role is None:
        raise RoleLayoutError(f"unknown Projection role subtype in {path}: {subtype!r}")
    return role


def _role_from_metadata(metadata: dict[str, Any], path: Path) -> str | None:
    """Return a role from an explicitly governed artifact Type."""
    artifact_type = metadata.get("artifact_type")
    subtype = metadata.get("artifact_subtype")
    if artifact_type is not None and not isinstance(artifact_type, str):
        raise RoleLayoutError(f"invalid artifact_type in {path}: {artifact_type!r}")
    if subtype is not None and not isinstance(subtype, str):
        raise RoleLayoutError(f"invalid artifact_subtype in {path}: {subtype!r}")
    if artifact_type == "version":
        return _role_for_version(subtype, path)
    if artifact_type == "plan":
        return _role_for_plan(subtype, path)
    if artifact_type in PROJECTION_TYPES:
        return _role_for_projection(subtype, path)
    return ROLE_BY_TYPE.get(artifact_type or "")


def _role_from_legacy_content(metadata: dict[str, Any], path: Path) -> str | None:
    """Route a pre-CAPRMADIO Type through its historical Content role."""
    content_role = metadata.get("content_role")
    if content_role is not None and not isinstance(content_role, str):
        raise RoleLayoutError(f"invalid content_role in {path}: {content_role!r}")
    return ROLE_BY_CONTENT_ROLE.get(content_role or "")


def _role_from_semantic_name(path: Path) -> str | None:
    """Return a role encoded by an explicit semantic Type token."""
    name = path.name.lower()
    concern_tokens = (
        "-question-",
        "-problem-",
        "-concern-",
        "-conflict-",
        "-defect-",
        "-gap-",
        "-debt-",
        "-opportunity-",
        "-risk-",
    )
    analysis_tokens = ("-analysis-report-", "-analysis-", "-anrp-")
    requirement_tokens = ("-requirement-", "-constraint-", "-contract-")
    method_tokens = ("-decision-", "-idec-", "-method-")
    assurance_tokens = (
        "-test-case-",
        "-evaluation-case-",
        "-qa-case-",
        "-assurance-",
    )
    ops_tokens = ("-evidence-record-", "-verification-record-", "-ops-")
    if any(token in name for token in concern_tokens):
        return "01_CONCERN"
    if any(token in name for token in requirement_tokens):
        return "03_REQUIREMENT"
    if any(token in name for token in analysis_tokens):
        return "02_ANALYSIS"
    if any(token in name for token in method_tokens):
        return "04_METHOD"
    if any(token in name for token in assurance_tokens):
        return "05_ASSURANCE"
    if any(token in name for token in ops_tokens):
        return "08_OPS"
    return None


def _role_from_name(path: Path) -> str:
    """Use narrow legacy filename fallbacks for carriers without a route."""
    semantic_role = _role_from_semantic_name(path)
    if semantic_role is not None:
        return semantic_role
    name = path.name.lower()
    if "external-review-packet" in name:
        return "02_ANALYSIS"
    if "plan-evaluation" in name or "plan-test" in name or "plan-verification" in name:
        return "05_ASSURANCE"
    if "plan-implementation" in name or "plan-work" in name:
        return "04_METHOD"
    if "specification" in name:
        return "03_REQUIREMENT"
    if "analysis" in name:
        return "02_ANALYSIS"
    if "evidence" in name or "verification" in name:
        return "08_OPS"
    if "version" in name or "roadmap" in name or "release" in name:
        return "06_DELIVERY"
    if "hub" in name:
        return "03_REQUIREMENT"
    if "ijrn" in name or "implementation-journal" in name:
        return "07_IMPLEMENTATION"
    raise RoleLayoutError(f"cannot infer Content role for carrier: {path}")


def _legacy_family(relative: Path) -> str | None:
    """Return the nearest recognized legacy family directory."""
    for part in relative.parts[:-1]:
        if part in ROLE_BY_FAMILY:
            return part
    return None


def _role_for(relative: Path, content: bytes, current_role: str | None) -> str:
    """Classify one carrier, preferring governed metadata over legacy paths."""
    metadata = _metadata(relative, content)
    role = _role_from_metadata(metadata, relative)
    if role is not None:
        return role
    role = _role_from_semantic_name(relative)
    if role is not None:
        return role
    if current_role is not None:
        return current_role
    try:
        return _role_from_name(relative)
    except RoleLayoutError:
        pass
    role = _role_from_legacy_content(metadata, relative)
    if role is not None:
        return role
    family = _legacy_family(relative)
    if family is not None:
        return ROLE_BY_FAMILY[family]
    raise RoleLayoutError(f"cannot infer Content role for carrier: {relative}")


def _lifecycle(relative: Path) -> str | None:
    """Preserve one existing active, draft, or archived placement."""
    found = [part for part in relative.parts[:-1] if part in LIFECYCLE_DIRECTORIES]
    if len(found) > 1:
        raise RoleLayoutError(f"multiple lifecycle directories in {relative}")
    if found:
        return found[0]
    if _legacy_family(relative) == "references":
        return "archive"
    return None


def _scope_and_relative(caprmadio: Path, path: Path) -> tuple[Path, Path]:
    """Resolve the target structural scope and source-relative route."""
    relative = path.relative_to(caprmadio)
    first = relative.parts[0]
    if first in {PROJECT_SOURCE, VERSIONS_SOURCE}:
        return caprmadio, Path(*relative.parts[1:])
    if first in ROLE_DIRECTORIES:
        return caprmadio, Path(*relative.parts[1:])
    if first[:3].isdigit() and "_layer_" in first:
        scope = caprmadio / first
        scoped_relative = Path(*relative.parts[1:])
        if scoped_relative.parts and scoped_relative.parts[0] in ROLE_DIRECTORIES:
            scoped_relative = Path(*scoped_relative.parts[1:])
        return scope, scoped_relative
    raise RoleLayoutError(f"unknown structural scope for carrier: {relative}")


def _current_role(caprmadio: Path, source: Path) -> str | None:
    """Return the role directory already containing one carrier, if any."""
    parts = source.relative_to(caprmadio).parts
    if parts[0] in ROLE_DIRECTORIES:
        return parts[0]
    if len(parts) > 1 and parts[1] in ROLE_DIRECTORIES:
        return parts[1]
    return None


def _target_for(caprmadio: Path, source: Path, content: bytes) -> Path:
    """Return one canonical target while preserving filename and lifecycle."""
    scope, relative = _scope_and_relative(caprmadio, source)
    role = _role_for(relative, content, _current_role(caprmadio, source))
    lifecycle = _lifecycle(relative)
    parent = scope / role
    if lifecycle is not None:
        parent /= lifecycle
    return parent / source.name


def _methodology_state(caprmadio: Path) -> bool:
    """Validate and return whether the reserved methodology boundary needs rename."""
    matches = [
        path
        for path in caprmadio.iterdir()
        if path.name.casefold() == METHODOLOGY_TARGET.casefold()
    ]
    if len(matches) != 1:
        raise RoleLayoutError("installed methodology boundary is missing or ambiguous")
    selected = matches[0]
    if selected.is_symlink() or not selected.is_dir():
        raise RoleLayoutError(f"installed methodology boundary is invalid: {selected}")
    if selected.name not in {METHODOLOGY_SOURCE, METHODOLOGY_TARGET}:
        raise RoleLayoutError(f"unknown methodology boundary spelling: {selected.name}")
    return selected.name == METHODOLOGY_SOURCE


def _inventory(caprmadio: Path) -> tuple[tuple[Path, ...], tuple[Path, ...]]:
    """Return candidate carriers and disposable Finder metadata."""
    files: list[Path] = []
    trash: list[Path] = []
    excluded = {METHODOLOGY_SOURCE, METHODOLOGY_TARGET}
    for path in sorted(caprmadio.rglob("*")):
        relative = path.relative_to(caprmadio)
        if relative.parts[0] in excluded:
            continue
        if path.is_dir():
            continue
        if path.name == ".DS_Store":
            trash.append(path)
            continue
        if len(relative.parts) == 1 and path.name in ROOT_FILES:
            continue
        files.append(path)
    return tuple(files), tuple(trash)


def _validate_targets(moves: tuple[Move, ...]) -> None:
    """Reject duplicate or occupied target paths before publication."""
    owners: dict[Path, Path] = {}
    sources = {move.source for move in moves}
    for move in moves:
        owner = owners.setdefault(move.target, move.source)
        if owner != move.source:
            message = f"target collision: {owner} and {move.source} -> {move.target}"
            raise RoleLayoutError(message)
        if move.target.exists() and move.target not in sources:
            raise RoleLayoutError(f"target already exists: {move.target}")


def _build_plan(root: Path) -> Plan:
    """Build a complete byte-bound collision-free move plan."""
    caprmadio = root / CAPRMADIO_ROOT
    if caprmadio.is_symlink() or not caprmadio.is_dir():
        raise RoleLayoutError(f"invalid CAPRMADIO root: {caprmadio}")
    carriers, trash_paths = _inventory(caprmadio)
    moves: list[Move] = []
    for source in carriers:
        content = _regular_bytes(source)
        target = _target_for(caprmadio, source, content)
        if source != target:
            moves.append(Move(source, target, _digest(content)))
    ordered = tuple(sorted(moves, key=lambda item: item.source.as_posix()))
    _validate_targets(ordered)
    trash = tuple((path, _digest(_regular_bytes(path))) for path in trash_paths)
    return Plan(ordered, trash, _methodology_state(caprmadio))


def _plan_payload(root: Path, plan: Plan) -> dict[str, Any]:
    """Render the stable repository-relative plan payload."""

    def relative(path: Path) -> str:
        return path.relative_to(root).as_posix()

    return {
        "moves": [
            {
                "source": relative(move.source),
                "target": relative(move.target),
                "sha256": move.sha256,
            }
            for move in plan.moves
        ],
        "trash": [
            {"path": relative(path), "sha256": digest} for path, digest in plan.trash
        ],
        "rename_methodology": plan.rename_methodology,
    }


def _plan_digest(root: Path, plan: Plan) -> str:
    """Bind every planned source, target, and preimage."""
    encoded = json.dumps(
        _plan_payload(root, plan), sort_keys=True, separators=(",", ":")
    )
    return _digest(encoded.encode("utf-8"))


def _print_plan(root: Path, plan: Plan) -> str:
    """Print the stable plan and return its digest."""
    payload = _plan_payload(root, plan)
    digest = _plan_digest(root, plan)
    print(json.dumps(payload, indent=2, sort_keys=True))
    print(f"moves: {len(plan.moves)}")
    print(f"trash: {len(plan.trash)}")
    print(f"plan-digest: {digest}")
    return digest


def _verify_preimages(plan: Plan) -> None:
    """Reject any source change since preview."""
    for move in plan.moves:
        if _digest(_regular_bytes(move.source)) != move.sha256:
            raise RoleLayoutError(f"source changed after preview: {move.source}")
    for path, digest in plan.trash:
        if _digest(_regular_bytes(path)) != digest:
            raise RoleLayoutError(f"trash preimage changed after preview: {path}")


def _stage_moves(
    runtime: Path, root: Path, plan: Plan
) -> tuple[tuple[Move, Path], ...]:
    """Stage and verify one byte-identical copy for every target."""
    staged: list[tuple[Move, Path]] = []
    for move in plan.moves:
        target = runtime / "staged" / move.target.relative_to(root)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(move.source, target)
        if _digest(_regular_bytes(target)) != move.sha256:
            raise RoleLayoutError(f"staged target digest mismatch: {move.target}")
        staged.append((move, target))
    return tuple(staged)


def _publish_staged(staged: tuple[tuple[Move, Path], ...]) -> list[Move]:
    """Publish all staged destinations without deleting sources."""
    published: list[Move] = []
    for move, stage in staged:
        move.target.parent.mkdir(parents=True, exist_ok=True)
        os.replace(stage, move.target)
        published.append(move)
    return published


def _retain_sources(runtime: Path, root: Path, plan: Plan) -> list[tuple[Path, Path]]:
    """Move every source and trash file into the rollback area."""
    retained: list[tuple[Path, Path]] = []
    sources = [move.source for move in plan.moves]
    sources.extend(item[0] for item in plan.trash)
    for source in sources:
        backup = runtime / "originals" / source.relative_to(root)
        backup.parent.mkdir(parents=True, exist_ok=True)
        os.replace(source, backup)
        retained.append((source, backup))
    return retained


def _rename_methodology(root: Path, plan: Plan) -> tuple[Path, Path] | None:
    """Rename the reserved installed-methodology boundary when required."""
    if not plan.rename_methodology:
        return None
    source = root / CAPRMADIO_ROOT / METHODOLOGY_SOURCE
    target = root / CAPRMADIO_ROOT / METHODOLOGY_TARGET
    temporary = root / CAPRMADIO_ROOT / ".methodology-case-migration"
    os.replace(source, temporary)
    os.replace(temporary, target)
    return source, target


def _rollback(
    published: list[Move],
    retained: list[tuple[Path, Path]],
    renamed: tuple[Path, Path] | None,
) -> None:
    """Restore every original path after a failed apply."""
    if renamed is not None and renamed[1].exists():
        temporary = renamed[0].parent / ".methodology-case-rollback"
        os.replace(renamed[1], temporary)
        os.replace(temporary, renamed[0])
    for source, backup in reversed(retained):
        source.parent.mkdir(parents=True, exist_ok=True)
        if backup.exists():
            os.replace(backup, source)
    for move in reversed(published):
        if move.target.exists():
            move.target.unlink()


def _remove_empty_directories(caprmadio: Path) -> None:
    """Remove empty legacy containers after a verified migration."""
    directories = (item for item in caprmadio.rglob("*") if item.is_dir())
    for path in sorted(directories, reverse=True):
        if METHODOLOGY_TARGET in path.relative_to(caprmadio).parts:
            continue
        with suppress(OSError):
            path.rmdir()


def _apply(root: Path, plan: Plan) -> None:
    """Apply one exact plan transactionally and verify convergence."""
    runtime = root / RUNTIME_ROOT
    if runtime.exists():
        raise RoleLayoutError(f"runtime folder already exists: {runtime}")
    published: list[Move] = []
    retained: list[tuple[Path, Path]] = []
    renamed: tuple[Path, Path] | None = None
    try:
        _verify_preimages(plan)
        staged = _stage_moves(runtime, root, plan)
        published = _publish_staged(staged)
        retained = _retain_sources(runtime, root, plan)
        renamed = _rename_methodology(root, plan)
        remaining = _build_plan(root)
        if remaining.moves or remaining.trash or remaining.rename_methodology:
            raise RoleLayoutError("migration did not converge to an empty plan")
        _remove_empty_directories(root / CAPRMADIO_ROOT)
    except Exception:
        _rollback(published, retained, renamed)
        raise
    finally:
        shutil.rmtree(runtime, ignore_errors=True)


def _parser() -> argparse.ArgumentParser:
    """Build the documented command-line contract."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPOSITORY_ROOT)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--expect-plan-digest")
    return parser


def main() -> int:
    """Preview, apply, or verify the recursive role-layout migration."""
    args = _parser().parse_args()
    if args.apply and args.check:
        print("--apply and --check are mutually exclusive", file=sys.stderr)
        return 2
    root = args.repo_root.resolve()
    try:
        plan = _build_plan(root)
        digest = _print_plan(root, plan)
        if args.check and (plan.moves or plan.trash or plan.rename_methodology):
            raise RoleLayoutError("role-layout migration is incomplete")
        if args.apply:
            if args.expect_plan_digest != digest:
                raise RoleLayoutError("--apply requires the exact preview plan digest")
            _apply(root, plan)
            print("migration applied and verified")
        elif args.check:
            print("role layout is current")
        return 0
    except (OSError, RoleLayoutError) as error:
        print(f"caprmadio-role-layout: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
