"""Checked, immutable D539 fact contexts; recognition never grants admission.

Bounded Core profiles can admit individually proven definitions. Unsupported
source families remain unresolved, and registry metadata alone admits no
Relation fact. The selected Core view is not project-effective methodology.
"""

from __future__ import annotations

import hashlib
import json
import re
import tomllib
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path, PurePosixPath


class FactContextError(ValueError):
    """Invalid or stale factory input, with a stable, non-secret error code."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(message)


def _fail(code: str, message: str) -> None:
    raise FactContextError(code, message)


def _json_value(value: object, ancestors: set[int]) -> None:
    if value is None or type(value) in (bool, int):
        return
    if isinstance(value, str):
        if any(0xD800 <= ord(character) <= 0xDFFF for character in value):
            _fail("context-json-invalid", "Unpaired surrogates are not canonical JSON")
        return
    if type(value) not in (dict, list):
        _fail("context-json-invalid", "Only integer-valued JSON objects are supported")
    identity = id(value)
    if identity in ancestors:
        _fail("context-json-invalid", "Canonical JSON cannot contain a cycle")
    ancestors.add(identity)
    if type(value) is dict:
        for key, item in value.items():
            if not isinstance(key, str):
                _fail("context-json-invalid", "Canonical JSON object keys must be strings")
            _json_value(key, ancestors)
            _json_value(item, ancestors)
    else:
        for item in value:
            _json_value(item, ancestors)
    ancestors.remove(identity)


def canonical_bytes(value: object) -> bytes:
    """The D539 byte rule: no floats, surrogates, normalization or newline."""
    _json_value(value, set())
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")


def _digest(value: object) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


_FACTORY_TOKEN = object()
_IMPLEMENTATION_PATH = Path(__file__).resolve()
# Never label already-loaded code with the digest of a later disk revision.
_LOADED_IMPLEMENTATION_SHA256 = hashlib.sha256(_IMPLEMENTATION_PATH.read_bytes()).hexdigest()
# This locator profile was checked against these actual assignment authorities.
# A changed authority is an unsupported profile, never an inferred assignment.
_DETAILS_ASSIGNMENT_PINS = (
    ("CA-D-478", 5, "a40ad3683ecddd536e5b7eb6c044e8da15806ab44946fa1354c408ce5e966464"),
    ("CA-D-479", 6, "0819f8433cde89484e21a200466504a9fdcad31b58958c777a761637fbb45ff1"),
    ("CA-R-1624", 2, "d985c624f5c0b92010a3f1a670e2e12ef0d018aa221ce1052faab293060966cf"),
)


def _check_loaded_profile() -> None:
    try:
        current = hashlib.sha256(_IMPLEMENTATION_PATH.read_bytes()).hexdigest()
    except OSError:
        _fail("profile-stale", "The loaded implementation cannot be checked against current bytes")
    if current != _LOADED_IMPLEMENTATION_SHA256:
        _fail("profile-stale", "Implementation bytes changed after this profile was loaded")


@dataclass(frozen=True, slots=True, init=False)
class DerivedFactContext:
    """An in-process factory result, not a deserializable caller capability."""

    _bytes: bytes
    _provenance_bytes: bytes
    _factory_token: object

    def __init__(self, data: bytes, provenance: bytes, *, _token: object = None) -> None:
        if _token is not _FACTORY_TOKEN:
            _fail("context-untrusted", "A fact context must be prepared by the checked factory")
        object.__setattr__(self, "_bytes", data)
        object.__setattr__(self, "_provenance_bytes", provenance)
        object.__setattr__(self, "_factory_token", _token)

    def as_dict(self) -> dict[str, object]:
        _trusted(self)
        return json.loads(self._bytes)

    @property
    def context_sha256(self) -> str:
        return self.as_dict()["context_sha256"]


def _trusted(context: object) -> None:
    if type(context) is not DerivedFactContext or getattr(context, "_factory_token", None) is not _FACTORY_TOKEN:
        _fail("context-untrusted", "Caller JSON is not a prepared fact context")


def context_evidence(context: DerivedFactContext) -> dict[str, object]:
    _trusted(context)
    data = context.as_dict()
    return {key: data[key] for key in ("context_sha256", "provider", "source_binding", "coverage")}


def verified_context(context: DerivedFactContext, repository: Path, graph_kind: str,
                     carriers: Sequence, selection: Mapping, source_frontier: Mapping,
                     authority_sources: Sequence) -> DerivedFactContext:
    """Reprepare current evidence and reject stale, foreign or caller contexts."""
    _trusted(context)
    current = prepare_fact_context(repository, graph_kind, carriers, selection,
                                   source_frontier, authority_sources)
    if context._bytes != current._bytes or context._provenance_bytes != current._provenance_bytes:
        _fail("context-binding-stale", "Fact context does not match current source, selection and profile bindings")
    return current


def _safe_path(repository: Path, value: object, *, folder: bool = False) -> Path:
    if not isinstance(value, str) or not value or "\\" in value or "\x00" in value:
        _fail("context-path-invalid", "A source path must be canonical repository-relative POSIX text")
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or value != path.as_posix() or (value == "." and not folder):
        _fail("context-path-invalid", "A source path must be canonical repository-relative POSIX text")
    resolved = (repository / value).resolve()
    if not resolved.is_relative_to(repository):
        _fail("context-path-invalid", "A source path escapes the repository")
    if resolved.relative_to(repository).as_posix() != value:
        _fail("context-path-ambiguous", "A source path alias does not match its canonical repository-relative path")
    return resolved


def _scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
        return value[1:-1]
    return value


def _raw_parts(raw: bytes) -> tuple[list[bytes], list[str], int, dict[str, str]]:
    try:
        lines = raw.splitlines(keepends=True)
        text = [line.decode("utf-8").rstrip("\r\n") for line in lines]
    except UnicodeDecodeError:
        _fail("context-carrier-invalid", "An authoritative Carrier is not UTF-8")
    if not text or text[0] != "---":
        _fail("context-carrier-invalid", "An authoritative Atom requires frontmatter")
    boundaries = [index for index, line in enumerate(text[1:], 1) if line == "---"]
    if not boundaries:
        _fail("context-carrier-invalid", "Authoritative Atom frontmatter is unterminated")
    boundary = boundaries[0]
    fields: dict[str, str] = {}
    for line in text[1:boundary]:
        match = re.fullmatch(r"([A-Za-z_][A-Za-z_0-9-]*):[ \t]*(.*)", line)
        if match:
            if match[1] in fields:
                _fail("context-carrier-duplicate", "An authoritative Carrier has duplicate frontmatter keys")
            fields[match[1]] = _scalar(match[2])
    return lines, text, boundary, fields


def _carrier_pin(repository: Path, carrier: object) -> tuple[dict[str, object], bytes]:
    if isinstance(carrier, Mapping):
        _fail("context-carrier-invalid", "Carrier objects, not caller evidence JSON, are required")
    names = ("atom_id", "version", "carrier_path", "sha256", "content_role", "atom_type", "status")
    if any(not hasattr(carrier, name) for name in names):
        _fail("context-carrier-invalid", "An AtomCarrier input is incomplete")
    atom_id, version = carrier.atom_id, carrier.version
    if not isinstance(atom_id, str) or not atom_id or type(version) is not int or version < 1:
        _fail("context-carrier-invalid", "Atom identity and revision are invalid")
    if not isinstance(carrier.sha256, str) or not re.fullmatch(r"[0-9a-f]{64}", carrier.sha256):
        _fail("context-carrier-invalid", "Carrier digest must be lowercase SHA-256")
    path = _safe_path(repository, carrier.carrier_path)
    try:
        raw = path.read_bytes()
    except OSError:
        _fail("context-carrier-unreadable", "An authoritative Carrier cannot be read")
    if hashlib.sha256(raw).hexdigest() != carrier.sha256:
        _fail("context-source-stale", "An authoritative Carrier no longer matches its bound bytes")
    _, _, _, fields = _raw_parts(raw)
    if fields.get("atom_id") != atom_id or fields.get("version") != str(version):
        _fail("context-carrier-identity", "Carrier identity or revision disagrees with its current bytes")
    expected = {"content_role": carrier.content_role, "type": carrier.atom_type,
                "status": carrier.status}
    if any(fields.get(key, "legacy-unspecified" if key == "status" else "") != value
           for key, value in expected.items()):
        _fail("context-carrier-identity", "Carrier metadata disagrees with its current bytes")
    if not fields.get("status"):
        _fail("context-lifecycle-unbound", "An authoritative Carrier requires an explicit nonempty lifecycle value")
    # Byte/pin validation is not lifecycle admission. Concern's role model,
    # for example, declares lowercase `active`; other roles declare `Active`.
    # Keep exact source values and require each semantic profile's own model.
    pin = {"atom_id": atom_id, "atom_revision": version, "carrier_path": carrier.carrier_path,
           "carrier_sha256": carrier.sha256}
    return pin, raw


def _pool(repository: Path, carriers: object) -> dict[str, tuple[object, dict[str, object], bytes]]:
    if not isinstance(carriers, Sequence) or isinstance(carriers, (str, bytes)):
        _fail("context-carrier-invalid", "Carrier inputs must be a sequence")
    result = {}
    paths = set()
    for carrier in carriers:
        pin, raw = _carrier_pin(repository, carrier)
        if pin["atom_id"] in result or pin["carrier_path"] in paths:
            _fail("context-carrier-duplicate", "Carrier identities and paths must be unique")
        result[pin["atom_id"]] = (carrier, pin, raw)
        paths.add(pin["carrier_path"])
    return result


def _selection(value: object, available: set[str]) -> dict[str, list[str]]:
    if not isinstance(value, Mapping) or set(value) - {"atom_ids", "scope_unit_names"} or "atom_ids" not in value:
        _fail("context-selection-invalid", "Selection must contain only its closed identity arrays")
    result = {}
    for key in ("atom_ids", "scope_unit_names"):
        items = value.get(key, [])
        if type(items) is not list or any(not isinstance(item, str) or not item for item in items):
            _fail("context-selection-invalid", "Selection identities must be nonempty strings")
        if items != sorted(set(items)):
            _fail("context-selection-ambiguous", "Selection identities must be sorted and unique")
        result[key] = list(items)
    if set(result["atom_ids"]) - available:
        _fail("context-selection-unbound", "Selection contains an Atom outside the sealed frontier")
    return result


def _frontier(repository: Path, value: object, pool: dict, selection: dict) -> dict[str, object]:
    if not isinstance(value, Mapping) or set(value) - {"selected_folder", "carriers", "source_frontier_sha256", "project_structure"}:
        _fail("context-frontier-invalid", "Source frontier has an unsupported shape")
    frontier = dict(value)
    canonical_bytes(frontier)
    if not {"selected_folder", "carriers", "source_frontier_sha256"} <= set(frontier):
        _fail("context-frontier-invalid", "A sealed source frontier is required")
    folder = _safe_path(repository, frontier["selected_folder"], folder=True)
    if not folder.is_dir():
        _fail("context-frontier-invalid", "The selected source folder cannot be read")
    rows = sorted(pool.values(), key=lambda item: item[1]["carrier_path"])
    expected = [{**pin, "content_role": carrier.content_role, "type": carrier.atom_type,
                 "status": carrier.status} for carrier, pin, _ in rows]
    if frontier["carriers"] != expected or frontier["source_frontier_sha256"] != _digest([pin for _, pin, _ in rows]):
        _fail("context-source-stale", "The sealed carrier frontier does not match the checked Carrier inputs")
    # Recheck membership, not just the listed hashes; additions cannot vanish.
    # Reuse the builder's exclusion policy without importing any execution path.
    from generate_entity_graph import _is_excluded, _structure_frontier
    observed_paths = set()
    for path in sorted(folder.rglob("*.md")):
        if _is_excluded(path, folder, repository):
            continue
        relative = path.relative_to(repository).as_posix()
        _safe_path(repository, relative)
        raw = path.read_bytes()
        if not raw.startswith((b"---\n", b"---\r\n")):
            continue
        _, _, _, fields = _raw_parts(raw)
        if "subjects" not in fields or fields.get("status", "").lower() not in ("", "active"):
            continue
        observed_paths.add(relative)
        expected_pin = next((pin for _, pin, _ in rows if pin["carrier_path"] == relative), None)
        if expected_pin is not None and hashlib.sha256(raw).hexdigest() != expected_pin["carrier_sha256"]:
            _fail("context-source-stale", "Current source bytes changed during frontier verification")
    if observed_paths != {pin["carrier_path"] for _, pin, _ in rows}:
        _fail("context-source-stale", "Current source membership differs from the sealed frontier")
    structure = frontier.get("project_structure")
    if structure is not None:
        if type(structure) is not dict or set(structure) != {"carrier_path", "carrier_sha256", "schema_version"} or type(structure["schema_version"]) is not int or structure["schema_version"] != 1:
            _fail("context-structure-invalid", "Project Structure evidence is not its closed supported record")
        path = _safe_path(repository, structure["carrier_path"])
        try:
            raw = path.read_bytes()
        except OSError:
            _fail("context-structure-unreadable", "Bound Project Structure cannot be read")
        if hashlib.sha256(raw).hexdigest() != structure["carrier_sha256"]:
            _fail("context-source-stale", "Bound Project Structure no longer matches its bytes")
        if structure != _structure_frontier(repository):
            _fail("context-source-stale", "Project Structure evidence differs from the current registered source")
        if selection["scope_unit_names"]:
            try:
                units = tomllib.loads(raw.decode("utf-8")).get("scope_units")
            except (UnicodeDecodeError, tomllib.TOMLDecodeError):
                _fail("context-structure-invalid", "Bound Project Structure is not readable TOML")
            if not isinstance(units, list) or any(not isinstance(unit, dict) or not isinstance(unit.get("scope_unit_name"), str) for unit in units):
                _fail("context-structure-invalid", "Bound Project Structure lacks named Scope Units")
            names = [unit["scope_unit_name"] for unit in units]
            if len(names) != len(set(names)) or set(selection["scope_unit_names"]) - set(names):
                _fail("context-selection-unbound", "Selected Scope Units are ambiguous or absent from bound Structure")
    elif selection["scope_unit_names"]:
        _fail("context-structure-unbound", "Scope Unit selection requires checked Project Structure evidence")
    return json.loads(canonical_bytes(frontier))


def _source_key(source: dict) -> tuple:
    contribution = source["contribution"]
    return (source["atom_id"], source["atom_revision"], source["carrier_path"],
            contribution["kind"], contribution.get("section", contribution.get("property_path", "")),
            contribution.get("canonical_target_reference", ""), contribution["start_line"],
            contribution["end_line"], contribution["text_sha256"])


def _source(pin: dict, lines: list[bytes], start: int, end: int, **location: object) -> dict:
    if start < 1 or end < start or end > len(lines):
        _fail("context-locator-invalid", "A contribution has no exact nonempty line span")
    return {**pin, "contribution": {**location, "start_line": start, "end_line": end,
            "text_sha256": hashlib.sha256(b"".join(lines[start - 1:end])).hexdigest()}}


def _body_headings(raw: bytes) -> tuple[list[bytes], list[tuple[int, int, str]], dict[str, str]]:
    """Read absolute raw headings, ignoring fenced and quoted examples."""
    lines, text, boundary, fields = _raw_parts(raw)
    headings = []
    fence = None
    for index in range(boundary + 1, len(text)):
        line = text[index]
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= fence[1] and not marker[2].strip():
                fence = None
            continue
        if marker:
            fence = (marker[1][0], len(marker[1]))
            continue
        heading = re.fullmatch(r"(#{1,6}) ([^\r\n]+)", line)
        if heading:
            headings.append((index, len(heading[1]), heading[2]))
    return lines, headings, fields


def _section_source(pin: dict, lines: list[bytes], headings: list[tuple],
                    section: str, *, kind: str) -> dict | None:
    targets = [entry for entry in headings if entry[1:] == (2, section)]
    if len(targets) > 1:
        _fail("context-primary-ambiguous", "An Atom has duplicate role-primary sections")
    if not targets:
        return None
    start = targets[0][0] + 2
    end = next((index for index, level, _ in headings if index >= start - 1 and level <= 2), len(lines))
    if end < start:
        return None
    return _source(pin, lines, start, end, kind=kind, section=section)


def _primary(pin: dict, raw: bytes, role: str) -> dict | None:
    section = "Claim" if role in {"Requirement", "Method", "Evaluation", "Delivery"} else "Operation" if role == "Operations" else None
    if section is None:
        return None
    lines, headings, _ = _body_headings(raw)
    return _section_source(pin, lines, headings, section, kind="primary_content")


def _details_assignment_bound(authorities: dict) -> bool:
    return all(atom_id in authorities and
               authorities[atom_id][1]["atom_revision"] == revision and
               authorities[atom_id][1]["carrier_sha256"] == digest
               for atom_id, revision, digest in _DETAILS_ASSIGNMENT_PINS)


def _details_source(pin: dict, raw: bytes, role: str) -> dict | None:
    """Locate source Atom/Details, not a Property of its GOVERNS target."""
    required = ["Scope", "Claim", "Details"] if role in {"Requirement", "Method", "Evaluation", "Delivery"} else ["Operation", "Details"] if role == "Operations" else None
    if required is None:
        return None
    lines, headings, fields = _body_headings(raw)
    if ([name for _, level, name in headings if level == 1] != ["Summary"] or
            not headings or headings[0][1:] != (1, "Summary") or
            [name for _, level, name in headings if level == 2] != required or
            any(key.casefold() == "details" for key in fields)):
        return None
    return _section_source(pin, lines, headings, "Details", kind="canonical_atom_property")


def raw_section_property_evidence(repository: Path, carrier: object, *,
                                  section: str = "Details",
                                  authority_sources: Sequence) -> dict | None:
    """Checked bounded Details locator; unsupported assignment returns None.

    The supporting value stays owned by its source Atom. This API produces
    source evidence only, not a native Property or a semantic admission result.
    """
    _check_loaded_profile()
    if section != "Details":
        _fail("context-section-unsupported", "Only the reviewed Details section locator is supported")
    repository = Path(repository).resolve()
    pin, raw = _carrier_pin(repository, carrier)
    authorities = _pool(repository, authority_sources)
    if not _details_assignment_bound(authorities):
        return None
    return _details_source(pin, raw, carrier.content_role)


def _governed_reference(pin: dict, raw: bytes) -> tuple[dict, str] | None:
    lines, text, boundary, fields = _raw_parts(raw)
    if fields.get("subjects") != "":
        return None
    start = next(index for index in range(1, boundary) if re.fullmatch(r"subjects:[ \t]*", text[index]))
    found = []
    for index in range(start + 1, boundary):
        line = text[index]
        if line and not line[0].isspace():
            break
        match = re.fullmatch(r"  governs:[ \t]*(.+)", line)
        if match:
            target = _scalar(match[1])
            if not target or target[0] in "[{*&!|>":
                continue
            found.append((_source(pin, lines, index + 1, index + 1,
                                  kind="canonical_atom_property", property_path="subjects.governs"), target))
    if len(found) > 1:
        _fail("context-property-ambiguous", "A canonical governed Subject location is duplicated")
    return found[0] if found else None


def _means_candidate(pin: dict, raw: bytes, primary: dict, target: str) -> dict | None:
    """Recognize one simple same-target declaration, not its semantic truth.

    Qualified paths, operational aliases, subordinate means and other forms
    require separate profiles. They remain covered by unknown, not absence.
    """
    _, text, _, _ = _raw_parts(raw)
    contribution = primary["contribution"]
    found = []
    fence = None
    for line in text[contribution["start_line"] - 1:contribution["end_line"]]:
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= fence[1] and not marker[2].strip():
                fence = None
            continue
        if marker:
            fence = (marker[1][0], len(marker[1]))
            continue
        match = re.fullmatch(r"(?:a |an |the )?([A-Za-z][A-Za-z0-9 -]*?) +(?:\*\*means\*\*|means) +(.+)", line, re.IGNORECASE)
        if match and match[1] == target:
            found.append(match[1])
    if len(found) != 1:
        return None
    return {"term_identity": found[0], "subject_path": target}


def _declared_core(repository: Path, frontier: dict, selection: dict) -> bool:
    """Recognize the isolated registered source, not effective methodology."""
    evidence = frontier.get("project_structure")
    if not evidence or selection["scope_unit_names"] != ["CORE_META_MODEL"]:
        return False
    path = _safe_path(repository, evidence["carrier_path"])
    units = tomllib.loads(path.read_text(encoding="utf-8")).get("scope_units", [])
    rows = [row for row in units if isinstance(row, dict) and row.get("scope_unit_name") == "CORE_META_MODEL"]
    return len(rows) == 1 and rows[0].get("authority_path") == frontier["selected_folder"]


def _bundle_sources(value: object):
    """Collect exact proof references, never carrier metadata as declarations."""
    if isinstance(value, dict):
        if set(value) == {"atom_id", "atom_revision", "carrier_path", "carrier_sha256", "contribution"}:
            yield value
        else:
            for item in value.values():
                yield from _bundle_sources(item)
    elif isinstance(value, list):
        for item in value:
            yield from _bundle_sources(item)


def _verify_bundle_sources(bundle: dict, pool: dict, sources: dict) -> None:
    for reference in _bundle_sources(bundle):
        record = pool.get(reference["atom_id"])
        if record is None or {key: reference[key] for key in record[1]} != record[1]:
            _fail("context-proof-unbound", "A profile proof does not bind a current source Carrier")
        carrier, pin, raw = record
        contribution = reference["contribution"]
        lines = raw.splitlines(keepends=True)
        start, end = contribution.get("start_line"), contribution.get("end_line")
        if (type(start) is not int or type(end) is not int or start < 1 or end < start or end > len(lines)
                or hashlib.sha256(b"".join(lines[start - 1:end])).hexdigest() != contribution.get("text_sha256")):
            _fail("context-proof-locator-invalid", "A profile proof span differs from exact source bytes")
        if contribution.get("kind") == "primary_content" and reference != _primary(pin, raw, carrier.content_role):
            _fail("context-proof-locator-invalid", "A primary proof must retain the exact role-primary contribution")
        sources[_source_key(reference)] = reference


def _core_admission(repository: Path, graph_kind: str, carriers: Sequence,
                    selection: dict, frontier: dict) -> dict:
    """Execute a bounded reviewed family; unavailable regions stay unresolved."""
    if graph_kind == "terms":
        from core_term_admission import prepare_core_term_profile, checked_requirement_source, review_core_term_candidates
        profile = prepare_core_term_profile(repository, carriers, frontier, selection)
        checked = [checked_requirement_source(repository, carrier, profile)
                   for carrier in carriers if carrier.atom_id in selection["atom_ids"]]
        return review_core_term_candidates(checked, profile)
    from core_entity_admission import (CoreEntityAdmissionError, prepare_core_entity_profile,
                                       checked_operations_source, review_core_entity_candidates)
    profile = prepare_core_entity_profile(repository, carriers, frontier, selection)
    checked, unresolved = [], []
    for carrier in carriers:
        if (carrier.atom_id not in selection["atom_ids"] or carrier.content_role != "Operations"
                or carrier.atom_type not in {"Action", "Workflow"} or carrier.status != "Active"):
            continue
        try:
            checked.append(checked_operations_source(repository, carrier, profile))
        except CoreEntityAdmissionError as error:
            if error.code not in {"core-source-unsupported", "core-operation-unresolved", "core-type-unresolved"}:
                _fail(error.code, "Core admission could not revalidate its checked source")
            unresolved.append({"code": "core-entity-source-unresolved", "severity": "warning", "source_refs": [],
                               "details": {"atom_id": carrier.atom_id, "carrier_path": carrier.carrier_path,
                                           "carrier_sha256": carrier.sha256, "reason": error.code}})
    bundle = review_core_entity_candidates(checked, profile)
    bundle["diagnostics"].extend(unresolved)
    return bundle


def prepare_fact_context(repository: Path, graph_kind: str, carriers: Sequence,
                         selection: Mapping, source_frontier: Mapping,
                         authority_sources: Sequence) -> DerivedFactContext:
    """Read and bind sources; keep unavailable semantic checks unresolved."""
    _check_loaded_profile()
    from fact_context_contract import ContractError, implementation_sha256, validate_fact_context
    contract_digest = implementation_sha256()
    repository = Path(repository).resolve()
    if not repository.is_dir() or graph_kind not in {"entities", "terms"}:
        _fail("context-input-invalid", "An existing repository and one supported graph kind are required")
    pool = _pool(repository, carriers)
    authorities = _pool(repository, authority_sources)
    selected = _selection(selection, set(pool))
    frontier = _frontier(repository, source_frontier, pool, selected)
    combined = dict(pool)
    for atom_id, value in authorities.items():
        if atom_id in combined and combined[atom_id][1] != value[1]:
            _fail("context-authority-conflict", "An authority identity binds conflicting Carrier evidence")
        combined[atom_id] = value
    profile = {"id": "caprmedio.graph-fact-context.partial", "version": "1",
               "profile_sha256": _digest({"implementation_sha256": _LOADED_IMPLEMENTATION_SHA256,
                                           "recognition": ["primary-simple-same-target-means-candidate"],
                                           "evidence_locators": ["role-primary-content", "assigned-atom-details"],
                                           "details_assignment_pins": [list(pin) for pin in _DETAILS_ASSIGNMENT_PINS],
                                           "admission": "unavailable"})}
    details_bound = _details_assignment_bound(authorities)
    declared_core = _declared_core(repository, frontier, selected)
    sources: dict[tuple, dict] = {}
    candidates = []
    diagnostics = []
    for atom_id in sorted(combined):
        carrier, pin, raw = combined[atom_id]
        if carrier.status != "Active":
            diagnostics.append({"code": "status-model-unresolved", "severity": "warning", "source_refs": [],
                                "details": {"atom_id": atom_id, "content_role": carrier.content_role,
                                            "carrier_path": pin["carrier_path"]}})
        primary = _primary(pin, raw, carrier.content_role)
        if primary is not None:
            sources[_source_key(primary)] = primary
        else:
            diagnostics.append({"code": "primary-content-unavailable", "severity": "warning", "source_refs": [],
                                "details": {"atom_id": atom_id, "carrier_path": pin["carrier_path"],
                                            "carrier_sha256": pin["carrier_sha256"]}})
        if details_bound and atom_id in authorities:
            details = _details_source(pin, raw, carrier.content_role)
            if details is not None:
                sources[_source_key(details)] = details
        if atom_id not in selected["atom_ids"] or primary is None or carrier.status != "Active":
            continue
        reference = _governed_reference(pin, raw)
        if reference:
            _, target = reference
            payload = _means_candidate(pin, raw, primary, target)
            if payload is None:
                continue
            candidate = {"fact_class": "definition", "payload": payload,
                         "recognizer": dict(profile), "source_ref": primary}
            candidate["candidate_id"] = "candidate:" + _digest(candidate)
            candidates.append(candidate)
    candidates.sort(key=lambda item: item["candidate_id"])
    decisions = []
    for candidate in candidates:
        source_ref = candidate["source_ref"]
        decision = {"candidate_id": candidate["candidate_id"], "disposition": "unresolved",
                    "evaluator": dict(profile), "authority_inputs": [],
                    "checks": [{"code": "source-pin-current", "disposition": "pass", "source_refs": [source_ref]},
                               {"code": "semantic-admission-profile", "disposition": "unresolved", "source_refs": [source_ref]}]}
        decision["checks"].sort(key=lambda item: item["code"])
        decision["decision_sha256"] = _digest(decision)
        decisions.append(decision)
    empty = not selected["atom_ids"] and not selected["scope_unit_names"]
    if not empty:
        diagnostics.append({"code": "semantic-profile-unavailable", "severity": "warning", "source_refs": [],
                            "details": {"graph_kind": graph_kind}})
        if not details_bound:
            diagnostics.append({"code": "details-assignment-profile-unavailable", "severity": "warning",
                                "source_refs": [], "details": {"required_authority_ids": [pin[0] for pin in _DETAILS_ASSIGNMENT_PINS]}})
    required = ("entity_admission", "entity_property", "relation") if graph_kind == "entities" else ("definition", "relation")
    coverage = [{"fact_class": fact_class, "disposition": "complete" if empty else "unknown",
                 "selected_result": "empty" if empty else "unknown",
                 "candidate_count": sum(candidate["fact_class"] == fact_class for candidate in candidates),
                 "admitted_count": 0,
                 "source_refs": sorted([candidate["source_ref"] for candidate in candidates if candidate["fact_class"] == fact_class], key=_source_key)}
                for fact_class in sorted(required)]
    admitted = []
    registry = []
    portfolio = []
    if declared_core and selected["atom_ids"]:
        try:
            bundle = _core_admission(repository, graph_kind, carriers, selected, frontier)
        except FactContextError:
            raise
        except (ImportError, ValueError, OSError):
            diagnostics.append({"code": "core-admission-profile-unavailable", "severity": "warning", "source_refs": [],
                                "details": {"graph_kind": graph_kind}})
        else:
            _verify_bundle_sources(bundle, combined, sources)
            candidates = bundle["candidates"]
            decisions = bundle["admission_decisions"]
            admitted = bundle["admitted_facts"]
            coverage = bundle["coverage"]
            diagnostics = [row for row in diagnostics if row["code"] != "semantic-profile-unavailable"]
            diagnostics.extend(bundle["diagnostics"])
            portfolio.append(bundle["provider"])
    if declared_core:
        from core_relation_registry import prepare_core_relation_registry
        registry_bundle = prepare_core_relation_registry(repository, carriers, frontier, selected)
        registry = [row for row in registry_bundle.records if row["kind"]["graph_kind"] == graph_kind]
        _verify_bundle_sources({"records": registry, "diagnostics": list(registry_bundle.diagnostics)}, combined, sources)
        diagnostics.extend(registry_bundle.diagnostics)
        if registry:
            portfolio.append(registry_bundle.profile)
        if graph_kind == "terms" and registry and selected["atom_ids"]:
            from core_relation_candidates import CoreRelationCandidateError, recognize_core_term_relations
            try:
                relation_bundle = recognize_core_term_relations(repository, carriers, selected, registry)
            except CoreRelationCandidateError as error:
                if error.code != "relation-registry-unavailable":
                    _fail(error.code, "Core relation recognition could not revalidate its checked sources")
                diagnostics.append({"code": "core-term-relation-profile-unavailable", "severity": "warning",
                                    "source_refs": [], "details": {"graph_kind": graph_kind}})
            else:
                _verify_bundle_sources(relation_bundle, combined, sources)
                candidates.extend(relation_bundle["candidates"])
                decisions.extend(relation_bundle["admission_decisions"])
                admitted.extend(relation_bundle["admitted_facts"])
                diagnostics.extend(relation_bundle["diagnostics"])
                portfolio.append(relation_bundle["provider"])
                relation_sources = {canonical_bytes(row["source_ref"]): row["source_ref"]
                                    for row in candidates if row["fact_class"] == "relation"}
                for row in coverage:
                    if row["fact_class"] == "relation":
                        row.update(disposition="unknown", selected_result="unknown",
                                   candidate_count=sum(item["fact_class"] == "relation" for item in candidates),
                                   admitted_count=sum(item["fact_class"] == "relation" for item in admitted),
                                   source_refs=sorted(relation_sources.values(), key=_source_key))
        profile = {"id": "caprmedio.graph-fact-context.declared-core", "version": "1",
                   "profile_sha256": _digest({"base_profile": profile, "portfolio": portfolio,
                                               "declaration_context": "declared_core_model"})}
    source_rows = sorted(sources.values(), key=_source_key)
    candidates.sort(key=lambda row: row["candidate_id"])
    decisions.sort(key=lambda row: row["candidate_id"])
    admitted.sort(key=lambda row: row["fact_id"])
    coverage.sort(key=lambda row: row["fact_class"])
    diagnostics.sort(key=lambda item: (item["code"], tuple(_source_key(ref) for ref in item["source_refs"]), canonical_bytes(item["details"])))
    profile = {"id": profile["id"], "version": profile["version"],
               "profile_sha256": _digest({"provider": profile, "contract_sha256": contract_digest})}
    context = {"schema_version": 1, "context_kind": "caprmedio.derived_fact_context", "graph_kind": graph_kind,
               "source_binding": {"source_frontier_sha256": frontier["source_frontier_sha256"],
                                  "selection_sha256": _digest(selected), "authority_frontier_sha256": _digest(source_rows)},
               "provider": profile, "authority_sources": source_rows, "relation_registry": registry,
               "coverage": coverage, "candidates": candidates, "admission_decisions": decisions,
               "admitted_facts": admitted, "derivations": [], "diagnostics": diagnostics}
    context["context_sha256"] = _digest(context)
    try:
        validate_fact_context(context)
    except ContractError as error:
        if error.code == "profile-stale":
            _fail("profile-stale", "Validator implementation changed after its profile was loaded")
        _fail("context-contract-invalid", "A provider record failed the closed fact-context contract")
    return DerivedFactContext(canonical_bytes(context), canonical_bytes({"repository": repository.as_posix(),
                              "source_frontier": frontier, "selection": selected}), _token=_FACTORY_TOKEN)
