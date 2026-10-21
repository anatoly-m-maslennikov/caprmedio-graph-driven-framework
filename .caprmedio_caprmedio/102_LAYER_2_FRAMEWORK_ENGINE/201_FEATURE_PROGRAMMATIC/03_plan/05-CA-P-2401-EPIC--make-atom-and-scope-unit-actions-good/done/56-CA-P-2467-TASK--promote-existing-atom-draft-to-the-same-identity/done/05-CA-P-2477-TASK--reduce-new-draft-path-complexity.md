---
atom_id: CA-P-2477
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2467]
version: 3
updated_at: "2026-10-20T20:11:04.319Z"
---
# Summary

Reduce new Draft path complexity

## Objective

Reduce new configured Ruff C901 findings and avoid worsening touched legacy complexity through small cohesive extractions in the new Draft implementation paths.

## Details

At most 15 minutes own work; split before extending. Root compared the exact HEAD baseline: atom_operations had 8 C901 findings and lifecycle_intents 5. Current output has 17, including new restore/publish/rename/preflight complexity plus increased existing dispatch/update complexity. These are not all pre-existing baseline debt. Preserve every guard, rollback, byte pin, caller and test; no behavior change or broad legacy cleanup. Keep one behavioral owner and extract only coherent new responsibilities.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.

### Verified execution checkpoint

New complex-function findings were removed and configured C901 total decreased 17 to 12, below HEAD 13. No new C901 function identity remains, but _run_create increased 13 to 14 and update_atom_action 61 to 71. C546 remains Active and P2478 Backlog owns that retained follow-up. This Task remains Active rather than falsely claiming all touched complexity returned to baseline; correctness and functional acceptance are independently complete.

### Verified execution checkpoint

P2478 has now completed the retained dispatch/update complexity correction. No newly complex function remains and _run_create/update_atom_action are back to their original 13/61 scores. Final frozen independent acceptance passed 124/124: native promotion 8, semantic assessment 7, Draft promotion golden 22, Atom cohort 30, selected lifecycle 48 and version history 9. Every final receipt is a fresh run bound before/after to atom_operations SHA-256 4d25dae0e7efb8e6d36755902af1ae11178d18a982f54d6a926e7aa71d11d31e, lifecycle_intents 568516545c8bbd870d9022d157bcdb6382a394da46420458251cd341a7aff4ea and shared fixture 79925d47d09c43a524bab2cb0928460e0dad308b009029743a3db6059daf92be. Independent exact-diff review passed. P2488 repaired only the frozen D288/D378 materialization gap; exact HEAD reproduced the prior failure set. No production guard relaxation, live port, MCP effect, Docker, release, deployment, migration or held-batch replay. This closes this bounded source-quality Task, not all legacy lint/typing debt or installed runtime adoption.
