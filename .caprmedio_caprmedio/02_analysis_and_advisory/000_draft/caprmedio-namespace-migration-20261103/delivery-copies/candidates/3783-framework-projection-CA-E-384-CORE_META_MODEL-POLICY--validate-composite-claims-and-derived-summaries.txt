---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom.Content
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Evaluation)
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Target Scope Unit
  - CAPRMEDIO <+ MODEL <+ Atom.Content.Summary
  - CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Authoring <+ Controlled English
  - CAPRMEDIO <+ MODEL <+ Scope Unit
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
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-384-CORE_META_MODEL-POLICY--validate-composite-claims-and-derived-summaries.md
  source_atom_id: CA-E-384
  source_atom_revision: 42
  source_sha256: e3626328a0d2157b641d5dde2793ae07bdbc39876991bad7f10f0c199a918ad0
  original_relations_sha256: 683edb070640fcebfd5b6aafbc8687ede3548fd2b5d1cd90dcd386920c548780
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
