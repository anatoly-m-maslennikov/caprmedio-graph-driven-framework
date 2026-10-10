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


_SHA256 = re.compile(r"[0-9a-f]{64}")
_TIMESTAMP = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} [+-]\d{4}")
_YAML_STRING = "tag:yaml.org,2002:str"


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


def preview_subject_patches(root: Path, items: list[object], *, timestamp: str | None = None) -> dict[str, Any]:
    """Prepare a sealed-in-memory preview of explicit Subject replacements.

    ``items`` uses only the Subject-only ATOM_UPDATE payload shape.  The module
    imports :mod:`atom_operations` lazily because the generic updater imports
    this preview helper when it detects that exclusive mode.
    """

    operations = _operations()
    project_root = Path(root).resolve()
    if not isinstance(items, list) or not items:
        _fail(operations, "subject-patches-required", "subject patch preview requires a non-empty atoms list")
    if timestamp is not None:
        _require_timestamp(operations, timestamp)

    planned: list[dict[str, Any]] = []
    selectors: set[str] = set()
    atom_ids: set[str] = set()
    has_change = False

    # Validate every precondition before resolving an illustrative time.  This
    # keeps an invalid request from looking like an accepted preview.
    for ordinal, item in enumerate(items):
        result = _plan_item(operations, project_root, item, ordinal, selectors, atom_ids)
        planned.append(result)
        has_change = has_change or not result["noop"]

    illustrative_at = _preview_timestamp(operations, project_root, timestamp) if has_change else None
    atoms: list[dict[str, Any]] = []
    for item in planned:
        atoms.append(_materialize_item(operations, project_root, item, illustrative_at))
    for item in planned:
        _assert_snapshot_current(operations, project_root, item["snapshot"], item["selector"])

    preview: dict[str, Any] = {
        "count": len(atoms),
        "atoms": atoms,
        "noop": not has_change,
        "illustrative_updated_at": illustrative_at,
    }
    preview["preview_sha256"] = hashlib.sha256(
        operations.canonical_json(preview).encode("utf-8")
    ).hexdigest()
    return preview


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
    records: list[dict[str, Any]] = []
    subject_replacements: list[_Replacement] = []
    occurrences: set[tuple[str, int | None]] = set()
    resulting_dependencies = [node.value for node in dependencies]
    for patch_ordinal, patch in enumerate(patches):
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
        if replacement is not None:
            subject_replacements.append(replacement)
    if len(set(resulting_dependencies)) != len(resulting_dependencies):
        _fail(operations, "subject-dependency-duplicate", "Subject patch would produce duplicate depends_on values")
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
    if operations._lifecycle(path, control) != "active":
        _fail(operations, "atom-not-active", "Subject patch source must be an active Atom carrier", {"selector": selector})
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
    if metadata.get("status") != "Active":
        _fail(operations, "atom-not-active", "Subject patch source metadata status must be Active", {"selector": selector})
    return atom_id, version


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
        index: int | None = None
        node = governs
    elif field == "depends_on":
        if set(patch) != {"field", "index", "old", "new"}:
            _fail(operations, "subject-patch-invalid", "depends_on patch has exactly field, index, old, and new")
        index = patch["index"]
        if isinstance(index, bool) or not isinstance(index, int) or index < 0 or index >= len(dependencies):
            _fail(operations, "subject-index-invalid", "depends_on patch index must identify one existing zero-based dependency")
        node = dependencies[index]
    else:
        _fail(operations, "subject-field-invalid", "subject patch field must be governs or depends_on")
    old = patch["old"]
    new = patch["new"]
    _valid_patch_value(operations, old, "old")
    _valid_patch_value(operations, new, "new")
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
