---
atom_id: CA-R-1833@3
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 3
updated_at: 2026-10-23 01:47:30 +0400
subjects:
  governs: Subject/Engineering/Change Reversal/Manifest Admission
  depends_on:
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/Term
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Domain/Node/Occurrent/Execution
relations:
  relates_to:
  - CA-O-130
  - CA-O-131
  - CA-O-132
  - CA-R-1525
  - CA-R-1720
type: Rule
---
# Summary

Admit exact approved change-reversal manifests

## Scope

The REVERT_CHANGES Tool's mutation-free admission and manifest construction boundary for one exact Operator-approved change reversal.

## Claim

REVERT_CHANGES **must** accept only a complete approved reversal manifest; it **must not** infer an inverse, approval, current target, hash, permission, affected reference, or recovery boundary.

## Details

The input is a `reversal_request` with: exact selected accepted change/Event/Revision references and before/after evidence; target identities; expected current Carrier/state hashes and affected-reference hashes; ordered approved effects and expected result; current governing-definition bindings; the recorded Operator decision binding exactly those effects; cancellation/recovery boundary; executor permission/capability evidence; and durable evidence location. Missing, stale, mismatched, revoked, unsupported, or unapproved input returns `blocked` before target mutation.

The manifest preserves those immutable request bindings plus an admission-time target/reference observation and a deterministic manifest ID. A manifest is invalid after any bound target, hash, authority, approval, permission, or effect ordering changes. It may represent an explicitly approved already-satisfied expected result, but still requires the same approval, currentness, history, and reference checks.

The Tool returns either `{ outcome: "blocked", manifest: null, missing_or_mismatched_bindings, evidence_refs }` or `{ outcome: "admitted", approved_reversal_manifest, evidence_refs }`. This admission helper runs before any Action dispatch and is neither an Action execution nor a Run/effect receipt; it neither appends the Journal nor mutates a target. That pre-dispatch result does not exempt an actual standalone CA-O-131 invocation from its distinct Action Run start and truthful terminal state. Plain Journal append/read records supplied observations independently; no confirmed Journal receipt, logging retry or recovery is an admission or source-effect completion prerequisite. The manifest is an exact request artifact, not arbitrary destructive instructions and not authority for internal failure rollback, Git reset, history deletion, or widened repair.

### Sources

- CA-O-131 v2, clauses 1–3 and outcomes; CA-O-132 v1 input binding; CA-O-130 v1 admission/recovery routing.
- CA-P-1463 v1 independently accepts O131v2's disjoint zero-confirmed/uncertain outcome predicates.
