---
atom_id: CA-R-2110@7-draft
ref_id: CA-R-2110@7-draft
role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
topics:
  main_subject: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Definition'
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
form: Definition
version: 7
updated_at: 2026-10-29 05:35:13 +0400
tier: 1
container:
  scope_unit: CA-SU-11
---
## Summary

Define Atom/Content Role: Requirement/Type: Definition

## Claim scope

The Definition Requirement Type and its use for Model definitions.

## Claim

A Definition has exactly one direct prose Claim that defines its scoped model contribution. It may add one Formal claim child whose value is counted independently; that child cannot replace the required prose. Semantics and Details remain explanatory and introduce no additional operative Claim.

### Formal claim

```yaml
Definition:
  content.claim:
    count: 1
    unit: content_role_and_type_defined
    own_text: prose
    formal_claim:
      minimum: 0
      maximum: 1
      representation: one_fenced_formal_expression
    substantive_content: prose_required
    child_values_count_toward_parent: false
  content.claim_scope:
    minimum: 0
    maximum: 1
  content.semantics:
    minimum: 0
    maximum: 1
    role: meaning_explanation
    operative: false
  content.details:
    minimum: 0
    maximum: 1
    role: support
    operative: false
  model_constraints:
    location: content.claim
    separate_graph_rule_instances: false
```

## Semantics

A Definition describes what is being modeled, including the formal structure and its valid constraints. For Model definitions, the required prose and any complementary formal expression form one operative definition in content.claim. A complete definition is one Type-defined Claim, not one Atom per representation, field or condition. Semantics explains its meaning; it is not a second Claim or another place to add constraints. Structure and constraints therefore belong to the same model rather than placing constraints in a separate population of Graph Rule instances.

## Details

This successor Draft records CA-A-1242. It supersedes the proposal to keep a special Graph Rule Atom Type for these definitions; ordinary Rule is not substituted. Other RMED Claims retain the unified content.claim contract under CA-A-1241. Current sources and consumers remain unchanged.

## Preparation status

Superseded — do not promote. A1302 renames the Type to Entity Definition and reserves Term Definition separately. Use the new generic Entity Definition Type Draft; retain this old Type/Summary and Model-specific preparation as history.
