---
atom_id: CA-P-2539@3
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2537
version: 3
updated_at: 2026-10-24 06:04:46 +0400
tier: 3
---
# Summary

Map the canonical Docker test network cleanup lifetime

## Objective

Resolve the observed isolated Docker network gate failure without affecting the working MCP.

## Details

Read-only source/caller/test mapping: fixture setUp/tearDown/addCleanup/finally; DockerRuntime down/stop; suite interruption and imageowner lifetime. Identify how networks persist on startupfailure,success,interruption. Propose smallest shared-owner repair preserving productionresourceboundaries. No writes/tests/Docker/MCP/release/Git. Return exactfiles/lines and evidence, not speculative broadcleanup.

### Actual result and next boundary

No current normal-path network leak is proven: ordinary, selected and first-cut HTTP fixtures already call scoped Compose down on teardown/finally, including partial startup. Existing production stop intentionally retains state and must remain unchanged. A forced child-process kill can bypass finally; a separate potential launcher no-container startup cleanup gap is recorded as C567 for reproduction, not patched speculatively. Old unattributed empty networks are not attributed to today's code.
