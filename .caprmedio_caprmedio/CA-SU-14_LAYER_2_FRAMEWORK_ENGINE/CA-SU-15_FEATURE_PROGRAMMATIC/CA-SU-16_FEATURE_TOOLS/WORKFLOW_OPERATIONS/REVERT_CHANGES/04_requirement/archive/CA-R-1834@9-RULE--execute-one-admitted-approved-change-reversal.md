---
atom_id: CA-R-1834@9
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-26 05:59:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Execution Control
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/Term
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Domain/Occurrent/Execution
relations: {}
type: Rule
tier: 3
---
# Summary

Execute one admitted approved change reversal

## Scope

The REVERT_CHANGES Tool's guarded execution and exact effect-account boundary for an admitted CA-R-1833 manifest.

## Claim

REVERT_CHANGES **must** revalidate current target, hash, affected-reference, authority, and permission bindings before each admitted effect; it **must** preserve history/provenance and report exact observed effects without automatic inverse or replay.

## Details

Before dispatch, including any separately approved later attempt, revalidate the manifest's exact bindings. A changed or unresolved binding blocks further effects and names the completed, failed, unattempted, and uncertain effects. Current complete satisfaction of the exact result plus required history/reference conditions returns `no_op` with zero applied effects. Otherwise apply only the ordered approved effects through governed capabilities, preserving before/after/result evidence, prior Revisions, archives, accepted Events, referenced identities, and the exact safe boundary.

The output is `{ outcome, manifest_id, selection_and_currentness_bindings, expected_result, observed_result, effect_account, history_reference_disposition, evidence_refs, run_receipt_refs }`. `effect_account` contains each ordered effect as `completed`, `failed`, `unattempted`, or `uncertain`; `applied_effect_count` is established completed effects only. The only successful outcomes are `reverted` and `no_op`. `failed` requires confirmed zero applied effects and zero uncertain completion. Any established applied effect **or any uncertain completion**, including with zero confirmed applied effects, is `partial_failure`. Revalidation/approval/currentness/permission/capability/reference failure before a further effect is `blocked`; admitted cancellation is `canceled`. Actual Run-start failure blocks before target effects. Actual Run-terminal failure preserves the independently observed target outcome and exact effect account and reports `run_error`, without claiming terminal Run persistence.

The Tool uses existing shared Run support: actual Run start precedes target effects, and actual Workflow/Step/Action lineage and exact revisions are retained. Plain Journal append/read records supplied observations without a prior-history, chain, confirmed-receipt, deduplication, logging retry or recovery prerequisite. Logging I/O failure is an ordinary diagnostic and does not downgrade an independently observed reversal outcome. Existing `run_receipt_refs` carry actual Run observations and diagnostics, not Journal durability or completion proof. No outcome or log entry authorizes an automatic inverse, effect replay, blind retry, substitute source Revision or broader repair.

### Sources

- CA-O-131 v2, clauses 2–5, outcomes, and durable handoff; CA-O-130 v1 terminal routing; CA-O-132 v1 returned-effect handoff.
- CA-P-1463 v1, exact accepted `failed`/`partial_failure` correction; CA-P-1451 J01–J08 shared contract.
