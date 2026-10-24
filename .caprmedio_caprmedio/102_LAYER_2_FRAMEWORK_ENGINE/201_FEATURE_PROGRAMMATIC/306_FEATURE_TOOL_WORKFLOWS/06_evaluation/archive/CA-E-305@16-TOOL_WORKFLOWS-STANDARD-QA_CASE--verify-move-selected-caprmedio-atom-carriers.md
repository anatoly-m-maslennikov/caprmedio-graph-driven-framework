---
claim_target_scope_unit: TOOL_WORKFLOWS
current_scope_unit: TOOL_WORKFLOWS
content_role: Evaluation
atom_id: CA-E-305@16
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/Tool//ATOM_MOVE
  depends_on: []
version: 16
status: Archived
updated_at: 2026-10-24 02:14:24 +0400
relations:
  evaluation_for:
  - CA-M-187
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
tier: 5
type: Eval Case
---
# Verify move selected caprmedio atom carriers

## Claim checked

CA-M-187 moves one sealed Atom through its explicitly admitted placement/owner/filename mapping while preserving stable ID, Summary, Type, Substance and unrelated content. A real changed move carries its admitted metadata, Version N+1, actual Updated At and exact prior history at N; it is not complete-byte preservation. A subtree selection is an ordered set of independent Atom actions under CA-M-372.

## Applicable when

Workflow admission owns identity, Version/time, lifecycle and complete schema decisions. Connector calls use CA-D-625 only to verify the supplied request, source preconditions and permission and to perform the explicit mechanical operation. A connector does not choose those decisions.

Apply before relying on an Atom Move realization. These cases specify required future checks, not an observed pass.

## Test case

Prepare one exact Atom and a two-level subtree with three Atoms and one non-Atom file. Freeze the explicit ordered Atom selection and expected source states. Verify default shape preservation and explicitly requested flattening maps without mutation. Each move needs its own permission/currentness, identity/schema admission and collision checks. Verify the actual admitted owner/path/filename metadata delta and exact predecessor history independently. No implicit rename or unrelated Substance/ID/Type edit is permitted.

## Failure cases

For ordered A, B and C, complete A and inject a destination collision or post-write failure for B. Retain A at its observed destination, report B's failure and leave C and the non-Atom untouched. Do not restore A merely because B failed.

Within one Move action, inject a failure after destination publication or during verification. Require that action's admitted all-or-nothing boundary and exact restoration where claimed; unverified restoration fails the check. Preserve unrelated files and accepted history. Preflight refusal is not post-effect rollback evidence, and any unresolved CA-C-119 owner/filename admission blocks that move rather than being bypassed.

## Acceptance criteria

Each completed changed move applies only its admitted mapping and metadata, preserves ID/Summary/Type/Substance and unrelated content, advances Version exactly once with actual time, retains exact prior bytes at N and removes only its admitted source. Verify before/current/history digests separately; the new current digest need not equal the predecessor digest. A true no-op leaves complete Carrier bytes and placement unchanged, retains Version/time and creates no new history. Maps and effects remain attributable per Atom. Dry runs and rejected preflight have no effect; earlier completed actions survive a later failure and the remainder is untouched. New workflow resume/retry and stronger concurrency/publication guarantees remain deferred.

## Failure disposition

Retain ordered selection, exact pins, mappings, permission decisions, observed source/destination states, successes, failure and unperformed remainder.
