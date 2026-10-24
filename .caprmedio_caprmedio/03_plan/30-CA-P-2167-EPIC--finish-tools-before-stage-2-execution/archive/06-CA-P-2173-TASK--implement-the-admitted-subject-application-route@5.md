---
atom_id: CA-P-2173
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Revision, Journal, Plan, Operator]
version: 5
updated_at: "2026-10-12 23:10:03 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
  blocks: [CA-P-2174]
---
# Summary

Implement the admitted Subject application route

## Objective

The existing governed mutation boundary can apply an exact sealed Subjects-only packet through its admitted route.

## Details

### Prospective rebuilt-contract gate

The latest logical connector/Workflow rebuild under CA-P-2167 is a new prospective contract input, not completion of this implementation. CA-P-2248 must independently accept the actual current affected contracts before implementation proceeds; the old CA-P-2170/2171 receipt remains historical and cannot release work against revised pins. Preserve this Plan's admitted Subject application outcome and the existing exact approval, one-Atom safety, currentness and truthful recording gates.

The prospective CA-P-2167 rebuild section supersedes conflicting older executable assumptions below and in CA-P-2179–2182. Across multiple Atom actions, stop on the first failure, retain prior successful actions and leave remaining targets untouched; no cross-Atom all-or-nothing rollback is allowed. Resume/retry and automatic continuation/replay remain DEFERRED, not an implicit required design. The older concurrent-publication choice also stays deferred under CA-P-2179; no publication mechanism or live capability is enabled.

After accepted contracts, create actual <=15-minute implementation leaves for any additional connector, configuration or section-edit work before executing it. This Plan alone cannot cover that new Tool set, and preparation/source authoring is not implementation. Historical completed children and receipt pins remain unchanged.

Own work: none. Required prerequisite for production implementation: CA-P-2170's actual current application contract packet independently accepted under CA-P-2171; unrelated preview/graph packets need not delay it. CA-P-2177 has prepared the bounded children below. Contract/fixture preparation may proceed independently, but implementation and acceptance must obey each child's gates. All children and their actual isolated outputs must complete; preparation alone cannot finish this group.

The Operator chose extending the existing admitted MCP update action with Subjects-only application. Implement that route only after its actual current contract packet passes independent acceptance. No local transport exception, completed capability or live migration approval is inferred; the exact CA-P-1910 sealed packet still needs separate approval.

Implement only the accepted application contracts through the existing boundary. Retain the standalone apply guard until the intended admitted route enforces exact approval, pins, source eligibility, Subjects-only bytes, Version/time/history and truthful Journal effects. Do not create a raw internal bypass, broad repair engine or invented runtime/MCP binding. Root owns shared state and Git; one owner controls each mutation scope.

Use valid isolated fixture carriers only. Production Core application stays under CA-P-1910's separately approved exact sealed packet and CA-P-1911's sole execution. A working Tool is not that approval or a live effect receipt.

CA-P-2178's pure intent/materialization is independently complete. Guarded native publication/recovery (CA-P-2179), full MCP selected-route application (CA-P-2180), the independent fixture portfolio (CA-P-2181) and combined verification (CA-P-2182) remain unresolved where they require successful publication. Keep a single target and existing Report/envelope/Run/recording boundaries. No `selected_routes.py`, Core body, installation or runtime-publication change is included. Live image/manifest readiness remains separate.

The Operator deferred the concurrent-publication safety choice. Live changed-Subject writes are blocked pending the later design and its actual review/verification; otherwise valid sealed approval does not open this gate. Existing CA-P-2179 owns the follow-up. Safe preview/no-op/materialization and five dispatch/five selected golden-request checks are bounded evidence, not acceptance of publication or concurrent restoration/history ownership. No exclusive-access requirement, quarantine policy or atomic exchange was approved. See [the verified intent and unfinished application receipt](../../../_projection/core-entity-review/stage2/tools-first/intent-and-application-status.md).

### Decomposing Plans

- [CA-P-2177 — Prepare bounded admitted application work](06-CA-P-2173-TASK--implement-the-admitted-subject-application-route/done/01-CA-P-2177-TASK--prepare-bounded-admitted-application-work.md)
- [CA-P-2178 — Define Subject intent and effect materialization](06-CA-P-2173-TASK--implement-the-admitted-subject-application-route/done/02-CA-P-2178-TASK--define-subject-intent-and-effect-materialization.md)
- [CA-P-2179 — Publish and recover guarded Subject effects](06-CA-P-2173-TASK--implement-the-admitted-subject-application-route/03-CA-P-2179-TASK--publish-and-recover-guarded-subject-effects.md)
- [CA-P-2180 — Integrate Subject application into the MCP update action](06-CA-P-2173-TASK--implement-the-admitted-subject-application-route/04-CA-P-2180-TASK--integrate-subject-application-into-the-mcp-update-action.md)
- [CA-P-2181 — Author independent Subject application fixtures](06-CA-P-2173-TASK--implement-the-admitted-subject-application-route/05-CA-P-2181-TASK--author-independent-subject-application-fixtures.md)
- [CA-P-2182 — Verify the combined Subject application route](06-CA-P-2173-TASK--implement-the-admitted-subject-application-route/06-CA-P-2182-TASK--verify-the-combined-subject-application-route.md)

### Definition of Done

The Plan is **not** Done if a direct child is not Done, actual implementation/check children are absent, only preparation/safe integration is complete, concurrent-publication design remains deferred or successful publication/full portfolio is unaccepted, admission is missing, a guard is bypassed, isolated effects diverge from contracts, or live approval/effects are inferred from bounded checks or Tool readiness.
