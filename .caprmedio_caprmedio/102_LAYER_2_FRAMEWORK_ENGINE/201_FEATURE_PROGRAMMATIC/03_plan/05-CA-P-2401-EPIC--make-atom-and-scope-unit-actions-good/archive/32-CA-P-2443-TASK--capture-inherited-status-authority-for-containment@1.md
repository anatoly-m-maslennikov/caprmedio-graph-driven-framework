---
atom_id: CA-P-2443
content_role: Plan
type: Plan
label: Task
work_sequence_number: 32
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
  is_decomposition_of: [CA-P-2401]
version: 1
updated_at: "2026-10-20 17:02:00 +0400"
---
# Summary

Capture inherited Status authority for containment

## Objective

Repair the default reference/containment Status binding path exposed by the complete frozen suite.

## Details

Twenty independent Plan prerequisite tests fail because contained_atom_targets._bindings calls _frontier_status_folders without a captured Status index. That fallback parses only finite role declarations and omits the Atom.Status base now required by inherited R1539. Reuse canonical capture_status_models and its selected reader/currentness boundary when no index is supplied; do not relax inheritance or add guessed Status values. Repair the directly affected frozen fixture dependencies and the whitelist test's explicit graph-vs-legacy source selection. Keep deliberate legacy sources intact. No live Atom corpus in tests or new strict digest gate. At most15minutes ownwork; split before extending. No production MCP, Docker or Git mutation.

### Definition of Done

Default contained/reference bindings resolve inherited models from one captured base; missing/ambiguous bases remain refused, affected frozen modules pass, and final full suite is rerun before imagefreeze.
