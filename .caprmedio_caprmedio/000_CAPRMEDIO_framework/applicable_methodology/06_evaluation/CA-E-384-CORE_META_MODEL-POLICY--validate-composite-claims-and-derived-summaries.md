---
atom_id: CA-E-384
ref_id: CA-E-384
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Policy
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Content
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Atom.Target Scope Unit
  - CAPRMEDIO_MODEL <+ Atom.Content.Summary
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Authoring <+ Controlled English
  - CAPRMEDIO_MODEL <+ Scope Unit
tier: 3
relations:
  evaluation_for:
  - CA-R-1596
  - CA-R-1270
  - CA-R-1271
  - CA-R-2503
  - CA-R-2499
  - CA-R-1273
status: Active
version: 42
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-E-384-CORE_META_MODEL-EVAL_POLICY--validate-composite-claims-and-derived-summaries.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-384-CORE_META_MODEL-POLICY--validate-composite-claims-and-derived-summaries.md
  source_atom_id: CA-E-384
  source_atom_revision: 42
  source_sha256: ecfe3f2e813c08014ba87bfa97d73658742fab6342c735f7becbebd7ccac1688
  original_relations_sha256: 683edb070640fcebfd5b6aafbc8687ede3548fd2b5d1cd90dcd386920c548780
---
## Summary

Validate Composite Claims and Derived Summaries

## Claim

### Prose Claim


the Claim boundary, applicability, supporting Details, **and** Summary of an Atom.


the Evaluation **must** reject an Atom **if** **any** applicable content-boundary condition fails:

- the Atom has **`!=1`** Claims, **`!=1`** resolved Claim Target Scope Units, an independently replaceable component inside **`=1`** Claim, ambiguous composite grouping, **or** a non-deterministic Scope Expression.
- RMED Scope is missing its applicability description, merely repeats the carried current **or** target Scope Unit, introduces a second independently replaceable Claim, **or** conflicts with the Claim. applicability **must** be explicit **in** Scope rather than maintained independently **in** Claim **or** Details.
- Details change, contradict, broaden, narrow, **or** add an independent contribution **to** the primary contribution within its applicability instead of expanding it under CA-R-2503-CORE_META_MODEL-DEFINITION--keep-details-within-the-primary-contribution.
- Summary is **not** source-faithful **to** the finalized primary contribution under CA-R-2499-CORE_META_MODEL-CORE-REQUIREMENT--define-summary-as-an-atom-property **and** CA-R-1273-CORE_META_MODEL-CORE-REQUIREMENT--keep-summary-source-faithful, including its applicability restrictions. for RMED, use the Claim read within Scope; a Summary of Scope alone fails. a Summary sourced from Analysis Results **or** TLDR instead of Question fails this check.

evaluate restrictions **to** selected sibling Scope Units under CA-E-461-CORE_META_MODEL-POLICY--warn-about-selected-sibling-claim-boundaries separately from these rejection criteria.
