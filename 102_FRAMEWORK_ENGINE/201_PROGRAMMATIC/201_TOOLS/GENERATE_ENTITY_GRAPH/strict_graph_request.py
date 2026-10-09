"""D539 construction/publication boundary; the shared executor owns recording.

Native facts come only from the internally recomputed fact context.  This
module never writes a Journal or turns a start receipt into terminal evidence.
"""
from __future__ import annotations

import hashlib
import re
from collections.abc import Mapping
from pathlib import Path
from graph_fact_context import FactContextError


QUALITY_KEYS = ("coverage", "fidelity", "validity", "currentness", "permission", "persistence", "recording")
CALLER_FIELDS = {
    "graph_kind", "source_frontier", "selection", "display_selection",
    "representation_configuration", "output_destination",
    "existing_projection_evidence", "capability_permission_evidence",
}
REQUIRED_FIELDS = {"graph_kind", "source_frontier", "selection", "representation_configuration", "capability_permission_evidence"}


def _diagnostic(code, message, **details):
    # Legacy readers sometimes attach the malformed scalar as `value`.
    # Source locator evidence is useful; raw rejected source values are not.
    safe_details = {key: value for key, value in details.items() if key not in {"value", "raw", "exception", "error", "status"}}
    return {"code": code, "severity": "error", "message": message, "details": safe_details, "source_refs": []}


def _effects(state="none", paths=None, before=None, after=None):
    return {"state": state, "paths": paths or [], "before": before, "after": after}


def error_result(graph_kind, error):
    result = {
        "outcome": "failed", "source_frontier_evidence": {}, "selection_evidence": {},
        "source_fact_context_evidence": {}, "lineage": [],
        "quality_dispositions": {key: "unresolved" for key in QUALITY_KEYS},
        "diagnostics": [_diagnostic(error.code, error.message, **error.details)],
        "non_authoritative": True, "output_effects": _effects(),
        "completion": {"state": "blocked"}, "run_receipt_refs": [],
    }
    if graph_kind in ("entities", "terms"):
        result[f"{graph_kind}_graph"] = {}
    return result


def _observed(path, repository):
    if not path.exists():
        return None
    if not path.is_file() or path.is_symlink():
        raise ValueError("Output is not a regular derived carrier")
    return {"carrier_path": path.relative_to(repository).as_posix(),
            "carrier_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}


def _native_payload(context, graph_kind, display, source_atoms, incidence, structure, api):
    facts = context["admitted_facts"]
    nodes = [row for row in facts if row["fact_class"] == ("entity_admission" if graph_kind == "entities" else "definition")]
    key = "entity_identity" if graph_kind == "entities" else "term_identity"
    identities = {row["payload"][key] for row in nodes}
    shown = identities
    if display is not None:
        if not isinstance(display, Mapping) or set(display) != {"mode", "native_identities"} or display.get("mode") != "explicit_native_identity_set":
            raise api.EntityGraphError("display-selection-invalid", "Display selection must be an explicit native identity set")
        selected = display["native_identities"]
        if not isinstance(selected, list) or any(not isinstance(item, str) or not item for item in selected) or selected != sorted(set(selected)):
            raise api.EntityGraphError("display-selection-invalid", "Display identities must be unique and sorted")
        if set(selected) - identities:
            raise api.EntityGraphError("display-selection-outside-source", "Display selection names an unadmitted native identity")
        shown = set(selected)
    relations = [row for row in facts if row["fact_class"] == "relation"]
    relations += [row for row in context["derivations"] if row["disposition"] == "admitted"]
    native, external = [], []
    for row in relations:
        payload = row["payload"]
        if payload["representation"] == "external_reference":
            external.append(row)
        elif payload["source"]["identity"] not in identities or payload["target"]["identity"] not in identities:
            raise api.EntityGraphError("native-endpoint-unadmitted", "Native Relation endpoint is not an admitted selected member")
        elif payload["source"]["identity"] in shown and payload["target"]["identity"] in shown:
            native.append(row)
    result = {
        "entities" if graph_kind == "entities" else "terms": [row for row in nodes if row["payload"][key] in shown],
        "native_relations": native, "external_references": external,
        "source_atoms": source_atoms, "incidence": incidence, "project_structure": structure,
    }
    if context["provider"]["id"] == "caprmedio.graph-fact-context.declared-core":
        result["declaration_context"] = {"kind": "declared_core_model", "scope_unit": "CORE_META_MODEL"}
    if graph_kind == "entities":
        result["native_properties"] = [row for row in facts if row["fact_class"] == "entity_property" and row["payload"]["entity_identity"] in shown]
        if any(row["payload"]["entity_identity"] not in identities for row in facts if row["fact_class"] == "entity_property"):
            raise api.EntityGraphError("property-bearer-unadmitted", "Entity Property bearer is not an admitted selected member")
    else:
        # Keep the full canonical hierarchy for root checks before display filtering.
        parents = {identity: [] for identity in sorted(identities)}
        for row in relations:
            payload = row["payload"]
            if payload["kind"]["canonical_name"] == "NARROWER_THAN" and payload["source"]["identity"] in parents:
                parents[payload["source"]["identity"]].append(payload["target"]["identity"])
        parents = {key: sorted(set(values)) for key, values in parents.items()}
        native_parents = {key: [value for value in values if value in parents] for key, values in parents.items()}
        ancestors, cycles = api._ancestor_sets(native_parents)
        if cycles:
            raise api.EntityGraphError("native-hierarchy-cycle", "Admitted hierarchy contains a cycle")
        relation_complete = all(row["disposition"] == "complete" for row in context["coverage"] if row["fact_class"] == "relation")
        result.update({"parents_by_term": parents, "ancestors_by_term": ancestors, "cycles": cycles,
                       "root_terms": [key for key, values in parents.items() if not values and key in shown] if relation_complete else []})
    return result


def build_graph(repository: Path, request, api):
    graph_kind = request.get("graph_kind") if isinstance(request, Mapping) else None
    destination = None
    before = None
    result = None
    attempted = False
    try:
        if not isinstance(request, Mapping):
            raise api.EntityGraphError("request-invalid", "Graph request must be an object")
        unknown = set(request) - CALLER_FIELDS - {"run_recording_context", "source_fact_context"}
        missing = REQUIRED_FIELDS - set(request)
        if unknown or missing:
            raise api.EntityGraphError("request-schema-invalid", "Graph request fields are not exact", unknown=sorted(unknown), missing=sorted(missing))
        if graph_kind not in ("entities", "terms"):
            raise api.EntityGraphError("graph-kind-invalid", "graph_kind must be entities or terms")
        from graph_fact_context import DerivedFactContext, canonical_bytes, context_evidence, prepare_fact_context, verified_context

        supplied = request.get("source_fact_context")
        if "source_fact_context" in request and not isinstance(supplied, DerivedFactContext):
            raise api.EntityGraphError("request-schema-invalid", "Caller JSON cannot provide a fact context")
        recording = request.get("run_recording_context")
        if "run_recording_context" in request and not api.is_actual_recording_context(recording):
            raise api.EntityGraphError("recording-context-untrusted", "Caller JSON cannot provide actual recording evidence")
        expected_action = "CA-O-134" if graph_kind == "entities" else "CA-O-137"
        if recording is not None and recording.start_event_receipt["action_id"] != expected_action:
            raise api.EntityGraphError("recording-action-mismatch", "Actual start context belongs to a different Action")
        configuration = api._mapping(request["representation_configuration"], "representation_configuration")
        if dict(configuration) != {"format": "canonical-json"}:
            raise api.EntityGraphError("representation-configuration-invalid", "Only canonical-json representation is supported")
        permission = api._mapping(request["capability_permission_evidence"], "capability_permission_evidence")
        if set(permission) != {"authorized"} or type(permission["authorized"]) is not bool:
            raise api.EntityGraphError("permission-evidence-invalid", "Permission assertion requires only authorized:boolean")
        existing = request.get("existing_projection_evidence")
        if existing is not None and (not isinstance(existing, Mapping) or set(existing) != {"sha256"} or not isinstance(existing["sha256"], str) or not re.fullmatch(r"[0-9a-f]{64}", existing["sha256"])):
            raise api.EntityGraphError("existing-projection-evidence-invalid", "Prior-output evidence must contain exactly one SHA-256 digest")
        repository = repository.resolve()
        if "output_destination" in request:
            destination = api._publication_path(repository, request["output_destination"])
            before = _observed(destination, repository)
        elif existing is not None:
            raise api.EntityGraphError("existing-projection-destination-unbound", "Prior-output evidence requires an explicit destination")
        frontier = api._mapping(request["source_frontier"], "source_frontier")
        selection = api._mapping(request["selection"], "selection")
        folder, actual_frontier, diagnostics = api._validate_frontier(repository, frontier)
        if diagnostics:
            result = error_result(graph_kind, api.EntityGraphError("source-frontier-stale", "Bound source frontier is stale"))
            result.update(outcome="stale", source_frontier_evidence=actual_frontier, diagnostics=diagnostics)
            result["output_effects"] = _effects("unchanged", before=before, after=before) if before else _effects()
            return result
        carriers, source_diagnostics = api.discover_atoms(repository, folder)
        selected, names = api._selected_carriers(carriers, selection)
        structure, structure_diagnostics = api._selected_structure(repository, frontier, names)
        harmless_exclusions = {"non-atom-markdown-skipped", "inactive-status-skipped"}
        if any(row.get("severity") != "info" or row.get("code") not in harmless_exclusions
               for row in source_diagnostics) or structure_diagnostics:
            raise api.EntityGraphError("source-selection-incomplete", "Selected source cannot be completely assessed")
        # These exclusions are already part of the sealed frontier's policy.
        # Retain their locators, not arbitrary rejected lifecycle spellings.
        diagnostics.extend({**row, "details": {key: value for key, value in row.get("details", {}).items()
                                               if key != "status"}, "source_refs": []}
                           for row in source_diagnostics)
        context = prepare_fact_context(repository, graph_kind, carriers, selection, frontier, carriers)
        if supplied is not None:
            context = verified_context(supplied, repository, graph_kind, carriers, selection, frontier, carriers)
        data = context.as_dict()
        incidence = []
        for carrier in selected:
            rows, errors = api.parse_subject_relations(carrier)
            incidence.extend(row.record() for row in rows)
            diagnostics.extend(errors)
        source_atoms = [{"source": carrier.evidence(), "metadata": api._frontmatter_properties(carrier)} for carrier in selected]
        namespace = _native_payload(data, graph_kind, request.get("display_selection"), source_atoms, incidence, structure, api)
        complete = all(row["disposition"] == "complete" for row in data["coverage"])
        quality = {key: "unresolved" for key in QUALITY_KEYS}
        authorization = recording.authorization_evidence() if recording is not None else None
        expected_route = "build_entities_graph" if graph_kind == "entities" else "build_terms_graph"
        actually_authorized = authorization is not None and authorization.get("operation_route") == expected_route
        quality.update(coverage="pass" if complete else "unresolved", fidelity="pass" if complete else "unresolved",
                       validity="pass" if complete else "unresolved", currentness="pass",
                       permission="pass" if permission["authorized"] and actually_authorized else "fail" if not permission["authorized"] else "unresolved",
                       persistence="not_applicable" if destination is None else "unresolved")
        diagnostics += [{**row, "message": "Fact-provider assessment is unresolved."} for row in data["diagnostics"]]
        if not complete:
            diagnostics.append(_diagnostic("fact-coverage-unresolved", "Required native fact coverage is not fully admitted"))
        selection_evidence = {"selection": {"atom_ids": list(selection["atom_ids"]), "scope_unit_names": list(names)}}
        if "display_selection" in request:
            selection_evidence["display_selection"] = dict(request["display_selection"])
        result = {"outcome": "incomplete", f"{graph_kind}_graph": namespace,
                  "source_frontier_evidence": actual_frontier, "selection_evidence": selection_evidence,
                  "source_fact_context_evidence": context_evidence(context),
                  "lineage": {"sources": [carrier.evidence() for carrier in selected], "candidates": data["candidates"],
                              "admission_decisions": data["admission_decisions"], "derivations": data["derivations"]},
                  "quality_dispositions": quality, "diagnostics": diagnostics, "non_authoritative": True,
                  "output_effects": _effects("unchanged", before=before, after=before) if before else _effects(),
                  "completion": {"state": "construction_only" if destination is None else "awaiting_terminal_recording"},
                  "run_receipt_refs": [recording.start_event_receipt["event_id"]] if recording is not None else []}
        final_frontier = api.source_frontier_for(repository, folder)
        if canonical_bytes(final_frontier) != canonical_bytes(frontier):
            result["outcome"] = "stale"
            quality["currentness"] = "fail"
            diagnostics.append(_diagnostic("source-frontier-changed-after-construction", "Bound source bytes changed during construction"))
            return result
        if destination is None:
            return result
        if quality["permission"] != "pass":
            result["outcome"] = "blocked"
            result["completion"] = {"state": "blocked"}
            diagnostics.append(_diagnostic("actual-permission-unavailable", "Publication requires the executor-bound actual authorized Action"))
            return result
        if not complete or any(row.get("severity") == "error" for row in diagnostics):
            return result
        publication = {"schema_version": api.SCHEMA_VERSION, "graph_kind": graph_kind,
                       f"{graph_kind}_graph": namespace, "source_frontier_evidence": actual_frontier,
                       "selection_evidence": selection_evidence, "source_fact_context_evidence": context_evidence(context),
                       "representation_configuration": dict(configuration), "lineage": result["lineage"], "non_authoritative": True}
        rendered = canonical_bytes(publication)
        after_digest = hashlib.sha256(rendered).hexdigest()
        # Recheck ultimate authority/profile bytes as well as the selected frontier.
        current_context = prepare_fact_context(repository, graph_kind, carriers, selection, frontier, carriers)
        if current_context.context_sha256 != context.context_sha256:
            raise api.EntityGraphError("fact-context-binding-stale", "Authority or provider profile changed before publication")
        if canonical_bytes(api.source_frontier_for(repository, folder)) != canonical_bytes(frontier):
            result["outcome"] = "stale"
            quality["currentness"] = "fail"
            diagnostics.append(_diagnostic("source-frontier-changed-before-publication", "Bound sources changed before publication"))
            return result
        current = _observed(destination, repository)
        if current != before or existing is not None and (current is None or current["carrier_sha256"] != existing["sha256"]):
            result["outcome"] = "stale"
            quality["currentness"] = "fail"
            result["output_effects"] = _effects("unchanged", before=current, after=current) if current else _effects()
            diagnostics.append(_diagnostic("existing-projection-stale", "Prior output evidence no longer matches current destination"))
            return result
        if current is not None and current["carrier_sha256"] == after_digest:
            quality["persistence"] = "pass"
            result["output_effects"] = _effects("unchanged", before=current, after=current)
            result["projection_revision"] = after_digest
            return result
        if current is not None and existing is None:
            result["outcome"] = "blocked"
            result["completion"] = {"state": "blocked"}
            diagnostics.append(_diagnostic("existing-projection-evidence-required", "Replacing different bytes requires exact current prior-output evidence"))
            return result
        # Probe path again before mutation; never follow an output symlink.
        if api._publication_path(repository, request["output_destination"]) != destination:
            raise api.EntityGraphError("output-destination-changed", "Output destination changed before publication")
        attempted = True
        api.atomic_write(destination, rendered.decode("utf-8"))
        after = _observed(destination, repository)
        if after is None or after["carrier_sha256"] != after_digest:
            raise OSError("Unconfirmed output bytes")
        result["output_effects"] = _effects("created" if before is None else "replaced", [after["carrier_path"]], before, after)
        result["projection_revision"] = after_digest
        quality["persistence"] = "pass"
        return result
    except FactContextError as error:
        if result is None:
            result = error_result(graph_kind, api.EntityGraphError(error.code, str(error)))
        else:
            result["diagnostics"].append(_diagnostic(error.code, str(error)))
        result["outcome"] = "stale" if "stale" in error.code else "failed"
        if result["outcome"] == "stale":
            result["quality_dispositions"]["currentness"] = "fail"
        if before and not attempted:
            result["output_effects"] = _effects("unchanged", before=before, after=before)
        return result
    except api.EntityGraphError as error:
        if result is None:
            result = error_result(graph_kind, error)
        else:
            result["outcome"] = "stale" if "stale" in error.code else "failed"
            result["diagnostics"].append(_diagnostic(error.code, error.message, **error.details))
        if before and not attempted:
            result["output_effects"] = _effects("unchanged", before=before, after=before)
        return result
    except (OSError, ValueError, TypeError, UnicodeError) as error:
        if result is None:
            result = error_result(graph_kind, api.EntityGraphError("graph-input-unavailable", "Graph input cannot be safely assessed"))
        else:
            result["outcome"] = "failed"
            result["diagnostics"].append(_diagnostic("projection-publication-failed" if attempted else "graph-input-unavailable", "Output publication failed." if attempted else "Graph input cannot be safely assessed."))
        if destination is not None:
            try:
                after = _observed(destination, repository)
                if after == before:
                    result["output_effects"] = (_effects("unchanged", before=before, after=after) if before
                                                else _effects("uncertain", [destination.relative_to(repository).as_posix()]) if attempted
                                                else _effects())
                else:
                    result["output_effects"] = _effects("replaced" if before else "created", [destination.relative_to(repository).as_posix()], before, after) if after else _effects("uncertain", [destination.relative_to(repository).as_posix()], before, None)
            except (OSError, ValueError):
                result["output_effects"] = _effects("uncertain", [destination.relative_to(repository).as_posix()], before, None) if attempted else _effects()
        return result
