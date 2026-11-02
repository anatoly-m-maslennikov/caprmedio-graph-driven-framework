---
atom_id: CA-O-127
content_role: Operations
type: Workflow
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Workflow"
  depends_on: ["Step", "Workflow Run", "Workflow/Relation Kind: On Result", "Operator", "Journal"]
version: 5
updated_at: "2026-10-15 10:01:40 +0000"
relations:
  relates_to: [CA-O-129, CA-O-145, CA-M-303, CA-R-1508, CA-R-1513, CA-R-1520, CA-R-1525, CA-R-1720]
---
# Summary

Manage atom lifecycle

## Operation

One reusable parameterized Workflow graph binds Create Atom, Update Atom, Replace Atom and Change Atom Status. Archive is only a Change Status shortcut admitted by the applicable model, not another Workflow. The Step definitions own all Action and input bindings.

Each invocation admits exactly one Create target or one existing current target/predecessor, with its complete required Carrier set. Replace retains the complete accepted set of >=1 distinct successors for that one predecessor, not additional predecessors. A request naming multiple independent targets/predecessors ends blocked before Step dispatch or effects; bulk callers expand their requests into separate individually admitted Runs of this same Workflow, with fresh exact inputs/assessment/permission bindings for each, except the reviewed Subjects-only batch admission below.

For a containment cascade required by R1521, the calling Workflow binds the parent and every selected contained Plan or Operations Atom's latest Revision as separate individually admitted Runs of this Workflow, all requesting the same Status under each target's own model. Older historical Revisions and references outside the parent Carrier tree are excluded. Each Run retains the single-target boundary below; none discovers, invokes or authorizes the other targets. The caller preserves nesting under D461/D467 and advances only after a verified applied or no-op result with required recording. It stops on the first failed, refused or uncertain result, retains earlier completed effects and leaves remaining targets untouched, without automatic retry or cross-Atom rollback. One completed Run proves only its bound target; the caller reports the whole cascade complete only after every selected target has a verified result.

### Nodes and entry

The graph has exactly two Step nodes: CA-O-145 and CA-O-129. An ordinary admitted Update request enters CA-O-145; admitted Create, Replace or Change Status requests enter CA-O-129. Unsupported request kinds end blocked without an effect.

### Typed transitions and terminal results

| Source Step result | Workflow-owned scheme |
| --- | --- |
| O145: identity-preserving | ON_RESULT O145→O129, subject to current authorization, compatible exact assessment and effect admission. |
| O145: replacement-required | End this Run with an R1520 terminal handoff to the Replace entry of CA-O-127 in a separately admitted Run. Do not call/wait for replacement, perform an intermediate update or treat the handoff as replacement permission. |
| O145: unresolved, invalid, stale, unauthorized or unavailable | End blocked with the exact evidence/decision gap; no approval inferred. |
| O129: reassessment-required for Update | ON_RESULT O129→O145 only with an explicitly admitted fresh proposal/evidence binding and remaining applicable retry allowance. Without them end blocked. |
| O129: applied or no-op | End complete only for the exact admitted boundary with verified results and all required durable Run/change receipts; no-op reports no Artifact change. |
| O129: invalid, stale, unauthorized, unsupported, blocked, recording-blocked, failed, partial or canceled | End with that truthful non-complete outcome, actual completed/incomplete effects and recoverable evidence; no automatic replay. |

The two ON_RESULT edges have Step endpoints in this Workflow. No other route, implicit retry, continuation, graph node or Action-selected successor is admitted. A changed definition pauses dispatch for R1525 revalidation; completed effects and retry accounting remain retained.

### Reviewed Subjects-only batch routing

For a reusable batch whose exact ordered Subject map and source-before pins have been explicitly reviewed and confirmed once by the Operator, one admitted O127 Workflow Run iterates the explicit map members in order, invoking O129 directly for each member. This is the batch exception to separate O127 Runs per target and to the ordinary no-other-continuation graph rule; it adds no new Step definition. Each member has its own actual distinct O129 Step Run and O128 Action Run, with the existing O030 effect Action Run and parent lineage where invoked. Retain exact map/member and batch-confirmation bindings through that one Workflow; do not fabricate per-Atom O145/O067 assessment Runs or Analysis Reports. The approved map supplies the declared Subject delta and lineage review; it does not authorize body, Summary, Type, Status or placement changes. Ordinary single-target routing and its two-Step graph remain unchanged.

Create the Git checkpoint before the batch as recovery evidence, not an additional recovery-readiness or restoration-receipt gate. Use the existing updater/archive semantics, and preserve each member's exact source-before, Subjects-only change, N+1/actual-time and independent current/history verification. Advance only after verified applied/no-op, stop first failed/refused/uncertain member, retain earlier successes and leave remaining members untouched; no automatic retry/resume or cross-Atom rollback. Existing low-level failed-Atom restoration remains. Actual results/logging errors are retained separately without treating Journal receipts as proof of source effects. No per-member confirmation form or same-MCP-connection staging is required for this branch; ordinary assessment, receipt and confirmation requirements do not reintroduce them.

## Details

Reuse O067 identity assessment through O145 and O051 accepted replacement persistence through the effect Action. The graph neither duplicates those behaviors nor owns their bindings. A Summary change always follows the replacement-required terminal route; a changed proposal or stale evidence requires reassessment before update persistence.

The separately admitted successor obtains fresh definition/input/permission bindings. Required pending replacement is not reported complete. Change Status resolves the actual current Atom, then its complete Content Role and optional Type-qualified model: use the applicable existing whitelist and transition rule under R1521/R1308, including current Operations R1874 and Analysis R1875 role bindings, not a Workflow list. A more-specific declared Role/Type model overrides its role model; otherwise the role model applies without duplicated Type value sets. A same current status is a no-op. Archive is only a shortcut when that qualified model explicitly defines an archival status; otherwise archive ends missing-archival-model/unsupported without mapping Concern resolved or canceled to archival meaning.

Every Workflow/Step/Action Run, including referenced Action executions, standalone use, nested lineage, failure/cancellation and no-op, retains exact definitions/inputs, parent references, start/terminal/result/effect evidence in the one authoritative Journal under R1720/R1525 and applicable Run policy. Missing durable receipts are recording-blocked, not journaled success. No secret or competing history store is introduced. This is a source graph, not evidence of implementation, MCP, prompt or runtime execution.

For draft-backed batch approval, the reviewed map is the completed packet containing every CA-D-446 Subjects-only edit-draft path/digest; the separately reviewed map-only batch remains admitted with no draft pins. Its temporary `<canonical-ID>@draft` and Status Draft identify a derived proposal, not another canonical target. Reopen exact source and draft; normalize to the pinned canonical ID and original Status, and require independent fresh Subjects-only canonical materialization/validation before the existing archive/update effect. A full proposal's other bytes cannot broaden the admitted patch. Actual publication changes only Subjects, N+1 and actual time; new-Atom Draft identity/lineage rules remain unchanged.
