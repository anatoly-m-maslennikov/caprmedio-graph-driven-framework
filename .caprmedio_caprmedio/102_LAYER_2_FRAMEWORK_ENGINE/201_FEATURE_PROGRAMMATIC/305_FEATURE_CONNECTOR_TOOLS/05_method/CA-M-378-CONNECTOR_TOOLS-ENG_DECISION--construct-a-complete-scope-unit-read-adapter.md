---
atom_id: CA-M-378
content_role: Method
type: Eng Decision
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
status: Active
author: Anatoly Maslennikov
version: 14
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Architecture/Communication
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Domain/Continuant/Project.Structure
  - Subject/Graph Node/Domain/Continuant/Project.Settings
relations: {}
tier: 3
---
# Summary

Construct a complete Scope Unit read adapter

## Scope

Construction of a storage-independent adapter for one complete Scope Unit declaration Read.

## Claim

**to** construct the Scope Unit Read adapter, the Implementer **must** refine CA-M-376-CONNECTOR_TOOLS-ENG_DECISION--execute-one-explicit-connector-operation:

- bind the explicit canonical Scope Unit Name to the supplied Project **and** source view using CA-D-627-CONNECTOR_TOOLS-ENG_DECISION--deliver-complete-scope-unit-read-data. resolve **only** that target; do **not** add an implicit Query, wrapper Workflow, alias search **or** version-selection heuristic.
- use the accepted declaration schema **and** authority bindings to obtain the complete non-Project declaration **or** root Project Settings `project` table. keep backend locations **and** serialization internal, preserve actual property values, **and** do **not** infer missing facts from a folder **or** Projection.
- return actual source-state evidence for an unpinned Read **and** enforce exact supplied pinned/historical evidence **where** requested. keep required schema/permission/currentness checks separate from target lookup **and** fail rather than substitute evidence.
- verify complete returned declaration data independently of merely completing backend access. compare **all** applicable carried fields **and** their presence/absence against the selected source; preserve read-only behavior on successful **and** failed requests.

## Details

CA-R-1938-CONNECTOR_TOOLS-RULE--read-one-complete-scope-unit-declaration owns the required result, CA-E-630-CONNECTOR_TOOLS-EVAL_CASE--verify-complete-scope-unit-reads owns future acceptance and CA-O-212-CONNECTOR_TOOLS-ACTION--read-one-complete-scope-unit-declaration defines the Action. This Method introduces no database implementation, storage-path selector, retry/resume policy or runnable binding.
