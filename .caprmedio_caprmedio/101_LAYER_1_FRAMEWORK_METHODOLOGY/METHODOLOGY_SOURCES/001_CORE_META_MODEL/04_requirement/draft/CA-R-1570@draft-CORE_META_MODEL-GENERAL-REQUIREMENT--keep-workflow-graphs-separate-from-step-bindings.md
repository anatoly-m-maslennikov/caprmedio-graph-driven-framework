---
subjects:
  governs: "Workflow"
  depends_on:
    ["Step", "Action", "Atom/Content Role: Operations/Type: Workflow", "Atom/Content Role: Operations/Type: Step", "Relation/Type: On Result"]
version: 5
updated_at: "2026-10-15 12:13:34 +0000"
relations: {"relates_to": ["CA-R-1508", "CA-R-1509", "CA-R-1513", "CA-R-1563", "CA-R-1569"]}
atom_id: "CA-R-1570@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Keep Workflow graphs separate from Step bindings

## Scope

Workflow graph schemes and Step bindings.

## Claim

a Workflow Atom **must** own **only** its graph scheme: Step references, typed directed Relations, entry points, transition conditions, **and** terminal outcomes.

- the referenced Step Atoms own Action references, parameters, **and** input bindings.
- reusable Action Atoms own Action behavior.
- the graph **must not** independently repeat those Step bindings **or** Action definitions; folder nesting **and** file order **must not** replace its declared control flow.

## Details
