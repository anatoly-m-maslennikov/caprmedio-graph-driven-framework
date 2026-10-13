---
atom_id: CA-P-2179
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Revision, Journal, Plan]
version: 2
updated_at: "2026-10-12 04:49:28 +0400"
relations:
  is_decomposition_of: [CA-P-2173]
  blocks: [CA-P-2180, CA-P-2182]
---
# Summary

Publish and recover guarded Subject effects

## Objective

Publish one contract-approved Subject effect with exact prior history and truthful bounded failure/recovery.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Prerequisites: CA-P-2178's actual API and CA-P-2170's current application packet independently accepted under CA-P-2171. No code starts from a proposed or stale packet.

Exclusive edits: new `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/atom_subject_apply.py`, only its required guarded raw-byte helper in `atom_operations.py`, and new `ATOM_UPDATE/tests/test_subject_apply_native.py` under Tools. Reopen every affected helper caller. Other workers own planner, route integration and independent fixtures; shared state/Git have one integration owner.

Reuse the existing governed mutation validation/publication mechanism for one eligible valid original. Verify exact source and history frontier, then use CA-P-2178 materialization for current Version N+1 and actual timestamp. Preserve exact old Version N bytes in history without another bump; preserve ID, intended Status and unrelated bytes. Validate complete before/after carriers. Reject duplicate current/history identities, projections, symlinks, stale pins, extra effects and direct standalone application. The caller must supply the admitted authorization context; do not create a raw bypass.

Bind publication ownership and failure disposition to the accepted contracts. Failed restoration or uncertain publication cannot report success or imply automatic replay. Expose truthful effects for the existing route's recording/recovery owner; do not fabricate Journal/Run completion. Check happy/no-op/refusal/publication/restoration paths on isolated valid fixtures and deliver exact code/effect pins. If this one-target scope cannot fit 15 minutes, split the concrete remainder before executing it.

### Deferred publication follow-up

The Operator deferred the concurrency safety choice. [Independent review](../../../../_projection/core-entity-review/stage2/tools-first/intent-and-application-status.md) reproduced an edit overwritten between the last fingerprint check and replacement; history removal has the same ownership window. Earlier validation does not close it. No exclusive-access requirement, quarantine policy or atomic exchange was approved. Live changed-Subject writes remain blocked even with otherwise valid packet approval, and this Task stays Active.

The native route now unconditionally refuses changed-Subject execution with `subject-publication-deferred` after actual admission and before materialization/current/history/rollback writes; preview and exact no-op return earlier. That ordering received independent static verification. Root's UPDATE 66, raw-helper four, selected-lifecycle 30 and dispatch five checks passed within their declared scopes. Raw mechanics and refusal checks do not accept the disabled publication/recovery prototype or prove concurrency safety.

Keep the follow-up here: later review a bounded publication design covering current/history ownership through publication and failed restoration; record the actual Operator choice, align any affected RMEDO and independently verify concurrent-edit controls before opening the live gate. Do not infer authority or implement a new concurrency framework from the deferral. Safe preview/materialization/no-op checks do not satisfy successful publication or restoration acceptance.

### Definition of Done

The Plan is **not** Done if concurrent-publication design remains deferred or successful publication/concurrent restoration is unaccepted, contracts/API are missing/stale, frontier or identity/history preservation weakens, unauthorized bytes are published, failure/recovery ownership is ambiguous, actual fixture effects differ, direct apply is unguarded, or own work exceeds 15 minutes without decomposition.
