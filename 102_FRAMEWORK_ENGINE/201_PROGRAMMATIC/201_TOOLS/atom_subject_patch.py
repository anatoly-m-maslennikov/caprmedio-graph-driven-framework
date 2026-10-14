"""Mutation-free, byte-preserving previews for explicit Atom Subject patches.

The public entry point deliberately has no apply path.  It is kept outside the
generic update implementation so the latter can route the exclusive input mode
without giving this small adapter any publication, history, or Journal powers.
"""

from __future__ import annotations

import errno
import hashlib
import json
import os
import re
import stat
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping, Sequence

import yaml
from yaml.nodes import MappingNode, Node, ScalarNode, SequenceNode

from subject_notation import SubjectNotationError, get_profile, parse_subject, profile_evidence
from VALIDATE_ATOMS.validate_atoms_workers.read_io import LimitReached, ReadContext
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS


_SHA256 = re.compile(r"[0-9a-f]{64}")
_TIMESTAMP = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} [+-]\d{4}")
_YAML_STRING = "tag:yaml.org,2002:str"
_TARGET_FIELDS = frozenset({
    "atom_id", "path", "filename", "version", "digest", "lifecycle", "status",
    "updated_at", "content_role", "type",
})
_INTENT_FIELDS = frozenset({
    "schema_version", "target", "subject_profile", "subject_profile_evidence",
    "subject_patches", "proposal", "execution_metadata", "predecessorArchive", "noop",
})


@dataclass(frozen=True)
class _Span:
    start: int
    end: int


@dataclass(frozen=True)
class _Replacement:
    span: _Span
    value: str


@dataclass(frozen=True)
class _SourceSnapshot:
    """One no-follow source read and the file identity that supplied it."""

    path: Path
    raw: bytes
    fingerprint: tuple[int, int, int, int, int]


def preview_subject_patches(
    root: Path,
    items: list[object],
    *,
    timestamp: str | None = None,
    subject_profile: str = "legacy",
) -> dict[str, Any]:
    """Prepare a sealed-in-memory preview of explicit Subject replacements.

    ``items`` uses only the Subject-only ATOM_UPDATE payload shape.  The module
    imports :mod:`atom_operations` lazily because the generic updater imports
    this preview helper when it detects that exclusive mode.
    """

    operations = _operations()
    try:
        profile = get_profile(subject_profile)
        profile_name = profile.name
        evidence = profile_evidence(profile_name)
    except SubjectNotationError as error:
        _fail(operations, error.code, str(error))
    project_root = Path(root).resolve()
    if not isinstance(items, list) or not items:
        _fail(operations, "subject-patches-required", "subject patch preview requires a non-empty atoms list")
    if timestamp is not None:
        _require_timestamp(operations, timestamp)
    grammar = _capture_grammar(operations, project_root, profile)
    identity_layout = _capture_identity_layout(operations, project_root)

    planned: list[dict[str, Any]] = []
    selectors: set[str] = set()
    atom_ids: set[str] = set()
    has_change = False

    # Validate every precondition before resolving an illustrative time.  This
    # keeps an invalid request from looking like an accepted preview.
    for ordinal, item in enumerate(items):
        result = _plan_item(
            operations,
            project_root,
            item,
            ordinal,
            selectors,
            atom_ids,
            profile_name,
        )
        if identity_layout is not None and result["path"].is_relative_to(identity_layout[0]):
            _fail(operations, "subject-selector-delivered", "Subject selector cannot address an installed source copy")
        planned.append(result)
        has_change = has_change or not result["noop"]

    for item in planned:
        _assert_snapshot_current(operations, project_root, item["snapshot"], item["selector"])
    _assert_original_identity_unique(operations, project_root, atom_ids, identity_layout)
    illustrative_at = _preview_timestamp(operations, project_root, timestamp) if has_change else None
    atoms: list[dict[str, Any]] = []
    for item in planned:
        atom = _materialize_item(operations, project_root, item, illustrative_at)
        prepared = _intent_from_plan(operations, project_root, item, profile_name, evidence)
        atom["subject_intent"] = prepared["subject_intent"]
        atom["subject_intent_sha256"] = prepared["subject_intent_sha256"]
        atoms.append(atom)
    for item in planned:
        _assert_snapshot_current(operations, project_root, item["snapshot"], item["selector"])
    _assert_original_identity_unique(operations, project_root, atom_ids, identity_layout)
    _assert_grammar_current(operations, project_root, grammar)
    _assert_identity_layout_current(operations, project_root, identity_layout)

    preview: dict[str, Any] = {
        "count": len(atoms),
        "atoms": atoms,
        "noop": not has_change,
        "illustrative_updated_at": illustrative_at,
        "subject_profile": profile_name,
        "subject_profile_evidence": evidence,
    }
    preview["preview_sha256"] = hashlib.sha256(
        operations.canonical_json(preview).encode("utf-8")
    ).hexdigest()
    return preview


def prepare_subject_intent(
    root: Path,
    target_descriptor: Mapping[str, Any],
    subject_patches: list[object],
    *,
    subject_profile: str = "legacy",
) -> dict[str, Any]:
    """Prepare one deterministic Subject intent without future effect metadata."""

    operations = _operations()
    if not isinstance(target_descriptor, Mapping) or set(target_descriptor) != _TARGET_FIELDS:
        _fail(operations, "subject-target-invalid", "Subject target must contain exactly its complete carrier descriptor")
    try:
        profile = get_profile(subject_profile)
        evidence = profile_evidence(profile.name)
    except SubjectNotationError as error:
        _fail(operations, error.code, str(error))
    project_root = Path(root).resolve()
    grammar = _capture_grammar(operations, project_root, profile)
    identity_layout = _capture_identity_layout(operations, project_root)
    plan = _plan_item(operations, project_root, {
        "selector": target_descriptor["path"],
        "expected": {
            "atom_id": target_descriptor["atom_id"], "version": target_descriptor["version"],
            "sha256": target_descriptor["digest"],
        },
        "subject_patches": subject_patches,
    }, 0, set(), set(), profile.name)
    if identity_layout is not None and plan["path"].is_relative_to(identity_layout[0]):
        _fail(operations, "subject-selector-delivered", "Subject selector cannot address an installed source copy")
    prepared = _intent_from_plan(operations, project_root, plan, profile.name, evidence)
    if _canonical(operations, dict(target_descriptor)) != _canonical(operations, prepared["subject_intent"]["target"]):
        _fail(operations, "subject-target-stale", "Subject target descriptor does not match the captured carrier")
    _validate_complete(operations, project_root, plan["path"], prepared["proposed"]["frontmatter"], prepared["proposed"]["content"])
    _assert_snapshot_current(operations, project_root, plan["snapshot"], plan["selector"])
    _assert_original_identity_unique(operations, project_root, {plan["atom_id"]}, identity_layout)
    _assert_grammar_current(operations, project_root, grammar)
    _assert_identity_layout_current(operations, project_root, identity_layout)
    plan["grammar_snapshots"] = grammar
    plan["identity_layout"] = identity_layout
    return prepared


def materialize_subject_intent(
    root: Path,
    prepared: Mapping[str, Any],
    actual_updated_at: str | None,
) -> dict[str, Any]:
    """Recheck a prepared intent and return bytes; this function never publishes."""

    operations = _operations()
    if not isinstance(prepared, Mapping) or set(prepared) != {
        "subject_intent", "subject_intent_sha256", "intended_carrier", "proposed", "_plan",
    }:
        _fail(operations, "subject-intent-invalid", "prepared Subject intent has unsupported or missing fields")
    intent = prepared["subject_intent"]
    if not isinstance(intent, Mapping) or set(intent) != _INTENT_FIELDS:
        _fail(operations, "subject-intent-invalid", "Subject intent has unsupported or missing fields")
    fresh = prepare_subject_intent(
        root, intent["target"], intent["subject_patches"], subject_profile=intent["subject_profile"],
    )
    if _canonical(operations, dict(intent)) != _canonical(operations, fresh["subject_intent"]):
        _fail(operations, "subject-intent-stale", "Subject intent differs from its freshly derived intent")
    if prepared["subject_intent_sha256"] != fresh["subject_intent_sha256"]:
        _fail(operations, "subject-intent-hash-mismatch", "Subject intent hash does not match its freshly derived intent")
    if (prepared["intended_carrier"] != fresh["intended_carrier"]
            or _canonical(operations, prepared["proposed"]) != _canonical(operations, fresh["proposed"])):
        _fail(operations, "subject-intent-stale", "Subject proposal differs from its freshly derived carrier")
    plan = fresh["_plan"]
    if not plan["noop"]:
        _require_timestamp(operations, actual_updated_at)
    project_root = Path(root).resolve()
    materialized = _materialize_item(operations, project_root, plan, actual_updated_at)
    _assert_snapshot_current(operations, project_root, plan["snapshot"], plan["selector"])
    _assert_original_identity_unique(operations, project_root, {plan["atom_id"]}, plan["identity_layout"])
    _assert_grammar_current(operations, project_root, plan["grammar_snapshots"])
    _assert_identity_layout_current(operations, project_root, plan["identity_layout"])
    return {
        "carrier_bytes": materialized["proposed_carrier"].encode("utf-8"),
        "materialization": {
            "version": materialized["after_version"],
            "updated_at": fresh["subject_intent"]["target"]["updated_at"] if plan["noop"] else actual_updated_at,
            "after_sha256": materialized["after_sha256"],
        },
    }


def _canonical(operations: Any, value: object) -> str:
    try:
        return operations.canonical_json(value)
    except (TypeError, ValueError) as error:
        raise operations.ToolError("subject-intent-invalid", "Subject intent must be canonical JSON data") from error


def _intent_from_plan(operations: Any, root: Path, plan: dict[str, Any], profile_name: str, evidence: dict[str, Any]) -> dict[str, Any]:
    _ensure_non_overlapping(operations, plan["subject_replacements"])
    frontmatter = _apply_replacements(plan["frontmatter"], plan["subject_replacements"])
    intended = _replace_frontmatter(plan["text"], plan["frontmatter"], frontmatter)
    target = {
        "atom_id": plan["atom_id"], "path": plan["selector"], "filename": plan["path"].name,
        "version": plan["version"], "digest": plan["before_sha256"],
        "lifecycle": operations._lifecycle(plan["path"], operations.control_root(root)),
        **{field: operations.frontmatter_scalar(plan["frontmatter"], field)
           for field in ("status", "updated_at", "content_role", "type")},
    }
    patches = [{key: patch[key] for key in ("field", "operation", "old", "new") if key in patch}
               for patch in plan["patches"]]
    predecessor = None
    if not plan["noop"]:
        role = next(parent for parent in plan["path"].parents if operations.ROLE_DIRECTORY.fullmatch(parent.name))
        archive = role / "archive" / f'{plan["path"].stem}@{plan["version"]}{plan["path"].suffix}'
        predecessor = {
            "atom_id": plan["atom_id"], "version": plan["version"],
            "path": archive.relative_to(root).as_posix(), "sha256": plan["before_sha256"], "lifecycle": "archived",
        }
    intent = {
        "schema_version": 1, "target": target, "subject_profile": profile_name,
        "subject_profile_evidence": evidence, "subject_patches": patches,
        "proposal": {
            "frontmatter_digest": hashlib.sha256(frontmatter.encode("utf-8")).hexdigest(),
            "content_digest": hashlib.sha256(plan["body"].encode("utf-8")).hexdigest(),
            "sha256": hashlib.sha256(intended.encode("utf-8")).hexdigest(),
        },
        "execution_metadata": {
            "version": plan["version"] if plan["noop"] else plan["version"] + 1,
            "updated_at": "preserve" if plan["noop"] else "actual_effect_time",
        },
        "predecessorArchive": predecessor, "noop": plan["noop"],
    }
    return {
        "subject_intent": intent,
        "subject_intent_sha256": hashlib.sha256(_canonical(operations, intent).encode("utf-8")).hexdigest(),
        "intended_carrier": intended, "proposed": {"frontmatter": frontmatter, "content": plan["body"]}, "_plan": plan,
    }


def _capture_grammar(operations: Any, root: Path, profile: Any) -> tuple[_SourceSnapshot, ...]:
    snapshots: list[_SourceSnapshot] = []
    for pin in profile.grammar_pins:
        try:
            snapshot = _read_source_snapshot(operations, root, root / pin.path, pin.path)
            metadata = operations.parse_carrier(snapshot.raw, Path(pin.path)).metadata
        except (operations.ToolError, operations.CarrierError) as error:
            code = "subject-grammar-pin-symlink" if getattr(error, "code", None) == "subject-selector-symlink" else "subject-grammar-pin-stale"
            raise operations.ToolError(code, "Subject grammar source cannot be bound to its declared pin") from error
        if (hashlib.sha256(snapshot.raw).hexdigest() != pin.sha256
                or metadata.get("atom_id") != pin.atom_id or type(metadata.get("version")) is not int
                or metadata["version"] != pin.version):
            _fail(operations, "subject-grammar-pin-stale", "Subject grammar source differs from its declared pin", {"path": pin.path})
        snapshots.append(snapshot)
    return tuple(snapshots)


def _assert_grammar_current(operations: Any, root: Path, snapshots: Sequence[_SourceSnapshot]) -> None:
    for snapshot in snapshots:
        try:
            _assert_snapshot_current(operations, root, snapshot, snapshot.path.relative_to(root).as_posix())
        except operations.ToolError as error:
            code = "subject-grammar-pin-symlink" if error.code == "subject-selector-symlink" else "subject-grammar-pin-stale"
            raise operations.ToolError(code, "Subject grammar source changed after intent preparation") from error


def _capture_identity_layout(operations: Any, root: Path) -> tuple[Path, tuple[_SourceSnapshot, ...]] | None:
    """Only a verified release layout distinguishes installed source copies."""

    from COMPILE_APPLICABLE_METHODOLOGY.compile_applicable_methodology import CompileError
    from RELEASE_VERSION.methodology_layout import resolve_methodology_layout

    registry = operations.control_root(root) / "project_structure.toml"
    try:
        snapshots = tuple(_read_source_snapshot(operations, root, path, path.relative_to(root).as_posix())
                          for path in (root / operations.SETTINGS_PATH, registry))
    except operations.ToolError as error:
        if error.code == "subject-selector-missing":
            return None
        raise
    try:
        layout = resolve_methodology_layout(root)
    except (CompileError, OSError, UnicodeError, ValueError):
        return None  # No release-layout exemption in ordinary or unverifiable Projects.
    for snapshot in snapshots:
        _assert_snapshot_current(operations, root, snapshot, snapshot.path.relative_to(root).as_posix())
    if (root / layout.control_root != operations.control_root(root)
            or hashlib.sha256(snapshots[1].raw).hexdigest() != layout.structure_sha256):
        _fail(operations, "subject-source-changed", "Project release layout changed while it was resolved")
    copied = root / layout.installed_root / Path(layout.source_copy_root).name
    return copied, snapshots


def _assert_identity_layout_current(
    operations: Any, root: Path, layout: tuple[Path, tuple[_SourceSnapshot, ...]] | None,
) -> None:
    if layout is None:
        return
    copied, snapshots = layout
    for snapshot in snapshots:
        _assert_snapshot_current(operations, root, snapshot, snapshot.path.relative_to(root).as_posix())
    if any(path.is_symlink() for path in (copied, *copied.parents)):
        _fail(operations, "subject-identity-inventory-unavailable", "installed source-copy place traverses a symlink")


def _assert_original_identity_unique(
    operations: Any, root: Path, atom_ids: set[str],
    layout: tuple[Path, tuple[_SourceSnapshot, ...]] | None,
) -> None:
    """Reject competing current identity claims, including outside the payload."""

    control = operations.control_root(root)
    _assert_identity_layout_current(operations, root, layout)
    reader = ReadContext(roots=[str(root)], limits=dict(CEILINGS))
    matches: dict[str, list[str]] = {atom_id: [] for atom_id in atom_ids}

    def candidates() -> tuple[Path, ...]:
        found: list[Path] = []
        for path in reader.inventory(control, remember=False):
            if ("_projection" in path.relative_to(control).parts
                    or operations._lifecycle(path, control) in {"draft", "archived"}):
                continue
            role = operations._role_directory(path, control)
            if path.is_symlink() and (operations.ROLE_DIRECTORY.fullmatch(path.name) or (role and path.is_dir())):
                _fail(operations, "subject-identity-inventory-unavailable", "an original role directory is a symlink")
            if role is None:
                continue
            if path.suffix.lower() == ".md":
                found.append(path)
        return tuple(found)

    try:
        paths_before = candidates()
        for path in paths_before:
            filename = operations.ATOM_ID.search(path.name)
            filename_id = filename.group(1) if filename else None
            if path.is_symlink():
                if filename_id in atom_ids:
                    _fail(operations, "subject-identity-inventory-unavailable", "a selected identity has an unsupported original source")
                continue
            raw = reader.read(path)
            try:
                metadata = operations.parse_carrier(raw, path).metadata
            except operations.CarrierError:
                normalized = raw.replace(b"\r\n", b"\n")
                header = (normalized.split(b"\n---\n", 1)[0] if normalized.startswith(b"---\n") else b"").decode("utf-8", errors="replace")
                claims = re.findall(r"(?m)^(?:atom_id|\"atom_id\"|'atom_id')\s*:\s*([^\n]*)$", header)
                identities = []
                for claim in claims:
                    try:
                        identities.append(yaml.safe_load(claim))
                    except yaml.YAMLError:
                        continue  # Malformed unrelated C/A does not establish a selected identity claim.
                if (filename_id in atom_ids or any(value in atom_ids for value in identities if isinstance(value, str))
                        or any(re.search(r"(?<![A-Za-z0-9_-])" + re.escape(atom_id) + r"(?![A-Za-z0-9_-])", header) for atom_id in atom_ids)):
                    _fail(operations, "subject-identity-inventory-unavailable", "a selected identity has a malformed original source")
                continue
            if "projection" in metadata:
                continue
            status = metadata.get("status")
            if isinstance(status, str) and status.casefold() in {"draft", "archived"}:
                continue
            atom_id = metadata.get("atom_id")
            if filename_id in atom_ids and atom_id != filename_id:
                _fail(operations, "subject-identity-inventory-unavailable", "a selected identity has an ambiguous original source")
            if isinstance(atom_id, str) and atom_id in atom_ids:
                if not isinstance(status, str) or not status:
                    _fail(operations, "subject-identity-inventory-unavailable", "a selected identity has an unresolved original Status")
                if layout is not None and path.is_relative_to(layout[0]):
                    continue
                matches[atom_id].append(path.relative_to(root).as_posix())
        if reader.currentness()["state"] != "unchanged" or candidates() != paths_before:
            _fail(operations, "subject-source-changed", "original identity sources changed during preview inventory")
    except (OSError, LimitReached) as error:
        raise operations.ToolError("subject-identity-inventory-unavailable", "original identity inventory is incomplete or unavailable") from error
    _assert_identity_layout_current(operations, root, layout)
    for atom_id, paths in matches.items():
        if len(paths) > 1:
            _fail(operations, "subject-identity-duplicate", "selected Atom identity has more than one original carrier", {"atom_id": atom_id, "paths": paths})
        if not paths:
            _fail(operations, "subject-identity-inventory-unavailable", "selected Atom identity has no current original carrier", {"atom_id": atom_id})


def _validate_subject_values(operations: Any, values: Sequence[str], subject_profile: str) -> None:
    """Apply the selected syntax only; it supplies no semantic admission."""

    for value in values:
        try:
            parse_subject(value, subject_profile=subject_profile)
        except SubjectNotationError as error:
            _fail(operations, error.code, str(error))


def _operations() -> Any:
    # The public wrapper imports atom_operations first.  A top-level import in
    # this module would therefore make subject-mode integration circular.
    import atom_operations

    return atom_operations


def _fail(operations: Any, code: str, message: str, details: Mapping[str, Any] | None = None) -> None:
    raise operations.ToolError(code, message, details)


def _plan_item(  # noqa: C901 - pinned preflight is intentionally all-or-nothing.
    operations: Any,
    root: Path,
    item: object,
    ordinal: int,
    selectors: set[str],
    atom_ids: set[str],
    subject_profile: str,
) -> dict[str, Any]:
    if not isinstance(item, Mapping) or set(item) != {"selector", "expected", "subject_patches"}:
        _fail(operations, "subject-patch-item-invalid", "each Subject patch item has exactly selector, expected, and subject_patches")
    selector = item["selector"]
    if not isinstance(selector, str):
        _fail(operations, "subject-selector-invalid", "Subject patch selector must be a repository-relative string")
    if selector in selectors:
        _fail(operations, "subject-selector-duplicate", "Subject patch payload selects one file more than once", {"selector": selector})
    path = _safe_source_path(operations, root, selector)
    snapshot = _read_source_snapshot(operations, root, path, selector)

    expected = item["expected"]
    _validate_expected(operations, expected)
    raw = snapshot.raw
    digest = hashlib.sha256(raw).hexdigest()

    try:
        text = raw.decode("utf-8")
        parsed = operations.parse_carrier(raw, Path(selector))
    except (UnicodeError, operations.CarrierError) as error:
        raise operations.ToolError("subject-carrier-invalid", "Subject patch source is not a complete readable Atom carrier") from error
    frontmatter, body = _raw_frontmatter(operations, text)
    try:
        document = yaml.compose(frontmatter, Loader=yaml.SafeLoader)
    except yaml.YAMLError as error:
        raise operations.ToolError("subject-carrier-invalid", "Subject patch source frontmatter is malformed") from error
    if document is None or not isinstance(document, MappingNode):
        _fail(operations, "subject-shape-invalid", "Subject patch source frontmatter must be one mapping")
    subjects = _subjects_node(operations, document)
    governs_node, dependencies = _subject_scalars(operations, subjects)
    _validate_subject_values(
        operations,
        [governs_node.value, *(node.value for node in dependencies)],
        subject_profile,
    )
    version_node = _top_level_scalar(operations, document, "version", require_string=False)
    updated_at_node = _top_level_scalar(operations, document, "updated_at", require_string=True)
    atom_id, version = _snapshot_identity(operations, root, path, selector, parsed.metadata)
    if atom_id in atom_ids:
        _fail(operations, "subject-identity-duplicate", "Subject patch payload selects one Atom identity more than once", {"atom_id": atom_id})
    if expected["atom_id"] != atom_id:
        _fail(operations, "subject-pin-stale", "expected atom_id does not match the selected carrier snapshot")
    if expected["version"] != version:
        _fail(operations, "subject-pin-stale", "expected version does not match the selected carrier snapshot")
    if expected["sha256"] != digest:
        _fail(operations, "subject-pin-stale", "expected sha256 does not match the selected carrier snapshot")

    patches = item["subject_patches"]
    if not isinstance(patches, list):
        _fail(operations, "subject-patches-invalid", "subject_patches must be an ordered list")
    dependency_patches = [patch for patch in patches if isinstance(patch, Mapping) and patch.get("field") == "depends_on"]
    if len(dependency_patches) > 1 and any(patch.get("operation") == "replace_set" for patch in dependency_patches):
        _fail(operations, "subject-occurrence-duplicate", "Complete dependency replacement cannot overlap another dependency patch")
    records: list[dict[str, Any]] = []
    subject_replacements: list[_Replacement] = []
    occurrences: set[tuple[str, int | None]] = set()
    resulting_dependencies = [node.value for node in dependencies]
    resulting_governs = governs_node.value
    for patch_ordinal, patch in enumerate(patches):
        if isinstance(patch, Mapping) and patch.get("operation") == "replace_set":
            record, replacement = _plan_dependency_set(operations, patch, subjects, frontmatter, resulting_dependencies)
        else:
            record, replacement = _plan_patch(
                operations,
                patch,
                patch_ordinal,
                governs_node,
                dependencies,
                occurrences,
                resulting_dependencies,
            )
        records.append(record)
        if record["field"] == "governs":
            resulting_governs = record["new"]
        if replacement is not None:
            subject_replacements.append(replacement)
    if len(set(resulting_dependencies)) != len(resulting_dependencies):
        _fail(operations, "subject-dependency-duplicate", "Subject patch would produce duplicate depends_on values")
    _validate_subject_values(
        operations,
        [resulting_governs, *resulting_dependencies],
        subject_profile,
    )
    # A preview may never turn an invalid source into an apparently valid
    # proposal through its allowed Version/Updated At metadata changes.
    _validate_complete(operations, root, path, frontmatter, body)

    selectors.add(selector)
    atom_ids.add(atom_id)
    return {
        "ordinal": ordinal,
        "selector": selector,
        "path": path,
        "atom_id": atom_id,
        "version": version,
        "before_sha256": digest,
        "snapshot": snapshot,
        "text": text,
        "frontmatter": frontmatter,
        "body": body,
        "patches": records,
        "subject_replacements": subject_replacements,
        "version_node": version_node,
        "updated_at_node": updated_at_node,
        "noop": not subject_replacements,
    }


def _safe_source_path(operations: Any, root: Path, selector: str) -> Path:  # noqa: C901 - path safety is deliberately explicit.
    if not selector or "\x00" in selector:
        _fail(operations, "subject-selector-invalid", "Subject selector must be a non-empty repository-relative path")
    relative = Path(selector)
    if relative.is_absolute() or not relative.parts or any(part in {"", ".", ".."} for part in relative.parts):
        _fail(operations, "subject-selector-invalid", "Subject selector must not be absolute or escape the repository")
    if relative.as_posix() != selector:
        _fail(operations, "subject-selector-not-exact", "Subject selector must use one canonical repository-relative path")
    lexical = root.joinpath(*relative.parts)
    control = operations.control_root(root)
    if not _inside(lexical, control):
        _fail(operations, "outside-control-root", "Subject selector is outside the configured Project control root")
    if "_projection" in lexical.relative_to(control).parts:
        _fail(operations, "subject-selector-projection", "Subject selector cannot address a projection carrier")
    return lexical


def _read_source_snapshot(operations: Any, root: Path, path: Path, selector: str) -> _SourceSnapshot:
    """Read one regular source file through no-follow directory descriptors.

    The path is never reopened through ``Path.read_*``.  Opening each ancestor
    relative to its already-open parent closes the window where a checked
    directory can become a symlink before the final file is read.
    """

    try:
        descriptor = _open_no_follow(operations, root, path, selector)
    except OSError as error:
        _source_open_error(operations, error, selector)
    try:
        before = os.fstat(descriptor)
        if not stat.S_ISREG(before.st_mode):
            _fail(operations, "subject-selector-invalid", "Subject selector must name a regular file", {"selector": selector})
        chunks: list[bytes] = []
        while chunk := os.read(descriptor, 1024 * 1024):
            chunks.append(chunk)
        after = os.fstat(descriptor)
    finally:
        os.close(descriptor)
    if _fingerprint(before) != _fingerprint(after):
        _fail(operations, "subject-source-changed", "Subject source changed while its pinned snapshot was read", {"selector": selector})
    return _SourceSnapshot(path=path, raw=b"".join(chunks), fingerprint=_fingerprint(after))


def _open_no_follow(operations: Any, root: Path, path: Path, selector: str) -> int:
    no_follow = getattr(os, "O_NOFOLLOW", None)
    directory = getattr(os, "O_DIRECTORY", 0)
    if no_follow is None or directory == 0:
        _fail(operations, "subject-snapshot-unavailable", "platform cannot safely take a no-follow Subject source snapshot")
    relative = path.relative_to(root)
    root_descriptor = os.open(root, os.O_RDONLY | directory | no_follow)
    current = root_descriptor
    try:
        for part in relative.parts[:-1]:
            next_descriptor = os.open(part, os.O_RDONLY | directory | no_follow, dir_fd=current)
            os.close(current)
            current = next_descriptor
        descriptor = os.open(relative.parts[-1], os.O_RDONLY | no_follow, dir_fd=current)
    finally:
        os.close(current)
    return descriptor


def _source_open_error(operations: Any, error: OSError, selector: str) -> None:
    if error.errno in {errno.ELOOP, errno.ENOTDIR}:
        _fail(operations, "subject-selector-symlink", "Subject selector cannot traverse a symlink", {"selector": selector})
    if isinstance(error, FileNotFoundError):
        _fail(operations, "subject-selector-missing", "Subject selector does not name an existing carrier", {"selector": selector})
    raise operations.ToolError("subject-snapshot-unavailable", "cannot safely open Subject source snapshot") from error


def _fingerprint(value: os.stat_result) -> tuple[int, int, int, int, int]:
    return (value.st_dev, value.st_ino, value.st_size, value.st_mtime_ns, value.st_ctime_ns)


def _assert_snapshot_current(operations: Any, root: Path, snapshot: _SourceSnapshot, selector: str) -> None:
    try:
        descriptor = _open_no_follow(operations, root, snapshot.path, selector)
    except OSError as error:
        _source_open_error(operations, error, selector)
    try:
        current = os.fstat(descriptor)
    finally:
        os.close(descriptor)
    if _fingerprint(current) != snapshot.fingerprint:
        _fail(operations, "subject-source-changed", "Subject source changed after its pinned snapshot was read", {"selector": selector})


def _inside(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def _validate_expected(operations: Any, expected: object) -> None:
    if not isinstance(expected, Mapping) or set(expected) != {"atom_id", "version", "sha256"}:
        _fail(operations, "subject-expected-invalid", "expected must contain exactly atom_id, version, and sha256")
    atom_id = expected["atom_id"]
    version = expected["version"]
    digest = expected["sha256"]
    if not isinstance(atom_id, str) or not atom_id:
        _fail(operations, "subject-expected-invalid", "expected atom_id must be a non-empty string")
    if isinstance(version, bool) or not isinstance(version, int) or version < 0:
        _fail(operations, "subject-expected-invalid", "expected version must be a non-negative integer")
    if not isinstance(digest, str) or _SHA256.fullmatch(digest) is None:
        _fail(operations, "subject-expected-invalid", "expected sha256 must be a lowercase full-file SHA-256")


def _raw_frontmatter(operations: Any, text: str) -> tuple[str, str]:
    first_end = _line_end(text, 0)
    if first_end is None or text[:first_end].rstrip("\r\n") != "---":
        _fail(operations, "subject-carrier-invalid", "Subject patch source must begin with YAML frontmatter")
    position = first_end
    while position < len(text):
        line_end = _line_end(text, position)
        if line_end is None:
            break
        if text[position:line_end].rstrip("\r\n") == "---":
            return text[first_end:position], text[line_end:]
        position = line_end
    _fail(operations, "subject-carrier-invalid", "Subject patch source frontmatter is not closed")
    raise AssertionError("unreachable")


def _line_end(text: str, start: int) -> int | None:
    newline = text.find("\n", start)
    return None if newline < 0 else newline + 1


def _mapping_entries(operations: Any, node: MappingNode, label: str) -> dict[str, Node]:
    result: dict[str, Node] = {}
    for key, value in node.value:
        if not isinstance(key, ScalarNode) or key.tag != _YAML_STRING:
            _fail(operations, "subject-shape-invalid", f"{label} keys must be strings")
        if key.value in result:
            _fail(operations, "subject-shape-invalid", f"{label} has duplicate {key.value} entries")
        result[key.value] = value
    return result


def _subjects_node(operations: Any, document: MappingNode) -> MappingNode:
    node = _mapping_entries(operations, document, "frontmatter").get("subjects")
    if not isinstance(node, MappingNode):
        _fail(operations, "subject-shape-invalid", "subjects must be one flat mapping")
    return node


def _subject_scalars(operations: Any, subjects: MappingNode) -> tuple[ScalarNode, list[ScalarNode]]:
    entries = _mapping_entries(operations, subjects, "subjects")
    governs = entries.get("governs")
    if not isinstance(governs, ScalarNode):
        _fail(operations, "subject-shape-invalid", "subjects.governs must be one direct scalar")
    _valid_scalar_node(operations, governs, "subjects.governs")
    dependencies_node = entries.get("depends_on")
    if dependencies_node is None:
        return governs, []
    if not isinstance(dependencies_node, SequenceNode):
        _fail(operations, "subject-shape-invalid", "subjects.depends_on must be one flat scalar list")
    dependencies: list[ScalarNode] = []
    for index, node in enumerate(dependencies_node.value):
        if not isinstance(node, ScalarNode):
            _fail(operations, "subject-shape-invalid", "subjects.depends_on entries must be direct scalars", {"index": index})
        _valid_scalar_node(operations, node, "subjects.depends_on")
        dependencies.append(node)
    values = [node.value for node in dependencies]
    if len(set(values)) != len(values):
        _fail(operations, "subject-dependency-duplicate", "subjects.depends_on already has duplicate values")
    return governs, dependencies


def _valid_scalar_node(operations: Any, node: ScalarNode, label: str) -> None:
    if node.tag != _YAML_STRING or node.style in {"|", ">"} or not node.value or "\n" in node.value or "\r" in node.value:
        _fail(operations, "subject-scalar-invalid", f"{label} must be one non-empty direct string scalar")


def _top_level_scalar(operations: Any, document: MappingNode, name: str, *, require_string: bool) -> ScalarNode:
    node = _mapping_entries(operations, document, "frontmatter").get(name)
    if not isinstance(node, ScalarNode):
        _fail(operations, "subject-carrier-invalid", f"{name} must be one direct scalar")
    if require_string:
        _valid_scalar_node(operations, node, name)
    return node


def _snapshot_identity(
    operations: Any,
    root: Path,
    path: Path,
    selector: str,
    metadata: Mapping[str, Any],
) -> tuple[str, int]:
    """Derive the Atom identity and eligibility from the captured bytes only."""

    control = operations.control_root(root)
    if path.suffix.lower() != ".md" or operations._role_directory(path, control) is None:
        _fail(operations, "not-markdown-atom", "Subject selector is not a CAPRMEDIO Markdown Atom carrier")
    if operations._lifecycle(path, control) in {"draft", "archived"}:
        _fail(operations, "atom-not-active", "Subject patch source must be a non-Draft, non-archived original Atom carrier", {"selector": selector})
    if "projection" in metadata:
        _fail(operations, "subject-selector-projection", "Subject selector cannot address a projection carrier")
    atom_id = metadata.get("atom_id")
    if not isinstance(atom_id, str) or re.fullmatch(r"CA-[CAPRMEDO]-[0-9]+", atom_id) is None:
        _fail(operations, "subject-identity-invalid", "Subject patch source must have one valid stable Atom identity")
    filename_identity = operations.ATOM_ID.search(path.name)
    if filename_identity is None or filename_identity.group(1) != atom_id:
        _fail(operations, "atom-frontmatter-id-mismatch", "Subject source filename and frontmatter Atom ID differ")
    version = metadata.get("version")
    if isinstance(version, bool) or not isinstance(version, int) or version < 1:
        _fail(operations, "atom-version-invalid", "Subject patch source has no positive integer Version")
    status = metadata.get("status")
    if not isinstance(status, str) or status.casefold() in {"draft", "archived"}:
        _fail(operations, "atom-not-active", "Subject patch source must carry a non-Draft, non-archived Status", {"selector": selector})
    return atom_id, version


def _plan_dependency_set(operations: Any, patch: Mapping[str, Any], subjects: MappingNode,
                         frontmatter: str, resulting_dependencies: list[str]) -> tuple[dict[str, Any], _Replacement | None]:
    if set(patch) != {"field", "operation", "old", "new"} or patch["field"] != "depends_on":
        _fail(operations, "subject-patch-invalid", "replace_set has exactly depends_on field, operation, old, and new")
    for name in ("old", "new"):
        values = patch[name]
        if not isinstance(values, list):
            _fail(operations, "subject-set-invalid", "Complete dependency sets must be lists")
        for value in values:
            _valid_patch_value(operations, value, name)
        if len(set(values)) != len(values):
            _fail(operations, "subject-dependency-duplicate", "Complete dependency sets must contain unique values")
    node = _mapping_entries(operations, subjects, "subjects").get("depends_on")
    if not isinstance(node, SequenceNode):
        _fail(operations, "subject-shape-invalid", "Complete dependency replacement requires an existing list")
    if set(patch["old"]) != set(resulting_dependencies):
        _fail(operations, "subject-old-stale", "Complete old dependency set differs from the pinned source")
    changed = set(patch["new"]) != set(resulting_dependencies)
    record = {"field": "depends_on", "operation": "replace_set", "old": patch["old"], "new": patch["new"],
              "changed": changed, "span": {"start": node.start_mark.index, "end": node.end_mark.index}}
    if not changed:
        return record, None
    from connector_property_carrier import _replace_value, _span_end

    start, end = node.start_mark.index, _span_end(frontmatter, node)
    transformed = _replace_value(frontmatter, node, patch["new"], "\r\n" if "\r\n" in frontmatter else "\n")
    value = transformed[start:len(transformed) - len(frontmatter[end:])]
    resulting_dependencies[:] = patch["new"]
    return record, _Replacement(_Span(start, end), value)


def _plan_patch(  # noqa: C901 - validates one closed public patch shape.
    operations: Any,
    patch: object,
    patch_ordinal: int,
    governs: ScalarNode,
    dependencies: Sequence[ScalarNode],
    occurrences: set[tuple[str, int | None]],
    resulting_dependencies: list[str],
) -> tuple[dict[str, Any], _Replacement | None]:
    if not isinstance(patch, Mapping):
        _fail(operations, "subject-patch-invalid", "each subject patch must be an object")
    field = patch.get("field")
    if field == "governs":
        if set(patch) != {"field", "old", "new"}:
            _fail(operations, "subject-patch-invalid", "governs patch has exactly field, old, and new")
    elif field == "depends_on":
        if set(patch) != {"field", "old", "new"}:
            _fail(operations, "subject-patch-invalid", "depends_on patch has exactly field, old, and new")
    else:
        _fail(operations, "subject-field-invalid", "subject patch field must be governs or depends_on")
    old = patch["old"]
    new = patch["new"]
    _valid_patch_value(operations, old, "old")
    _valid_patch_value(operations, new, "new")
    index: int | None = None
    node = governs
    if field == "depends_on":
        matches = [ordinal for ordinal, dependency in enumerate(dependencies) if dependency.value == old]
        if len(matches) != 1:
            _fail(operations, "subject-old-stale", "Subject patch old value must match exactly one original dependency")
        index = matches[0]
        node = dependencies[index]
    occurrence = (field, index)
    if occurrence in occurrences:
        _fail(operations, "subject-occurrence-duplicate", "Subject patch may name an occurrence only once", {"field": field, "index": index})
    occurrences.add(occurrence)
    if old != node.value:
        _fail(operations, "subject-old-stale", "Subject patch old value does not match the selected scalar", {"field": field, "index": index})
    changed = old != new
    if field == "depends_on":
        assert index is not None
        resulting_dependencies[index] = new
    record = {
        "field": field,
        "index": index,
        "old": old,
        "new": new,
        "changed": changed,
        "span": {"start": node.start_mark.index, "end": node.end_mark.index},
    }
    if not changed:
        return record, None
    return record, _Replacement(_Span(node.start_mark.index, node.end_mark.index), _yaml_scalar(new))


def _valid_patch_value(operations: Any, value: object, name: str) -> None:
    if not isinstance(value, str) or not value or "\x00" in value or "\n" in value or "\r" in value:
        _fail(operations, "subject-value-invalid", f"subject patch {name} must be one non-empty scalar string")


def _yaml_scalar(value: str) -> str:
    """Return an unambiguous, one-line YAML string scalar without reserializing a map."""

    return json.dumps(value, ensure_ascii=False)


def _preview_timestamp(operations: Any, root: Path, timestamp: str | None) -> str:
    if timestamp is not None:
        return timestamp
    try:
        from artifact_metadata import configured_timezone

        timezone = configured_timezone(root)
        moment = datetime.now().astimezone() if timezone is None else datetime.now(timezone)
        value = moment.strftime("%Y-%m-%d %H:%M:%S %z")
    except Exception as error:
        raise operations.ToolError(
            "subject-preview-time-unavailable",
            "cannot obtain the Project illustrative preview time",
        ) from error
    _require_timestamp(operations, value)
    return value


def _require_timestamp(operations: Any, timestamp: object) -> None:
    if not isinstance(timestamp, str) or _TIMESTAMP.fullmatch(timestamp) is None:
        _fail(operations, "subject-preview-time-invalid", "illustrative timestamp must be YYYY-MM-DD HH:MM:SS +ZZZZ")


def _materialize_item(operations: Any, root: Path, item: Mapping[str, Any], illustrative_at: str | None) -> dict[str, Any]:
    replacements = list(item["subject_replacements"])
    metadata_patches: list[dict[str, Any]] = []
    if not item["noop"]:
        assert illustrative_at is not None
        version_node = item["version_node"]
        updated_at_node = item["updated_at_node"]
        replacements.extend((
            _Replacement(_Span(version_node.start_mark.index, version_node.end_mark.index), str(item["version"] + 1)),
            _Replacement(_Span(updated_at_node.start_mark.index, updated_at_node.end_mark.index), _yaml_scalar(illustrative_at)),
        ))
        metadata_patches = [
            {"field": "version", "old": item["version"], "new": item["version"] + 1},
            {"field": "updated_at", "old": updated_at_node.value, "new": illustrative_at},
        ]
    _ensure_non_overlapping(operations, replacements)
    proposed_frontmatter = _apply_replacements(item["frontmatter"], replacements)
    proposed_text = _replace_frontmatter(item["text"], item["frontmatter"], proposed_frontmatter)
    proposed_raw = proposed_text.encode("utf-8")
    _validate_complete(operations, root, item["path"], proposed_frontmatter, item["body"])
    after_sha256 = hashlib.sha256(proposed_raw).hexdigest()
    after_version = item["version"] if item["noop"] else item["version"] + 1
    return {
        "selector": item["selector"],
        "relative_path": item["selector"],
        "atom_id": item["atom_id"],
        "before_sha256": item["before_sha256"],
        "after_sha256": after_sha256,
        "before_version": item["version"],
        "after_version": after_version,
        "proposed_version": after_version,
        "patches": item["patches"],
        "revision_metadata_patches": metadata_patches,
        "proposed_carrier": proposed_text,
        "noop": item["noop"],
        "illustrative_updated_at": illustrative_at if not item["noop"] else None,
        "byte_preservation": {
            "preserved": True,
            "permitted_fields": ["subjects", "version", "updated_at"] if not item["noop"] else [],
        },
    }


def _ensure_non_overlapping(operations: Any, replacements: Sequence[_Replacement]) -> None:
    ordered = sorted(replacements, key=lambda value: (value.span.start, value.span.end))
    for previous, current in zip(ordered, ordered[1:]):
        if previous.span.end > current.span.start:
            _fail(operations, "subject-span-overlap", "Subject patch spans overlap")


def _apply_replacements(frontmatter: str, replacements: Sequence[_Replacement]) -> str:
    result = frontmatter
    for replacement in sorted(replacements, key=lambda value: value.span.start, reverse=True):
        result = result[:replacement.span.start] + replacement.value + result[replacement.span.end:]
    return result


def _replace_frontmatter(text: str, before: str, after: str) -> str:
    # ``before`` is the exact slice returned by _raw_frontmatter, so this
    # operation cannot touch delimiters, line endings, or body bytes.
    start = text.find(before)
    if start < 0:
        raise RuntimeError("frontmatter slice disappeared during preview")
    return text[:start] + after + text[start + len(before):]


def _validate_complete(operations: Any, root: Path, path: Path, frontmatter: str, body: str) -> None:
    try:
        operations._validate_complete_carrier(root, path, frontmatter, body, creating=False)
    except operations.ToolError:
        raise
    except Exception as error:
        raise operations.ToolError(
            "complete-carrier-authority-unavailable",
            "complete-carrier validation authority is unavailable",
        ) from error
