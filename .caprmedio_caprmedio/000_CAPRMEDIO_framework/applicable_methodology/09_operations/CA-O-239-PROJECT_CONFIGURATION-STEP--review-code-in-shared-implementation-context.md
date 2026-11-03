---
atom_id: CA-O-239
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
version: 1
updated_at: 2026-10-30 03:11:57 +0400
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run.Agentic Step Execution Context
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
relations:
  depends_on:
  - CA-O-016
  - CA-O-238
  - CA-O-231
  - CA-R-1527
tier: 3
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-239-PROJECT_CONFIGURATION-STEP--review-code-in-shared-implementation-context.md
  source_atom_id: CA-O-239
  source_atom_revision: 1
  source_sha256: eac6020f7ca4c86d1419b0bc3dc9fa9471985a4140e45a4671efeca0f45102c4
  original_relations_sha256: c715bd737a4276cf3e12e4d0840322d3b2f2b3782d0651705201e3eace5d4d2e
---
## Summary

Review code in shared implementation context

## Operation

Shared Implementation Review Step **means** the node of `CA-O-016-PROJECT_CONFIGURATION-WORKFLOW--implement-evaluations-before-required-behavior` that invokes exactly one Action, `CA-O-238-PROJECT_CONFIGURATION-ACTION--review-code-candidate-evidence-and-applicable-method-policy-without-editing`, in explicit Integrated context under `CA-R-1527-CORE_META_MODEL-DEFINITION--define-agentic-step-execution-context`.

- Require explicit `review_phase` preliminary **or** final from `CA-O-231-PROJECT_CONFIGURATION-STEP--prepare-shared-context-implementation-work`. Do **not** derive the phase from absent evidence **or** use the standalone default.
- Bind:
  - the selected Project, bounded request **and** P/Plan;
  - the owned candidate **and** changed paths;
  - direct full `requirements`, `methods`, `evaluations`, **and** `delivery` rows with applicable Project-owned Tier 0 Atom sources;
  - the substantive obligation/coverage map;
  - actual check **and** diagnosis evidence with pending/stale outcomes;
  - relevant inputs **and** permissions; **and**
  - retained findings **and** remaining retry/resource state.
- An optional legacy `method_projection` **may** accompany direct rows but is **not** required.
- Retain the participating session **without** replacing complete source-bound inputs with conversational memory. Revalidate source/candidate/test/input bindings before assessment **and** preserve actual partial findings.
- Pass `preliminary_clear`, `passed`, `findings`, `partial`, **or** `unresolved` directly to `CA-O-016-PROJECT_CONFIGURATION-WORKFLOW--implement-evaluations-before-required-behavior`. Read-only review never edits code, changes authority, grants a retry, **or** launches release; repairs remain in the enclosing implementation Workflow.
- Preserve exact Action/Step revisions, candidate **and** evidence bindings, actual effects, **and** returned results.
