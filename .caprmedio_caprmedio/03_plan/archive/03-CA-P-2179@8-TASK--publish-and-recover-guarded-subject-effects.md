---
atom_id: CA-P-2179@8
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
status: Archived
subjects:
  governs: Tool
  depends_on:
  - Atom
  - Subject
  - Revision
  - Journal
  - Plan
version: 8
updated_at: 2026-10-23 23:03:23 +0400
relations:
  is_decomposition_of:
  - CA-P-2173
  blocks:
  - CA-P-2180
  - CA-P-2182
---
# Summary

Publish and recover guarded Subject effects

## Objective

Publish one contract-approved Subject effect with exact prior history and truthful bounded failure/recovery.

## Details

### Local completion — 2026-10-13

Done after independent acceptance of guarded publication, actual selected-route integration, complete independent byte/effect ledgers and actual recording-only repair without replay. The final continuation passed 119 distinct Subject checks and 26 generic Atom Operations checks; it also fixed the refusal-side-effect regression exposed by the broader suite. [Exact evidence, source/code pins and limits](../../../../_projection/core-entity-review/stage2/tools-first/subject-publication-local-completion.md).

This is the Task's local implementation/verification outcome, not installed runtime or migration readiness. Its scope excludes runtime/image/manifest activation. The absent installed confirmation provider therefore does not keep this Task open. Recording-only repair does not reconcile a service's cached pending result. Earlier Active/deferral checkpoints below are historical and are superseded by this completion.

### Local implementation checkpoint — 2026-10-13

The approved Option 1 publication and private exact-change confirmation are implemented and independently reviewed. The public request is unchanged. Shared locking covers the selected Action and declared cooperating Engine writers. Final scoped verification passed 192 distinct checks, including real selected-route execution, caught restoration, interruption evidence, no replay, contention and truthful lock-error outcomes. [Exact evidence and limits](../../../../_projection/core-entity-review/stage2/tools-first/subject-publication-option-1-implementation-acceptance.md).

This is local implementation acceptance only. The installed trusted-host confirmation provider and runtime activation remain unconfigured; ordinary changed-Subject execution still refuses without actual confirmation. Six older composition tests remain blocked by pre-existing stale fixture pins. No live Core migration or full tools-Epic completion is claimed. This Plan remains Active for the remaining route/runtime gates. This checkpoint supersedes historical unconditional-prototype-deferral descriptions below, not their historical evidence.

### Approved failure handling and authorization binding

The Operator selected Option 1 after the bounded publication FPF review: caught errors attempt Action-local restoration, with observed failed/partial results; abrupt process interruption or crash is not crash-atomic and may leave partial state. Retain interruption evidence, inspect actual current/history/Run state before another change, and never automatically replay the Atom effect. This explicitly clarifies the earlier all-or-nothing wording; it does not permit false success, predecessor loss, or rollback of earlier independent actions.

The Operator authorized the narrow rule updates, shared-lock/exclusive-window implementation and full-path isolated tests. The existing authorization reference must bind explicit Operator confirmation for the exact reviewed change and affected current/history/authority files. Its purpose-specific internal trusted-host binding keeps public request fields unchanged; request data cannot manufacture confirmation. Missing, stale or mismatched confirmation refuses effects. No installed runtime provider or live Core migration is activated by this approval.

Implementation is divided into bounded responsibilities: source clarification and independent acceptance; internal authorization and Subject publication; shared locking of cooperating Engine writers; current selected-route fixtures; and independent contention/failure verification. Completed raw-helper checks alone cannot close publication acceptance. The existing publication Tasks and this Plan remain Active until their actual checks pass. This checkpoint supersedes conflicting historical deferral statements below without changing their past evidence.

### Selected publication model

The Operator selected staged review followed by a short exclusive publication window. Manual edits, Git operations and sync writes to affected files must be paused; participating Engine writers use one shared lock. Outside writers that ignore this constraint are not protected by the model. Review the approved change and source state before entering the window; preserve the existing distinction between reviewed intent/delta and governed effect-time metadata. Final revalidation, publication, readback and any existing action-local restoration must remain inside the protected interval.

This supersedes the earlier choice deferral below, not the remaining source/API/FPF, implementation, independent proof or route-admission gates. Keep the current changed-Subject guard until those gates pass. Do not infer a stronger crash-atomic guarantee, relax existing safety requirements, invent public approval fields, add automatic retry/replay, or apply live Core migration. The unresolved interpretation of existing all-or-nothing wording must be reviewed, not silently weakened.

Estimated own work: 15 minutes. Assignee: AI Agent. Prerequisites: CA-P-2178's actual API and CA-P-2170's current application packet independently accepted under CA-P-2171. No code starts from a proposed or stale packet.

Exclusive edits: new `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/atom_subject_apply.py`, only its required guarded raw-byte helper in `atom_operations.py`, and new `ATOM_UPDATE/tests/test_subject_apply_native.py` under Tools. Reopen every affected helper caller. Other workers own planner, route integration and independent fixtures; shared state/Git have one integration owner.

Reuse the existing governed mutation validation/publication mechanism for one eligible valid original. Verify exact source and history frontier, then use CA-P-2178 materialization for current Version N+1 and actual timestamp. Preserve exact old Version N bytes in history without another bump; preserve ID, intended Status and unrelated bytes. Validate complete before/after carriers. Reject duplicate current/history identities, projections, symlinks, stale pins, extra effects and direct standalone application. The caller must supply the admitted authorization context; do not create a raw bypass.

Bind publication ownership and failure disposition to the accepted contracts. Failed restoration or uncertain publication cannot report success or imply automatic replay. Expose truthful effects for the existing route's recording/recovery owner; do not fabricate Journal/Run completion. Check happy/no-op/refusal/publication/restoration paths on isolated valid fixtures and deliver exact code/effect pins. If this one-target scope cannot fit 15 minutes, split the concrete remainder before executing it.

### Earlier deferred publication follow-up

The Operator deferred the concurrency safety choice. [Independent review](../../../../_projection/core-entity-review/stage2/tools-first/intent-and-application-status.md) reproduced an edit overwritten between the last fingerprint check and replacement; history removal has the same ownership window. Earlier validation does not close it. No exclusive-access requirement, quarantine policy or atomic exchange was approved. Live changed-Subject writes remain blocked even with otherwise valid packet approval, and this Task stays Active.

The native route now unconditionally refuses changed-Subject execution with `subject-publication-deferred` after actual admission and before materialization/current/history/rollback writes; preview and exact no-op return earlier. That ordering received independent static verification. Root's UPDATE 66, raw-helper four, selected-lifecycle 30 and dispatch five checks passed within their declared scopes. Raw mechanics and refusal checks do not accept the disabled publication/recovery prototype or prove concurrency safety.

Keep the follow-up here: later review a bounded publication design covering current/history ownership through publication and failed restoration; record the actual Operator choice, align any affected RMEDO and independently verify concurrent-edit controls before opening the live gate. Do not infer authority or implement a new concurrency framework from the deferral. Safe preview/materialization/no-op checks do not satisfy successful publication or restoration acceptance.

### Earlier reopening of design and testing

The Operator explicitly reopened publication design and testing. The earlier deferral above is the historical decision; it no longer blocks bounded comparison and isolated tests. At that reopening checkpoint the concurrency/access mechanism was not yet selected; the current decision above supersedes this. Compare practical one-Atom choices and present the exact operational constraint to the Operator before enabling changed writes.

Keep the existing publication guard while designing. No live Core migration, automatic replay, new broad recovery framework or unchosen exclusive-access requirement is approved. After the mechanism is chosen, align affected contracts and independently verify current/history ownership, actual effects and failure disposition before enabling any route. Record concrete implementation portions within the existing 15-minute bound and split larger work before execution.

### Definition of Done

The Plan is **not** Done if concurrent-publication design remains deferred or successful publication/concurrent restoration is unaccepted, contracts/API are missing/stale, frontier or identity/history preservation weakens, unauthorized bytes are published, failure/recovery ownership is ambiguous, actual fixture effects differ, direct apply is unguarded, or own work exceeds 15 minutes without decomposition.
