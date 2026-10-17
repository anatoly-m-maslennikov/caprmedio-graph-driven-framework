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
  governs: "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Workflow"
  depends_on: ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step", "Entity/Occurrent/Execution/Workflow Run", "Entity/Continuant/Object/Relation/Type: On Result", "Entity/Continuant/Actor/Type: Operator", "Entity/Continuant/History/Journal"]
version: 10
updated_at: "2026-10-16 12:09:40 +0000"
relations:
  relates_to: [CA-O-129, CA-O-145, CA-M-303, CA-R-1508, CA-R-1513, CA-R-1520, CA-R-1525, CA-R-1720]
---
# Summary

Manage atom lifecycle

## Operation

One reusable parameterized Workflow graph binds Create Atom, Update Atom, Replace Atom and Change Atom Status. Archive is only a Change Status shortcut admitted by the applicable model, not another Workflow. The Step definitions own all Action and input bindings.

Each invocation admits exactly one Create target or one existing current target/predecessor, with its complete required Carrier set. Replace retains the complete accepted set of >=1 distinct successors for that one predecessor, not additional predecessors. A request naming multiple independent targets/predecessors ends blocked before Step dispatch or effects; bulk callers expand their requests into separate individually admitted Runs of this same Workflow, with fresh exact inputs/assessment/permission bindings for each, except the instructed Subjects-only batch admission below.

For a containment cascade required by R1521, the calling Workflow binds the parent and every selected contained Plan or Operations Atom's latest Revision as separate individually admitted Runs of this Workflow, all requesting the same Status under each target's own model. Older historical Revisions and references outside the parent Carrier tree are excluded. Each Run retains the single-target boundary below; none discovers, invokes or authorizes the other targets. The caller preserves nesting under D461/D467 and advances only after a verified applied or no-op result. It stops on the first failed, refused or uncertain result, retains earlier completed effects and leaves remaining targets untouched, without automatic retry or cross-Atom rollback. One completed Run proves only its bound target; the caller reports the whole cascade complete only after every selected target has a verified result.

### Nodes and entry

The graph has exactly two Step nodes: CA-O-145 and CA-O-129. An ordinary admitted Update request enters CA-O-145; admitted Create, Replace or Change Status requests enter CA-O-129. Unsupported request kinds end blocked without an effect.

### Typed transitions and terminal results

| Source Step result | Workflow-owned scheme |
| --- | --- |
| O145: identity-preserving | ON_RESULT O145→O129, subject to current authorization, compatible exact assessment and effect admission. |
| O145: replacement-required | End this Run with an R1520 terminal handoff to the Replace entry of CA-O-127 in a separately admitted Run. Do not call/wait for replacement, perform an intermediate update or treat the handoff as replacement permission. |
| O145: unresolved, invalid, stale, unauthorized or unavailable | End blocked with the exact evidence/decision gap; no approval inferred. |
| O129: reassessment-required for Update | ON_RESULT O129→O145 only with an explicitly admitted fresh proposal/evidence binding and remaining applicable retry allowance. Without them end blocked. |
| O129: applied or no-op | End complete only for the exact admitted boundary with verified effect/postcondition results; no-op reports no Artifact change. An independent Journal append failure is a recording diagnostic, not a non-complete result. |
| O129: invalid, stale, unauthorized, unsupported, blocked, failed, partial or canceled | End with that truthful non-complete outcome, actual completed/incomplete effects and recoverable evidence; no automatic replay. |

The two ON_RESULT edges have Step endpoints in this Workflow. No other route, implicit retry, continuation, graph node or Action-selected successor is admitted. A changed definition pauses dispatch for R1525 revalidation; completed effects and retry accounting remain retained.

### Instructed Subjects-only batch routing

The exact ordered Subjects packet is admitted by the actual Operator instruction and existing request Initiative/authorization, without a separate form, review/pause response, content review or confirmation receipt. One O127 Workflow Run iterates explicit members through distinct actual O129 Step/O128 Action and existing O030 effect Runs with parent lineage. This is the existing batch exception to separate O127 Runs/no-other-continuation; ordinary two-Step/singleton routing remains unchanged. Do not fabricate O145/O067 Runs or Analysis Reports.

The caller composes commit-current → create-drafts → commit-drafts → archive/promote → rebuild-graph, using actual existing operation results. Each member retains normal exact source/draft/patch/layout, conditional-write, archive, N+1/time and readback checks, not an additional full-candidate validation or initial intent-metadata gate. Stop first failure/uncertainty, keep completed effects and leave remaining and held sources untouched. Preserve native failed-write handling; no automatic batch rollback/replay/retry/resume is introduced. Actual logging errors remain separate from source-effect truth.

## Details

Reuse O067 identity assessment through O145 and O051 accepted replacement persistence through the effect Action. The graph neither duplicates those behaviors nor owns their bindings. A Summary change always follows the replacement-required terminal route; a changed proposal or stale evidence requires reassessment before update persistence.

The separately admitted successor obtains fresh definition/input/permission bindings. Required pending replacement is not reported complete. Change Status resolves the actual current Atom, then its complete Content Role and optional Type-qualified model: admit any requested value from that model under R1521/R1308, including current Operations R1874 and Analysis R1875 role bindings, without a Workflow-owned list, required intermediate Atom Status or transition matrix. A more-specific declared Role/Type model overrides its role model; otherwise the role model applies without duplicated Type value sets. Ordinary schema, identity/collision, expected-source/currentness, permission and Carrier safeguards remain. A same current status is a no-op. Archive is only a shortcut when that qualified model explicitly defines an archival status; otherwise archive ends missing-archival-model/unsupported without mapping Concern resolved or canceled to archival meaning.

Every Workflow/Step/Action Run, including referenced Action executions, standalone use, nested lineage, failure/cancellation and no-op, independently attempts to append its actual exact definitions/inputs, parent references and start/terminal/result/effect observations to the one authoritative Journal under R1720/R1525 and applicable Run policy. A Journal append failure is a truthful recording diagnostic: it does not invalidate a verified effect, make success non-complete, authorize replay or create a secret or competing history store. This is a source graph, not evidence of implementation, MCP, prompt or runtime execution.

For the instructed draft-backed batch, the final schema1 packet pins every CA-D-446 edit draft; a separately instructed map-only batch remains admitted. Temporary `<canonical-ID>@draft`/Status Draft denotes a derived proposal. Restore canonical ID/original Status and actual time through normal per-target Subjects-only operation checks, without a separate full-candidate review/validation round. The proposal cannot authorize unrelated bytes or a new identity/Status transition; existing new-Atom Draft policy remains.
