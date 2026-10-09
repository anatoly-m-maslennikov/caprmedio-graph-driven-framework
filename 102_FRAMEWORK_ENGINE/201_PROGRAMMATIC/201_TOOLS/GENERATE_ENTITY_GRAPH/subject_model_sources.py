"""Immutable raw Subjects occurrences, without model or native admission.

This support reader checks current Carrier pins and canonical flat Subjects
serialization only. Target resolution, Main Content conformance, lifecycle
admission, Entity membership, prefix expansion and native facts are unassessed.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType

import generate_entity_graph as graph
import graph_fact_context as facts


_TOKEN = object()
_IMPLEMENTATION_PATH = Path(__file__).resolve()
_LOADED_IMPLEMENTATION_SHA256 = hashlib.sha256(_IMPLEMENTATION_PATH.read_bytes()).hexdigest()
_PARSER_PATH = Path(graph.__file__).resolve()
_LOADED_PARSER_SHA256 = hashlib.sha256(_PARSER_PATH.read_bytes()).hexdigest()
_CORE_PATH = ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL"
# These identify the reviewed grammar; this reader does not claim the root
# factory has bound their current authority contributions or resolved targets.
_GRAMMAR_PINS = (
    {"atom_id": "CA-D-269", "atom_revision": 12,
     "carrier_path": _CORE_PATH + "/07_delivery/CA-D-269-CORE_META_MODEL-DELIVERY--serialize-atom-subjects-in-frontmatter.md",
     "carrier_sha256": "eea15e5b1c2411acdd552c8701da98ac34bab89a107ee05f28760eb1ce8eeac3"},
    {"atom_id": "CA-R-1194", "atom_revision": 14,
     "carrier_path": _CORE_PATH + "/04_requirement/CA-R-1194-CORE_META_MODEL-CORE-REQUIREMENT--define-subject-path.md",
     "carrier_sha256": "159ff72818c390f6d126c543587ebb8de49d5d5ae53cfc0e437df25d25e3c30e"},
)


class SubjectModelSourceError(ValueError):
    def __init__(self, code: str) -> None:
        self.code = code
        super().__init__(code)


class _UnsupportedForm(ValueError):
    pass


def _digest(value: object) -> str:
    return hashlib.sha256(facts.canonical_bytes(value)).hexdigest()


def _check_code() -> None:
    facts._check_loaded_profile()
    try:
        if (hashlib.sha256(_IMPLEMENTATION_PATH.read_bytes()).hexdigest() != _LOADED_IMPLEMENTATION_SHA256 or
                hashlib.sha256(_PARSER_PATH.read_bytes()).hexdigest() != _LOADED_PARSER_SHA256):
            raise SubjectModelSourceError("profile-stale")
    except OSError as error:
        raise SubjectModelSourceError("profile-stale") from error


def _readonly(value: object) -> object:
    if isinstance(value, dict):
        return MappingProxyType({key: _readonly(item) for key, item in value.items()})
    if isinstance(value, list):
        return tuple(_readonly(item) for item in value)
    return value


@dataclass(frozen=True, slots=True, init=False)
class SubjectModelSources:
    _bytes: bytes
    _token: object

    def __init__(self, data: bytes, *, _token: object = None) -> None:
        if _token is not _TOKEN:
            raise SubjectModelSourceError("subject-model-sources-untrusted")
        object.__setattr__(self, "_bytes", data)
        object.__setattr__(self, "_token", _token)

    def as_dict(self) -> dict:
        if type(self) is not SubjectModelSources or self._token is not _TOKEN:
            raise SubjectModelSourceError("subject-model-sources-untrusted")
        return json.loads(self._bytes)

    @property
    def collection_sha256(self) -> str:
        return self.as_dict()["collection_sha256"]

    @property
    def profile_sha256(self) -> str:
        return self.as_dict()["provider"]["profile_sha256"]

    @property
    def occurrences(self) -> tuple:
        return _readonly(self.as_dict()["occurrences"])

    @property
    def coverage(self) -> Mapping:
        return _readonly(self.as_dict()["coverage"])


def _scalar_path(value: str) -> str:
    raw = value.strip()
    if not raw or raw[0] in "[{*&!|>" or raw[-1:] in {"[", "{"}:
        raise _UnsupportedForm("subject-scalar-unsupported")
    if raw[0] in "\"'" and (len(raw) < 2 or raw[-1] != raw[0]):
        raise _UnsupportedForm("subject-scalar-unsupported")
    if raw[0] in "\"'" and (raw[0] in raw[1:-1] or (raw[0] == '"' and "\\" in raw)):
        raise _UnsupportedForm("subject-scalar-unsupported")
    if raw[0] not in "\"'" and any(char in raw for char in "[]{}"):
        raise _UnsupportedForm("subject-scalar-unsupported")
    path = graph.scalar_value(raw)
    try:
        graph._subject_parts(path)
    except graph.EntityGraphError as error:
        raise _UnsupportedForm("subject-path-malformed") from error
    # Preserve the complete source string: no terminalization or path rewrite.
    return path


def _inline_paths(value: str) -> list[str]:
    raw = value.strip()
    if not (raw.startswith("[") and raw.endswith("]")):
        raise _UnsupportedForm("subject-dependencies-not-collection")
    body = raw[1:-1].strip()
    if not body:
        return []
    # Match the existing parser's bounded comma-separated inline-list grammar.
    # Quoted commas/escapes needing a wider YAML reader remain unsupported.
    return [_scalar_path(item) for item in body.split(",")]


def _property_rows(pin: dict, raw: bytes) -> tuple[list[dict], list[str], dict[str, dict]]:
    lines, text, boundary, fields = facts._raw_parts(raw)
    if fields.get("subjects") != "":
        raise _UnsupportedForm("subjects-flat-block-unavailable")
    start = next(index for index in range(1, boundary) if re.fullmatch(r"subjects:[ \t]*", text[index]))
    end = start + 1
    while end < boundary and (not text[end] or text[end][0].isspace()):
        end += 1
    properties = {}
    values = {}
    index = start + 1
    while index < end:
        if not text[index].strip():
            index += 1
            continue
        matched = re.fullmatch(r"  (governs|depends_on):[ \t]*(.*)", text[index])
        if matched is None:
            raise _UnsupportedForm("subjects-unassigned-syntax")
        key, value = matched[1], matched[2]
        if key in properties:
            raise _UnsupportedForm("subjects-duplicate-key")
        property_end = index + 1
        while property_end < end and (not text[property_end] or text[property_end].startswith("    ")):
            property_end += 1
        nested = [line for line in text[index + 1:property_end] if line.strip()]
        if key == "governs":
            if nested:
                raise _UnsupportedForm("subjects-governs-not-scalar")
            values[key] = [_scalar_path(value)]
        elif value.strip():
            if nested:
                raise _UnsupportedForm("subject-dependencies-ambiguous")
            values[key] = _inline_paths(value)
        else:
            if not nested:
                raise _UnsupportedForm("subject-dependencies-not-collection")
            parsed = []
            for line in nested:
                item = re.fullmatch(r"    -[ \t]+(.+)", line)
                if item is None:
                    raise _UnsupportedForm("subjects-unassigned-syntax")
                parsed.append(_scalar_path(item[1]))
            values[key] = parsed
        if key == "depends_on" and len(values[key]) != len(set(values[key])):
            raise _UnsupportedForm("subject-dependencies-duplicate-path")
        properties[key] = facts._source(pin, lines, index + 1, property_end,
                                         kind="canonical_atom_property", property_path="subjects." + key)
        index = property_end
    if "governs" not in values:
        raise _UnsupportedForm("subjects-governs-unavailable")
    parser_carrier = graph.AtomCarrier(
        atom_id=pin["atom_id"], version=pin["atom_revision"], cce_form=fields.get("cce_form", ""),
        content_role=fields.get("content_role", ""), atom_type=fields.get("type", ""),
        status=fields.get("status", ""), carrier_path=pin["carrier_path"], sha256=pin["carrier_sha256"],
        frontmatter="\n".join(text[1:boundary]), body="\n".join(text[boundary + 1:]),
    )
    try:
        relations, diagnostics = graph.parse_subject_relations(parser_carrier)
    except graph.EntityGraphError as error:
        raise _UnsupportedForm(error.code) from error
    expected = [("GOVERNS", path) for path in values["governs"]] + [("DEPENDS_ON", path) for path in values.get("depends_on", [])]
    if diagnostics or sorted((row.kind, row.subject_path) for row in relations) != sorted(expected):
        raise _UnsupportedForm("subjects-parser-form-unresolved")
    occurrences = [{"subject_path": row.subject_path, "role": row.kind,
                    "source_ref": properties["governs" if row.kind == "GOVERNS" else "depends_on"]} for row in relations]
    return occurrences, text, properties


def collect_subject_model_sources(repository: Path, selected_carriers: Sequence) -> SubjectModelSources:
    """Collect checked source occurrences, not admitted model facts.

    Coverage describes this bounded extraction only. Unsupported source forms
    are isolated; stale/forged pins and ambiguous selected identities fail.
    The root factory separately binds the profile's reviewed grammar pins.
    """
    _check_code()
    repository = Path(repository).resolve()
    if not isinstance(selected_carriers, Sequence) or isinstance(selected_carriers, (str, bytes)):
        raise SubjectModelSourceError("subject-carrier-selection-invalid")
    pins, occurrences, diagnostics = [], [], []
    identities, paths = set(), set()
    resolved_count = 0
    for carrier in selected_carriers:
        if isinstance(carrier, Mapping) or any(not hasattr(carrier, name) for name in
                ("atom_id", "version", "carrier_path", "sha256", "content_role", "atom_type", "status")):
            raise SubjectModelSourceError("subject-carrier-untrusted")
        if (not isinstance(carrier.atom_id, str) or not carrier.atom_id or type(carrier.version) is not int or
                carrier.version < 1 or not isinstance(carrier.carrier_path, str) or not carrier.carrier_path or
                not isinstance(carrier.sha256, str) or re.fullmatch(r"[0-9a-f]{64}", carrier.sha256) is None or
                any(not isinstance(getattr(carrier, key), str) for key in ("content_role", "atom_type", "status"))):
            raise SubjectModelSourceError("subject-carrier-untrusted")
        if carrier.atom_id in identities or carrier.carrier_path in paths:
            raise SubjectModelSourceError("subject-carrier-selection-ambiguous")
        identities.add(carrier.atom_id)
        paths.add(carrier.carrier_path)
        try:
            pin, raw = facts._carrier_pin(repository, carrier)
        except facts.FactContextError as error:
            if error.code not in {"context-carrier-duplicate", "context-carrier-invalid", "context-lifecycle-unbound"}:
                raise
            # No contribution is minted for malformed top-level keys. The pin
            # reader already checked current path/digest before this failure.
            diagnostics.append({"code": error.code, "severity": "warning", "source_refs": [],
                                "details": {"carrier_path": carrier.carrier_path, "carrier_sha256": carrier.sha256}})
            continue
        pins.append(pin)
        try:
            rows, _, _ = _property_rows(pin, raw)
        except _UnsupportedForm as error:
            diagnostics.append({"code": str(error), "severity": "warning", "source_refs": [],
                                "details": {"atom_id": pin["atom_id"], "carrier_path": pin["carrier_path"],
                                            "carrier_sha256": pin["carrier_sha256"]}})
            continue
        occurrences.extend(rows)
        resolved_count += 1
    occurrences.sort(key=lambda row: (row["subject_path"], row["role"], facts._source_key(row["source_ref"])))
    pins.sort(key=lambda row: row["carrier_path"])
    diagnostics.sort(key=lambda row: (row["code"], row["details"]["carrier_path"]))
    profile = {"implementation_sha256": _LOADED_IMPLEMENTATION_SHA256,
               "parser_implementation_sha256": _LOADED_PARSER_SHA256,
               "fact_context_implementation_sha256": facts._LOADED_IMPLEMENTATION_SHA256,
               "reviewed_grammar_pins": list(_GRAMMAR_PINS),
               "recognition": "current-flat-scalar-governs-unique-dependency-collection",
               "grammar_authority_binding": "root_required",
               "semantic_conformance": "not_performed"}
    count = len(selected_carriers)
    result = {"provider": {"id": "caprmedio.subject-model-sources", "version": "1", "profile_sha256": _digest(profile)},
              "grammar_pins": list(_GRAMMAR_PINS), "source_pins": pins, "occurrences": occurrences,
              "coverage": {"scope": "subject_occurrence_extraction", "disposition": "complete" if resolved_count == count else "incomplete",
                           "source_count": count, "resolved_source_count": resolved_count,
                           "unresolved_source_count": count - resolved_count, "occurrence_count": len(occurrences)},
              "unperformed": ["grammar_authority_binding", "target_resolution", "main_content_conformance", "native_admission"],
              "diagnostics": diagnostics}
    result["collection_sha256"] = _digest(result)
    _check_code()
    return SubjectModelSources(facts.canonical_bytes(result), _token=_TOKEN)
