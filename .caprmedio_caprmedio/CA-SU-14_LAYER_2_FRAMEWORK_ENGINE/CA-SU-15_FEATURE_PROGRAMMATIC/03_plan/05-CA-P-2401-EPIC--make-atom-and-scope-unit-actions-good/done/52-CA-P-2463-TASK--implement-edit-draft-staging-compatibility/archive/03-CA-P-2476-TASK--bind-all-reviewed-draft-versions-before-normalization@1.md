---
atom_id: CA-P-2476
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
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
  is_decomposition_of: [CA-P-2463]
version: 1
updated_at: "2026-10-20T18:46:25.899Z"
---
# Summary

Bind all reviewed Draft Versions before normalization

## Objective

Require carried YAML Version to equal the materialized canonical candidate/explicit Version binding for legacy and ID-free reviewed Subject Drafts, before normalization can erase a mismatch.

## Details

At most 15 minutes own work; split before extending. Independent P2466 review confirmed R866 requires Version-drift refusal for every Draft-backed promotion input. P2473 qualified-marker checks remain correct; extend the shared candidate boundary rather than duplicate normalization. Add legacy and ID-free repinned Version-drift regressions while retaining positive compatibility/no-op coverage.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.
