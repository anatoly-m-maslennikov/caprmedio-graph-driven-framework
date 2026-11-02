---
atom_id: CA-P-2531
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2527]
version: 1
updated_at: "2026-10-21T10:42:00Z"
---
# Summary

Retire eligible stopped noncandidate Project containers

## Objective

Implement the accepted Project-only candidate-retention contract.

## Details

Own release_cleanup.py and test_release_cleanup.py only, including its shared DockerFixture. Remove only positively identified stopped selected-Project MCP containers using noncandidate images, even with matching fingerprint; exact candidate and other running containers remain protected. Inspect positive runtime classification before removal; no force/retry. Give fixture-created owned images explicit ownership metadata, not arbitrary inserted orphans. Synthetic tests only, at most15 minutes own work; split before extending.
