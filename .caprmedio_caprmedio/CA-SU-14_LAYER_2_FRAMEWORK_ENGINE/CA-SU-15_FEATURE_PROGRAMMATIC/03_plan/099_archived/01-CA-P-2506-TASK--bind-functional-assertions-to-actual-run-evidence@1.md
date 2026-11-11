---
atom_id: CA-P-2506
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2502]
version: 1
updated_at: "2026-10-20T22:00:48.809Z"
---
# Summary

Bind functional assertions to actual Run evidence

## Objective

Remove unsupported lexical Run-ID assumptions without weakening real execution evidence checks.

## Details

At most 15 minutes own work; split before extending. Own the functional acceptance test only. E542@1 requires distinct actual Workflow/Step/Action invocation identities and actual lineage, not a run-prefix or inequality between requested and actual textual ID. Ordinary RunExecutionSession.start_run explicitly preserves the requested Workflow ID by default. Assert non-null actual identity only after canonical terminal/Journal proof, distinct members and technical coordinator exclusion; allow requested and actual labels to coincide after genuine observation. Keep real Archive/Done, byte-exact history, auth-tamper, mutation stop and duplicate-dispatch checks. Diagnose current before-effect admission failure separately; never change shared Run support merely to satisfy a test. At most15minutes own work.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.
