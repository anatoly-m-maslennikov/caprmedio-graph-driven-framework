"""Requirement-only Core Term declaration admission.

The profile is deliberately narrow.  It admits a declared Core-model Term
only after checking the complete registered Core authority frontier, twelve
fixed governing sources, an exact raw Scope/Claim/GOVERNS locator triplet,
and whole-frontier terminal cardinality.  It never turns a Claim into a
project implementation fact.
"""

from __future__ import annotations

import hashlib
import json
import re
import tomllib
from collections import defaultdict
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from types import MappingProxyType

import generate_entity_graph as graph


_TOKEN = object()
_MODULE_PATH = Path(__file__).resolve()
_LOADED_PROFILE_CODE_SHA256 = hashlib.sha256(_MODULE_PATH.read_bytes()).hexdigest()
_CORE_SCOPE = "CORE_META_MODEL"
_STRUCTURE_PATH = ".caprmedio_caprmedio/project_structure.toml"
_REQUIRED_AUTHORITIES = {
    "CA-M-310": (5, "b41cd2dfe70813a227d0253e717c5d39ac6d5cb842ea72524ce0582476ed0db6", "Method", "05_method/CA-M-310-CORE_META_MODEL--write-requirement-claims-with-the-requirement-cce-profile.md"),
    "CA-D-280": (12, "1f4289f4d3c0e0b832b4017edf7dac48f505802c8e65daafe7383c8264f68849", "Delivery", "07_delivery/CA-D-280-CORE_META_MODEL-DELIVERY--serialize-cce-operators-in-bold.md"),
    "CA-D-495": (1, "60bb7faad37efa795acd0a730b8af40c6759fd29cbf435aa4ea1599902088234", "Delivery", "07_delivery/CA-D-495-CORE_META_MODEL-CORE-DELIVERY--carry-applicability-in-the-registered-body-sections.md"),
    "CA-D-478": (5, "a40ad3683ecddd536e5b7eb6c044e8da15806ab44946fa1354c408ce5e966464", "Delivery", "07_delivery/CA-D-478-CORE_META_MODEL-CORE-DELIVERY--store-every-atom-property-in-one-internal-location.md"),
    "CA-R-1279": (12, "80e2ba7b9461cf5909891d3c7c2c2bcd12baccc161b7a86f7b977552a61666d5", "Requirement", "04_requirement/CA-R-1279-CORE_META_MODEL-CORE-REQUIREMENT--govern-every-defined-term.md"),
    "CA-R-126": (17, "433949d977649ee9622dffaec028e899ec725a6c9b3edf8b34c3a9537093f562", "Requirement", "04_requirement/CA-R-126-CORE_META_MODEL-CORE--give-each-governed-term-one-definition-atom.md"),
    "CA-R-1318": (11, "b30f5d73b9c4aff8cfc69c228a2ed4759c9d260297162cea46d0f42b75dd6e6b", "Requirement", "04_requirement/CA-R-1318-CORE_META_MODEL-CORE-REQUIREMENT--define-term.md"),
    "CA-R-1319": (10, "9c7f8ebf078c05a7d5ebef82ddec4e0903d269a387341a5c7fb6731b8ffbea58", "Requirement", "04_requirement/CA-R-1319-CORE_META_MODEL-CORE--define-governed-term.md"),
    "CA-R-1335": (13, "98ef6a5058ada19dd51563545a1c3ad46e8b18a637305dce90dde15eb5bfddf1", "Requirement", "04_requirement/CA-R-1335-CORE_META_MODEL-CORE-REQUIREMENT--define-terms-graph.md"),
    "CA-M-114": (20, "16513dca0a7370d9a98999f537da293fd8d14ae4d9a47fee7f70fb1f8a9b1dd6", "Method", "05_method/CA-M-114-CORE_META_MODEL--derive-terminology-projection-from-definition-atoms.md"),
    "CA-D-479": (6, "0819f8433cde89484e21a200466504a9fdcad31b58958c777a761637fbb45ff1", "Delivery", "07_delivery/CA-D-479-CORE_META_MODEL-DELIVERY--use-stable-headings-for-atom-body-properties.md"),
    "CA-R-1454": (7, "bab78ca52edb070123af5d40dd61fe4f44cf70941253aeb6aaf9deab0a5283f5", "Requirement", "04_requirement/CA-R-1454-CORE_META_MODEL-GENERAL--derive-governed-terms-views-from-selected-authority.md"),
}
_CLAIM_PRIMARY_ROLES = frozenset({"Requirement", "Method", "Evaluation", "Delivery"})
_TERM_SYSTEM_AUTHORITY_IDS = frozenset({"CA-R-1318", "CA-R-1319", "CA-R-1335"})
_FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
_HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
_MEANS = re.compile(r"\*\*means\*\*", re.IGNORECASE)
_DECLARATION = re.compile(
    r"(?:the\s+Term\s+|the\s+|an?\s+)?([A-Za-z][A-Za-z0-9 -]*?)\s+\*\*means\*\*\s+(\S.*)",
    re.IGNORECASE,
)


class CoreTermAdmissionError(ValueError):
    """Stable failure for stale, foreign or malformed checked inputs."""


@dataclass(frozen=True, slots=True)
class SourceRef:
    atom_id: str
    atom_revision: int
    carrier_path: str
    carrier_sha256: str
    contribution: Mapping[str, object]

    def as_dict(self) -> dict[str, object]:
        return {
            "atom_id": self.atom_id,
            "atom_revision": self.atom_revision,
            "carrier_path": self.carrier_path,
            "carrier_sha256": self.carrier_sha256,
            "contribution": dict(self.contribution),
        }


@dataclass(frozen=True, slots=True)
class CheckedRequirementSource:
    """Factory-checked source input; unresolved grammar is explicit state."""

    atom_id: str
    atom_revision: int
    carrier_path: str
    carrier_sha256: str
    content_role: str
    status: str
    subject_path: str | None
    term_identity: str | None
    claim_source: SourceRef | None
    scope_source: SourceRef | None
    governs_source: SourceRef | None
    unresolved_codes: tuple[str, ...]
    _token: object


@dataclass(frozen=True, slots=True)
class CoreTermProfile:
    authority_path: str
    authority_inputs: tuple[SourceRef, ...]
    selected_atom_ids: tuple[str, ...]
    terminal_carriers: Mapping[str, tuple[str, ...]]
    selected_metadata: Mapping[str, Mapping[str, str]]
    frontier_complete: bool
    frontier_diagnostics: tuple[str, ...]
    profile_sha256: str
    profile_code_sha256: str
    _token: object


def _canonical(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def _digest(value: object) -> str:
    return hashlib.sha256(_canonical(value)).hexdigest()


def _current_code() -> None:
    try:
        current = hashlib.sha256(_MODULE_PATH.read_bytes()).hexdigest()
    except OSError as error:
        raise CoreTermAdmissionError("profile code cannot be reread") from error
    if current != _LOADED_PROFILE_CODE_SHA256:
        raise CoreTermAdmissionError("profile code changed after import")


def _safe_path(repository: Path, value: object) -> Path:
    if not isinstance(value, str) or not value or "\\" in value or "\x00" in value:
        raise CoreTermAdmissionError("carrier path is not canonical POSIX text")
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or path.as_posix() != value:
        raise CoreTermAdmissionError("carrier path is not repository-relative")
    resolved = (repository / value).resolve()
    if not resolved.is_relative_to(repository) or resolved.relative_to(repository).as_posix() != value:
        raise CoreTermAdmissionError("carrier path aliases or escapes the repository")
    return resolved


def _scalar(value: str) -> str:
    value = value.strip()
    if len(value) > 1 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def _raw_carrier(raw: bytes) -> tuple[list[bytes], list[str], int, dict[str, str]]:
    try:
        lines = raw.splitlines(keepends=True)
        text = [line.decode("utf-8").rstrip("\r\n") for line in lines]
    except UnicodeDecodeError as error:
        raise CoreTermAdmissionError("carrier is not UTF-8") from error
    if not text or text[0] != "---":
        raise CoreTermAdmissionError("carrier has no frontmatter")
    boundary = next((index for index, line in enumerate(text[1:], 1) if line == "---"), None)
    if boundary is None:
        raise CoreTermAdmissionError("carrier frontmatter is unterminated")
    fields: dict[str, str] = {}
    for line in text[1:boundary]:
        match = re.fullmatch(r"([A-Za-z_][A-Za-z0-9_-]*):[ \t]*(.*)", line)
        if match:
            if match[1] in fields:
                raise CoreTermAdmissionError("carrier has duplicate frontmatter key")
            fields[match[1]] = _scalar(match[2])
    return lines, text, boundary, fields


def _pin(repository: Path, carrier: object) -> tuple[dict[str, object], bytes, dict[str, str], list[bytes], list[str], int]:
    names = (
        "atom_id", "version", "carrier_path", "sha256", "content_role", "atom_type", "status",
        "cce_form", "frontmatter", "body",
    )
    if isinstance(carrier, Mapping) or any(not hasattr(carrier, name) for name in names):
        raise CoreTermAdmissionError("AtomCarrier object is incomplete")
    if not isinstance(carrier.atom_id, str) or not carrier.atom_id or type(carrier.version) is not int or carrier.version < 1:
        raise CoreTermAdmissionError("carrier identity is invalid")
    if not isinstance(carrier.sha256, str) or not re.fullmatch(r"[0-9a-f]{64}", carrier.sha256):
        raise CoreTermAdmissionError("carrier hash is invalid")
    path = _safe_path(repository, carrier.carrier_path)
    try:
        raw = path.read_bytes()
    except OSError as error:
        raise CoreTermAdmissionError("carrier cannot be reread") from error
    if hashlib.sha256(raw).hexdigest() != carrier.sha256:
        raise CoreTermAdmissionError("carrier bytes are stale")
    lines, text, boundary, fields = _raw_carrier(raw)
    frontmatter_end = sum(len(line) for line in lines[:boundary])
    raw_frontmatter = raw[len(lines[0]):frontmatter_end]
    if raw_frontmatter.endswith(b"\r\n"):
        raw_frontmatter = raw_frontmatter[:-2]
    elif raw_frontmatter.endswith(b"\n"):
        raw_frontmatter = raw_frontmatter[:-1]
    try:
        current_frontmatter = raw_frontmatter.decode("utf-8")
        current_body = b"".join(lines[boundary + 1:]).decode("utf-8")
    except UnicodeDecodeError as error:
        raise CoreTermAdmissionError("carrier is not UTF-8") from error
    actual = {
        "atom_id": fields.get("atom_id"), "version": fields.get("version"),
        "content_role": fields.get("content_role", ""), "type": fields.get("type", ""),
        "cce_form": fields.get("cce_form", "").lower(),
        "status": fields.get("status", "legacy-unspecified"),
    }
    expected = {
        "atom_id": carrier.atom_id, "version": str(carrier.version),
        "content_role": carrier.content_role, "type": carrier.atom_type,
        "cce_form": carrier.cce_form, "status": carrier.status,
    }
    if actual != expected or carrier.frontmatter != current_frontmatter or carrier.body != current_body:
        raise CoreTermAdmissionError("carrier metadata disagrees with actual bytes")
    return (
        {"atom_id": carrier.atom_id, "atom_revision": carrier.version,
         "carrier_path": carrier.carrier_path, "carrier_sha256": carrier.sha256},
        raw, fields, lines, text, boundary,
    )


def _body_headings(text: list[str], boundary: int) -> tuple[list[tuple[int, int, str]], list[bool]]:
    visible = [True] * len(text)
    headings: list[tuple[int, int, str]] = []
    fence: tuple[str, int] | None = None
    for index in range(boundary + 1, len(text)):
        line = text[index]
        if line.lstrip().startswith(">"):
            visible[index] = False
            continue
        marker = _FENCE.match(line)
        if fence is not None:
            visible[index] = False
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= fence[1] and not marker[2].strip():
                fence = None
            continue
        if marker:
            visible[index] = False
            fence = (marker[1][0], len(marker[1]))
            continue
        heading = _HEADING.match(line)
        if heading:
            headings.append((index, len(heading[1]), heading[2]))
    return headings, visible


def _registered_rmed_layout(text: list[str], boundary: int) -> bool:
    """Require D479's literal RMED body headings without widening the grammar."""

    headings, _ = _body_headings(text, boundary)
    top_level = [(index, text[index]) for index, level, _ in headings if level <= 2]
    expected = ["# Summary", "## Scope", "## Claim", "## Details"]
    if [line for _, line in top_level] != expected:
        return False
    details_index = top_level[-1][0]
    return not any(level > 2 and index < details_index for index, level, _ in headings)


def _normalized_raw_scope(value: str) -> str:
    """Normalize only harmless formatting before detecting a structural scope copy."""

    normalized = " ".join(value.split())
    if normalized.endswith("."):
        normalized = normalized[:-1].rstrip()
    if len(normalized) >= 2 and normalized[0] == normalized[-1] == "`":
        normalized = normalized[1:-1].strip()
    return normalized


def _source(pin: Mapping[str, object], lines: list[bytes], start: int, end: int, **location: object) -> SourceRef:
    if start < 1 or end < start or end > len(lines):
        raise CoreTermAdmissionError("source contribution span is invalid")
    contribution = {**location, "start_line": start, "end_line": end,
                    "text_sha256": hashlib.sha256(b"".join(lines[start - 1:end])).hexdigest()}
    return SourceRef(str(pin["atom_id"]), int(pin["atom_revision"]), str(pin["carrier_path"]),
                     str(pin["carrier_sha256"]), MappingProxyType(contribution))


def _section_source(pin: Mapping[str, object], lines: list[bytes], text: list[str], boundary: int,
                    section: str, *, kind: str) -> tuple[SourceRef | None, str | None, str | None]:
    headings, visible = _body_headings(text, boundary)
    matches = [item for item in headings if item[1] == 2 and item[2] == section]
    if len(matches) != 1:
        return None, None, f"{section.casefold()}-section-{'missing' if not matches else 'duplicate'}"
    start_index, level, _ = matches[0]
    end_index = next((index for index, heading_level, _ in headings if index > start_index and heading_level <= level), len(lines))
    visible_content = "\n".join(text[index] for index in range(start_index + 1, end_index)
                                if visible[index]).strip()
    if not visible_content:
        return None, None, f"{section.casefold()}-section-empty"
    return _source(pin, lines, start_index + 2, end_index, kind=kind, section=section), visible_content, None


def _governs_source(pin: Mapping[str, object], lines: list[bytes], text: list[str], boundary: int) -> tuple[SourceRef | None, str | None, str | None, str | None]:
    subject_index = next((index for index in range(1, boundary) if text[index] == "subjects:"), None)
    if subject_index is None:
        return None, None, None, "governs-missing"
    matches = []
    noncanonical_scalar = False
    for index in range(subject_index + 1, boundary):
        line = text[index]
        if line and not line[0].isspace():
            break
        match = re.fullmatch(r"  governs:[ \t]*(.+)", line)
        if match:
            raw_value = match[1]
            value = _scalar(raw_value)
            if "\\" in raw_value or any(ord(character) < 32 or ord(character) == 127 for character in raw_value):
                noncanonical_scalar = True
                continue
            if value and value[0] not in "[{*&!|>":
                matches.append((index, value))
    if noncanonical_scalar:
        return None, None, None, "governs-noncanonical-scalar"
    if len(matches) != 1:
        return None, None, None, "governs-missing" if not matches else "governs-duplicate-or-nonscalar"
    index, subject_path = matches[0]
    terminal = subject_path.rsplit("/", 1)[-1].strip()
    if ":" in terminal:
        terminal = terminal.rsplit(":", 1)[-1].strip()
    if not terminal:
        return None, None, None, "governs-terminal-invalid"
    return (
        _source(pin, lines, index + 1, index + 1, kind="canonical_atom_property", property_path="subjects.governs"),
        subject_path, terminal, None,
    )


def _structure_authority_path(repository: Path) -> str:
    path = _safe_path(repository, _STRUCTURE_PATH)
    try:
        rows = tomllib.loads(path.read_text(encoding="utf-8")).get("scope_units", [])
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise CoreTermAdmissionError("registered Project Structure cannot be read") from error
    matches = [row for row in rows if isinstance(row, dict) and row.get("scope_unit_name") == _CORE_SCOPE]
    if len(matches) != 1 or matches[0].get("authority_mode") != "strict":
        raise CoreTermAdmissionError("CORE_META_MODEL registration is ambiguous or not strict")
    value = matches[0].get("authority_path")
    _safe_path(repository, value)
    return str(value)


def _frontier_selection(selection: object, available: set[str]) -> tuple[str, ...]:
    if not isinstance(selection, Mapping) or set(selection) != {"atom_ids", "scope_unit_names"}:
        raise CoreTermAdmissionError("selection shape is not closed")
    atom_ids = selection.get("atom_ids")
    scopes = selection.get("scope_unit_names")
    if type(atom_ids) is not list or atom_ids != sorted(set(atom_ids)) or any(not isinstance(item, str) or not item for item in atom_ids):
        raise CoreTermAdmissionError("selection Atom identities are not canonical")
    if scopes != [_CORE_SCOPE] or set(atom_ids) - available:
        raise CoreTermAdmissionError("selection is not Core-owned and Core-targeted")
    return tuple(atom_ids)


def _profile_record(authority_path: str, authority_inputs: Sequence[SourceRef], selected: Sequence[str],
                    terminal_carriers: Mapping[str, Sequence[str]]) -> dict[str, object]:
    return {
        "id": "caprmedio.core-term-requirement-profile", "version": "1",
        "profile_code_sha256": _LOADED_PROFILE_CODE_SHA256, "authority_path": authority_path,
        "authority_inputs": [source.as_dict() for source in authority_inputs], "selected_atom_ids": list(selected),
        "terminal_cardinality": {term: sorted(carriers) for term, carriers in sorted(terminal_carriers.items())},
        "native_graph_context": "declared_core_model",
    }


def prepare_core_term_profile(repository: Path, authority_carriers: Sequence[object],
                              frontier: Mapping[str, object], selection: Mapping[str, object]) -> CoreTermProfile:
    """Bind this closed Requirement profile to the registered full Core frontier."""

    _current_code()
    repository = Path(repository).resolve(strict=True)
    authority_path = _structure_authority_path(repository)
    root = _safe_path(repository, authority_path)
    if not root.is_dir():
        raise CoreTermAdmissionError("registered Core authority path is unavailable")
    try:
        actual_carriers, discovery_diagnostics = graph.discover_atoms(repository, root)
        actual_frontier = graph.source_frontier_for(repository, root)
    except Exception as error:  # graph parser carries no trustworthy partial frontier
        raise CoreTermAdmissionError("registered Core authority frontier is malformed") from error
    if dict(frontier) != actual_frontier:
        raise CoreTermAdmissionError("registered Core authority frontier is stale or incomplete")
    if not isinstance(authority_carriers, Sequence) or isinstance(authority_carriers, (str, bytes)):
        raise CoreTermAdmissionError("authority carriers must be a complete sequence")
    expected = [(carrier.atom_id, carrier.version, carrier.carrier_path, carrier.sha256) for carrier in actual_carriers]
    supplied = [(getattr(carrier, "atom_id", None), getattr(carrier, "version", None),
                 getattr(carrier, "carrier_path", None), getattr(carrier, "sha256", None)) for carrier in authority_carriers]
    if supplied != expected:
        raise CoreTermAdmissionError("authority carrier input is not the complete current Core frontier")
    selected = _frontier_selection(selection, {carrier.atom_id for carrier in actual_carriers})
    pins: dict[str, dict[str, object]] = {}
    raw_by_id: dict[str, tuple[bytes, dict[str, str], list[bytes], list[str], int]] = {}
    relations_by_id: dict[str, list[object]] = {}
    # The registered frontier deliberately excludes inactive/non-Atom files;
    # their informational discovery notices do not make the Active frontier
    # incomplete.  Only an actual discovery error can do that.
    diagnostics = [
        str(item.get("code"))
        for item in discovery_diagnostics
        if isinstance(item, Mapping) and item.get("severity") == "error" and item.get("code")
    ]
    for carrier in actual_carriers:
        pin, raw, fields, lines, text, boundary = _pin(repository, carrier)
        pins[carrier.atom_id] = pin
        raw_by_id[carrier.atom_id] = (raw, fields, lines, text, boundary)
        try:
            relations, _ = graph.parse_subject_relations(carrier)
        except Exception:
            relations = []
            diagnostics.append("frontier-subjects-malformed")
        relations_by_id[carrier.atom_id] = relations
    authority_inputs: list[SourceRef] = []
    for atom_id, (revision, digest, role, suffix) in _REQUIRED_AUTHORITIES.items():
        carrier = next((item for item in actual_carriers if item.atom_id == atom_id), None)
        if carrier is None or (carrier.version, carrier.sha256, carrier.content_role) != (revision, digest, role):
            raise CoreTermAdmissionError("required governing authority is missing or changed")
        if not carrier.carrier_path.startswith(authority_path + "/") or not carrier.carrier_path.endswith(suffix):
            raise CoreTermAdmissionError("required governing authority is outside registered Core path")
        _, _, lines, text, boundary = raw_by_id[atom_id]
        source, _, problem = _section_source(pins[atom_id], lines, text, boundary, "Claim", kind="primary_content")
        if source is None or problem is not None:
            raise CoreTermAdmissionError("required governing authority lacks one canonical Claim")
        authority_inputs.append(source)
    terminal_carriers: dict[str, list[str]] = defaultdict(list)
    for carrier in actual_carriers:
        governs = [row for row in relations_by_id[carrier.atom_id] if getattr(row, "kind", "") == "GOVERNS"]
        if len(governs) != 1 or not isinstance(getattr(governs[0], "subject_path", None), str):
            diagnostics.append("frontier-governs-not-singleton")
            continue
        terminal = governs[0].subject_path.rsplit("/", 1)[-1].strip()
        if ":" in terminal:
            terminal = terminal.rsplit(":", 1)[-1].strip()
        if not terminal:
            diagnostics.append("frontier-governs-terminal-invalid")
            continue
        terminal_carriers[terminal].append(carrier.atom_id)
    selected_metadata = {
        carrier.atom_id: MappingProxyType({
            "content_role": carrier.content_role, "status": carrier.status,
            "current_scope_unit": raw_by_id[carrier.atom_id][1].get("current_scope_unit", ""),
            "claim_target_scope_unit": raw_by_id[carrier.atom_id][1].get("claim_target_scope_unit", ""),
            "atom_revision": str(pins[carrier.atom_id]["atom_revision"]),
            "carrier_path": str(pins[carrier.atom_id]["carrier_path"]),
            "carrier_sha256": str(pins[carrier.atom_id]["carrier_sha256"]),
        }) for carrier in actual_carriers if carrier.atom_id in selected
    }
    authority_inputs.sort(key=lambda item: _source_key(item.as_dict()))
    profile_data = _profile_record(authority_path, authority_inputs, selected, terminal_carriers)
    return CoreTermProfile(
        authority_path, tuple(authority_inputs), selected,
        MappingProxyType({term: tuple(sorted(ids)) for term, ids in sorted(terminal_carriers.items())}),
        MappingProxyType(selected_metadata), not diagnostics, tuple(sorted(set(diagnostics))),
        _digest(profile_data), _LOADED_PROFILE_CODE_SHA256, _TOKEN,
    )


def checked_requirement_source(repository: Path, carrier: object, profile: CoreTermProfile) -> CheckedRequirementSource:
    """Re-open one selected source and return candidate or explicit unresolved state."""

    _current_code()
    if type(profile) is not CoreTermProfile or profile._token is not _TOKEN:
        raise CoreTermAdmissionError("reviewed Core Term profile is required")
    repository = Path(repository).resolve(strict=True)
    pin, _, fields, lines, text, boundary = _pin(repository, carrier)
    atom_id = str(pin["atom_id"])
    if atom_id not in profile.selected_atom_ids:
        raise CoreTermAdmissionError("source is outside the Core selection")
    expected = profile.selected_metadata.get(atom_id)
    current_pin = (
        str(pin["atom_revision"]), str(pin["carrier_path"]), str(pin["carrier_sha256"]),
    )
    reviewed_pin = None if expected is None else (
        expected.get("atom_revision"), expected.get("carrier_path"), expected.get("carrier_sha256"),
    )
    if current_pin != reviewed_pin:
        raise CoreTermAdmissionError("selected source does not match profile frontier")
    problems: list[str] = []
    content_role = fields.get("content_role", "")
    if content_role != "Requirement":
        problems.append("unhandled-content-role")
    if fields.get("status") != "Active" or fields.get("current_scope_unit") != _CORE_SCOPE or fields.get("claim_target_scope_unit") != _CORE_SCOPE:
        problems.append("selected-source-not-active-core-owner-target")
    claim_source = None
    claim_text = None
    scope_source = None
    if content_role in _CLAIM_PRIMARY_ROLES:
        claim_source, claim_text, claim_problem = _section_source(
            pin, lines, text, boundary, "Claim", kind="primary_content",
        )
        if claim_source is None:
            problems.append(str(claim_problem))
    if content_role == "Requirement":
        if any(key.casefold() == "scope" for key in fields):
            problems.append("frontmatter-scope-duplicate")
        if not _registered_rmed_layout(text, boundary):
            problems.append("registered-body-layout-unresolved")
        scope_source, scope_text, scope_problem = _section_source(
            pin, lines, text, boundary, "Scope", kind="canonical_atom_property",
        )
        if scope_source is None:
            problems.append(str(scope_problem))
        else:
            scope_values = {
                _normalized_raw_scope(value)
                for value in (fields.get("current_scope_unit", ""), fields.get("claim_target_scope_unit", ""))
                if value
            }
            if _normalized_raw_scope(scope_text) in scope_values:
                problems.append("scope-structural-copy")
    governs_source, governed_subject_path, terminal, governs_problem = _governs_source(pin, lines, text, boundary)
    if governs_problem is not None:
        problems.append(governs_problem)
    term_identity = None
    subject_path = None
    if content_role == "Requirement" and claim_text is not None:
        markers = list(_MEANS.finditer(claim_text))
        if len(markers) != 1 or markers[0].group(0) != "**means**":
            problems.append("claim-means-not-one-bold-lowercase")
        else:
            visible_lines = [line.strip() for line in claim_text.splitlines() if line.strip()]
            match = _DECLARATION.fullmatch(visible_lines[0]) if len(visible_lines) == 1 else None
            if match is None:
                problems.append("claim-grammar-unhandled")
            elif terminal is None or governed_subject_path is None:
                pass
            elif terminal is not None and match.group(1).strip() != terminal:
                problems.append("claim-terminal-mismatch")
            else:
                term_identity = match.group(1).strip()
                subject_path = governed_subject_path
    return CheckedRequirementSource(
        atom_id, int(pin["atom_revision"]), str(pin["carrier_path"]), str(pin["carrier_sha256"]),
        content_role, fields.get("status", ""), subject_path, term_identity,
        claim_source, scope_source, governs_source, tuple(sorted(set(problems))), _TOKEN,
    )


def _refs(*sources: SourceRef | None) -> list[dict[str, object]]:
    return _dedupe_source_dicts([source.as_dict() for source in sources if source is not None])


def _source_key(source: Mapping[str, object]) -> tuple[object, ...]:
    contribution = source.get("contribution")
    if not isinstance(contribution, Mapping):
        raise CoreTermAdmissionError("D539 source reference has no contribution")
    return (
        source.get("atom_id"), source.get("atom_revision"), source.get("carrier_path"),
        contribution.get("kind"), contribution.get("section", contribution.get("property_path", "")),
        contribution.get("canonical_target_reference", ""), contribution.get("start_line"),
        contribution.get("end_line"), contribution.get("text_sha256"),
    )


def _dedupe_source_dicts(sources: Sequence[Mapping[str, object]]) -> list[dict[str, object]]:
    unique: dict[tuple[object, ...], dict[str, object]] = {}
    for source in sources:
        key = _source_key(source)
        unique[key] = dict(source)
    return [unique[key] for key in sorted(unique)]


def _profile_descriptor(profile: CoreTermProfile) -> dict[str, str]:
    return {"id": "caprmedio.core-term-requirement-profile", "version": "1",
            "profile_sha256": profile.profile_sha256}


def review_core_term_candidates(sources: Sequence[CheckedRequirementSource], profile: CoreTermProfile) -> dict[str, object]:
    """Purely review factory-checked Requirement sources against a bound profile."""

    _current_code()
    if type(profile) is not CoreTermProfile or profile._token is not _TOKEN:
        raise CoreTermAdmissionError("reviewed Core Term profile is required")
    if any(type(source) is not CheckedRequirementSource or source._token is not _TOKEN for source in sources):
        raise CoreTermAdmissionError("factory-checked Requirement sources are required")
    if len({source.atom_id for source in sources}) != len(sources):
        raise CoreTermAdmissionError("selected source identities must be unique")
    if set(source.atom_id for source in sources) - set(profile.selected_atom_ids):
        raise CoreTermAdmissionError("checked source lies outside profile selection")
    candidates: list[dict[str, object]] = []
    decisions: list[dict[str, object]] = []
    admitted: list[dict[str, object]] = []
    diagnostics: list[dict[str, object]] = []
    observed = {source.atom_id for source in sources}
    missing = sorted(set(profile.selected_atom_ids) - observed)
    for atom_id in missing:
        diagnostics.append({"code": "selected-source-unreviewed", "severity": "warning", "source_refs": [],
                            "details": {"atom_id": atom_id}})
    for source in sorted(sources, key=lambda item: item.atom_id):
        refs = _refs(source.claim_source, source.scope_source, source.governs_source)
        if source.term_identity is not None and source.subject_path is not None and source.claim_source is not None:
            candidate = {
                "candidate_id": f"core-term:{source.atom_id}:{source.atom_revision}",
                "fact_class": "definition",
                "payload": {"term_identity": source.term_identity, "subject_path": source.subject_path},
                "recognizer": _profile_descriptor(profile),
                "source_ref": source.claim_source.as_dict(),
            }
            candidates.append(candidate)
            collision = len(profile.terminal_carriers.get(source.term_identity, ())) != 1
            unresolved = list(source.unresolved_codes)
            if not profile.frontier_complete:
                unresolved.append("authority-frontier-incomplete")
            if collision:
                unresolved.append("same-terminal-frontier-collision")
            authority_inputs = _dedupe_source_dicts([*[_ref.as_dict() for _ref in profile.authority_inputs], *refs])
            term_system_authority = _refs(*[
                reference for reference in profile.authority_inputs
                if reference.atom_id in _TERM_SYSTEM_AUTHORITY_IDS
            ])
            base = {
                "candidate_id": candidate["candidate_id"],
                "disposition": "unresolved" if unresolved else "admitted",
                "evaluator": _profile_descriptor(profile),
                "authority_inputs": authority_inputs,
                "checks": [
                    {"code": "fixed-profile-code-current", "disposition": "pass", "source_refs": []},
                    {"code": "current-core-governing-authority-bound", "disposition": "pass", "source_refs": _refs(*profile.authority_inputs)},
                    {"code": "term-definition-governed-term-terms-graph-authority-bound", "disposition": "pass", "source_refs": term_system_authority},
                    {"code": "requirement-scope-claim-governs-bound", "disposition": "pass" if not source.unresolved_codes else "unresolved", "source_refs": refs},
                    {"code": "complete-frontier-terminal-cardinality", "disposition": "unresolved" if collision else "pass", "source_refs": _refs(source.governs_source)},
                ],
            }
            if not profile.frontier_complete:
                base["checks"].append({"code": "complete-core-frontier", "disposition": "unresolved", "source_refs": []})
            base["checks"].sort(key=lambda item: item["code"])
            base["decision_sha256"] = _digest(base)
            decisions.append(base)
            if base["disposition"] == "admitted":
                admitted.append({
                    "fact_id": "fact:" + candidate["candidate_id"], "candidate_id": candidate["candidate_id"],
                    "fact_class": "definition",
                    "payload": candidate["payload"], "decision_sha256": base["decision_sha256"],
                })
            else:
                diagnostics.append({"code": "term-declaration-unresolved", "severity": "warning", "source_refs": refs,
                                    "details": {"atom_id": source.atom_id, "reasons": sorted(set(unresolved))}})
        else:
            diagnostics.append({"code": "term-source-grammar-unhandled", "severity": "warning", "source_refs": refs,
                                "details": {"atom_id": source.atom_id, "atom_revision": source.atom_revision,
                                            "carrier_path": source.carrier_path, "carrier_sha256": source.carrier_sha256,
                                            "reasons": list(source.unresolved_codes)}})
    unsupported_count = len([row for row in diagnostics if row["code"] == "term-source-grammar-unhandled"])
    unresolved_count = len(missing) + unsupported_count + sum(1 for decision in decisions if decision["disposition"] != "admitted")
    complete = not missing and not unresolved_count and profile.frontier_complete
    coverage = [
        {
            "fact_class": "definition", "disposition": "complete" if complete else "unknown",
            "selected_result": "empty" if not profile.selected_atom_ids else "nonempty" if complete else "unknown",
            "candidate_count": len(candidates), "admitted_count": len(admitted),
            "source_refs": _dedupe_source_dicts([candidate["source_ref"] for candidate in candidates]),
        },
        {
            "fact_class": "relation", "disposition": "unknown", "selected_result": "unknown",
            "candidate_count": 0, "admitted_count": 0, "source_refs": [],
        },
    ]
    diagnostics.sort(key=lambda item: (item["code"], _canonical(item["details"])))
    return {
        "native_graph_context": "declared_core_model", "provider": _profile_descriptor(profile),
        "candidates": candidates, "admission_decisions": decisions, "admitted_facts": admitted,
        "coverage": coverage, "diagnostics": diagnostics,
    }
