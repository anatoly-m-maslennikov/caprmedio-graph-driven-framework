---
atom_id: CA-P-2506@3
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2502
version: 3
updated_at: '2026-10-21T09:57:28Z'
---
# Summary

Bind functional assertions to actual Run evidence

## Objective

Remove unsupported lexical Run-ID assumptions without weakening real execution evidence checks.

## Details

At most 15 minutes own work; split before extending. Own the functional acceptance test only. E542@1 requires distinct actual Workflow/Step/Action invocation identities and actual lineage, not a run-prefix or inequality between requested and actual textual ID. Ordinary RunExecutionSession.start_run explicitly preserves the requested Workflow ID by default. Assert non-null actual identity only after canonical terminal/Journal proof, distinct members and technical coordinator exclusion; allow requested and actual labels to coincide after genuine observation. Keep real Archive/Done, byte-exact history, auth-tamper, mutation stop and duplicate-dispatch checks. Diagnose current before-effect admission failure separately; never change shared Run support merely to satisfy a test. At most15minutes own work.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.

### Dependency review after image-naming increment

Independent source review finds coordinator/member/provider/MCP wiring present; no speculative source rewrite. Fresh pure34checks pass, but the fresh native functional attempt was interrupted after90seconds during currentness scanning, not accepted. P2524 owns exact readiness diagnosis and frozen-fixture-only correction if justified; P2525 owns strengthened native member-lineage/partial-stop assertions. Final acceptance waits for both, independent review and root native rerun. Production remains unchanged; existing safety and evidence gates are not waived.

### Current reviewed acceptance frontier

P2525Done@3 accepted after native7/7 in67.783s, root finalpartial1/1 in10.710s and adjacent36/36. Actual Workflow/Step/Action Journal IDs, actualparents, definitions, exactdurablereceipts and Initiative/actionpropagation replace unsupported lexical actual/requested equality. Same-label requested/actual IDs remain allowed after genuineproof; no sharedRun support/productioncode change. Final frozen634eed... independentreviewAPPROVE. ParentP2502 and finalP2495matrix remain open; their remaining scope is not claimed here.
