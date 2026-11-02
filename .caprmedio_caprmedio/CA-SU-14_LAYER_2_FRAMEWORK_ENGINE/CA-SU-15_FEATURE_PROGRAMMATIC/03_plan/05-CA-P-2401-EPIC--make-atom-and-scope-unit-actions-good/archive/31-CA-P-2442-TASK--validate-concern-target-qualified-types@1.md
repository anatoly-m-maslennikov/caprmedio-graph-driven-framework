---
atom_id: CA-P-2442
content_role: Plan
type: Plan
label: Task
work_sequence_number: 31
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
updated_at: "2026-10-20 17:00:00 +0400"
---
# Summary

Validate Concern target qualified Types

## Objective

Close the independent review's target-validity gap without inventing a parallel Type registry.

## Details

R1022 v17 admits only valid uniquely resolved Current Atoms. Reuse the existing source-bound schema qualified Role/Type check for Concern targets, with captured selected schema authority and any required target-specific lazy sources. Unknown or unresolved Types remain failures/gaps, not admitted merely because their Status inherits a generic Role model. Preserve ordinary RMED Type omission under R1700 and extension declaration uncertainty. Do not ban a literal Revision string or create new Type contributions. Use complete frozen schema sources in focused positive/negative tests, not mock validity. If an entire Content Role lacks an admitted Type schema, retain an explicit unsupported result and report that evidence limitation rather than guessing a type. No recursive relation or semantic validation is added.

At most15minutes ownwork; split before extending. Worker owns only the shared Concern target adapter/captured inputs and directly affected frozen tests. No Docker, production MCP, source policy, Journal gate or Git mutation.

### Definition of Done

Valid declared Role/Types and ordinary omitted Types pass; invalid/unresolved qualified Types do not pass; existing Current/identity/reference safeguards and focused regressions remain intact.
