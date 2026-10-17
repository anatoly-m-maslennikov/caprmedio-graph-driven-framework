---
subjects:
  governs: "Atom/Content Role"
  depends_on:
    ["Entity/Continuant/Object/Atom.Substance", "Entity/Continuant/Object/Atom.Local Tier: Principle", "Entity/Continuant/Object/Atom/Content Role: Plan", "Entity/Continuant/Object/Atom/Content Role: Requirement", "Entity/Continuant/Object/Atom/Content Role: Method", "Entity/Continuant/Object/Atom/Content Role: Evaluation", "Entity/Continuant/Object/Atom/Content Role: Delivery", "Entity/Continuant/Object/Atom/Content Role: Operations", "Implementation", "Atom/Content Role: Plan/Type: Plan", "Entity/Continuant/Actor", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Workflow", "Artifact Carrier"]
version: 13
updated_at: "2026-10-15 18:49:44 +0000"
relations:
  evaluation_for:
    - CA-R-1531
    - CA-R-1338
    - CA-R-1339
    - CA-R-1340
    - CA-R-1341
    - CA-R-1342
    - CA-R-1530
    - CA-R-1566
    - CA-R-1018
atom_id: "CA-E-482"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/06_evaluation/CA-E-482-CORE_META_MODEL-GENERAL-EVALUATION_APPROACH--validate-principle-content-role-semantics.md
  source_atom_id: CA-E-482
  source_atom_revision: 13
  source_sha256: 1b54dfeed4e9ddaef91fff58cf2b76f63efb15e4779c1e23f2fa393de64f40c8
  original_relations_sha256: d63238eff976077a998317d0a36e32fdc3e09e703d6f3a9cee15c60755964d5c
---
# Summary

Validate Principle Content-role semantics

## Scope

a Principle's Content Role classification.

## Claim

a Principle's Content Role classification **must** fail this Evaluation **if** its complete Claim's primary contribution does **not** match the applicable Content Role definition.

CAPO **and** I content **must not** acquire Principle through this classification: CA-R-1566 fixes those Atoms at Standard. a Principle governing Actors, Plans, **or** Workflows remains specification **and** **must** be classified by its own RMED contribution.

## Details

### role distinctions

- Operations covers specific reusable Action, Workflow, **or** Actor participation/authorization behavior under CA-R-1530, **not** a Claim merely mentioning an Actor **or** Operation.
- Requirement covers model definitions, required properties, outcomes, obligations, permissions, prohibitions, **or** externally observable boundaries according **to** its primary model contribution.
- Delivery covers what a Carrier stores **and** how it represents **or** places that content.
- Method covers an authorship, construction, **or** Implementation choice **or** convention, **not** the authoritative operational Action **or** Workflow definition.
- Evaluation covers a falsifiable check, acceptance criterion, **or** disposition rule. its checked authority follows CA-R-1018 **and** is **not** limited **to** RMED Spec.
- intended Task **or** Objective content belongs **to** Plan, **not** Operations merely because its intended work involves an Actor.

the semantic test uses the complete Claim **and** does **not** require a literal wording template. the active Content Role definitions remain the authority for these distinctions; this Evaluation does **not** create a second classification system.
