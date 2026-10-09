"""Pure validation for the closed CA-D-539 derived fact-context contract.

The factory in :mod:`graph_fact_context` is responsible for checking current
carrier bytes and producing a trusted context.  This module only validates an
already-materialized context mapping.  It deliberately does not read source
carriers, infer facts, or turn a candidate into an admission.
"""

from __future__ import annotations

import hashlib
import re
from collections.abc import Callable
from pathlib import Path, PurePosixPath
from typing import Any


class ContractError(ValueError):
    """Stable validation failure whose public information is only ``code``."""

    def __init__(self, code: str) -> None:
        self.code = code
        # Never include a rejected value, source text, or exception detail.
        super().__init__(code)


_IMPLEMENTATION_PATH = Path(__file__).resolve()
_LOADED_IMPLEMENTATION_SHA256 = hashlib.sha256(_IMPLEMENTATION_PATH.read_bytes()).hexdigest()
# Public aliases let the owning factory expose the validator's own code pin.
IMPLEMENTATION_PATH = _IMPLEMENTATION_PATH
LOADED_IMPLEMENTATION_SHA256 = _LOADED_IMPLEMENTATION_SHA256

_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_GRAPH_KINDS = frozenset(("entities", "terms"))
_FACT_CLASSES = frozenset((
    "entity_admission", "definition", "classification", "entity_property", "relation",
))
_DISPOSITIONS = frozenset(("admitted", "rejected", "unresolved"))
_CHECK_DISPOSITIONS = frozenset(("pass", "fail", "unresolved", "not_applicable"))
_COVERAGE_DISPOSITIONS = frozenset(("complete", "incomplete", "unknown"))
_SELECTED_RESULTS = frozenset(("nonempty", "empty", "unknown"))
_DIAGNOSTIC_SEVERITIES = frozenset(("error", "warning", "info"))
_REPRESENTATIONS = frozenset(("native", "external_reference"))

# Diagnostic details are deliberately generic, but they are not a carrier or
# credential channel.  Keep this boundary key-based and narrow enough not to
# reject legitimate Atom identifiers, paths, semantic names, or SHA-256
# values.  The check is recursive because details may contain provider-owned
# nested objects and arrays.
_REDACTED_DETAIL_KEYS = frozenset((
    "message", "raw", "raw_source", "raw_content", "source_text", "secret",
    "password", "passwd", "api_key", "apikey", "access_token", "auth_token",
    "bearer_token", "session_token", "refresh_token", "credential", "credentials",
    "authorization", "private_key", "secret_key", "client_secret", "token",
))
_REDACTED_DETAIL_KEY_SUFFIXES = ("_password", "_passwd", "_secret", "_credential", "_credentials")
_SECRET_VALUE_PATTERNS = (
    re.compile(r"-----BEGIN [^-]*PRIVATE KEY-----", re.IGNORECASE),
    re.compile(r"\b(?:bearer|basic)\s+[A-Za-z0-9._~+/=-]{16,}\b", re.IGNORECASE),
    re.compile(r"\b(?:sk|ghp|gho|github_pat|xox[baprs])[-_][A-Za-z0-9_-]{12,}\b", re.IGNORECASE),
    re.compile(r"^[A-Za-z0-9_-]{24,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}$"),
)

_TOP_FIELDS = frozenset((
    "schema_version", "context_kind", "graph_kind", "source_binding", "provider",
    "authority_sources", "relation_registry", "coverage", "candidates",
    "admission_decisions", "admitted_facts", "derivations", "diagnostics",
    "context_sha256",
))
_SOURCE_FIELDS = frozenset(("atom_id", "atom_revision", "carrier_path", "carrier_sha256", "contribution"))
_CONTRIBUTION_FIELDS = {
    "primary_content": frozenset(("kind", "section", "start_line", "end_line", "text_sha256")),
    "authored_direct_relation": frozenset((
        "kind", "property_path", "canonical_target_reference", "start_line", "end_line", "text_sha256",
    )),
    "canonical_atom_property": frozenset(("kind", "start_line", "end_line", "text_sha256")),
}
_SOURCE_BINDING_FIELDS = frozenset((
    "source_frontier_sha256", "selection_sha256", "authority_frontier_sha256",
))
_PROVIDER_FIELDS = frozenset(("id", "version", "profile_sha256"))
_EVALUATOR_FIELDS = frozenset(("id", "version", "profile_sha256"))
_REGISTRY_FIELDS = frozenset((
    "kind", "metadata", "authority_inputs", "evaluator", "checks", "registry_record_sha256",
))
_REGISTRY_KIND_FIELDS = frozenset(("graph_kind", "canonical_name"))
_REGISTRY_METADATA_FIELDS = frozenset((
    "meaning", "direction", "inverse", "source_class", "target_class", "source_graph_context",
    "target_graph_context", "cardinality", "authority_effect", "transitivity", "applicability",
    "status", "exclusive_purpose",
))
_CHECK_FIELDS = frozenset(("code", "disposition", "source_refs"))
_COVERAGE_FIELDS = frozenset((
    "fact_class", "disposition", "selected_result", "candidate_count", "admitted_count", "source_refs",
))
_CANDIDATE_FIELDS = frozenset(("candidate_id", "fact_class", "payload", "recognizer", "source_ref"))
_DECISION_FIELDS = frozenset((
    "candidate_id", "disposition", "evaluator", "authority_inputs", "checks", "decision_sha256",
))
_FACT_FIELDS = frozenset(("fact_id", "candidate_id", "fact_class", "payload", "decision_sha256"))
_DERIVATION_FIELDS = frozenset((
    "derivation_id", "fact_class", "payload", "input_fact_ids", "authority_inputs", "evaluator",
    "checks", "disposition", "derivation_sha256",
))
_DIAGNOSTIC_FIELDS = frozenset(("code", "severity", "source_refs", "details"))


def _fail(code: str) -> None:
    raise ContractError(code)


def current_implementation_sha256() -> str:
    """Return the current on-disk digest of this validator implementation."""

    try:
        return hashlib.sha256(_IMPLEMENTATION_PATH.read_bytes()).hexdigest()
    except OSError:
        _fail("profile-stale")
    raise AssertionError("unreachable")


def recheck_implementation() -> None:
    """Reject a validator whose loaded code differs from current disk bytes."""

    if current_implementation_sha256() != _LOADED_IMPLEMENTATION_SHA256:
        _fail("profile-stale")


def check_loaded_implementation() -> None:
    """Alias used by factories when rechecking the loaded validator profile."""

    recheck_implementation()


def implementation_sha256() -> str:
    """Return the load-time implementation digest used in profile bindings."""

    return _LOADED_IMPLEMENTATION_SHA256


def current_digest() -> str:
    """Short compatibility alias for the current implementation digest."""

    return current_implementation_sha256()


def loaded_implementation_sha256() -> str:
    """Return the digest captured when this module was loaded."""

    return _LOADED_IMPLEMENTATION_SHA256


def current_implementation_digest() -> str:
    """Descriptive alias for :func:`current_implementation_sha256`."""

    return current_implementation_sha256()


def recheck_loaded_implementation() -> None:
    """Descriptive alias for :func:`recheck_implementation`."""

    recheck_implementation()


def _check_loaded_profile() -> None:
    """Factory-compatible private spelling for a loaded-code recheck."""

    recheck_implementation()


def _canonical(value: object) -> bytes:
    """Use the factory's exact canonical JSON rule without an import cycle."""

    try:
        try:
            from graph_fact_context import canonical_bytes
        except ModuleNotFoundError:
            from .graph_fact_context import canonical_bytes  # type: ignore[import-not-found]
        return canonical_bytes(value)
    except ContractError:
        raise
    except Exception:
        _fail("canonical-json-invalid")
    raise AssertionError("unreachable")


def _digest(value: object) -> str:
    return hashlib.sha256(_canonical(value)).hexdigest()


def _without(value: dict[str, Any], field: str) -> dict[str, Any]:
    result = dict(value)
    result.pop(field, None)
    return result


def _keys(value: object, expected: frozenset[str], code: str) -> dict[str, Any]:
    if type(value) is not dict or set(value) != expected:
        _fail(code)
    return value


def _list(value: object, code: str) -> list[Any]:
    if type(value) is not list:
        _fail(code)
    return value


def _string(value: object, code: str, *, nonempty: bool = True) -> str:
    if type(value) is not str or (nonempty and not value):
        _fail(code)
    return value


def _sha(value: object, code: str) -> str:
    if type(value) is not str or _SHA256.fullmatch(value) is None:
        _fail(code)
    return value


def _allowed(value: object, allowed: frozenset[str], code: str) -> str:
    if type(value) is not str or value not in allowed:
        _fail(code)
    return value


def _positive_int(value: object, code: str) -> int:
    if type(value) is not int or value < 1:
        _fail(code)
    return value


def _nonnegative_int(value: object, code: str) -> int:
    if type(value) is not int or value < 0:
        _fail(code)
    return value


def _path(value: object, code: str) -> str:
    text = _string(value, code)
    if "\\" in text or "\x00" in text:
        _fail(code)
    path = PurePosixPath(text)
    if path.is_absolute() or ".." in path.parts or path.as_posix() != text or text == ".":
        _fail(code)
    return text


def _ordered_unique(
    values: list[Any], key: Callable[[Any], Any], code: str, *, identity: Callable[[Any], Any] | None = None,
) -> None:
    identities = [identity(item) if identity is not None else key(item) for item in values]
    try:
        duplicate = len(identities) != len(set(identities))
        ordered = values == sorted(values, key=key)
    except (TypeError, ValueError):
        _fail(code)
    if duplicate or not ordered:
        _fail(code)


def _source_key(source: dict[str, Any]) -> tuple[Any, ...]:
    contribution = source["contribution"]
    return (
        source["atom_id"], source["atom_revision"], source["carrier_path"], contribution["kind"],
        contribution.get("section", contribution.get("property_path", "")),
        contribution.get("canonical_target_reference", ""), contribution["start_line"],
        contribution["end_line"], contribution["text_sha256"],
    )


def _source_identity(source: dict[str, Any]) -> tuple[Any, ...]:
    key = _source_key(source)
    return key[:-1]


def _validate_source(source: object) -> dict[str, Any]:
    row = _keys(source, _SOURCE_FIELDS, "source-evidence-schema-invalid")
    _string(row["atom_id"], "source-evidence-invalid")
    _positive_int(row["atom_revision"], "source-evidence-invalid")
    _path(row["carrier_path"], "source-evidence-invalid")
    _sha(row["carrier_sha256"], "source-evidence-invalid")
    contribution = row["contribution"]
    if type(contribution) is not dict:
        _fail("source-evidence-schema-invalid")
    # The locator kind is the discriminator, so inspect it before checking its
    # exact closed keys.  All three forms carry an inclusive line span/hash.
    kind = _string(contribution.get("kind"), "source-locator-invalid")
    if kind not in _CONTRIBUTION_FIELDS:
        _fail("source-locator-invalid")
    if kind == "canonical_atom_property":
        locator_keys = set(contribution)
        allowed = {"kind", "property_path", "section", "start_line", "end_line", "text_sha256"}
        if locator_keys - allowed or ("property_path" in contribution) == ("section" in contribution):
            _fail("source-locator-invalid")
        if "property_path" in contribution:
            _string(contribution["property_path"], "source-locator-invalid")
        else:
            _string(contribution["section"], "source-locator-invalid")
    else:
        _keys(contribution, _CONTRIBUTION_FIELDS[kind], "source-locator-invalid")
        if kind == "primary_content":
            _allowed(contribution["section"], frozenset(("Claim", "Operation")), "source-locator-invalid")
        else:
            property_path = _string(contribution["property_path"], "source-locator-invalid")
            if not property_path.startswith("relations.") or property_path == "relations.":
                _fail("source-locator-invalid")
            _string(contribution["canonical_target_reference"], "source-locator-invalid")
    _positive_int(contribution["start_line"], "source-locator-invalid")
    end_line = _positive_int(contribution["end_line"], "source-locator-invalid")
    if end_line < contribution["start_line"]:
        _fail("source-locator-invalid")
    _sha(contribution["text_sha256"], "source-locator-invalid")
    return row


def _source_array(
    value: object, known: dict[bytes, dict[str, Any]], code: str,
) -> list[dict[str, Any]]:
    rows = _list(value, code)
    result: list[dict[str, Any]] = []
    seen: set[tuple[Any, ...]] = set()
    for item in rows:
        row = _validate_source(item)
        serialized = _canonical(row)
        if serialized not in known or known[serialized] != row:
            _fail("source-reference-unknown")
        identity = _source_identity(row)
        if identity in seen:
            _fail("source-reference-duplicate")
        seen.add(identity)
        result.append(row)
    _ordered_unique(result, _source_key, code, identity=_source_identity)
    return result


def _validate_evaluator(value: object, code: str) -> dict[str, Any]:
    row = _keys(value, _EVALUATOR_FIELDS, code)
    _string(row["id"], code)
    _string(row["version"], code)
    _sha(row["profile_sha256"], code)
    return row


def _validate_inverse(value: object) -> dict[str, Any]:
    if type(value) is not dict:
        _fail("registry-inverse-invalid")
    kind = value.get("kind")
    if kind == "none":
        _keys(value, frozenset(("kind",)), "registry-inverse-invalid")
    elif kind == "reverse_navigation":
        _keys(value, frozenset(("kind",)), "registry-inverse-invalid")
    elif kind == "declared":
        row = _keys(value, frozenset(("kind", "graph_kind", "canonical_name")), "registry-inverse-invalid")
        _allowed(row["graph_kind"], _GRAPH_KINDS, "registry-inverse-invalid")
        _string(row["canonical_name"], "registry-inverse-invalid")
    else:
        _fail("registry-inverse-invalid")
    return value


def _validate_checks(
    value: object, known_sources: dict[bytes, dict[str, Any]], code: str,
) -> list[dict[str, Any]]:
    rows = _list(value, code)
    result: list[dict[str, Any]] = []
    for item in rows:
        row = _keys(item, _CHECK_FIELDS, code)
        _string(row["code"], code)
        _allowed(row["disposition"], _CHECK_DISPOSITIONS, code)
        _source_array(row["source_refs"], known_sources, code)
        result.append(row)
    _ordered_unique(result, lambda item: item["code"], code, identity=lambda item: item["code"])
    return result


def _validate_registry(
    value: object, graph_kind: str, known_sources: dict[bytes, dict[str, Any]],
) -> tuple[list[dict[str, Any]], dict[tuple[str, str], dict[str, Any]], dict[str, dict[str, Any]]]:
    rows = _list(value, "registry-schema-invalid")
    result: list[dict[str, Any]] = []
    by_kind: dict[tuple[str, str], dict[str, Any]] = {}
    by_digest: dict[str, dict[str, Any]] = {}
    for item in rows:
        row = _keys(item, _REGISTRY_FIELDS, "registry-schema-invalid")
        kind = _keys(row["kind"], _REGISTRY_KIND_FIELDS, "registry-schema-invalid")
        if kind["graph_kind"] != graph_kind:
            _fail("registry-kind-invalid")
        _string(kind["canonical_name"], "registry-kind-invalid")
        metadata = _keys(row["metadata"], _REGISTRY_METADATA_FIELDS, "registry-metadata-invalid")
        _validate_inverse(metadata["inverse"])
        _source_array(row["authority_inputs"], known_sources, "registry-source-invalid")
        _validate_evaluator(row["evaluator"], "registry-evaluator-invalid")
        _validate_checks(row["checks"], known_sources, "registry-checks-invalid")
        digest = _sha(row["registry_record_sha256"], "registry-digest-invalid")
        if digest != _digest(_without(row, "registry_record_sha256")):
            _fail("registry-digest-mismatch")
        name = kind["canonical_name"]
        identity = (kind["graph_kind"], name)
        if identity in by_kind or digest in by_digest:
            _fail("registry-duplicate")
        if name == "BEARS":
            # BEARS is a derived inverse view, never an authored primitive kind.
            _fail("registry-inverse-invalid")
        by_kind[identity] = row
        by_digest[digest] = row
        result.append(row)
    _ordered_unique(result, lambda item: (item["kind"]["graph_kind"], item["kind"]["canonical_name"]), "registry-order-invalid")
    return result, by_kind, by_digest


def _validate_kind(value: object, graph_kind: str, code: str) -> dict[str, Any]:
    row = _keys(value, frozenset(("graph_kind", "canonical_name")), code)
    if row["graph_kind"] != graph_kind:
        _fail(code)
    _string(row["canonical_name"], code)
    return row


def _validate_endpoint(value: object, code: str) -> dict[str, Any]:
    row = _keys(value, frozenset(("identity", "graph_kind", "node_class")), code)
    _string(row["identity"], code)
    _allowed(row["graph_kind"], _GRAPH_KINDS, code)
    _string(row["node_class"], code)
    return row


def _validate_nonrelation_payload(
    value: object, fact_class: str, graph_kind: str | None, code: str, enforce_context_kind: bool,
) -> dict[str, Any]:
    if fact_class == "entity_admission":
        row = _keys(value, frozenset(("entity_identity",)), code)
        if enforce_context_kind and graph_kind != "entities":
            _fail(code)
        _string(row["entity_identity"], code)
    elif fact_class == "definition":
        row = _keys(value, frozenset(("term_identity", "subject_path")), code)
        if enforce_context_kind and graph_kind != "terms":
            _fail(code)
        _string(row["term_identity"], code)
        _string(row["subject_path"], code)
    elif fact_class == "classification":
        row = _keys(value, frozenset(("entity_identity", "class_identity")), code)
        if enforce_context_kind and graph_kind != "entities":
            _fail(code)
        _string(row["entity_identity"], code)
        _string(row["class_identity"], code)
    elif fact_class == "entity_property":
        row = _keys(value, frozenset(("entity_identity", "property_identity", "value")), code)
        if enforce_context_kind and graph_kind != "entities":
            _fail(code)
        _string(row["entity_identity"], code)
        _string(row["property_identity"], code)
        value_row = _keys(row["value"], frozenset(("type", "data")), code)
        _string(value_row["type"], code)
        _canonical(value_row["data"])
    else:
        _fail("fact-class-invalid")
    return row


def _validate_relation_payload(
    value: object, graph_kind: str | None, code: str,
) -> dict[str, Any]:
    row = _keys(value, frozenset(("kind", "registry_record_sha256", "source", "target", "representation")), code)
    if graph_kind is None:
        kind = _keys(row["kind"], frozenset(("graph_kind", "canonical_name")), code)
        _allowed(kind["graph_kind"], _GRAPH_KINDS, code)
        _string(kind["canonical_name"], code)
    else:
        _validate_kind(row["kind"], graph_kind, code)
    _sha(row["registry_record_sha256"], code)
    _validate_endpoint(row["source"], code)
    _validate_endpoint(row["target"], code)
    _allowed(row["representation"], _REPRESENTATIONS, code)
    return row


def _validate_payload(
    value: object, fact_class: str, graph_kind: str | None, code: str,
    *, enforce_context_kind: bool = True,
) -> dict[str, Any]:
    if fact_class == "relation":
        return _validate_relation_payload(value, graph_kind, code)
    return _validate_nonrelation_payload(value, fact_class, graph_kind, code, enforce_context_kind)


def _registry_for_payload(
    payload: dict[str, Any], by_digest: dict[str, dict[str, Any]], graph_kind: str, code: str,
) -> dict[str, Any]:
    digest = payload["registry_record_sha256"]
    registry = by_digest.get(digest)
    if registry is None:
        _fail("registry-reference-unknown")
    relation_name = payload["kind"]["canonical_name"]
    registry_name = registry["kind"]["canonical_name"]
    if relation_name == "BEARS":
        inverse = registry["metadata"]["inverse"]
        if not (
            inverse.get("kind") == "declared" and inverse.get("graph_kind") == graph_kind
            and inverse.get("canonical_name") == "BEARS" and registry_name != "BEARS"
        ):
            _fail("registry-inverse-invalid")
    elif registry_name != relation_name or registry["kind"]["graph_kind"] != graph_kind:
        _fail("registry-reference-mismatch")
    return registry


def _all_checks_pass(checks: list[dict[str, Any]]) -> bool:
    return bool(checks) and all(row["disposition"] in {"pass", "not_applicable"} for row in checks)


def _payload_bytes(value: object) -> bytes:
    return _canonical(value)


def _validate_candidates(
    value: object, graph_kind: str, known_sources: dict[bytes, dict[str, Any]],
    by_digest: dict[str, dict[str, Any]],
) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    rows = _list(value, "candidate-schema-invalid")
    result: list[dict[str, Any]] = []
    by_id: dict[str, dict[str, Any]] = {}
    for item in rows:
        row = _keys(item, _CANDIDATE_FIELDS, "candidate-schema-invalid")
        candidate_id = _string(row["candidate_id"], "candidate-invalid")
        fact_class = _string(row["fact_class"], "candidate-invalid")
        if fact_class not in _FACT_CLASSES:
            _fail("candidate-class-invalid")
        _validate_payload(
            row["payload"], fact_class, graph_kind, "candidate-payload-invalid",
            enforce_context_kind=False,
        )
        _validate_evaluator(row["recognizer"], "candidate-recognizer-invalid")
        source_ref = _source_array([row["source_ref"]], known_sources, "candidate-source-invalid")
        if len(source_ref) != 1:
            _fail("candidate-source-invalid")
        if fact_class == "relation":
            _registry_for_payload(row["payload"], by_digest, graph_kind, "candidate-registry-invalid")
            if row["payload"]["kind"]["canonical_name"] == "BEARS":
                _fail("candidate-inverse-direct")
        if candidate_id in by_id:
            _fail("candidate-duplicate")
        by_id[candidate_id] = row
        result.append(row)
    _ordered_unique(result, lambda item: item["candidate_id"], "candidate-order-invalid", identity=lambda item: item["candidate_id"])
    return result, by_id


def _validate_decisions(
    value: object, candidates: dict[str, dict[str, Any]], known_sources: dict[bytes, dict[str, Any]],
) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    rows = _list(value, "decision-schema-invalid")
    result: list[dict[str, Any]] = []
    by_candidate: dict[str, dict[str, Any]] = {}
    for item in rows:
        row = _keys(item, _DECISION_FIELDS, "decision-schema-invalid")
        candidate_id = _string(row["candidate_id"], "decision-invalid")
        if candidate_id not in candidates or candidate_id in by_candidate:
            _fail("decision-reference-invalid")
        _allowed(row["disposition"], _DISPOSITIONS, "decision-invalid")
        _validate_evaluator(row["evaluator"], "decision-evaluator-invalid")
        _source_array(row["authority_inputs"], known_sources, "decision-source-invalid")
        _validate_checks(row["checks"], known_sources, "decision-checks-invalid")
        digest = _sha(row["decision_sha256"], "decision-digest-invalid")
        if digest != _digest(_without(row, "decision_sha256")):
            _fail("decision-digest-mismatch")
        if row["disposition"] == "admitted" and not _all_checks_pass(row["checks"]):
            _fail("decision-check-failed")
        by_candidate[candidate_id] = row
        result.append(row)
    if set(by_candidate) != set(candidates):
        _fail("decision-coverage-invalid")
    _ordered_unique(result, lambda item: item["candidate_id"], "decision-order-invalid", identity=lambda item: item["candidate_id"])
    return result, by_candidate


def _validate_facts(
    value: object, graph_kind: str, candidates: dict[str, dict[str, Any]],
    decisions: dict[str, dict[str, Any]], by_digest: dict[str, dict[str, Any]],
) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    rows = _list(value, "fact-schema-invalid")
    result: list[dict[str, Any]] = []
    by_id: dict[str, dict[str, Any]] = {}
    for item in rows:
        row = _keys(item, _FACT_FIELDS, "fact-schema-invalid")
        fact_id = _string(row["fact_id"], "fact-invalid")
        candidate_id = _string(row["candidate_id"], "fact-invalid")
        if fact_id in by_id or candidate_id not in candidates:
            _fail("fact-reference-invalid")
        candidate = candidates[candidate_id]
        if type(row["fact_class"]) is not str or row["fact_class"] != candidate["fact_class"] or row["fact_class"] not in _FACT_CLASSES:
            _fail("fact-class-mismatch")
        _validate_payload(row["payload"], row["fact_class"], graph_kind, "fact-payload-invalid")
        decision = decisions.get(candidate_id)
        if decision is None or decision["disposition"] != "admitted":
            _fail("fact-decision-invalid")
        if row["decision_sha256"] != decision["decision_sha256"]:
            _fail("fact-decision-mismatch")
        if _payload_bytes(row["payload"]) != _payload_bytes(candidate["payload"]):
            _fail("fact-payload-mismatch")
        if row["fact_class"] == "relation":
            _registry_for_payload(row["payload"], by_digest, graph_kind, "fact-registry-invalid")
            if row["payload"]["kind"]["canonical_name"] == "BEARS":
                _fail("fact-inverse-direct")
        by_id[fact_id] = row
        result.append(row)
    admitted_candidates = {candidate_id for candidate_id, decision in decisions.items() if decision["disposition"] == "admitted"}
    if {row["candidate_id"] for row in result} != admitted_candidates:
        _fail("fact-coverage-invalid")
    _ordered_unique(result, lambda item: item["fact_id"], "fact-order-invalid", identity=lambda item: item["fact_id"])
    return result, by_id


def _validate_derivation_row(
    item: object, graph_kind: str, known_sources: dict[bytes, dict[str, Any]],
    by_digest: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    row = _keys(item, _DERIVATION_FIELDS, "derivation-schema-invalid")
    _string(row["derivation_id"], "derivation-invalid")
    if row["fact_class"] != "relation":
        _fail("derivation-class-invalid")
    _validate_payload(row["payload"], "relation", graph_kind, "derivation-payload-invalid")
    inputs = _list(row["input_fact_ids"], "derivation-input-invalid")
    if not inputs or any(type(item_id) is not str or not item_id for item_id in inputs):
        _fail("derivation-input-invalid")
    if inputs != sorted(set(inputs)):
        _fail("derivation-input-order-invalid")
    _source_array(row["authority_inputs"], known_sources, "derivation-source-invalid")
    _validate_evaluator(row["evaluator"], "derivation-evaluator-invalid")
    _validate_checks(row["checks"], known_sources, "derivation-checks-invalid")
    _allowed(row["disposition"], _DISPOSITIONS, "derivation-invalid")
    _sha(row["derivation_sha256"], "derivation-digest-invalid")
    if row["derivation_sha256"] != _digest(_without(row, "derivation_sha256")):
        _fail("derivation-digest-mismatch")
    _registry_for_payload(row["payload"], by_digest, graph_kind, "derivation-registry-invalid")
    if row["disposition"] == "admitted" and not _all_checks_pass(row["checks"]):
        _fail("derivation-check-failed")
    return row


def _validate_derivations(
    value: object, graph_kind: str, facts: dict[str, dict[str, Any]], known_sources: dict[bytes, dict[str, Any]],
    by_digest: dict[str, dict[str, Any]],
) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    rows = _list(value, "derivation-schema-invalid")
    result: list[dict[str, Any]] = []
    by_id: dict[str, dict[str, Any]] = {}
    all_ids = set(facts)
    for item in rows:
        row = _validate_derivation_row(item, graph_kind, known_sources, by_digest)
        derivation_id = row["derivation_id"]
        if derivation_id in all_ids or derivation_id in by_id:
            _fail("derivation-duplicate")
        all_ids.add(derivation_id)
        by_id[derivation_id] = row
        result.append(row)
    _ordered_unique(result, lambda item: item["derivation_id"], "derivation-order-invalid", identity=lambda item: item["derivation_id"])
    for row in result:
        for input_id in row["input_fact_ids"]:
            if input_id not in facts and input_id not in by_id:
                _fail("derivation-input-unknown")
    # Inputs are allowed only from admitted relation facts/derivations.  This
    # is checked after all IDs are known so forward references remain valid.
    for row in result:
        for input_id in row["input_fact_ids"]:
            source = facts.get(input_id, by_id.get(input_id))
            if source is None or source.get("fact_class", "relation") != "relation":
                _fail("derivation-input-invalid")
            if input_id in by_id and source["disposition"] != "admitted":
                _fail("derivation-input-unadmitted")
    return result, by_id


def _check_derivation_dag(derivations: dict[str, dict[str, Any]]) -> None:
    state: dict[str, int] = {}

    def visit(identifier: str) -> None:
        marker = state.get(identifier, 0)
        if marker == 1:
            _fail("derivation-cycle")
        if marker == 2:
            return
        state[identifier] = 1
        row = derivations[identifier]
        for input_id in row["input_fact_ids"]:
            if input_id in derivations:
                visit(input_id)
        state[identifier] = 2

    for identifier in derivations:
        visit(identifier)


def _check_inverse_derivations(
    derivations: list[dict[str, Any]], facts: dict[str, dict[str, Any]],
    derivation_map: dict[str, dict[str, Any]], by_digest: dict[str, dict[str, Any]], graph_kind: str,
) -> None:
    for row in derivations:
        payload = row["payload"]
        relation_name = payload["kind"]["canonical_name"]
        if relation_name != "BEARS":
            continue
        if row["disposition"] != "admitted":
            continue
        owner = _registry_for_payload(payload, by_digest, graph_kind, "derivation-inverse-invalid")
        owner_name = owner["kind"]["canonical_name"]
        source_endpoint = payload["source"]
        target_endpoint = payload["target"]
        found_inverse_input = False
        for input_id in row["input_fact_ids"]:
            source = facts.get(input_id, derivation_map.get(input_id))
            if source is None or source.get("disposition", "admitted") != "admitted":
                continue
            source_payload = source["payload"]
            if source_payload["kind"]["canonical_name"] != owner_name:
                continue
            if (
                source_payload["source"] == target_endpoint
                and source_payload["target"] == source_endpoint
            ):
                found_inverse_input = True
                break
        if not found_inverse_input:
            _fail("derivation-inverse-input-invalid")


def _check_native_semantics(
    graph_kind: str, facts: list[dict[str, Any]], derivations: list[dict[str, Any]],
) -> None:
    native_ids = {
        row["payload"]["entity_identity"]
        for row in facts
        if row["fact_class"] == "entity_admission"
    }
    native_ids.update(
        row["payload"]["term_identity"]
        for row in facts
        if row["fact_class"] == "definition"
    )
    for row in facts:
        if row["fact_class"] == "entity_property" and row["payload"]["entity_identity"] not in native_ids:
            _fail("property-bearer-unadmitted")
    for row in (*facts, *[item for item in derivations if item["disposition"] == "admitted"]):
        if row["fact_class"] != "relation":
            continue
        payload = row["payload"]
        endpoints_native = all(
            endpoint["graph_kind"] == graph_kind and endpoint["identity"] in native_ids
            for endpoint in (payload["source"], payload["target"])
        )
        if payload["representation"] == "native" and not endpoints_native:
            _fail("native-endpoint-unadmitted")
        if payload["representation"] == "external_reference" and endpoints_native:
            _fail("external-endpoint-native")


def _validate_coverage_rows(
    value: object, required: set[str], known_sources: dict[bytes, dict[str, Any]],
) -> dict[str, dict[str, Any]]:
    rows = _list(value, "coverage-schema-invalid")
    result: dict[str, dict[str, Any]] = {}
    for item in rows:
        row = _keys(item, _COVERAGE_FIELDS, "coverage-schema-invalid")
        fact_class = _string(row["fact_class"], "coverage-invalid")
        if fact_class not in required or fact_class in result:
            _fail("coverage-class-invalid")
        _allowed(row["disposition"], _COVERAGE_DISPOSITIONS, "coverage-disposition-invalid")
        _allowed(row["selected_result"], _SELECTED_RESULTS, "coverage-disposition-invalid")
        _nonnegative_int(row["candidate_count"], "coverage-count-invalid")
        _nonnegative_int(row["admitted_count"], "coverage-count-invalid")
        _source_array(row["source_refs"], known_sources, "coverage-source-invalid")
        disposition = row["disposition"]
        selected_result = row["selected_result"]
        if (disposition == "complete") == (selected_result == "unknown"):
            _fail("coverage-result-invalid")
        if disposition != "complete" and selected_result != "unknown":
            _fail("coverage-result-invalid")
        if disposition == "complete" and selected_result == "nonempty" and row["admitted_count"] == 0:
            _fail("coverage-result-invalid")
        if disposition == "complete" and selected_result == "empty" and row["admitted_count"] != 0:
            _fail("coverage-result-invalid")
        result[fact_class] = row
    if set(result) != required:
        _fail("coverage-class-invalid")
    rows = [result[fact_class] for fact_class in result]
    _ordered_unique(rows, lambda item: item["fact_class"], "coverage-order-invalid", identity=lambda item: item["fact_class"])
    return result


def _coverage_counts(
    candidates: list[dict[str, Any]], facts: list[dict[str, Any]], derivations: list[dict[str, Any]],
) -> tuple[dict[str, int], dict[str, int]]:
    candidate_counts = {fact_class: 0 for fact_class in _FACT_CLASSES}
    for row in candidates:
        candidate_counts[row["fact_class"]] += 1
    derivation_counts = {fact_class: 0 for fact_class in _FACT_CLASSES}
    admitted_derivation_counts = {fact_class: 0 for fact_class in _FACT_CLASSES}
    for row in derivations:
        derivation_counts[row["fact_class"]] += 1
        if row["disposition"] == "admitted":
            admitted_derivation_counts[row["fact_class"]] += 1
    fact_counts = {fact_class: 0 for fact_class in _FACT_CLASSES}
    for row in facts:
        fact_counts[row["fact_class"]] += 1
    return (
        {fact_class: candidate_counts[fact_class] + derivation_counts[fact_class] for fact_class in _FACT_CLASSES},
        {fact_class: fact_counts[fact_class] + admitted_derivation_counts[fact_class] for fact_class in _FACT_CLASSES},
    )


def _validate_coverage(
    value: object, graph_kind: str, candidates: list[dict[str, Any]], decisions: dict[str, dict[str, Any]],
    facts: list[dict[str, Any]], derivations: list[dict[str, Any]], known_sources: dict[bytes, dict[str, Any]],
) -> None:
    required = {"entity_admission", "entity_property", "relation"} if graph_kind == "entities" else {"definition", "relation"}
    by_class = _validate_coverage_rows(value, required, known_sources)
    candidate_counts, admitted_counts = _coverage_counts(candidates, facts, derivations)
    for fact_class, row in by_class.items():
        if row["candidate_count"] != candidate_counts[fact_class]:
            _fail("coverage-count-mismatch")
        if row["admitted_count"] != admitted_counts[fact_class]:
            _fail("coverage-count-mismatch")
        if row["disposition"] == "complete" and row["selected_result"] == "empty":
            class_candidates = [item for item in candidates if item["fact_class"] == fact_class]
            if any(decisions[item["candidate_id"]]["disposition"] != "rejected" for item in class_candidates):
                _fail("coverage-empty-unproven")
            if any(item["fact_class"] == fact_class and item["disposition"] != "rejected" for item in derivations):
                _fail("coverage-empty-unproven")
    # ``rows`` was checked for exact sorted order before this arithmetic pass.


def _diagnostic_key(row: dict[str, Any]) -> tuple[Any, ...]:
    refs = tuple(_source_key(item) for item in row["source_refs"])
    return (row["code"], refs, _canonical(row["details"]))


def _redacted_detail_key(value: object) -> bool:
    if type(value) is not str:
        return True
    normalized = re.sub(r"[^a-z0-9]+", "_", value.casefold()).strip("_")
    return normalized in _REDACTED_DETAIL_KEYS or normalized.endswith(_REDACTED_DETAIL_KEY_SUFFIXES)


def _secret_shaped_detail_value(value: object) -> bool:
    if type(value) is not str:
        return False
    return any(pattern.search(value) is not None for pattern in _SECRET_VALUE_PATTERNS)


def _contains_redacted_detail(value: object) -> bool:
    if type(value) is dict:
        for key, item in value.items():
            if _redacted_detail_key(key) or _secret_shaped_detail_value(item):
                return True
            if _contains_redacted_detail(item):
                return True
        return False
    if type(value) is list:
        return any(_contains_redacted_detail(item) for item in value)
    return _secret_shaped_detail_value(value)


def _validate_diagnostics(value: object, known_sources: dict[bytes, dict[str, Any]]) -> None:
    rows = _list(value, "diagnostic-schema-invalid")
    result: list[dict[str, Any]] = []
    for item in rows:
        row = _keys(item, _DIAGNOSTIC_FIELDS, "diagnostic-schema-invalid")
        _string(row["code"], "diagnostic-invalid")
        _allowed(row["severity"], _DIAGNOSTIC_SEVERITIES, "diagnostic-invalid")
        _source_array(row["source_refs"], known_sources, "diagnostic-source-invalid")
        if type(row["details"]) is not dict:
            _fail("diagnostic-details-invalid")
        if _contains_redacted_detail(row["details"]):
            _fail("diagnostic-details-redacted")
        _canonical(row["details"])
        result.append(row)
    _ordered_unique(result, _diagnostic_key, "diagnostic-order-invalid", identity=_diagnostic_key)


def validate_fact_context(data: dict[str, Any]) -> None:
    """Validate a complete D539 fact context without mutating or admitting it."""

    recheck_implementation()
    if type(data) is not dict:
        _fail("context-schema-invalid")
    # Do this before traversing fields so every nested value is subject to the
    # exact canonical JSON rule, including floats, cycles and surrogates.
    _canonical(data)
    context = _keys(data, _TOP_FIELDS, "context-schema-invalid")
    if (
        type(context["schema_version"]) is not int
        or context["schema_version"] != 1
        or context["context_kind"] != "caprmedio.derived_fact_context"
    ):
        _fail("context-header-invalid")
    graph_kind = _allowed(context["graph_kind"], _GRAPH_KINDS, "graph-kind-invalid")
    binding = _keys(context["source_binding"], _SOURCE_BINDING_FIELDS, "source-binding-invalid")
    for value in binding.values():
        _sha(value, "source-binding-invalid")
    provider = _keys(context["provider"], _PROVIDER_FIELDS, "provider-schema-invalid")
    _string(provider["id"], "provider-invalid")
    _string(provider["version"], "provider-invalid")
    _sha(provider["profile_sha256"], "provider-invalid")

    authority_rows = _list(context["authority_sources"], "source-evidence-schema-invalid")
    validated_authority = [_validate_source(item) for item in authority_rows]
    _ordered_unique(validated_authority, _source_key, "source-evidence-order-invalid", identity=_source_identity)
    known_sources = {_canonical(row): row for row in validated_authority}
    if len(known_sources) != len(validated_authority):
        _fail("source-evidence-duplicate")
    if binding["authority_frontier_sha256"] != _digest(validated_authority):
        _fail("source-binding-authority-frontier-mismatch")

    _, _, registry_by_digest = _validate_registry(context["relation_registry"], graph_kind, known_sources)
    candidates, candidate_map = _validate_candidates(
        context["candidates"], graph_kind, known_sources, registry_by_digest,
    )
    decisions, decision_map = _validate_decisions(context["admission_decisions"], candidate_map, known_sources)
    facts, fact_map = _validate_facts(
        context["admitted_facts"], graph_kind, candidate_map, decision_map, registry_by_digest,
    )
    derivations, derivation_map = _validate_derivations(
        context["derivations"], graph_kind, fact_map, known_sources, registry_by_digest,
    )
    _check_derivation_dag(derivation_map)
    _check_inverse_derivations(derivations, fact_map, derivation_map, registry_by_digest, graph_kind)
    _check_native_semantics(graph_kind, facts, derivations)
    _validate_coverage(
        context["coverage"], graph_kind, candidates, decision_map, facts, derivations, known_sources,
    )
    _validate_diagnostics(context["diagnostics"], known_sources)

    digest = _sha(context["context_sha256"], "context-digest-invalid")
    if digest != _digest(_without(context, "context_sha256")):
        _fail("context-digest-mismatch")


__all__ = [
    "ContractError", "validate_fact_context", "current_implementation_sha256",
    "current_implementation_digest", "loaded_implementation_sha256", "recheck_implementation",
    "recheck_loaded_implementation", "check_loaded_implementation", "implementation_sha256", "current_digest",
    "IMPLEMENTATION_PATH", "LOADED_IMPLEMENTATION_SHA256",
]
