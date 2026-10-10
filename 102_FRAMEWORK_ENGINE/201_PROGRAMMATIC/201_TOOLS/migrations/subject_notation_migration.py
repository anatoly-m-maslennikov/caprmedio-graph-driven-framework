"""Prepare a sealed, dry-run Subject-notation changeset.

This module is intentionally a planner, not a writer.  It consumes the sealed
read-only inventory produced for the Subject-notation review and an explicit,
normalised per-case decision sequence.  A decision is never inferred from an
old path, a bucket number, or a source spelling.  The planner may show safe
candidate byte patches for resolved cases, but it never exposes an apply path
and never changes a carrier.

The normalised decision boundary is deliberately small::

    {"case_id": "slash:...", "new_separator": "." or "/" or None,
     "confidence_percent": 99, "source_refs": [...],
     "disposition": "accepted" or "blocked"}

``source_refs`` are checked against the sealed carrier pins and, when a line
span is supplied, against the current bytes at that span.  The caller may use
its own authority-review format before producing this boundary; this module
does not translate guesses from that format.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections.abc import Mapping, Sequence
from pathlib import Path, PurePosixPath
from typing import Any


MIN_CONFIDENCE_PERCENT = 90
SCHEMA_VERSION = 1
SHA256 = re.compile(r"^[0-9a-f]{64}$")
_HEX_DIGITS = frozenset(b"0123456789abcdefABCDEF")
_ACCEPTED_DISPOSITIONS = frozenset({"accepted"})
_BLOCKED_DISPOSITIONS = frozenset({"blocked"})
_FRONTMATTER_DELIMITER = b"---"


class SubjectNotationMigrationError(ValueError):
    """A deterministic planner input or source-frontier failure."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(message)


# A short compatibility alias for callers using the other migration tools'
# exception name.  It does not broaden the accepted input grammar.
MigrationPreparationError = SubjectNotationMigrationError


def _fail(code: str, message: str) -> None:
    raise SubjectNotationMigrationError(code, message)


def canonical_json_bytes(value: object) -> bytes:
    """Return the compact, deterministic JSON bytes used by sealed digests."""

    try:
        return json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("utf-8")
    except (TypeError, ValueError, UnicodeEncodeError) as error:
        _fail("canonical-json-invalid", "The changeset contains non-canonical JSON data")
        raise AssertionError from error


def canonical_digest(value: object) -> str:
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _is_sha256(value: object) -> bool:
    return isinstance(value, str) and SHA256.fullmatch(value) is not None


def _copy_json(value: object) -> object:
    """Copy caller data through JSON without allowing shared mutable state."""

    try:
        return json.loads(json.dumps(value, ensure_ascii=False, allow_nan=False))
    except (TypeError, ValueError, UnicodeEncodeError) as error:
        _fail("decision-json-invalid", "Decision data must be JSON-compatible")
        raise AssertionError from error


def _safe_relative_path(repository: Path, value: object, field: str) -> Path:
    if not isinstance(value, str) or not value or "\\" in value or "\x00" in value:
        _fail("path-invalid", f"{field} must be a repository-relative POSIX path")
    relative = PurePosixPath(value)
    if relative.is_absolute() or ".." in relative.parts or relative.as_posix() != value:
        _fail("path-invalid", f"{field} must be a canonical repository-relative POSIX path")
    resolved = (repository / relative.as_posix()).resolve()
    try:
        resolved.relative_to(repository)
    except ValueError as error:
        _fail("path-escapes-repository", f"{field} escapes the repository")
        raise AssertionError from error
    if resolved.relative_to(repository).as_posix() != value:
        _fail("path-ambiguous", f"{field} is not the canonical repository-relative path")
    return resolved


def _without_digest(value: Mapping[str, Any], field: str) -> dict[str, Any]:
    return {key: item for key, item in value.items() if key != field}


def _as_nonempty_string(value: object, code: str, field: str) -> str:
    if not isinstance(value, str) or not value:
        _fail(code, f"{field} must be a non-empty string")
    return value


def _as_positive_int(value: object, code: str, field: str) -> int:
    if type(value) is not int or value < 1:
        _fail(code, f"{field} must be a positive integer")
    return value


def _pin_shape(value: object, *, field: str = "source pin") -> dict[str, Any]:
    if not isinstance(value, Mapping):
        _fail("inventory-pin-invalid", f"{field} must be an object")
    pin = dict(value)
    atom_id = _as_nonempty_string(pin.get("atom_id"), "inventory-pin-invalid", f"{field}.atom_id")
    revision = pin.get("atom_revision", pin.get("revision"))
    revision = _as_positive_int(revision, "inventory-pin-invalid", f"{field}.atom_revision")
    path = _as_nonempty_string(pin.get("carrier_path"), "inventory-pin-invalid", f"{field}.carrier_path")
    digest = pin.get("carrier_sha256", pin.get("source_sha256"))
    if not _is_sha256(digest):
        _fail("inventory-pin-invalid", f"{field}.carrier_sha256 must be lowercase SHA-256")
    return {
        "atom_id": atom_id,
        "atom_revision": revision,
        "carrier_path": path,
        "carrier_sha256": digest,
    }


def _source_pin_key(pin: Mapping[str, Any]) -> tuple[str, str, int, str]:
    return (str(pin["carrier_path"]), str(pin["atom_id"]), int(pin["atom_revision"]), str(pin["carrier_sha256"]))


def _validate_inventory(inventory: Mapping[str, Any]) -> tuple[dict[str, Any], dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:  # noqa: C901
    if not isinstance(inventory, Mapping):
        _fail("inventory-invalid", "sealed inventory must be one JSON object")
    value = dict(inventory)
    if value.get("kind") != "subject_notation_migration_analysis_inventory":
        _fail("inventory-invalid", "sealed inventory kind is unsupported")
    if value.get("source_mutation") is not False:
        _fail("inventory-mutation-enabled", "sealed inventory must prove source_mutation=false")
    if value.get("native_fact_admission") != "not_performed":
        _fail("inventory-admission-enabled", "sealed inventory must prove native admission was not performed")
    inventory_digest = value.get("inventory_sha256")
    if not _is_sha256(inventory_digest):
        _fail("inventory-digest-missing", "sealed inventory must carry inventory_sha256")
    if canonical_digest(_without_digest(value, "inventory_sha256")) != inventory_digest:
        _fail("inventory-digest-mismatch", "sealed inventory bytes no longer match inventory_sha256")

    raw_pins = value.get("source_pins")
    if type(raw_pins) is not list or not raw_pins:
        _fail("inventory-pins-missing", "sealed inventory must contain source_pins")
    pins: list[dict[str, Any]] = []
    by_path: dict[str, dict[str, Any]] = {}
    by_id: dict[str, dict[str, Any]] = {}
    for index, raw_pin in enumerate(raw_pins):
        pin = _pin_shape(raw_pin, field=f"source_pins[{index}]")
        if pin["carrier_path"] in by_path or pin["atom_id"] in by_id:
            _fail("inventory-pin-duplicate", "source pins must have unique paths and Atom identities")
        by_path[pin["carrier_path"]] = pin
        by_id[pin["atom_id"]] = pin
        pins.append(pin)
    if pins != sorted(pins, key=lambda item: item["carrier_path"]):
        _fail("inventory-pins-unsorted", "source pins must be sorted by carrier_path")

    frontier = value.get("source_frontier")
    if not isinstance(frontier, Mapping):
        _fail("inventory-frontier-missing", "sealed inventory must contain source_frontier")
    frontier_value = dict(frontier)
    carriers = frontier_value.get("carriers")
    frontier_pins: list[dict[str, Any]] = []
    if type(carriers) is list and carriers:
        for index, item in enumerate(carriers):
            if not isinstance(item, Mapping):
                _fail("inventory-frontier-invalid", f"source_frontier.carriers[{index}] must be an object")
            frontier_pins.append(_pin_shape(item, field=f"source_frontier.carriers[{index}]"))
        if len({pin["carrier_path"] for pin in frontier_pins}) != len(frontier_pins):
            _fail("inventory-frontier-invalid", "source frontier carriers must have unique paths")
        if frontier_pins != sorted(frontier_pins, key=lambda item: item["carrier_path"]):
            _fail("inventory-frontier-invalid", "source frontier carriers must be sorted by carrier_path")
        frontier_by_path = {pin["carrier_path"]: pin for pin in frontier_pins}
        if any(frontier_by_path.get(pin["carrier_path"]) != pin for pin in pins):
            _fail("inventory-frontier-mismatch", "source pins are not bound to the sealed source frontier")
    else:
        _fail("inventory-frontier-missing", "sealed source frontier must contain carriers")
    frontier_digest = frontier_value.get("source_frontier_sha256")
    if frontier_digest is not None and not _is_sha256(frontier_digest):
        _fail("inventory-frontier-invalid", "source_frontier_sha256 must be lowercase SHA-256")
    if frontier_digest is not None and frontier_digest != canonical_digest(frontier_pins):
        _fail("inventory-frontier-mismatch", "source frontier digest does not match source pins")

    raw_cases = value.get("cases")
    if type(raw_cases) is not list:
        _fail("inventory-cases-missing", "sealed inventory must contain cases")
    cases: dict[str, dict[str, Any]] = {}
    for index, raw_case in enumerate(raw_cases):
        if not isinstance(raw_case, Mapping):
            _fail("inventory-case-invalid", f"cases[{index}] must be an object")
        case = dict(raw_case)
        case_id = _as_nonempty_string(case.get("case_id"), "inventory-case-invalid", f"cases[{index}].case_id")
        parent = _as_nonempty_string(case.get("old_parent"), "inventory-case-invalid", f"{case_id}.old_parent")
        child = _as_nonempty_string(case.get("old_child"), "inventory-case-invalid", f"{case_id}.old_child")
        if not child.startswith(parent + "/"):
            _fail("inventory-case-invalid", f"{case_id} does not identify one old slash step")
        occurrences = case.get("occurrences")
        if type(occurrences) is not list or not occurrences:
            _fail("inventory-case-invalid", f"{case_id} must contain occurrences")
        for occurrence_index, occurrence in enumerate(occurrences):
            if not isinstance(occurrence, Mapping):
                _fail("inventory-occurrence-invalid", f"{case_id}.occurrences[{occurrence_index}] must be an object")
            source_ref = occurrence.get("source_ref")
            if not isinstance(source_ref, Mapping):
                _fail("inventory-occurrence-invalid", f"{case_id} occurrence lacks source_ref")
            source_pin = _pin_shape(source_ref, field=f"{case_id}.source_ref")
            pinned = by_path.get(source_pin["carrier_path"])
            if pinned != source_pin:
                _fail("inventory-occurrence-unbound", f"{case_id} occurrence is not bound to its source frontier")
            _as_nonempty_string(occurrence.get("subject_path"), "inventory-occurrence-invalid", f"{case_id}.subject_path")
            contribution = source_ref.get("contribution")
            if not isinstance(contribution, Mapping):
                _fail("inventory-occurrence-invalid", f"{case_id} occurrence lacks an exact contribution span")
            property_path = contribution.get("property_path")
            if property_path not in {"subjects.governs", "subjects.depends_on"}:
                _fail("inventory-occurrence-invalid", f"{case_id} occurrence is not a Subjects property")
        if case_id in cases:
            _fail("inventory-case-duplicate", "sealed inventory contains duplicate case IDs")
        cases[case_id] = case
    if list(cases) != sorted(cases):
        _fail("inventory-cases-unsorted", "sealed inventory cases must be sorted by case_id")
    return value, by_path, cases


def _parse_confidence_percent(value: object) -> int:
    """Validate the closed integer confidence boundary.

    Confidence deliberately has no float representation at this boundary:
    JSON floats are not canonical contract data and a decimal-to-float
    round-trip could silently move a decision across the 90% threshold.
    """

    if type(value) is not int or not 0 <= value <= 100:
        _fail("decision-confidence-invalid", "decision confidence_percent must be an integer from 0 to 100")
    return value


def _normalise_decisions(decisions: Sequence[Mapping[str, Any]] | Mapping[str, Any], cases: Mapping[str, Mapping[str, Any]]) -> dict[str, dict[str, Any]]:  # noqa: C901
    if isinstance(decisions, Mapping):
        if set(decisions) == {"decisions"}:
            decisions = decisions["decisions"]
        else:
            _fail("decision-envelope-invalid", "decision input must be a sequence or {decisions:[...]}")
    if not isinstance(decisions, Sequence) or isinstance(decisions, (str, bytes, bytearray)):
        _fail("decision-envelope-invalid", "decision input must be a sequence")
    result: dict[str, dict[str, Any]] = {}
    for index, raw in enumerate(decisions):
        if not isinstance(raw, Mapping):
            _fail("decision-invalid", f"decision[{index}] must be an object")
        row = dict(raw)
        if set(row) != {"case_id", "new_separator", "confidence_percent", "source_refs", "disposition"}:
            _fail("decision-shape-invalid", f"decision[{index}] must use the normalized closed fields")
        case_id = _as_nonempty_string(row.get("case_id"), "decision-invalid", f"decision[{index}].case_id")
        if case_id not in cases:
            _fail("decision-unknown-case", f"decision refers to an unknown sealed case: {case_id}")
        if case_id in result:
            _fail("decision-duplicate-case", f"decision repeats sealed case: {case_id}")
        separator = row.get("new_separator")
        if separator not in {None, ".", "/"}:
            _fail("decision-separator-invalid", f"decision separator is outside the closed notation set: {case_id}")
        confidence_percent = _parse_confidence_percent(row.get("confidence_percent"))
        refs = row.get("source_refs")
        if type(refs) is not list or not refs:
            _fail("decision-source-refs-missing", f"decision has no source_refs: {case_id}")
        disposition = row.get("disposition")
        if not isinstance(disposition, str):
            _fail("decision-disposition-invalid", f"decision disposition is missing: {case_id}")
        if disposition not in _ACCEPTED_DISPOSITIONS and disposition not in _BLOCKED_DISPOSITIONS:
            _fail("decision-disposition-invalid", f"decision disposition is outside the closed set: {case_id}")
        accepted = separator in {".", "/"} and disposition in _ACCEPTED_DISPOSITIONS
        blocked = separator is None and disposition in _BLOCKED_DISPOSITIONS
        if not accepted and not blocked:
            _fail("decision-disposition-invalid", f"decision has no closed outcome: {case_id}")
        if accepted and confidence_percent < MIN_CONFIDENCE_PERCENT:
            _fail("decision-confidence-below-threshold", f"accepted decision is below confidence threshold: {case_id}")
        result[case_id] = {
            "case_id": case_id,
            "new_separator": separator,
            "confidence_percent": confidence_percent,
            "source_refs": _copy_json(refs),
            "disposition": "accepted" if accepted else "blocked",
            "original_disposition": disposition,
        }
    return result


def _line_records(raw: bytes) -> list[tuple[int, int, bytes, bytes]]:
    records: list[tuple[int, int, bytes, bytes]] = []
    offset = 0
    for line in raw.splitlines(keepends=True):
        content = line[:-2] if line.endswith(b"\r\n") else line[:-1] if line.endswith(b"\n") else line
        records.append((offset, offset + len(line), content, line))
        offset += len(line)
    if not records or offset < len(raw):
        if offset < len(raw):
            records.append((offset, len(raw), raw[offset:], raw[offset:]))
    return records


def _frontmatter(raw: bytes, path: str) -> tuple[list[tuple[int, int, bytes, bytes]], int, int, int]:
    try:
        raw.decode("utf-8")
    except UnicodeDecodeError as error:
        _fail("source-not-utf8", f"current carrier is not UTF-8: {path}")
        raise AssertionError from error
    lines = _line_records(raw)
    if not lines or lines[0][2] != _FRONTMATTER_DELIMITER:
        _fail("source-frontmatter-invalid", f"carrier lacks YAML frontmatter: {path}")
    boundary_index = next((index for index, item in enumerate(lines[1:], 1) if item[2] == _FRONTMATTER_DELIMITER), None)
    if boundary_index is None:
        _fail("source-frontmatter-invalid", f"carrier frontmatter is unterminated: {path}")
    frontmatter_start = lines[0][1]
    frontmatter_end = lines[boundary_index][0]
    body_start = lines[boundary_index][1]
    return lines, frontmatter_start, frontmatter_end, body_start


def _decode_scalar(token: bytes, *, path: str) -> str:
    value = token.strip()
    if not value:
        _fail("subject-scalar-invalid", f"empty Subject scalar in {path}")
    if value[:1] in {b"'", b'"'}:
        quote = value[:1]
        if len(value) < 2 or value[-1:] != quote or quote in value[1:-1] or b"\\" in value:
            _fail("subject-scalar-unsupported", f"quoted Subject scalar is not safely patchable: {path}")
        value = value[1:-1]
    elif value[:1] in {b"[", b"{", b"*", b"&", b"!", b"|", b">"} or any(char in value for char in b"[]{}"):
        _fail("subject-scalar-unsupported", f"Subject scalar form is not safely patchable: {path}")
    try:
        decoded = value.decode("utf-8")
    except UnicodeDecodeError as error:
        _fail("subject-scalar-invalid", f"Subject scalar is not UTF-8: {path}")
        raise AssertionError from error
    if not decoded:
        _fail("subject-scalar-invalid", f"empty Subject scalar in {path}")
    return decoded


def _token_from_span(line_start: int, content: bytes, token_start: int, token_end: int, *, property_path: str, ordinal: int, line_number: int, path: str) -> dict[str, Any]:
    raw_token = content[token_start:token_end]
    value = _decode_scalar(raw_token, path=path)
    left = token_start
    right = token_end
    while left < right and content[left:left + 1] in {b" ", b"\t"}:
        left += 1
    while right > left and content[right - 1:right] in {b" ", b"\t"}:
        right -= 1
    return {
        "property_path": property_path,
        "ordinal": ordinal,
        "value": value,
        "start": line_start + left,
        "end": line_start + right,
        "line": line_number,
        "raw": content[left:right],
    }


def _inline_tokens(line_start: int, content: bytes, value_start: int, *, property_path: str, path: str, line_number: int) -> list[dict[str, Any]]:  # noqa: C901
    while value_start < len(content) and content[value_start:value_start + 1] in {b" ", b"\t"}:
        value_start += 1
    if value_start >= len(content) or content[value_start:value_start + 1] != b"[":
        _fail("subject-collection-unsupported", f"Subject dependency collection is not an inline list: {path}")
    end = len(content)
    while end > value_start and content[end - 1:end] in {b" ", b"\t"}:
        end -= 1
    if end <= value_start + 1 or content[end - 1:end] != b"]":
        _fail("subject-collection-unsupported", f"Subject inline list is malformed: {path}")
    tokens: list[dict[str, Any]] = []
    index = value_start + 1
    item_start: int | None = None
    quoted: int | None = None
    while index < end - 1:
        byte = content[index]
        if quoted is not None:
            if byte == 92:
                _fail("subject-scalar-unsupported", f"escaped Subject scalar is not safely patchable: {path}")
            if byte == quoted:
                quoted = None
            index += 1
            continue
        if byte in (34, 39):
            quoted = byte
            if item_start is None:
                item_start = index
            index += 1
            continue
        if byte == 44:
            if item_start is None:
                _fail("subject-collection-unsupported", f"inline Subject list has an empty item: {path}")
            item_end = index
            while item_end > item_start and content[item_end - 1:item_end] in {b" ", b"\t"}:
                item_end -= 1
            tokens.append(_token_from_span(line_start, content, item_start, item_end, property_path=property_path,
                                           ordinal=len(tokens), line_number=line_number, path=path))
            item_start = None
            index += 1
            continue
        if item_start is None and byte not in (32, 9):
            item_start = index
        index += 1
    if quoted is not None:
        _fail("subject-scalar-unsupported", f"unterminated quoted Subject scalar: {path}")
    if item_start is not None:
        item_end = end - 1
        while item_end > item_start and content[item_end - 1:item_end] in {b" ", b"\t"}:
            item_end -= 1
        tokens.append(_token_from_span(line_start, content, item_start, item_end, property_path=property_path,
                                       ordinal=len(tokens), line_number=line_number, path=path))
    elif content[value_start + 1:end - 1].strip():
        _fail("subject-collection-unsupported", f"inline Subject list has an empty item: {path}")
    return tokens


def _subject_tokens(raw: bytes, path: str) -> tuple[list[dict[str, Any]], dict[str, Any]]:  # noqa: C901
    lines, _, _, body_start = _frontmatter(raw, path)
    boundary = next(index for index, item in enumerate(lines[1:], 1) if item[2] == _FRONTMATTER_DELIMITER)
    tokens: list[dict[str, Any]] = []
    properties: dict[str, list[dict[str, Any]]] = {}
    index = 1
    while index < boundary:
        line_start, _, content, _ = lines[index]
        matched = re.fullmatch(rb"  (governs|depends_on):([ \t]*)(.*)", content)
        if matched is None:
            index += 1
            continue
        key = matched[1].decode("ascii")
        property_path = "subjects." + key
        if key in properties:
            _fail("subject-property-duplicate", f"duplicate Subjects property in {path}")
        value = matched[3]
        colon_value_start = line_start + matched.start(3)
        while value[:1] in {b" ", b"\t"}:
            value = value[1:]
            colon_value_start += 1
        property_tokens: list[dict[str, Any]] = []
        if key == "governs":
            if not value:
                _fail("subject-governs-unsupported", f"governs must be one scalar in {path}")
            property_tokens.append(_token_from_span(line_start, content, matched.start(3), len(content),
                                                    property_path=property_path, ordinal=0,
                                                    line_number=index + 1, path=path))
        elif value.startswith(b"["):
            property_tokens = _inline_tokens(line_start, content, matched.start(3), property_path=property_path,
                                              path=path, line_number=index + 1)
        elif value:
            _fail("subject-dependencies-unsupported", f"depends_on must be an inline list or block list in {path}")
        else:
            cursor = index + 1
            while cursor < boundary and (not lines[cursor][2].strip() or lines[cursor][2].startswith(b"    ")):
                nested = lines[cursor][2]
                if not nested.strip():
                    cursor += 1
                    continue
                item_match = re.fullmatch(rb"    -[ \t]+(.+)", nested)
                if item_match is None:
                    _fail("subject-dependencies-unsupported", f"depends_on block list is not safely patchable in {path}")
                nested_start = lines[cursor][0]
                property_tokens.append(_token_from_span(nested_start, nested, item_match.start(1), len(nested),
                                                        property_path=property_path, ordinal=len(property_tokens),
                                                        line_number=cursor + 1, path=path))
                cursor += 1
            index = cursor - 1
        properties[property_path] = property_tokens
        tokens.extend(property_tokens)
        index += 1
    if "subjects.governs" not in properties or len(properties["subjects.governs"]) != 1:
        _fail("subject-governs-missing", f"Subjects must contain exactly one governs scalar in {path}")
    for property_path, property_tokens in properties.items():
        values = [token["value"] for token in property_tokens]
        if len(values) != len(set(values)):
            _fail("subject-target-duplicate", f"Subjects contains duplicate targets in {path}")
    metadata = _frontmatter_metadata(raw, path)
    metadata["body_start"] = body_start
    metadata["properties"] = properties
    return tokens, metadata


def _frontmatter_metadata(raw: bytes, path: str) -> dict[str, Any]:
    lines, _, _, _ = _frontmatter(raw, path)
    boundary = next(index for index, item in enumerate(lines[1:], 1) if item[2] == _FRONTMATTER_DELIMITER)
    fields: dict[str, str] = {}
    for index in range(1, boundary):
        text = lines[index][2].decode("utf-8")
        matched = re.fullmatch(r"([A-Za-z_][A-Za-z0-9_-]*):[ \t]*(.*)", text)
        if matched is None:
            continue
        key, value = matched.groups()
        if key in fields:
            _fail("frontmatter-duplicate", f"duplicate frontmatter field in {path}")
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        fields[key] = value
    atom_id = fields.get("atom_id")
    version_text = fields.get("version")
    updated_at = fields.get("updated_at")
    if not atom_id or not version_text or not version_text.isdigit() or int(version_text) < 1 or not updated_at:
        _fail("revision-metadata-missing", f"carrier lacks current Atom revision metadata: {path}")
    return {"atom_id": atom_id, "version": int(version_text), "updated_at": updated_at, "fields": fields}


def _line_span_digest(raw: bytes, start_line: int, end_line: int) -> str:
    lines = _line_records(raw)
    if start_line < 1 or end_line < start_line or end_line > len(lines):
        _fail("source-ref-span-invalid", "source reference line span is outside current carrier bytes")
    return _sha256(b"".join(item[3] for item in lines[start_line - 1:end_line]))


def _ref_span(ref: Mapping[str, Any]) -> tuple[int, int] | None:
    contribution = ref.get("contribution")
    source = contribution if isinstance(contribution, Mapping) else ref
    start = source.get("start_line")
    end = source.get("end_line")
    if start is None or end is None:
        lines = source.get("lines", source.get("primary_lines"))
        if isinstance(lines, list) and len(lines) == 2:
            start, end = lines
        elif isinstance(lines, str) and re.fullmatch(r"[0-9]+-[0-9]+", lines):
            start, end = lines.split("-", 1)
    if type(start) is not int:
        try:
            start = int(start)
        except (TypeError, ValueError):
            return None
    if type(end) is not int:
        try:
            end = int(end)
        except (TypeError, ValueError):
            return None
    return start, end


def _validate_decision_refs(case: Mapping[str, Any], decision: Mapping[str, Any], by_path: Mapping[str, Mapping[str, Any]], current: Mapping[str, bytes]) -> list[dict[str, Any]]:  # noqa: C901
    expected_atoms = {
        occurrence["source_ref"]["atom_id"]
        for occurrence in case["occurrences"]
        if isinstance(occurrence, Mapping) and isinstance(occurrence.get("source_ref"), Mapping)
    }
    candidate_atoms = case.get("content_source_candidates")
    if isinstance(candidate_atoms, list):
        expected_atoms.update(item for item in candidate_atoms if isinstance(item, str))
    seen: set[str] = set()
    validated: list[dict[str, Any]] = []
    for index, raw_ref in enumerate(decision["source_refs"]):
        if not isinstance(raw_ref, Mapping):
            _fail("decision-source-ref-invalid", f"source_refs[{index}] is not an object")
        ref = dict(raw_ref)
        if set(ref) != {"atom_id", "atom_revision", "carrier_path", "carrier_sha256", "contribution"}:
            _fail("decision-source-ref-shape-invalid", f"source_refs[{index}] is outside the closed source-reference shape")
        contribution = ref.get("contribution")
        if not isinstance(contribution, Mapping) or set(contribution) != {
            "kind", "property_path", "start_line", "end_line", "text_sha256"
        }:
            _fail("decision-source-ref-shape-invalid", f"source_refs[{index}] lacks the exact body-line locator")
        pin = _pin_shape(ref, field=f"{decision['case_id']}.source_refs[{index}]")
        path = pin["carrier_path"]
        bound = by_path.get(path)
        if bound != pin or pin["atom_id"] not in expected_atoms:
            _fail("decision-source-ref-unbound", f"source_ref is not an exact current candidate reference: {decision['case_id']}")
        identity = canonical_digest(pin | {"ref": ref})
        if identity in seen:
            _fail("decision-source-ref-duplicate", f"decision repeats a source_ref: {decision['case_id']}")
        seen.add(identity)
        raw = current.get(path)
        if raw is None:
            _fail("source-frontier-changed", f"source_ref carrier is not current: {decision['case_id']}")
        span = _ref_span(ref)
        if span is not None:
            start, end = span
            actual = _line_span_digest(raw, start, end)
            source = ref.get("contribution") if isinstance(ref.get("contribution"), Mapping) else ref
            expected_digest = source.get("text_sha256")
            if expected_digest is not None and actual != expected_digest:
                _fail("decision-source-ref-stale", f"source_ref content span is stale: {decision['case_id']}")
        validated.append(ref)
    return validated


def _case_paths(case: Mapping[str, Any]) -> set[str]:
    return {
        occurrence["source_ref"]["carrier_path"]
        for occurrence in case["occurrences"]
        if isinstance(occurrence, Mapping) and isinstance(occurrence.get("source_ref"), Mapping)
    }


def _boundary_case_ids(subject_path: str, case_by_key: Mapping[tuple[str, str], Mapping[str, Any]]) -> list[tuple[int, Mapping[str, Any]]]:
    result: list[tuple[int, Mapping[str, Any]]] = []
    for index, char in enumerate(subject_path):
        if char != "/":
            continue
        parent = subject_path[:index]
        child_end = index + 1
        while child_end < len(subject_path) and subject_path[child_end] not in "/:":
            child_end += 1
        child = subject_path[:child_end]
        case = case_by_key.get((parent, child))
        if case is not None:
            result.append((index, case))
    return result


def _candidate_for_source(path: str, raw: bytes, tokens: Sequence[Mapping[str, Any]], case_by_key: Mapping[tuple[str, str], Mapping[str, Any]], decisions: Mapping[str, Mapping[str, Any]], case_status: Mapping[str, str]) -> tuple[dict[str, Any] | None, set[str], list[dict[str, Any]]]:  # noqa: C901
    patches: list[dict[str, Any]] = []
    blocked_cases: set[str] = set()
    diagnostics: list[dict[str, Any]] = []
    for token in tokens:
        value = str(token["value"])
        transformed = value
        boundaries = _boundary_case_ids(value, case_by_key)
        slash_offsets = [offset for offset, char in enumerate(value) if char == "/"]
        if len(boundaries) != len(slash_offsets):
            diagnostics.append({"code": "subject-case-unindexed", "carrier_path": path,
                                 "property_path": token["property_path"], "ordinal": token["ordinal"]})
            continue
        for offset, case in boundaries:
            case_id = case["case_id"]
            status = case_status.get(case_id, "missing")
            decision = decisions.get(case_id)
            if status != "accepted" or decision is None:
                blocked_cases.add(case_id)
                continue
            separator = decision["new_separator"]
            if separator == ".":
                transformed = transformed[:offset] + "." + transformed[offset + 1:]
        if transformed != value:
            old_bytes = value.encode("utf-8")
            new_bytes = transformed.encode("utf-8")
            token_raw = bytes(token["raw"])
            relative = token_raw.find(old_bytes)
            if relative < 0 or token_raw.find(old_bytes, relative + 1) >= 0:
                diagnostics.append({"code": "subject-token-ambiguous", "carrier_path": path,
                                     "property_path": token["property_path"], "ordinal": token["ordinal"]})
                continue
            start = int(token["start"]) + relative
            patches.append({"start": start, "end": start + len(old_bytes),
                            "old": old_bytes.decode("utf-8"), "new": new_bytes.decode("utf-8"),
                            "property_path": token["property_path"], "ordinal": token["ordinal"]})
    seen_ranges: dict[tuple[int, int], str] = {}
    for patch in patches:
        key = (patch["start"], patch["end"])
        previous = seen_ranges.get(key)
        if previous is not None and previous != patch["new"]:
            diagnostics.append({"code": "subject-patch-collision", "carrier_path": path, "offset": patch["start"]})
        seen_ranges[key] = patch["new"]
    if diagnostics or blocked_cases:
        return None, blocked_cases, diagnostics
    if not patches:
        return None, set(), []
    candidate = raw
    for patch in sorted(patches, key=lambda item: item["start"], reverse=True):
        candidate = candidate[:patch["start"]] + patch["new"].encode("utf-8") + candidate[patch["end"]:]
    # The only changed bytes must be the recorded Subject scalar spans.
    for index, (before, after) in enumerate(zip(raw, candidate)):
        if before != after and not any(patch["start"] <= index < patch["end"] for patch in patches):
            diagnostics.append({"code": "candidate-unrelated-byte-change", "carrier_path": path, "offset": index})
    if len(raw) != len(candidate):
        diagnostics.append({"code": "candidate-length-changed", "carrier_path": path})
    if diagnostics:
        return None, set(), diagnostics
    return {"candidate_bytes": candidate, "patches": sorted(patches, key=lambda item: (item["start"], item["end"]))}, set(), []


def build_changeset(repository: Path | str, inventory: Mapping[str, Any], normalized_mapping: Sequence[Mapping[str, Any]] | Mapping[str, Any], *, inventory_file_sha256: str | None = None) -> dict[str, Any]:  # noqa: C901
    """Build a dry-run candidate changeset; never write source bytes.

    ``global_status`` is ``ready_for_governed_apply`` only when every sealed
    case has an accepted decision and all source/patch checks pass.  Even then
    ``apply_supported`` remains false: a separate governed operation owns any
    future mutation.
    """

    repository = Path(repository).resolve()
    if not repository.is_dir():
        _fail("repository-invalid", "repository must be an existing directory")
    if inventory_file_sha256 is not None and not _is_sha256(inventory_file_sha256):
        _fail("inventory-file-digest-invalid", "inventory_file_sha256 must be lowercase SHA-256")
    sealed, by_path, cases = _validate_inventory(inventory)
    decisions = _normalise_decisions(normalized_mapping, cases)

    current: dict[str, bytes] = {}
    modified_paths: set[str] = set()
    source_errors: list[dict[str, Any]] = []
    metadata_by_path: dict[str, dict[str, Any]] = {}
    tokens_by_path: dict[str, list[dict[str, Any]]] = {}
    for path, pin in by_path.items():
        try:
            resolved = _safe_relative_path(repository, path, "carrier_path")
            raw = resolved.read_bytes()
        except (OSError, SubjectNotationMigrationError):
            modified_paths.add(path)
            source_errors.append({"code": "source-frontier-changed", "carrier_path": path})
            continue
        if _sha256(raw) != pin["carrier_sha256"]:
            modified_paths.add(path)
            source_errors.append({"code": "source-frontier-changed", "carrier_path": path})
            continue
        try:
            tokens, metadata = _subject_tokens(raw, path)
        except SubjectNotationMigrationError as error:
            modified_paths.add(path)
            source_errors.append({"code": error.code, "carrier_path": path})
            continue
        if metadata["atom_id"] != pin["atom_id"] or metadata["version"] != pin["atom_revision"]:
            modified_paths.add(path)
            source_errors.append({"code": "source-revision-mismatch", "carrier_path": path})
            continue
        current[path] = raw
        metadata_by_path[path] = metadata
        tokens_by_path[path] = tokens

    case_status: dict[str, str] = {}
    case_rows: list[dict[str, Any]] = []
    affected_paths: set[str] = set(modified_paths)
    diagnostics: list[dict[str, Any]] = list(source_errors)
    for case_id in sorted(cases):
        case = cases[case_id]
        decision = decisions.get(case_id)
        paths = _case_paths(case)
        if decision is None:
            case_status[case_id] = "missing"
            affected_paths.update(paths)
            case_rows.append({"case_id": case_id, "status": "missing", "new_separator": None,
                              "confidence_percent": None, "source_paths": sorted(paths), "occurrence_count": len(case["occurrences"])})
            continue
        try:
            refs = _validate_decision_refs(case, decision, by_path, current)
        except SubjectNotationMigrationError as error:
            case_status[case_id] = "blocked"
            affected_paths.update(paths)
            diagnostics.append({"code": error.code, "case_id": case_id, "source_paths": sorted(paths)})
            case_rows.append({"case_id": case_id, "status": "blocked", "new_separator": decision["new_separator"],
                              "confidence_percent": decision["confidence_percent"], "source_paths": sorted(paths),
                              "occurrence_count": len(case["occurrences"])})
            continue
        if decision["disposition"] != "accepted":
            case_status[case_id] = "blocked"
            affected_paths.update(paths)
            case_rows.append({"case_id": case_id, "status": "blocked", "new_separator": decision["new_separator"],
                              "confidence_percent": decision["confidence_percent"], "source_paths": sorted(paths),
                              "occurrence_count": len(case["occurrences"]), "source_refs": refs})
            continue
        case_status[case_id] = "accepted"
        case_rows.append({"case_id": case_id, "status": "accepted", "new_separator": decision["new_separator"],
                          "confidence_percent": decision["confidence_percent"], "source_paths": sorted(paths),
                          "occurrence_count": len(case["occurrences"]), "source_refs": refs})

    case_by_key = {(case["old_parent"], case["old_child"]): case for case in cases.values()}
    candidate_changes: list[dict[str, Any]] = []
    path_diagnostics: list[dict[str, Any]] = []
    for path, raw in current.items():
        if path in modified_paths:
            continue
        tokens = tokens_by_path[path]
        # A carrier can be proposed only when every case touching it is
        # resolved.  This retains partial candidates from unaffected carriers
        # while keeping affected paths explicitly blocked.
        touching_ids = {
            case["case_id"]
            for case in cases.values()
            if path in _case_paths(case)
        }
        if any(case_status.get(case_id) != "accepted" for case_id in touching_ids):
            affected_paths.add(path)
            continue
        try:
            candidate, blocked, candidate_diagnostics = _candidate_for_source(path, raw, tokens, case_by_key, decisions, case_status)
        except SubjectNotationMigrationError as error:
            affected_paths.add(path)
            path_diagnostics.append({"code": error.code, "carrier_path": path})
            continue
        if blocked or candidate_diagnostics:
            affected_paths.add(path)
            path_diagnostics.extend(candidate_diagnostics)
            if blocked:
                path_diagnostics.append({"code": "unresolved-case-on-carrier", "carrier_path": path,
                                         "case_ids": sorted(blocked)})
            continue
        if candidate is None:
            continue
        candidate_bytes = candidate["candidate_bytes"]
        # Reparse the candidate to prove only Subject values changed and that
        # lexical order/cardinality remained intact.
        try:
            before_tokens, before_meta = _subject_tokens(raw, path)
            after_tokens, after_meta = _subject_tokens(candidate_bytes, path)
        except SubjectNotationMigrationError as error:
            affected_paths.add(path)
            path_diagnostics.append({
                "code": "subject-target-collision" if error.code == "subject-target-duplicate" else "candidate-reparse-failed",
                "carrier_path": path,
                "detail": error.code,
            })
            continue
        before_values = [(token["property_path"], token["ordinal"], token["value"]) for token in before_tokens]
        after_values = [(token["property_path"], token["ordinal"], token["value"]) for token in after_tokens]
        if [item[:2] for item in before_values] != [item[:2] for item in after_values]:
            affected_paths.add(path)
            path_diagnostics.append({"code": "candidate-order-changed", "carrier_path": path})
            continue
        if before_meta["fields"].get("atom_id") != after_meta["fields"].get("atom_id") or before_meta["fields"].get("version") != after_meta["fields"].get("version") or before_meta["fields"].get("updated_at") != after_meta["fields"].get("updated_at"):
            affected_paths.add(path)
            path_diagnostics.append({"code": "candidate-metadata-changed", "carrier_path": path})
            continue
        body_start = int(before_meta["body_start"])
        if raw[body_start:] != candidate_bytes[body_start:]:
            affected_paths.add(path)
            path_diagnostics.append({"code": "candidate-body-changed", "carrier_path": path})
            continue
        if any(before_values[index][0:2] != after_values[index][0:2] for index in range(len(before_values))):
            affected_paths.add(path)
            path_diagnostics.append({"code": "candidate-order-changed", "carrier_path": path})
            continue
        if any(before_values[index][2] == after_values[index][2] and before_values[index][2] != after_values[index][2] for index in range(len(before_values))):
            affected_paths.add(path)
            path_diagnostics.append({"code": "candidate-value-check-failed", "carrier_path": path})
            continue
        # A changed target may not duplicate another target in the same
        # relation collection.  This is checked on the reparsed values.
        for property_path in {item[0] for item in after_values}:
            values = [item[2] for item in after_values if item[0] == property_path]
            if len(values) != len(set(values)):
                affected_paths.add(path)
                path_diagnostics.append({"code": "subject-target-collision", "carrier_path": path, "property_path": property_path})
        if path in affected_paths:
            continue
        candidate_changes.append({
            "carrier_path": path,
            "source_pin": _copy_json(by_path[path]),
            "source_frontier_sha256": sealed["source_frontier"].get("source_frontier_sha256"),
            "atom_id": metadata_by_path[path]["atom_id"],
            "atom_revision": metadata_by_path[path]["version"],
            "version": metadata_by_path[path]["version"],
            "updated_at": metadata_by_path[path]["updated_at"],
            "current": True,
            "before_sha256": _sha256(raw),
            "candidate_sha256": _sha256(candidate_bytes),
            "body_sha256": _sha256(raw[body_start:]),
            "patches": candidate["patches"],
            "changed_fields": ["subjects"],
        })
    diagnostics.extend(path_diagnostics)

    missing_case_ids = sorted(case_id for case_id, status in case_status.items() if status == "missing")
    blocked_case_ids = sorted(case_id for case_id, status in case_status.items() if status == "blocked")
    reasons: list[str] = []
    if missing_case_ids:
        reasons.append("missing-cases")
    if blocked_case_ids:
        reasons.append("blocked-cases")
    if modified_paths:
        reasons.append("source-frontier-changed")
    if diagnostics:
        reasons.append("candidate-validation-failed")
    if not candidate_changes:
        reasons.append("zero-ops")
    reasons = sorted(set(reasons))
    global_status = "ready_for_governed_apply" if not reasons else "blocked"
    result: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "kind": "subject_notation_migration_dry_run",
        "mode": "dry-run",
        "apply_supported": False,
        "inventory_sha256": sealed["inventory_sha256"],
        "inventory_file_sha256": inventory_file_sha256,
        "source_frontier_sha256": sealed["source_frontier"].get("source_frontier_sha256"),
        "case_count": len(cases),
        "decision_count": len(decisions),
        "accepted_case_count": sum(status == "accepted" for status in case_status.values()),
        "missing_case_ids": missing_case_ids,
        "blocked_case_ids": blocked_case_ids,
        "affected_paths": sorted(affected_paths),
        "global_status": global_status,
        "blocked_reasons": reasons,
        "cases": case_rows,
        "candidate_changes": sorted(candidate_changes, key=lambda item: item["carrier_path"]),
        "diagnostics": sorted(diagnostics, key=lambda item: canonical_json_bytes(item)),
        "native_fact_admission": "not_performed",
        "source_mutation": False,
    }
    result["changeset_sha256"] = canonical_digest(result)
    return result


def build_dry_run(repository: Path | str, inventory: Mapping[str, Any], normalized_mapping: Sequence[Mapping[str, Any]] | Mapping[str, Any], *, inventory_file_sha256: str | None = None) -> dict[str, Any]:
    """Alias retained for callers that name the operation by its mode."""

    return build_changeset(repository, inventory, normalized_mapping, inventory_file_sha256=inventory_file_sha256)


def prepare_subject_notation_changeset(repository: Path | str, inventory: Mapping[str, Any], normalized_mapping: Sequence[Mapping[str, Any]] | Mapping[str, Any], *, inventory_file_sha256: str | None = None) -> dict[str, Any]:
    """Explicitly named public entry point for the root integration lane."""

    return build_changeset(repository, inventory, normalized_mapping, inventory_file_sha256=inventory_file_sha256)


def _load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        _fail("json-input-invalid", f"cannot load JSON input: {path}")
        raise AssertionError from error


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=Path, default=Path.cwd())
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--decisions", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        inventory = _load_json(args.inventory)
        decisions = _load_json(args.decisions)
        if not isinstance(inventory, Mapping):
            _fail("inventory-invalid", "inventory JSON must be an object")
        file_sha = _sha256(args.inventory.read_bytes())
        result = build_changeset(args.repository, inventory, decisions, inventory_file_sha256=file_sha)
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
        return 0
    except SubjectNotationMigrationError as error:
        print(f"subject notation dry-run refused: {error.code}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
