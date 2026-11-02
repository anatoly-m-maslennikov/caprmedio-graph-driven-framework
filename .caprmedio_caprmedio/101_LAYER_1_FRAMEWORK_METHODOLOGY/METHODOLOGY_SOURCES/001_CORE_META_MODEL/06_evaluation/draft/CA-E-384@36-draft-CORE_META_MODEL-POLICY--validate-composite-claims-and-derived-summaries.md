---
subjects:
  governs: Model::CAPRMEDIO::Continuant/Governing Objects/Atom.content
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Target Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Summary
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Controlled English
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
version: 36
updated_at: 2026-10-29 00:04:17 +0400
relations:
  evaluation_for:
  - CA-R-1596
  - CA-R-1270
  - CA-R-1271
  - CA-R-1624
  - CA-R-1465
  - CA-R-1273
atom_id: CA-E-384@36-draft
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
type: Policy
tier: 3
---
# Summary

Validate Composite Claims and Derived Summaries

## Claim scope

The primary-contribution boundary, applicability, support and Summary of an Atom.

## Claim

the Evaluation **must** reject an Atom **if** **any** applicable content-boundary condition fails:

- the Atom has **`!=1`** Claims, **`!=1`** resolved Claim Target Scope Units, an independently replaceable component inside **`=1`** Claim, ambiguous composite grouping, **or** a non-deterministic Scope Expression.
- a required RMED Claim scope is missing, merely repeats structural Scope Unit references, conflicts with the Claim, or supplies another independently replaceable Claim. Its absence passes only when the applicable full-coverage omission condition holds; an absent optional Semantics or Details section is not a failure.
- an RMED Atom has zero or more than one content.claim, carries a duplicate Claim in frontmatter atom.claim/formal_claim, or treats an example in Details as its operative Claim. The formal_claim child, when present, must contain one complete fenced expression conforming to its declared syntax; complementary prose may coexist in ## Claim without becoming another Claim.
- Details change, contradict, broaden, narrow, **or** add an independent contribution **to** the primary contribution within its applicability instead of expanding it under CA-R-1624-CORE_META_MODEL-DEFINITION--keep-details-within-the-primary-contribution.
- Summary is **not** source-faithful **to** the finalized primary contribution under CA-R-1465-CORE_META_MODEL-CORE-REQUIREMENT--define-summary-as-an-atom-property **and** CA-R-1273-CORE_META_MODEL-CORE-REQUIREMENT--keep-summary-source-faithful, including its applicability restrictions. for RMED, use the Claim read within any applicable Claim scope; a Summary of Scope alone fails. a Summary sourced from Analysis Results **or** TLDR instead of Question fails this check.

evaluate restrictions **to** selected sibling Scope Units under CA-E-461-CORE_META_MODEL-POLICY--warn-about-selected-sibling-claim-boundaries separately from these rejection criteria.

## Details

The existing non-RMED contribution checks and separate selected-sibling boundary evaluation remain applicable. Code fences mark declared formal representation; syntax/schema validation is still required. The exact RMED layout is CA-D-479.

The Claim unit is defined by its Role/Type. Formal and complementary prose parts of one Definition are not independent contributions merely because they occupy different representations. A completely empty Claim fails; an absent optional formal child does not.

R-only scope refinement (CA-A-1244): the optional ### Formal claim / content.claim.formal_claim is admitted only for Requirement Atoms for now. Method, Evaluation and Delivery have prose Claims with no operative formal child; code examples remain examples. Any earlier generic optional-formal wording in this Draft is limited by that Role condition. The complete one-Claim contract and optional supporting sections remain unchanged.
