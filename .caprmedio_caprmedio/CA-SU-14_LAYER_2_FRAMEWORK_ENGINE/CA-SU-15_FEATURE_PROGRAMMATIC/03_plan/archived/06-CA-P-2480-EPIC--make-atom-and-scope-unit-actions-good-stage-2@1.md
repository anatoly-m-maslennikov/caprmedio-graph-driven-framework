---
atom_id: CA-P-2480
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 6
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Backlog
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  relates_to: [CA-P-2401]
version: 1
updated_at: "2026-10-20T19:46:21.487Z"
---
# Summary

Make Atom and Scope Unit Actions Good — Stage 2

## Objective

Own the deferred Scope Unit operations and their structure, binding and folder coherence; Stage 1 CA-P-2401 continues Atom operations.

## Details

At most 15 minutes own work; split before extending. Scope Unit work is deferred, not complete or executable by this creation. Preserve current governing authority, activated model rules, protected identity and exact history.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.

### Deferred scope

Create, rename, move and delete Scope Units; validate Project Structure and real governing/delivery folders; reconcile declarations/properties/files with explicit files/folders-canonical, properties-canonical or manual policy. Apply empty-only deletion to both places: refuse Atoms, child units, code or any other content. Preserve parent-relative paths, unit name/prefix, levels, ordering/coordinates and upstream bindings under current atoms; a delivery place is not another Scope Unit.

The agreed unordered PROGRAMMATIC topology migration, governing/delivery moves and declaration synchronization belong here. Stage 1 may consume existing valid scope bindings for Atom safety, but does not perform deferred Scope Unit changes or bypass invalid bindings. Atom file/container operations, including nested Plan archival, remain Stage 1.

### Dependencies and acceptance

Reuse historical Scope Unit audit P2403/P2406 and related Concerns without moving or relabeling completed records. Inventory current RMEDO, project_structure.toml, real places and callers before creating implementation Tasks. One Task/file, at most 15 minutes own work; split and review dependent next tasks before execution. Align source contracts before behavior changes. Functional golden tests must cover safe deletion refusal, relative bindings, intentional non-materialization, collisions and both places. Runtime tests require isolated nonproduction state/port; deployment/release and migration need separate authority.

### Stage boundary

Stage 1 retains Atom actions/validation/reconciliation, connectors, Workflow/MCP handoff, configurable model and multi-Project runtime work insofar as it does not execute deferred Scope Unit operations. This Epic is a separate peer, not a duplicate owner or a claim of completed Scope Unit delivery.
