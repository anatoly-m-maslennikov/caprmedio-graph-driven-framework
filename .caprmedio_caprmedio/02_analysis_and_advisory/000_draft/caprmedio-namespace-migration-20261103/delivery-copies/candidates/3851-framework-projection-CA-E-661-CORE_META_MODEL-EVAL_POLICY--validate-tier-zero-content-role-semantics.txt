---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom.Role
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom.Content
  - CAPRMEDIO <+ MODEL <+ Atom.Tier
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan)
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Requirement)
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Method)
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Evaluation)
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Delivery)
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Operations)
  - CAPRMEDIO <+ MODEL <+ Package/Implementation
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan/Type: Plan'
  - CAPRMEDIO <+ MODEL <+ Actor
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role:=Operations)/Action
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role:=Operations)/Workflow
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - CAPRMEDIO <+ MODEL <+ Carrier
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations:
  evaluation_for:
  - CA-R-1531@20
  - CA-R-2511
  - CA-R-2512
  - CA-R-2513
  - CA-R-2514
  - CA-R-2515
  - CA-R-2463
  - CA-R-1018
atom_id: CA-E-661
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Evaluation
form: Eval Policy
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-661-CORE_META_MODEL-EVAL_POLICY--validate-tier-zero-content-role-semantics.md
  source_atom_id: CA-E-661
  source_atom_revision: 4
  source_sha256: 84066413047e0c4a0b6500198c6cc7bed0c2f2b1f4223c0a797c722f7e7ef909
  original_relations_sha256: 7eef9f5f282a619ccb53a135385f48bb199e24ae1368e6fdc99d1159cc5d18a5
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
