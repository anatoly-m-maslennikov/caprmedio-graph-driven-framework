---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom/Content Role
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom.Content
  - Entity/Object/Continuant/Governing Objects/Atom.Tier
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Method'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Evaluation'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Delivery'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations'
  - Entity/Object/Continuant/Package/Project Implementation
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan/Type: Plan'
  - Entity/Object/Continuant/Actor
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - Entity/Carrier
version: 1
updated_at: 2026-10-29 22:26:56 +0400
relations:
  evaluation_for:
  - CA-R-1531
  - CA-R-1338
  - CA-R-1339
  - CA-R-1340
  - CA-R-1341
  - CA-R-1342
  - CA-R-1530
  - CA-R-1018
atom_id: CA-E-661@1
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Eval Policy
tier: 2
---
## Summary

Validate Tier Zero Content-role semantics

## Claim scope

a Tier 0 Atom’s Content Role classification.

## Claim

a Tier 0 Atom’s Content Role classification **must** fail this Evaluation **if** its complete Claim's primary contribution does **not** match the applicable Content Role definition.

Numeric Tier `0` is a local Scope Unit foundation and its readable Tier Label is Scope Contract; that label alone does not change an Atom’s Content Role or Type. Its complete primary contribution must satisfy its own Content Role definition. Operations retains its existing Action, Workflow and Step Types where applicable. This Evaluation introduces no Content-Role or Type-to-Tier restriction and does not require all Content Roles in a unit.

## Details

### role distinctions

- Operations covers specific reusable Action behavior, Workflow graph, **or** Step invocation binding, **not** a Claim merely mentioning an Actor **or** Operation.
- Requirement covers model definitions, required properties, outcomes, obligations, permissions, prohibitions, **or** externally observable boundaries according **to** its primary model contribution.
- Delivery covers what a Carrier stores **and** how it represents **or** places that content.
- Method covers an authorship, construction, **or** Implementation choice **or** convention, **not** the authoritative operational Action **or** Workflow definition.
- Evaluation covers a falsifiable check, acceptance criterion, **or** disposition rule. its checked authority follows CA-R-1018 **and** is **not** limited **to** RMED Spec.
- intended Task **or** Objective content belongs **to** Plan, **not** Operations merely because its intended work involves an Actor.

the semantic test uses the complete Claim **and** does **not** require a literal wording template. the active Content Role definitions remain the authority for these distinctions; this Evaluation does **not** create a second classification system.
