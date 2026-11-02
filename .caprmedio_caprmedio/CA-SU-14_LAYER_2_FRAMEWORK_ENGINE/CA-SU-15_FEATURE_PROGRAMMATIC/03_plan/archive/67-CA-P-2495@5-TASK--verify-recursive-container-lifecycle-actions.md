---
atom_id: CA-P-2495@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 67
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Domain/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2401
version: 5
updated_at: 2026-10-24 08:06:50 +0400
tier: 3
---
# Summary

Verify recursive container lifecycle Actions

## Objective

Independently accept Archive and target-Done recursion using disposable frozen Projects.

## Details

At most 15 minutes own work; split before extending. Depends on reviewed P2494 implementation. Use a small functional matrix: nested Archive including Done children, target-Done preserves Done descendants and cancels unfinished descendant Plans, exact old history bytes, external-reference exclusion, unsupported-model or occupied-destination refusal, and partial failure preserving earlier successes. Verify parent carrier relocation never silently carries a still-current child and no optional descendant mode exists. Bind receipts to frozen source and fixture hashes; do not use live Atoms or the production MCP port.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.

### Dependent acceptance review

P2497 planner, P2498/P2504 frozen fixture and P2500 pure seal are accepted; P2499/P2503 coordinator and P2501/P2505 entrypoints/status still require review before this gate activates. P2502 prepares tests independently but is not this final receipt. Freeze the complete production/fixture hash set before and after testing. Verify current frozen O127/O128/O129/O02915/15/12/10, exact original root authorization, no child container seal, distinct canonical per-member IDs, no fake root Source Run, same Initiative/action/actual lineage, original snapshot/model equality, and unknown descendant injection refusal after prior effects. Verify marked status distinguishes requested from actual IDs, partial/uncertain stops preserve observed effects, and dispatching-frontier reentry never replays. Include positive multi-level native Archive/Done cases before accepting mocked wiring evidence. No whole-Epic or installed-runtime claim; no production port, release, deployment, migration or held-batch replay.

### Current reviewed acceptance frontier

P2524Done@3 corrected only defaultfixturetemp underProjectTemporaryState; closure/guards/budgets unchanged. P2525Done@3/P2506Done@3 now provide native7pass67.783s, rootpartial1pass10.710s, adjacent36pass0.071s and finalindependentreviewAPPROVE, exactfunctionalhash634eed485a1cbeba0967d16cffea8372309e203e757666201c55f8eb0020dd27. Existing coordinator/provider/MCPwiring observed present; no speculative source rewrite. This is bounded acceptance, not this full gate. Remaining native cases: external-reference exclusion, unsupportedmodel/occupieddestination refusal, uncertainty/dispatching-frontier no-replay and failure with later untouchedmembers. Use actual uncertainty at admittedexecution/effectseams, never require completeJournal or infer failure solely from missingJournal. Freeze complete source/fixture set and review P2499/P2503/P2501 against this evidence before activation; productionport/release/replay still excluded.
