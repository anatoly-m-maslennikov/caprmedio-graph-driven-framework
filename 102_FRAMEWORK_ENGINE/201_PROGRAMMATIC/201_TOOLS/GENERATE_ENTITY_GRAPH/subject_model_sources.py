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
import subject_notation


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
# The extractor's longstanding D269/R1194 evidence above remains deliberately
# frozen.  Approved parsing additionally binds these exact current grammar
# sources before it reads any carrier; this proves only source-pin freshness,
# never native endpoint admission.
_APPROVED_CORE_GRAMMAR_PINS = (
    {
        "atom_id": "CA-R-1931",
        "version": 1,
        "path": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1931-CORE_META_MODEL--use-subject-path-separators-for-broader-to-narrower-and-bearer-to-dependent.md",
        "sha256": "f11bc913a0f7b31abc746a86599eaeaa76db8be412568ef4c34f68c7d01525c8",
    },
    {
        "atom_id": "CA-R-1321",
        "version": 14,
        "path": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1321-CORE_META_MODEL-CORE--define-subject-expression.md",
        "sha256": "d883f1bd53ac3ea83aeff2d3d1fdfb5498641a0e5f2db5e8e79d8dfd5c5a84df",
    },
    {
        "atom_id": "CA-R-1324",
        "version": 12,
        "path": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1324-CORE_META_MODEL-REQUIREMENT--reserve-subject-expression-separators.md",
        "sha256": "33cbfee9844ba4dd895ae6745121fd5db5793a20aab27eb8b8d7b4591e7fb9a3",
    },
    {
        "atom_id": "CA-M-228",
        "version": 16,
        "path": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/05_method/CA-M-228-CORE_META_MODEL-METHOD--write-subject-expressions-with-bearer-and-value-qualification.md",
        "sha256": "0f398721d7d15aaf8e0b0f69a20b1b541e8d306839073c98eea4b80f9580b40d",
    },
    {
        "atom_id": "CA-E-383",
        "version": 16,
        "path": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/06_evaluation/CA-E-383-CORE_META_MODEL-EVALUATION_APPROACH--reject-invalid-subject-expressions.md",
        "sha256": "a356617c341cd1d3c723e3e3ddbf9852c720781c8f22dd31f07cf33dfa4ec512",
    },
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


def _subject_profile(subject_profile: str = "legacy") -> object:
    try:
        return subject_notation.get_profile(subject_profile)
    except ValueError as error:
        raise SubjectModelSourceError(getattr(error, "code", "subject-profile-invalid")) from error


def _profile_pins(profile: object) -> tuple[dict[str, object], ...]:
    pins = getattr(profile, "grammar_pins", None)
    if not isinstance(pins, Sequence) or isinstance(pins, (str, bytes)):
        raise SubjectModelSourceError("subject-profile-invalid")
    rows: list[dict[str, object]] = []
    for pin in pins:
        row = (
            dict(pin)
            if isinstance(pin, Mapping)
            else {
                "atom_id": getattr(pin, "atom_id", None),
                "version": getattr(pin, "version", None),
                "path": getattr(pin, "path", None),
                "sha256": getattr(pin, "sha256", None),
            }
        )
        if set(row) != {"atom_id", "version", "path", "sha256"}:
            raise SubjectModelSourceError("subject-profile-invalid")
        if (not isinstance(row["atom_id"], str) or not row["atom_id"] or type(row["version"]) is not int
                or row["version"] < 1 or not isinstance(row["path"], str) or not row["path"]
                or not isinstance(row["sha256"], str) or re.fullmatch(r"[0-9a-f]{64}", row["sha256"]) is None):
            raise SubjectModelSourceError("subject-profile-invalid")
        rows.append(row)
    return tuple(rows)


def _check_current_approved_grammar_pins(repository: Path, profile: object) -> None:
    if getattr(profile, "name", None) != "approved":
        return
    expected = tuple(_APPROVED_CORE_GRAMMAR_PINS)
    actual = _profile_pins(profile)
    if actual != expected:
        raise SubjectModelSourceError("approved-grammar-pins-mismatch")
    for pin in actual:
        path = repository / str(pin["path"])
        try:
            for probe in (path, *path.parents):
                if probe == repository:
                    break
                if probe.is_symlink():
                    raise SubjectModelSourceError("approved-grammar-pin-symlink")
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != pin["sha256"]:
                raise SubjectModelSourceError("approved-grammar-pin-stale")
        except SubjectModelSourceError:
            raise
        except OSError as error:
            raise SubjectModelSourceError("approved-grammar-pin-stale") from error


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


def _scalar_path(value: str, *, subject_profile: str = "legacy") -> str:
    if subject_profile == "approved":
        try:
            path = graph.subject_scalar_value(value, path="", field="subjects", subject_profile=subject_profile)
        except graph.EntityGraphError as error:
            raise _UnsupportedForm("subject-scalar-unsupported") from error
        return _checked_subject_path(path, subject_profile=subject_profile)
    raw = value.strip()
    if not raw or raw[0] in "[{*&!|>" or raw[-1:] in {"[", "{"}:
        raise _UnsupportedForm("subject-scalar-unsupported")
    if raw[0] in "\"'" and (len(raw) < 2 or raw[-1] != raw[0]):
        raise _UnsupportedForm("subject-scalar-unsupported")
    if raw[0] in "\"'" and (raw[0] in raw[1:-1] or (raw[0] == '"' and "\\" in raw)):
        raise _UnsupportedForm("subject-scalar-unsupported")
    if raw[0] not in "\"'" and any(char in raw for char in "[]{}"):
        raise _UnsupportedForm("subject-scalar-unsupported")
    return _checked_subject_path(graph.scalar_value(raw), subject_profile=subject_profile)


def _checked_subject_path(path: str, *, subject_profile: str) -> str:
    try:
        graph._subject_parts(path, subject_profile=subject_profile)
    except graph.EntityGraphError as error:
        raise _UnsupportedForm("subject-path-malformed") from error
    # Preserve the complete source string: no terminalization or path rewrite.
    return path


def _inline_paths(value: str, *, subject_profile: str = "legacy") -> list[str]:
    raw = value.strip()
    if not (raw.startswith("[") and raw.endswith("]")):
        raise _UnsupportedForm("subject-dependencies-not-collection")
    if subject_profile == "approved":
        try:
            decoded = graph.yaml_scalar_or_list(raw, path="", field="depends_on", subject_profile=subject_profile)
        except graph.EntityGraphError as error:
            raise _UnsupportedForm("subject-scalar-unsupported") from error
        return [_checked_subject_path(item, subject_profile=subject_profile) for item in decoded]
    body = raw[1:-1].strip()
    if not body:
        return []
    # Match the existing parser's bounded comma-separated inline-list grammar.
    # Quoted commas/escapes needing a wider YAML reader remain unsupported.
    return [_scalar_path(item, subject_profile=subject_profile) for item in body.split(",")]


def _property_rows(
    pin: dict, raw: bytes, *, subject_profile: str = "legacy"
) -> tuple[list[dict], list[str], dict[str, dict]]:
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
            values[key] = [_scalar_path(value, subject_profile=subject_profile)]
        elif value.strip():
            if nested:
                raise _UnsupportedForm("subject-dependencies-ambiguous")
            values[key] = _inline_paths(value, subject_profile=subject_profile)
        else:
            if not nested:
                raise _UnsupportedForm("subject-dependencies-not-collection")
            parsed = []
            for line in nested:
                item = re.fullmatch(r"    -[ \t]+(.+)", line)
                if item is None:
                    raise _UnsupportedForm("subjects-unassigned-syntax")
                parsed.append(_scalar_path(item[1], subject_profile=subject_profile))
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
        relations, diagnostics = graph.parse_subject_relations(
            parser_carrier, subject_profile=subject_profile
        )
    except graph.EntityGraphError as error:
        raise _UnsupportedForm(error.code) from error
    expected = [("GOVERNS", path) for path in values["governs"]] + [("DEPENDS_ON", path) for path in values.get("depends_on", [])]
    if diagnostics or sorted((row.kind, row.subject_path) for row in relations) != sorted(expected):
        raise _UnsupportedForm("subjects-parser-form-unresolved")
    occurrences = [{"subject_path": row.subject_path, "role": row.kind,
                    "source_ref": properties["governs" if row.kind == "GOVERNS" else "depends_on"]} for row in relations]
    return occurrences, text, properties


def collect_subject_model_sources(
    repository: Path, selected_carriers: Sequence, *, subject_profile: str = "legacy"
) -> SubjectModelSources:
    """Collect checked source occurrences, not admitted model facts.

    Coverage describes this bounded extraction only. Unsupported source forms
    are isolated; stale/forged pins and ambiguous selected identities fail.
    The root factory separately binds the profile's reviewed grammar pins.
    """
    _check_code()
    repository = Path(repository).resolve()
    profile = _subject_profile(subject_profile)
    _check_current_approved_grammar_pins(repository, profile)
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
            rows, _, _ = _property_rows(pin, raw, subject_profile=subject_profile)
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
    profile_evidence = subject_notation.profile_evidence(subject_profile)
    provider_profile = {"implementation_sha256": _LOADED_IMPLEMENTATION_SHA256,
                        "parser_implementation_sha256": _LOADED_PARSER_SHA256,
                        "fact_context_implementation_sha256": facts._LOADED_IMPLEMENTATION_SHA256,
                        "reviewed_grammar_pins": list(_GRAMMAR_PINS),
                        "subject_profile": profile.name,
                        "subject_profile_evidence": profile_evidence,
                        "recognition": "current-flat-scalar-governs-unique-dependency-collection",
                        "grammar_authority_binding": "root_required",
                        "semantic_conformance": "not_performed"}
    count = len(selected_carriers)
    result = {"provider": {"id": "caprmedio.subject-model-sources", "version": "1", "profile_sha256": _digest(provider_profile)},
              "grammar_pins": list(_GRAMMAR_PINS), "subject_profile": profile.name,
              "subject_profile_evidence": profile_evidence, "source_pins": pins, "occurrences": occurrences,
              "coverage": {"scope": "subject_occurrence_extraction", "disposition": "complete" if resolved_count == count else "incomplete",
                           "source_count": count, "resolved_source_count": resolved_count,
                           "unresolved_source_count": count - resolved_count, "occurrence_count": len(occurrences)},
              "unperformed": ["grammar_authority_binding", "target_resolution", "main_content_conformance", "native_admission"],
              "diagnostics": diagnostics}
    result["collection_sha256"] = _digest(result)
    _check_code()
    return SubjectModelSources(facts.canonical_bytes(result), _token=_TOKEN)
