---
atom_id: CA-R-1835
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-09 19:23:34 +0400"
subjects:
  governs: "Tool/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/Entities Graph"
  depends_on: [Tool, Workflow, Action, Entity, Property, Projection, Project Structure, Relation Kind, Artifact, Journal]
relations:
  relates_to: [CA-O-133, CA-O-134, CA-O-135, CA-R-1387, CA-M-259, CA-R-1438, CA-R-1456, CA-R-1483]
---
# Summary

Build faithful Entities Graph projections

## Scope

One selected `GENERATE_ENTITY_GRAPH` Entities Graph build/confirmation request and its non-authoritative derived output.

## Claim

The builder **must** represent all and only selected native Entity identities, their selected authoritative Property facts, admitted Entity-graph Relations, and selected declared Project Structure facts with exact source identity, Revision, location, and digest traceability.

## Details

The strict request binds graph kind `entities`, an exact source frontier and selection (plus optional narrower display selection), representation configuration, target derived-output destination, existing output/evidence if any, capability/permission evidence, and Run/Journal references. Each represented Entity preserves its canonical/bearer-qualified identity and complete selected Property values; no duplicate identity, inferred Property value, folder-derived Scope Unit, or foreign graph-kind Relation is permitted. When Scope Units are selected, their only declaration source is the selected `project_structure.toml` record, retaining its `scope_unit_name`, parent, type, label, structural level, conditional local order, navigational order, authority path, delivery path, and explicit authority mode if present.

The result has a separate `entities_graph` namespace and records source Atoms/Claims and non-Atom Project Structure evidence independently. It reports selected/unselected boundaries, external references, unresolved endpoints, malformed/inaccessible/stale sources, conflicts, coverage, fidelity, validity, currentness, permissions, effects, and exact Journal receipt references. It does not change any source Atom, Claim, Property, Relation, Project Structure declaration, or Journal authority.

Generic Atom/Carrier metadata (including author, content role, status, and version) remains only on that Atom/Carrier's source record. It is not an Entity Property and is never transferred to the Entity governed by a Subject. `GOVERNS` and `DEPENDS_ON` Subject rows are Atom-incidence/provenance evidence, not native Entity-graph Relation facts: each retains its source Atom identity, Revision, location, and digest. `DEPENDS_ON` remains a distinguishable external reference unless an admitted source-fact context independently establishes a native Relation. No generic Property-fact syntax is admitted here; absent such admitted source-fact context, the projection reports Property coverage as unavailable rather than fabricating values or claiming full Property coverage.

Construction is split from execution recording. The pure builder reads the already admitted frontier and produces no source or Journal write. The shared executor alone appends actual Action/Run recording evidence to the existing Journal history; it neither replaces prior entries nor permits an unrecorded construction to claim a complete Run.

`built` or `no_op` is permitted only when the exact selection/configuration is current, complete, faithful, graph-valid, authorized, and durably recorded. Otherwise return `incomplete`, `conflicting`, `stale`, `blocked`, `failed`, or `canceled` with the affected frontier and actual limited effects; no partial output can claim a complete Projection or Run.

### Sources

- CA-O-133 v2, CA-O-134 v3, CA-O-135 v1.
- CA-R-1387 v8 and CA-M-259 v8 provide the existing reproducibility and persistence baseline.
