---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Content.Claim
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement.Content.Claim'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Method.Content.Claim'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Evaluation.Content.Claim'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Delivery.Content.Claim'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Entity Definition'
version: 31
updated_at: 2026-10-29 09:46:50 +0400
relations: {}
atom_id: CA-R-1269@31
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Entity Definition
---
## Summary

Define Claim

## Claim scope

The Claims of Requirement, Method, Evaluation and Delivery Atoms.

## Claim

A Claim means one complete scoped primary contribution under its Atom's Content Role and Type, carried once as atom.content.claim. Every complete RMED Atom has content.claim{1}. The Type defines the Claim's unit and required internal structure; one Claim need not be one sentence, paragraph, code block or condition.

A complete RMED Claim has exactly one direct prose value, atom.content.claim[string]{1}. For R only, atom.content.claim.formal_claim[string]{0..1} independently permits zero or one formal child. The formal child does not replace or satisfy the required prose value. Both describe the same Type-defined contribution; nested content does not contribute to the parent cardinality. Formal and prose parts must agree and remain within that one Type-defined unit; unrelated definitions or contributions remain separate Atoms. A separate atom.claim, atom.formal_claim or content.claim.prose layer is not introduced.

Required prose belongs directly under ## Claim. For R only, the optional formal child belongs under ### Formal claim and contains one complete fenced expression in its declared syntax. Formal and natural-language forms each have the optional supporting properties content.claim_scope{0..1}, content.semantics{0..1} and content.details{0..1}; their values are counted independently and do not duplicate the Claim. Method, Evaluation and Delivery have prose Claims with no operative formal child.

### Formal claim

```text
Atom.Content.Claim[string]{1}
Atom/Content Role: Requirement.Content.Claim[string]{1}
Atom/Content Role: Method.Content.Claim[string]{1}
Atom/Content Role: Evaluation.Content.Claim[string]{1}
Atom/Content Role: Delivery.Content.Claim[string]{1}
Atom/Content Role: Requirement.Content.Claim.Formal Claim[string]{0..1}
Atom.Content.Claim Scope[string]{0..1}
Atom.Content.Semantics[string]{0..1}
Atom.Content.Details[string]{0..1}
```

## Semantics

A Requirement Claim states a required outcome; a Method Claim states how it is achieved; an Evaluation Claim states a check and its expected result; a Delivery Claim states delivery or representation. A Definition can define one model element using formal structure plus complementary prose without creating two Atoms. Semantics remains a separate optional explanation, not another operative part.

## Details

Operator decision recorded in CA-A-1241. This successor Draft replaces the earlier separate frontmatter Claim arrangement, including its Graph Rule exception; Current carriers and code remain unchanged.

R-only scope refinement (CA-A-1244): the optional ### Formal claim / content.claim.formal_claim is admitted only for Requirement Atoms for now. Method, Evaluation and Delivery have prose Claims with no operative formal child; code examples remain examples. Any earlier generic optional-formal wording in this Draft is limited by that Role condition. The complete one-Claim contract and optional supporting sections remain unchanged.
