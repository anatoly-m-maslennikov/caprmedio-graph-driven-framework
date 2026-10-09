"""Raw-checked, bounded Core Operations identity and Atom/Type candidates.

This family recognizes existing selected Action/Workflow Atom identities only.
Semantic Action/Workflow admission is unperformed: no native facts are emitted.
It does not admit GOVERNS targets or transfer other Carrier metadata, and it
does not establish complete graph/source-model validity.
"""

from __future__ import annotations

import hashlib
import json
import re
import tomllib
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path

import graph_fact_context as facts


class CoreEntityAdmissionError(ValueError):
    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(message)


def _fail(code: str, message: str) -> None:
    raise CoreEntityAdmissionError(code, message)


_TOKEN = object()
_IMPLEMENTATION_PATH = Path(__file__).resolve()
_LOADED_IMPLEMENTATION_SHA256 = hashlib.sha256(_IMPLEMENTATION_PATH.read_bytes()).hexdigest()
# Reviewed semantics, not whatever a future same-ID Carrier happens to say.
_REQUIRED_AUTHORITIES = {
    "CA-E-449": ("06_evaluation/CA-E-449-CORE_META_MODEL-GENERAL-EVALUATION_APPROACH--validate-entities-graph.md", 12, "29db3bbff5744963c4fc7960042e6267a826b2fe16198e954039f5b223f3b00a", "Evaluation"),
    "CA-R-1456": ("04_requirement/CA-R-1456-CORE_META_MODEL-GENERAL--derive-entities-views-from-selected-authority.md", 8, "3e389c9c223a5200e8fd7a1f3929dfa800f107e2b4e9a606a4eaf70247094fc8", "Requirement"),
    "CA-M-314": ("05_method/CA-M-314-CORE_META_MODEL-METHOD--write-operations-claims-with-type-specific-cce-profiles.md", 4, "a3f8c559979f66d1130dc199f1a842fff3e77e1e589fca77ff32e3276d61bbbc", "Method"),
    "CA-D-276": ("07_delivery/CA-D-276-CORE_META_MODEL-DELIVERY--use-economical-yaml-frontmatter.md", 15, "ea6013f935f9b465d4a6ea5afd80a20a44dbc4ab50db2d031f325510f4881b06", "Delivery"),
    "CA-R-1766": ("04_requirement/CA-R-1766-CORE_META_MODEL-CORE--make-the-type-value-of-an-atom-identity-bearing.md", 18, "693cf56a21f43b0e36cd07bfccb25332a6a29c529366131660cd7f29801d4ce8", "Requirement"),
    "CA-D-478": ("07_delivery/CA-D-478-CORE_META_MODEL-CORE-DELIVERY--store-every-atom-property-in-one-internal-location.md", 5, "a40ad3683ecddd536e5b7eb6c044e8da15806ab44946fa1354c408ce5e966464", "Delivery"),
    "CA-D-479": ("07_delivery/CA-D-479-CORE_META_MODEL-DELIVERY--use-stable-headings-for-atom-body-properties.md", 6, "0819f8433cde89484e21a200466504a9fdcad31b58958c777a761637fbb45ff1", "Delivery"),
    "CA-R-1624": ("04_requirement/CA-R-1624-CORE_META_MODEL-CORE-REQUIREMENT--keep-details-within-the-primary-contribution.md", 2, "d985c624f5c0b92010a3f1a670e2e12ef0d018aa221ce1052faab293060966cf", "Requirement"),
    "CA-R-1248": ("04_requirement/CA-R-1248-CORE_META_MODEL-CORE-REQUIREMENT--define-entity.md", 12, "7dc7c6805b23dc758fdca38e2d50506b86c2035844b90a78612c1690f664aad5", "Requirement"),
    "CA-E-246": ("06_evaluation/CA-E-246-CORE_META_MODEL-QA_CASE--validate-atom-subjects.md", 25, "6d5e65915b857be8e399aee9b32364dde2caa56ec6757bd8e69282b4ffee0098", "Evaluation"),
    "CA-D-446": ("07_delivery/CA-D-446-CORE_META_MODEL-CORE--give-every-non-draft-atom-revision-one-identifier.md", 7, "3391dbfa646ef362dd1c54cd8c9dab590ee7650f2215d51aec5b7f9ef49d4829", "Delivery"),
    "CA-R-1530": ("04_requirement/CA-R-1530-CORE_META_MODEL-CORE-REQUIREMENT--define-the-operations-content-role.md", 6, "8e6280d4acbbab76d70b936a69803d95d0d6e855845003d1e92e5d71470e328f", "Requirement"),
    "CA-R-1565": ("04_requirement/CA-R-1565-CORE_META_MODEL-CORE-REQUIREMENT--admit-the-operations-atom-types.md", 5, "ec302438794099e2a70d5bccf49b6489b92516b38bccb204e1266a55b2696f0e", "Requirement"),
    "CA-R-1562": ("04_requirement/CA-R-1562-CORE_META_MODEL-CORE-REQUIREMENT--define-the-action-operations-atom-type.md", 5, "05aeaca7cb5ac654f2f2303471587fa795914cd7c516bde1eb7be98a43cd594e", "Requirement"),
    "CA-R-1452": ("04_requirement/CA-R-1452-CORE_META_MODEL-CORE--define-action.md", 10, "d469011478752241340e3dd544f0744bddc7b7129e3ae7e1e249144363e5c007", "Requirement"),
    "CA-R-1563": ("04_requirement/CA-R-1563-CORE_META_MODEL-CORE-REQUIREMENT--define-the-workflow-operations-atom-type.md", 6, "302bc6369eb00725ed10692d423b17b333f343bf94f49be2e58ee0f042fc226f", "Requirement"),
    "CA-R-1508": ("04_requirement/CA-R-1508-CORE_META_MODEL-CORE-REQUIREMENT--define-workflow.md", 7, "ed2727d3a4457544c2aea4aea3f4364ca5fbe650e830eeb316fc4a0f41b4b4c5", "Requirement"),
}


def _digest(value: object) -> str:
    return hashlib.sha256(facts.canonical_bytes(value)).hexdigest()


def _check_code() -> None:
    facts._check_loaded_profile()
    try:
        digest = hashlib.sha256(_IMPLEMENTATION_PATH.read_bytes()).hexdigest()
    except OSError:
        _fail("profile-stale", "Loaded Core implementation cannot be checked")
    if digest != _LOADED_IMPLEMENTATION_SHA256:
        _fail("profile-stale", "Core implementation bytes changed after load")


@dataclass(frozen=True, slots=True, init=False)
class CoreEntityProfile:
    _bytes: bytes
    _repository: Path
    _carriers: tuple
    _token: object

    def __init__(self, data: bytes, repository: Path, carriers: tuple, *, _token: object = None) -> None:
        if _token is not _TOKEN:
            _fail("core-profile-untrusted", "Core profiles require the raw checked factory")
        object.__setattr__(self, "_bytes", data)
        object.__setattr__(self, "_repository", repository)
        object.__setattr__(self, "_carriers", carriers)
        object.__setattr__(self, "_token", _token)

    def as_dict(self) -> dict:
        _trusted_profile(self)
        return json.loads(self._bytes)

    @property
    def profile_sha256(self) -> str:
        return self.as_dict()["profile_sha256"]


@dataclass(frozen=True, slots=True, init=False)
class CheckedCarrierSource:
    _bytes: bytes
    _profile_sha256: str
    _token: object

    def __init__(self, data: bytes, profile_sha256: str, *, _token: object = None) -> None:
        if _token is not _TOKEN:
            _fail("core-source-untrusted", "Operations sources require the raw checked reader")
        object.__setattr__(self, "_bytes", data)
        object.__setattr__(self, "_profile_sha256", profile_sha256)
        object.__setattr__(self, "_token", _token)

    def as_dict(self) -> dict:
        if type(self) is not CheckedCarrierSource or self._token is not _TOKEN:
            _fail("core-source-untrusted", "Checked Operations sources are required")
        return json.loads(self._bytes)


def _trusted_profile(profile: object) -> None:
    if type(profile) is not CoreEntityProfile or getattr(profile, "_token", None) is not _TOKEN:
        _fail("core-profile-untrusted", "Caller descriptors or flags are not checked profiles")


def _registered_core(repository: Path, frontier: dict) -> dict:
    evidence = frontier.get("project_structure")
    if not isinstance(evidence, dict):
        _fail("core-structure-unbound", "Core admission needs sealed registered Project Structure")
    try:
        raw = facts._safe_path(repository, evidence["carrier_path"]).read_bytes()
        structure = tomllib.loads(raw.decode("utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError):
        _fail("core-structure-invalid", "Registered Project Structure cannot be read")
    if hashlib.sha256(raw).hexdigest() != evidence["carrier_sha256"]:
        _fail("core-structure-stale", "Registered Project Structure changed after sealing")
    records = structure.get("scope_units")
    if not isinstance(records, list):
        _fail("core-structure-invalid", "Project Structure lacks Scope Unit records")
    core = [record for record in records if isinstance(record, dict) and record.get("scope_unit_name") == "CORE_META_MODEL"]
    if len(core) != 1 or not isinstance(core[0].get("authority_path"), str):
        _fail("core-structure-invalid", "Exactly one Core authority path must be registered")
    authority_path = core[0]["authority_path"]
    facts._safe_path(repository, authority_path, folder=True)
    if frontier["selected_folder"] != authority_path:
        _fail("core-folder-foreign", "Selected folder is not registered Core authority")
    return {"scope_unit_name": "CORE_META_MODEL", "authority_path": authority_path, "source": dict(evidence)}


def prepare_core_entity_profile(repository: Path, authorities: Sequence,
                                source_frontier: Mapping, selection: Mapping) -> CoreEntityProfile:
    """Validate the complete sealed Core carrier sequence, not descriptors."""
    _check_code()
    repository = Path(repository).resolve()
    pool = facts._pool(repository, authorities)
    selected = facts._selection(selection, set(pool))
    frontier = facts._frontier(repository, source_frontier, pool, selected)
    registration = _registered_core(repository, frontier)
    authority_path = registration["authority_path"]
    for carrier, pin, raw in pool.values():
        if facts._raw_parts(raw)[3].get("current_scope_unit") != "CORE_META_MODEL":
            _fail("core-owner-foreign", "Sealed Core carrier has another current Scope owner")
        if not (repository / pin["carrier_path"]).is_relative_to(repository / authority_path):
            _fail("core-owner-foreign", "Sealed carrier is outside registered Core authority")
    evidence = []
    for atom_id, (suffix, revision, digest, role) in sorted(_REQUIRED_AUTHORITIES.items()):
        if atom_id not in pool:
            _fail("core-authority-missing", "Reviewed Core authority manifest is incomplete")
        carrier, pin, raw = pool[atom_id]
        if (pin["carrier_path"] != authority_path + "/" + suffix or pin["atom_revision"] != revision or
                pin["carrier_sha256"] != digest or carrier.content_role != role or carrier.status != "Active"):
            _fail("core-authority-unsupported", "Current Core authority differs from reviewed semantics")
        primary = facts._primary(pin, raw, role)
        if primary is None:
            _fail("core-authority-unsupported", "Reviewed authority lacks exact primary contribution")
        evidence.append(primary)
    for atom_id in ("CA-D-276", "CA-M-314", "CA-E-246"):
        details = facts.raw_section_property_evidence(repository, pool[atom_id][0], authority_sources=authorities)
        if details is None:
            _fail("core-authority-unsupported", "Encoding, role or Entity identity authority lacks checked Details")
        evidence.append(details)
    evidence.sort(key=facts._source_key)
    binding = {"registration": registration, "source_frontier": frontier, "selection": selected,
               "authority_inputs": evidence, "implementation_sha256": _LOADED_IMPLEMENTATION_SHA256,
               "fact_context_implementation_sha256": facts._LOADED_IMPLEMENTATION_SHA256,
               "profile_id": "core-operations-entity-profile", "profile_version": "1"}
    binding["profile_sha256"] = _digest(binding)
    return CoreEntityProfile(facts.canonical_bytes(binding), repository, tuple(authorities), _token=_TOKEN)


def _recheck_profile(profile: CoreEntityProfile) -> None:
    _trusted_profile(profile)
    data = profile.as_dict()
    current = prepare_core_entity_profile(profile._repository, profile._carriers,
                                          data["source_frontier"], data["selection"])
    if current._bytes != profile._bytes:
        _fail("core-profile-stale", "Core profile differs from current checked evidence")


def _operation_layout(raw: bytes) -> bool:
    """Apply the pinned D479 literal Property headings, not their position."""
    _, headings, fields = facts._body_headings(raw)
    return (bool(headings) and headings[0][1:] == (1, "Summary") and
            [name for _, level, name in headings if level == 1] == ["Summary"] and
            [name for _, level, name in headings if level == 2] == ["Operation", "Details"] and
            not any(key.casefold() in {"summary", "operation", "details"} for key in fields))


def _named_operation_type(raw: bytes, operation: dict, target: str) -> str | None:
    """One bounded primary means form proves its explicit Type head only.

    The remainder is one whole operational contribution, not a complete
    behavioral or Workflow validity evaluation. Secondary named definitions,
    mixed Type heads, bare means and unknown heads remain unsupported.
    """
    _, text, _, _ = facts._raw_parts(raw)
    contribution = operation["contribution"]
    declarations = []
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
        if re.fullmatch(r"(?:a |an |the )?[A-Za-z][A-Za-z0-9 -]*? +(?:\*\*means\*\*|means) +.+", line, re.IGNORECASE):
            declarations.append(line)
    if len(declarations) != 1:
        return None
    typed = re.fullmatch(re.escape(target) + r" \*\*means\*\* the (?:reusable )?(Action|Workflow) (?:that|whose) .+",
                         declarations[0])
    return typed[1] if typed else None


def checked_operations_source(repository: Path, carrier: object,
                              profile: CoreEntityProfile) -> CheckedCarrierSource:
    """Read current selected bytes, never claimed type/locator/pass fields."""
    _trusted_profile(profile)
    _check_code()
    repository = Path(repository).resolve()
    if repository != profile._repository:
        _fail("core-profile-foreign", "Core profile belongs to another repository")
    data = profile.as_dict()
    pin, raw = facts._carrier_pin(repository, carrier)
    if pin["atom_id"] not in data["selection"]["atom_ids"]:
        _fail("core-source-unselected", "Operations source is outside sealed native selection")
    bound = [row for row in data["source_frontier"]["carriers"] if row["atom_id"] == pin["atom_id"]]
    if len(bound) != 1 or any(bound[0][key] != value for key, value in pin.items()):
        _fail("core-source-stale", "Operations source differs from complete sealed Core frontier")
    lines, text, boundary, fields = facts._raw_parts(raw)
    if (fields.get("current_scope_unit") != "CORE_META_MODEL" or carrier.content_role != "Operations" or
            carrier.atom_type not in {"Action", "Workflow"} or carrier.status != "Active"):
        _fail("core-source-unsupported", "Only owned Core Active Action/Workflow source forms are supported")
    if not _operation_layout(raw):
        _fail("core-operation-unresolved", "Operations Property headings do not match the reviewed canonical layout")
    operation = facts._primary(pin, raw, "Operations")
    if operation is None:
        _fail("core-operation-unresolved", "Source lacks exact whole Operation contribution")
    governed = facts._governed_reference(pin, raw)
    if governed is None or _named_operation_type(raw, operation, governed[1]) != carrier.atom_type:
        _fail("core-operation-unresolved", "Exactly one named operational definition must prove the source Atom Type")
    type_lines = [index for index in range(1, boundary) if re.fullmatch(r"type:[ \t]*.+", text[index])]
    if len(type_lines) != 1 or fields.get("type") != carrier.atom_type:
        _fail("core-type-unresolved", "Atom Type lacks one exact scalar source location")
    type_source = facts._source(pin, lines, type_lines[0] + 1, type_lines[0] + 1,
                                kind="canonical_atom_property", property_path="type")
    source = {**pin, "content_role": carrier.content_role, "atom_type": carrier.atom_type,
              "status": carrier.status, "operation_source": operation, "type_source": type_source}
    return CheckedCarrierSource(facts.canonical_bytes(source), profile.profile_sha256, _token=_TOKEN)


def _decision(candidate: dict, profile: CoreEntityProfile, source: dict) -> dict:
    evidence = profile.as_dict()["authority_inputs"]
    semantic_refs = sorted([source["operation_source"], *evidence], key=facts._source_key)
    checks = [
        {"code": "core-authority-current", "disposition": "pass", "source_refs": evidence},
        {"code": "selected-core-native-source", "disposition": "pass", "source_refs": [candidate["source_ref"]]},
        {"code": "actual-atom-identity-and-property-owner", "disposition": "pass", "source_refs": [candidate["source_ref"]]},
        {"code": "named-operational-definition-form", "disposition": "pass", "source_refs": [source["operation_source"]]},
        {"code": "named-operational-definition-type-consistency", "disposition": "pass", "source_refs": sorted([source["operation_source"], source["type_source"]], key=facts._source_key)},
        {"code": "canonical-operations-property-layout", "disposition": "pass", "source_refs": [source["operation_source"]]},
        {"code": "single-canonical-atom-type", "disposition": "pass", "source_refs": [source["type_source"]]},
        {"code": "semantic-profile-unperformed", "disposition": "unresolved", "source_refs": semantic_refs},
    ]
    checks.sort(key=lambda row: row["code"])
    decision = {"candidate_id": candidate["candidate_id"], "disposition": "unresolved",
                "evaluator": {"id": "core-operations-entity-profile", "version": "1", "profile_sha256": profile.profile_sha256},
                "authority_inputs": evidence, "checks": checks}
    decision["decision_sha256"] = _digest(decision)
    return decision


def review_core_entity_candidates(sources: Sequence[CheckedCarrierSource], profile: CoreEntityProfile) -> dict:
    """Retain checked candidates; semantic admission and coverage are unresolved."""
    _recheck_profile(profile)
    if not isinstance(sources, Sequence) or isinstance(sources, (str, bytes)):
        _fail("core-source-untrusted", "Checked Operations source objects are required")
    rows = []
    for source in sources:
        if type(source) is not CheckedCarrierSource or source._token is not _TOKEN or source._profile_sha256 != profile.profile_sha256:
            _fail("core-source-untrusted", "Source was not checked against this sealed profile")
        row = source.as_dict()
        carrier = next((item for item in profile._carriers if item.atom_id == row["atom_id"]), None)
        current = checked_operations_source(profile._repository, carrier, profile)
        if current._bytes != source._bytes:
            _fail("core-source-stale", "Checked Operations source is no longer current")
        rows.append(row)
    if len({row["atom_id"] for row in rows}) != len(rows):
        _fail("core-source-duplicate", "Checked source identities must be unique")
    candidates = []
    for row in sorted(rows, key=lambda item: item["atom_id"]):
        for fact_class, payload, source_ref in (
            ("entity_admission", {"entity_identity": row["atom_id"]}, row["operation_source"]),
            ("entity_property", {"entity_identity": row["atom_id"], "property_identity": "Atom/Type",
                                 "value": {"type": "string", "data": row["atom_type"]}}, row["type_source"]),
        ):
            candidate = {"fact_class": fact_class, "payload": payload, "source_ref": source_ref,
                         "recognizer": {"id": "core-operations-entity-profile", "version": "1", "profile_sha256": profile.profile_sha256}}
            candidate["candidate_id"] = "core-candidate:" + _digest(candidate)
            candidates.append(candidate)
    candidates.sort(key=lambda row: row["candidate_id"])
    by_atom = {row["atom_id"]: row for row in rows}
    decisions = [_decision(candidate, profile, by_atom[candidate["source_ref"]["atom_id"]]) for candidate in candidates]
    admitted = []
    coverage = [{"fact_class": fact_class, "disposition": "unknown", "selected_result": "unknown",
                 "candidate_count": sum(row["fact_class"] == fact_class for row in candidates),
                 "admitted_count": sum(row["fact_class"] == fact_class for row in admitted),
                 "source_refs": sorted([row["source_ref"] for row in candidates if row["fact_class"] == fact_class], key=facts._source_key)}
                for fact_class in ("entity_admission", "entity_property", "relation")]
    return {"provider": {"id": "core-operations-entity-profile", "version": "1", "profile_sha256": profile.profile_sha256},
            "candidates": candidates, "admission_decisions": decisions, "admitted_facts": admitted,
            "coverage": coverage, "diagnostics": [{"code": "core-profile-partial", "severity": "info",
                                                    "source_refs": [], "details": {"supported_family": "selected-core-operations-action-workflow-identity-and-atom-type-candidates",
                                                                                   "semantic_admission": "unperformed"}}]}
