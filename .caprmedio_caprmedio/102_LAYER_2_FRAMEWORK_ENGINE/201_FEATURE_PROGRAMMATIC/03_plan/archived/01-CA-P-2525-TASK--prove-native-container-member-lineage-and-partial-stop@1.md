---
atom_id: CA-P-2525
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
  is_decomposition_of: [CA-P-2506]
version: 1
updated_at: "2026-10-21T09:38:06Z"
---
# Summary

Prove native container member lineage and partial stop

## Objective

Prove native container member lineage and partial stop.

## Details

At most15minutes own work; split before extending. Own tests/test_container_lifecycle_functional.py only. Prepare independently of P2524 but final native execution waits for fixture readiness. Use existing checked-in frozen inputs and disposable Project; assert durable per-member one-target receipt/frontier/effects excludes container seal, actual Workflow/Step/Action identities and parent lineage with unchanged Initiative/action IDs; technical coordinator is not a fake Workflow Run. Add a native failure/mutation after first successful member to prove preserved exact history/effects, untouched remainder/parent, fresh rebind and no automatic replay. Retain all existing Archive/Done/auth/source-drift/duplicate checks. Do not alter source logic/guards or infer success from Journal alone; test controlled seam cannot replace native admission/effects. Missing other refusal/uncertainty cases remain explicit for P2495. Final native acceptance waits for P2524 and root review; no production MCP/Docker/release.
