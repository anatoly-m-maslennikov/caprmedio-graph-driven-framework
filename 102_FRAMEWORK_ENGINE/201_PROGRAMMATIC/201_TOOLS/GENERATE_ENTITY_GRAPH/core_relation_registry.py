"""Closed, source-pinned Core Relation registry for the graph fact context.

This profile compiles only the three Relation Kinds whose governing Core
authorities have been reviewed here.  It is intentionally not a general
Relation parser: a changed authority, unavailable assignment evidence, or an
unreviewed Relation Kind produces no registry entries.
"""

from __future__ import annotations

import hashlib
import json
import re
import tomllib
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path

import generate_entity_graph as graph
from graph_fact_context import (
    FactContextError,
    _frontier,
    _pool,
    _primary,
    _safe_path,
    _selection,
    _source_key,
    canonical_bytes,
    raw_section_property_evidence,
)


_TOKEN = object()
_IMPLEMENTATION_PATH = Path(__file__).resolve()
_LOADED_IMPLEMENTATION_SHA256 = hashlib.sha256(_IMPLEMENTATION_PATH.read_bytes()).hexdigest()
_STRUCTURE_PATH = ".caprmedio_caprmedio/project_structure.toml"
_CORE_AUTHORITY_PATH = (
    ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
    "000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL"
)
_CORE_SCOPE = "CORE_META_MODEL"

# These are reviewed source identities, not a rule that a same-named future
# Atom carries the present Relation semantics.  The Details-assignment pins
# match graph_fact_context's bounded raw Details locator.
_REQUIRED_AUTHORITIES = {
    "CA-D-478": (
        5,
        "a40ad3683ecddd536e5b7eb6c044e8da15806ab44946fa1354c408ce5e966464",
        "Delivery",
        "07_delivery/CA-D-478-CORE_META_MODEL-CORE-DELIVERY--store-every-atom-property-in-one-internal-location.md",
    ),
    "CA-D-479": (
        6,
        "0819f8433cde89484e21a200466504a9fdcad31b58958c777a761637fbb45ff1",
        "Delivery",
        "07_delivery/CA-D-479-CORE_META_MODEL-DELIVERY--use-stable-headings-for-atom-body-properties.md",
    ),
    "CA-R-1624": (
        2,
        "d985c624f5c0b92010a3f1a670e2e12ef0d018aa221ce1052faab293060966cf",
        "Requirement",
        "04_requirement/CA-R-1624-CORE_META_MODEL-CORE-REQUIREMENT--keep-details-within-the-primary-contribution.md",
    ),
    "CA-R-806": (
        21,
        "933901316d347a2e09222d19d3a985c2feb93c7efc86e0a8332ab292cd169dd0",
        "Requirement",
        "04_requirement/CA-R-806-CORE_META_MODEL-GENERAL--register-complete-relation-kind-metadata.md",
    ),
    "CA-M-120": (
        14,
        "4f1a2004c885b1134ef57e309c37e1ab14c86bf008a3374fc93bbc20a2c104db",
        "Method",
        "05_method/CA-M-120-CORE_META_MODEL-CORE--compile-the-direct-relation-registry.md",
    ),
    "CA-R-1260": (
        13,
        "ea7911f8d3bc88bcba954332193354c80df63005dbf94812960dda162615f54d",
        "Requirement",
        "04_requirement/CA-R-1260-CORE_META_MODEL-CORE-REQUIREMENT--define-is-borne-by.md",
    ),
    "CA-R-1347": (
        11,
        "8d74cf6b7af6a0738844b4d17054fe713a55773c6bed88cf0e48981eec6f9138",
        "Requirement",
        "04_requirement/CA-R-1347-CORE_META_MODEL-CORE-REQUIREMENT--define-root-term.md",
    ),
    "CA-R-1435": (
        8,
        "15fa6d3511be9f2d4ad76eea38373f13bcbb37522a2f7c5b985e0a4b836f54cb",
        "Requirement",
        "04_requirement/CA-R-1435-CORE_META_MODEL-CORE--define-narrower-than.md",
    ),
    "CA-R-1436": (
        8,
        "a33bdc582beb140647e6012022730abf531f6311923edf80ed7d1fe1614dabad",
        "Requirement",
        "04_requirement/CA-R-1436-CORE_META_MODEL-CORE--define-is-allowed-value-of.md",
    ),
}
_DETAILS_ASSIGNMENT_IDS = ("CA-D-478", "CA-D-479", "CA-R-1624")
_COMMON_METADATA_IDS = (*_DETAILS_ASSIGNMENT_IDS, "CA-R-806", "CA-M-120")

# CA-R-806 makes every field mandatory.  These are reviewed semantic
# descriptors bound to the exact authorities above; they are not extracted
# from arbitrary matching prose and are interpreted only by this profile.
_RELATIONS = (
    {
        "authority_id": "CA-R-1260",
        "graph_kind": "entities",
        "canonical_name": "IS_BORNE_BY",
        "metadata": {
            "meaning": "source_dependent_entity_identity_requires_target_immediate_bearer",
            "direction": "dependent_entity_to_immediate_bearer_entity",
            "inverse": {"kind": "declared", "graph_kind": "entities", "canonical_name": "BEARS"},
            "source_class": "Dependent Entity",
            "target_class": "Entity",
            "source_graph_context": "entities",
            "target_graph_context": "entities",
            "cardinality": {"outgoing": "exactly_one", "incoming": "unconstrained"},
            "authority_effect": "identity_bearer_requirement",
            "transitivity": "nontransitive",
            "applicability": "entities_graph",
            "status": "Active",
            "exclusive_purpose": "immediate_bearer_identity",
        },
        "support_ids": (),
    },
    {
        "authority_id": "CA-R-1436",
        "graph_kind": "entities",
        "canonical_name": "IS_ALLOWED_VALUE_OF",
        "metadata": {
            "meaning": "source_value_occurrence_is_admitted_as_a_possible_target_property_value_in_qualified_context",
            "direction": "value_occurrence_to_property",
            "inverse": {"kind": "reverse_navigation"},
            "source_class": "Value occurrence",
            "target_class": "Property",
            "source_graph_context": "entities",
            "target_graph_context": "entities",
            "cardinality": {"outgoing": "unconstrained", "incoming": "unconstrained"},
            "authority_effect": "qualified_possible_value_admission",
            "transitivity": "nontransitive",
            "applicability": "qualified_property_value_context",
            "status": "Active",
            "exclusive_purpose": "possible_value_admission_without_assignment_or_cardinality_effect",
        },
        "support_ids": (),
    },
    {
        "authority_id": "CA-R-1435",
        "graph_kind": "terms",
        "canonical_name": "NARROWER_THAN",
        "metadata": {
            "meaning": "source_narrower_term_definition_implies_target_broader_term_definition_for_the_same_referent",
            "direction": "narrower_term_to_broader_term",
            "inverse": {"kind": "reverse_navigation"},
            "source_class": "Term",
            "target_class": "Term",
            "source_graph_context": "terms",
            "target_graph_context": "terms",
            "cardinality": {"outgoing": "zero_or_more_direct_parents", "incoming": "unconstrained"},
            "authority_effect": "acyclic_definition_implication",
            "transitivity": "semantic_transitivity_without_implicit_edge_materialization",
            "applicability": "terms_graph",
            "status": "Active",
            "exclusive_purpose": "definition_implication_not_property_ownership_or_allowed_value_membership",
        },
        "support_ids": ("CA-R-1347",),
    },
)
_METADATA_FIELDS = {
    "meaning",
    "direction",
    "inverse",
    "source_class",
    "target_class",
    "source_graph_context",
    "target_graph_context",
    "cardinality",
    "authority_effect",
    "transitivity",
    "applicability",
    "status",
    "exclusive_purpose",
}


class CoreRelationRegistryError(ValueError):
    """Stable failure used to create a no-entry, inspectable factory result."""

    def __init__(
        self,
        code: str,
        *,
        source_refs: Sequence[Mapping[str, object]] = (),
        details: Mapping[str, object] | None = None,
    ) -> None:
        self.code = code
        self.source_refs = tuple(dict(item) for item in source_refs)
        self.details = {} if details is None else dict(details)
        super().__init__(code)


@dataclass(frozen=True, slots=True, init=False)
class CoreRelationRegistry:
    """Factory-minted immutable registry bytes with detached read views."""

    _records_bytes: bytes
    _diagnostics_bytes: bytes
    _profile_bytes: bytes
    _binding_bytes: bytes
    _token: object

    def __init__(
        self,
        records: bytes,
        diagnostics: bytes,
        profile: bytes,
        binding: bytes,
        *,
        _token: object = None,
    ) -> None:
        if _token is not _TOKEN:
            raise CoreRelationRegistryError("registry-untrusted")
        object.__setattr__(self, "_records_bytes", records)
        object.__setattr__(self, "_diagnostics_bytes", diagnostics)
        object.__setattr__(self, "_profile_bytes", profile)
        object.__setattr__(self, "_binding_bytes", binding)
        object.__setattr__(self, "_token", _token)

    @property
    def records(self) -> tuple[dict[str, object], ...]:
        """Return detached records; mutation cannot alter the factory result."""
        return tuple(json.loads(self._records_bytes))

    @property
    def diagnostics(self) -> tuple[dict[str, object], ...]:
        """Return detached diagnostic records in D539 sort order."""
        return tuple(json.loads(self._diagnostics_bytes))

    @property
    def profile(self) -> dict[str, object]:
        """Return the checked profile descriptor without exposing mutable state."""
        return json.loads(self._profile_bytes)

    def as_dict(self) -> dict[str, object]:
        return {
            "relation_registry": [dict(record) for record in self.records],
            "diagnostics": [dict(row) for row in self.diagnostics],
            "profile": self.profile,
        }


def _digest(value: object) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def _current_code() -> None:
    try:
        current = hashlib.sha256(_IMPLEMENTATION_PATH.read_bytes()).hexdigest()
    except OSError as error:
        raise CoreRelationRegistryError("registry-profile-unavailable") from error
    if current != _LOADED_IMPLEMENTATION_SHA256:
        raise CoreRelationRegistryError("registry-profile-stale")


def _source_refs(*groups: Sequence[Mapping[str, object]]) -> list[dict[str, object]]:
    unique: dict[bytes, dict[str, object]] = {}
    for group in groups:
        for source in group:
            item = dict(source)
            unique[canonical_bytes(item)] = item
    return sorted(unique.values(), key=_source_key)


def _diagnostic_sort_key(item: Mapping[str, object]) -> tuple[object, ...]:
    refs = item.get("source_refs", [])
    source_keys = tuple(_source_key(ref) for ref in refs) if isinstance(refs, list) else ()
    return (str(item["code"]), source_keys, canonical_bytes(item["details"]))


def _diagnostic(
    code: str,
    *,
    source_refs: Sequence[Mapping[str, object]] = (),
    details: Mapping[str, object] | None = None,
) -> dict[str, object]:
    return {
        "code": code,
        "severity": "warning",
        "source_refs": _source_refs(source_refs),
        "details": {} if details is None else dict(details),
    }


def _empty(
    code: str,
    *,
    source_refs: Sequence[Mapping[str, object]] = (),
    details: Mapping[str, object] | None = None,
) -> CoreRelationRegistry:
    diagnostics = [_diagnostic(code, source_refs=source_refs, details=details)]
    profile = {"id": "caprmedio.core-relation-registry", "version": "1", "profile_sha256": ""}
    return CoreRelationRegistry(
        canonical_bytes([]),
        canonical_bytes(diagnostics),
        canonical_bytes(profile),
        canonical_bytes({"state": "unavailable", "diagnostic_code": code}),
        _token=_TOKEN,
    )


def _authority_path(repository: Path) -> str:
    path = _safe_path(repository, _STRUCTURE_PATH)
    try:
        parsed = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise CoreRelationRegistryError("registry-project-structure-unavailable") from error
    units = parsed.get("scope_units")
    if not isinstance(units, list):
        raise CoreRelationRegistryError("registry-project-structure-invalid")
    matches = [
        item
        for item in units
        if isinstance(item, dict) and item.get("scope_unit_name") == _CORE_SCOPE
    ]
    if len(matches) != 1 or matches[0].get("authority_path") != _CORE_AUTHORITY_PATH:
        raise CoreRelationRegistryError("registry-core-authority-path-unsupported")
    return _CORE_AUTHORITY_PATH


def _carrier_identity(carrier: object) -> tuple[object, object, object, object]:
    return (
        getattr(carrier, "atom_id", None),
        getattr(carrier, "version", None),
        getattr(carrier, "carrier_path", None),
        getattr(carrier, "sha256", None),
    )


def _registered_core_frontier(repository: Path) -> tuple[list[object], dict[str, object]]:
    authority_path = _authority_path(repository)
    root = _safe_path(repository, authority_path, folder=True)
    if not root.is_dir():
        raise CoreRelationRegistryError("registry-core-authority-unavailable")
    try:
        actual_carriers, discovery_diagnostics = graph.discover_atoms(repository, root)
        actual_frontier = graph.source_frontier_for(repository, root)
    except Exception as error:
        raise CoreRelationRegistryError("registry-core-frontier-unavailable") from error
    if any(
        isinstance(row, Mapping) and row.get("severity") == "error" for row in discovery_diagnostics
    ):
        raise CoreRelationRegistryError("registry-core-frontier-unavailable")
    return actual_carriers, actual_frontier


def _checked_frontier(
    repository: Path, carriers: object, frontier: object, selection: object
) -> tuple[dict, dict, dict[str, tuple[object, dict, bytes]]]:
    actual_carriers, actual_frontier = _registered_core_frontier(repository)
    if not isinstance(carriers, Sequence) or isinstance(carriers, (str, bytes)):
        raise CoreRelationRegistryError("registry-carriers-unverified")
    if [_carrier_identity(item) for item in carriers] != [
        _carrier_identity(item) for item in actual_carriers
    ]:
        raise CoreRelationRegistryError("registry-carriers-unverified")
    if not isinstance(frontier, Mapping):
        raise CoreRelationRegistryError("registry-frontier-unverified")
    try:
        if canonical_bytes(dict(frontier)) != canonical_bytes(actual_frontier):
            raise CoreRelationRegistryError("registry-frontier-stale")
    except FactContextError as error:
        raise CoreRelationRegistryError("registry-frontier-unverified") from error
    try:
        pool = _pool(repository, carriers)
        selected = _selection(selection, set(pool))
        checked_frontier = _frontier(repository, frontier, pool, selected)
    except FactContextError as error:
        raise CoreRelationRegistryError("registry-input-unverified") from error
    if selected["scope_unit_names"] != [_CORE_SCOPE]:
        raise CoreRelationRegistryError("registry-selection-unsupported")
    return checked_frontier, selected, pool


def _checked_authorities(
    repository: Path, pool: Mapping[str, tuple[object, dict, bytes]], carriers: Sequence[object]
) -> tuple[dict[str, dict[str, object]], dict[str, dict[str, object]]]:
    primary: dict[str, dict[str, object]] = {}
    details: dict[str, dict[str, object]] = {}
    for atom_id, (revision, digest, role, suffix) in _REQUIRED_AUTHORITIES.items():
        item = pool.get(atom_id)
        if item is None:
            raise CoreRelationRegistryError(
                "registry-authority-unavailable", details={"atom_id": atom_id}
            )
        carrier, pin, raw = item
        if (
            pin["atom_revision"] != revision
            or pin["carrier_sha256"] != digest
            or carrier.content_role != role
            or carrier.status != "Active"
            or not str(pin["carrier_path"]).startswith(_CORE_AUTHORITY_PATH + "/")
            or not str(pin["carrier_path"]).endswith(suffix)
        ):
            raise CoreRelationRegistryError(
                "registry-authority-unsupported", details={"atom_id": atom_id}
            )
        contribution = _primary(pin, raw, carrier.content_role)
        if contribution is None:
            raise CoreRelationRegistryError(
                "registry-primary-unavailable", details={"atom_id": atom_id}
            )
        primary[atom_id] = contribution
    for atom_id in ("CA-R-1260", "CA-R-1435", "CA-R-1436"):
        carrier = pool[atom_id][0]
        contribution = raw_section_property_evidence(
            repository, carrier, authority_sources=carriers
        )
        if contribution is None:
            raise CoreRelationRegistryError(
                "registry-details-unavailable", details={"atom_id": atom_id}
            )
        details[atom_id] = contribution
        raw = pool[atom_id][2]
        text = b"".join(
            raw.splitlines(keepends=True)[
                contribution["contribution"]["start_line"] - 1 : contribution["contribution"][
                    "end_line"
                ]
            ]
        ).decode("utf-8")
        name = next(
            item["canonical_name"] for item in _RELATIONS if item["authority_id"] == atom_id
        )
        pattern = rf"(?m)^- Status: the {re.escape(name)} Relation Kind is Active\.\s*$"
        if re.search(pattern, text) is None:
            raise CoreRelationRegistryError(
                "registry-kind-status-unavailable",
                source_refs=[contribution],
                details={"atom_id": atom_id},
            )
    return primary, details


def _profile(
    frontier: Mapping[str, object],
    selection: Mapping[str, object],
    primary: Mapping[str, Mapping[str, object]],
    details: Mapping[str, Mapping[str, object]],
) -> dict[str, object]:
    authority_inputs = _source_refs(primary.values(), details.values())
    body = {
        "id": "caprmedio.core-relation-registry",
        "version": "1",
        "implementation_sha256": _LOADED_IMPLEMENTATION_SHA256,
        "authority_path": _CORE_AUTHORITY_PATH,
        "source_frontier_sha256": frontier["source_frontier_sha256"],
        "selection_sha256": _digest(selection),
        "authority_inputs": authority_inputs,
        "relation_kinds": [
            {
                "graph_kind": item["graph_kind"],
                "canonical_name": item["canonical_name"],
                "authority_id": item["authority_id"],
                "metadata": item["metadata"],
            }
            for item in _RELATIONS
        ],
    }
    return {"id": body["id"], "version": body["version"], "profile_sha256": _digest(body)}


def _record(
    specification: Mapping[str, object],
    primary: Mapping[str, Mapping[str, object]],
    details: Mapping[str, Mapping[str, object]],
    evaluator: Mapping[str, object],
) -> dict[str, object]:
    authority_id = str(specification["authority_id"])
    support_ids = tuple(specification["support_ids"])
    metadata_sources = _source_refs(
        [primary[item] for item in _COMMON_METADATA_IDS],
        [primary[authority_id], details[authority_id]],
        [primary[item] for item in support_ids],
    )
    status_source = details[authority_id]
    checks = [
        {
            "code": "complete-relation-kind-metadata-current",
            "disposition": "pass",
            "source_refs": metadata_sources,
        },
        {
            "code": "details-location-assignment-current",
            "disposition": "pass",
            "source_refs": _source_refs(
                [primary[item] for item in _DETAILS_ASSIGNMENT_IDS], [status_source]
            ),
        },
        {
            "code": "explicit-relation-kind-status-current",
            "disposition": "pass",
            "source_refs": _source_refs([status_source]),
        },
        {
            "code": "reviewed-relation-semantics-current",
            "disposition": "pass",
            "source_refs": _source_refs(
                [primary[authority_id]], [primary[item] for item in support_ids]
            ),
        },
    ]
    checks.sort(key=lambda item: item["code"])
    metadata = dict(specification["metadata"])
    if set(metadata) != _METADATA_FIELDS:
        raise CoreRelationRegistryError("registry-metadata-incomplete")
    record = {
        "kind": {
            "graph_kind": specification["graph_kind"],
            "canonical_name": specification["canonical_name"],
        },
        "metadata": metadata,
        "authority_inputs": metadata_sources,
        "evaluator": dict(evaluator),
        "checks": checks,
    }
    record["registry_record_sha256"] = _digest(record)
    return record


def prepare_core_relation_registry(
    repository: Path, carriers: Sequence, frontier: Mapping, selection: Mapping
) -> CoreRelationRegistry:
    """Mint the closed registry from a rechecked current Core source frontier.

    ``carriers`` must be the complete discovered Core frontier, rather than
    caller-created evidence rows.  The result is inspectable even when the
    profile is unavailable, but then contains no Relation records.
    """
    try:
        _current_code()
        repository = Path(repository).resolve(strict=True)
        checked_frontier, selected, pool = _checked_frontier(
            repository, carriers, frontier, selection
        )
        primary, details = _checked_authorities(repository, pool, carriers)
        profile = _profile(checked_frontier, selected, primary, details)
        records = [_record(item, primary, details, profile) for item in _RELATIONS]
        records.sort(key=lambda item: (item["kind"]["graph_kind"], item["kind"]["canonical_name"]))
        binding = {
            "repository": repository.as_posix(),
            "source_frontier": checked_frontier,
            "selection": selected,
            "profile": profile,
        }
        return CoreRelationRegistry(
            canonical_bytes(records),
            canonical_bytes([]),
            canonical_bytes(profile),
            canonical_bytes(binding),
            _token=_TOKEN,
        )
    except CoreRelationRegistryError as error:
        return _empty(error.code, source_refs=error.source_refs, details=error.details)
    except (FactContextError, OSError, ValueError, TypeError, KeyError) as error:
        return _empty(
            "registry-profile-unavailable", details={"exception_type": type(error).__name__}
        )


def verified_core_relation_registry(
    registry: CoreRelationRegistry,
    repository: Path,
    carriers: Sequence,
    frontier: Mapping,
    selection: Mapping,
) -> CoreRelationRegistry:
    """Rebuild before use; stale or forged bundles are never accepted as facts."""
    current = prepare_core_relation_registry(repository, carriers, frontier, selection)
    if not current.records:
        return current
    if (
        type(registry) is not CoreRelationRegistry
        or getattr(registry, "_token", None) is not _TOKEN
    ):
        return _empty("registry-untrusted")
    if (
        registry._binding_bytes != current._binding_bytes
        or registry._records_bytes != current._records_bytes
    ):
        return _empty("registry-binding-stale")
    return current
