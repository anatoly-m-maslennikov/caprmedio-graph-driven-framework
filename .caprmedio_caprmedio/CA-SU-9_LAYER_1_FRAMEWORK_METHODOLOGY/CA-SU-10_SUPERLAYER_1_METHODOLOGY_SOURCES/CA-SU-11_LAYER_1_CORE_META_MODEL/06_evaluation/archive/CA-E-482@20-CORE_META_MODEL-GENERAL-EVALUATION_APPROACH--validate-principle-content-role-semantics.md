---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom/Content Role
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Substance
  - 'Subject/Domain/Node/Continuant/Atom.Tier: 0 / Principle'
  - Subject/Domain/Node/Continuant/Atom.Tier
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Method'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations'
  - Implementation
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan/Type: Plan'
  - Subject/Domain/Node/Continuant/Actor
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Engineering/Carrier
version: 20
updated_at: 2026-10-24 00:38:25 +0400
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
atom_id: CA-E-482@20
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Policy
tier: 2
---
# Summary

Validate Principle Content-role semantics

## Scope

a Principle's Content Role classification.

## Claim

a Principle's Content Role classification **must** fail this Evaluation **if** its complete Claim's primary contribution does **not** match the applicable Content Role definition.

CAPO **and** I content **must not** acquire Principle through this classification merely from a role or type label. A Principle is numeric Tier `0` only when its complete Claim satisfies CA-R-2126 and its Project ownership is established; a Principle governing Actors, Plans, **or** Workflows remains specification **and** **must** be classified by its own RMED contribution. This Evaluation imposes no Content-Role or Type-to-Tier restriction.

## Details

### role distinctions

- Operations covers specific reusable Action, Workflow, **or** Actor participation/authorization behavior under CA-R-1530, **not** a Claim merely mentioning an Actor **or** Operation.
- Requirement covers model definitions, required properties, outcomes, obligations, permissions, prohibitions, **or** externally observable boundaries according **to** its primary model contribution.
- Delivery covers what a Carrier stores **and** how it represents **or** places that content.
- Method covers an authorship, construction, **or** Implementation choice **or** convention, **not** the authoritative operational Action **or** Workflow definition.
- Evaluation covers a falsifiable check, acceptance criterion, **or** disposition rule. its checked authority follows CA-R-1018 **and** is **not** limited **to** RMED Spec.
- intended Task **or** Objective content belongs **to** Plan, **not** Operations merely because its intended work involves an Actor.

the semantic test uses the complete Claim **and** does **not** require a literal wording template. the active Content Role definitions remain the authority for these distinctions; this Evaluation does **not** create a second classification system.

