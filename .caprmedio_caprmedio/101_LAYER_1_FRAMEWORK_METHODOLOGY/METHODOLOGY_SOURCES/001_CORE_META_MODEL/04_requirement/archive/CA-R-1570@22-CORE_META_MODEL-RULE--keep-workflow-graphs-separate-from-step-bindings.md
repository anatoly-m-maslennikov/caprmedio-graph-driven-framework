---
subjects:
  active: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  passive:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
version: 22
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1570@22
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 2
role: Requirement
form: Rule
---
## Summary

Keep Workflow graphs separate from Step bindings

## Claim scope

Workflow graph schemes and Step bindings.

## Claim

a Workflow Atom **must** own **only** its graph scheme: Step references, declared order and structural Relations, entry points, **and** terminal outcomes. a Conditional Step definition owns its result-based routing; the Workflow graph does not use a separate result-transition Relation.

- the referenced Step Atoms own Action references, parameters, **and** input bindings.
- reusable Action Atoms own Action behavior.
- the graph **must not** independently repeat those Step bindings **or** Action definitions; folder nesting **and** file order **must not** replace its declared control flow.
