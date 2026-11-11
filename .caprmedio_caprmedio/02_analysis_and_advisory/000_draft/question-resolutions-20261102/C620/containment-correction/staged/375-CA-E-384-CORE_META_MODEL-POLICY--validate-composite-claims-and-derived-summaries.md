---
subjects:
  active: Atom.Content
  passive:
  - Atom
  - Atom/(.Role := Evaluation)
  - Entity/Object/Continuant/Governing Objects/Atom.Target Scope Unit
  - Atom.Content.Summary
  - Aspects <+ Engineering <+ Authoring <+ Controlled English
  - Scope Unit
version: 42
updated_at: 2026-11-02 18:35:20 +0400
relations:
  evaluation_for:
  - CA-R-1596
  - CA-R-1270
  - CA-R-1271
  - CA-R-2503
  - CA-R-2499
  - CA-R-1273
atom_id: CA-E-384
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Evaluation
form: Eval Policy
---
## Summary

Validate Composite Claims and Derived Summaries

## Claim scope

the Claim boundary, applicability, supporting Details, **and** Summary of an Atom.

## Claim

the Evaluation **must** reject an Atom **if** **any** applicable content-boundary condition fails:

- the Atom has **`!=1`** Claims, **`!=1`** resolved Claim Target Scope Units, an independently replaceable component inside **`=1`** Claim, ambiguous composite grouping, **or** a non-deterministic Scope Expression.
- RMED Scope is missing its applicability description, merely repeats the carried current **or** target Scope Unit, introduces a second independently replaceable Claim, **or** conflicts with the Claim. applicability **must** be explicit **in** Scope rather than maintained independently **in** Claim **or** Details.
- Details change, contradict, broaden, narrow, **or** add an independent contribution **to** the primary contribution within its applicability instead of expanding it under CA-R-2503-CORE_META_MODEL-DEFINITION--keep-details-within-the-primary-contribution.
- Summary is **not** source-faithful **to** the finalized primary contribution under CA-R-2499-CORE_META_MODEL-CORE-REQUIREMENT--define-summary-as-an-atom-property **and** CA-R-1273-CORE_META_MODEL-CORE-REQUIREMENT--keep-summary-source-faithful, including its applicability restrictions. for RMED, use the Claim read within Scope; a Summary of Scope alone fails. a Summary sourced from Analysis Results **or** TLDR instead of Question fails this check.

evaluate restrictions **to** selected sibling Scope Units under CA-E-461-CORE_META_MODEL-POLICY--warn-about-selected-sibling-claim-boundaries separately from these rejection criteria.
