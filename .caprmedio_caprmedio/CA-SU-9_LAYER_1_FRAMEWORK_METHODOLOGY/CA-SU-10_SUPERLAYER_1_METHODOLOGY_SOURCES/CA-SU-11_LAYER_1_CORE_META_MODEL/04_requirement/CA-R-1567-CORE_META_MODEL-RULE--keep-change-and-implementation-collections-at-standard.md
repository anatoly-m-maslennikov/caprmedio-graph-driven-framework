---
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
  passive:
  - CAPRMEDIO_MODEL <+ Projection
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Package/Project Implementation
  - CAPRMEDIO_MODEL <+ Atom.Tier
  - 'CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  - 'CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan/Type: Plan'
version: 25
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1567
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary

Keep Change and Implementation collections at Standard

## Claim scope

Atom Collections and decomposition views grouping CAPO or I content.

## Claim

an Atom Collection **or** decomposition view grouping CAPO **or** I content **must** remain a derived grouping and **must not** acquire an Atom Tier or imply a Tier from its grouped Content Roles or Types. When a view displays a source Atom, it preserves that source Atom's numeric Tier; the grouping itself has no independent Tier.

nesting expresses composition, **not** Core **or** General authority; a Plan Directory Carrier remains a Carrier of its existing Atom under CA-D-460-CORE_META_MODEL-ENG_DECISION--serialize-plan-atom-carrier-bundles, **not** an independently tiered collection **or** second Atom.
