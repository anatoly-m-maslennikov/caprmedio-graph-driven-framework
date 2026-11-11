---
atom_id: CA-A-1244
ref_id: CA-A-1244
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: Formal Model
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 15:49:28 +0400
carrier_destination:
  file:
    name: CA-A-1244-CAPRMEDIO-SPECIFICATION_PROPOSAL--limit-operative-formal-claims-to-requirements.md
    path: .caprmedio_caprmedio/02_analysis_and_advisory
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Limit operative formal Claims to Requirements

## Decision

For this iteration, only Requirement Atoms may carry the operative formal child content.claim.formal_claim{0..1}. R may use prose, the formal expression, or their complementary combination as its one Role/Type-defined Claim. Method, Evaluation and Delivery keep prose Claims; illustrative code or notation examples do not create an operative formal_claim property on them.

Every complete RMED Atom still has content.claim{1}, optional Claim scope, Semantics and Details. The chosen ### Formal claim heading maps to atom.content.claim.formal_claim, but it is admitted only for R for now. This limits Claim formalization, not which Roles can govern syntax, Formats or Relations. M/E/D still specify their applicable methods, checks and delivery contracts in prose.

## Scope and supersession

This narrows the formalization stage in P2683 and supersedes earlier Draft language admitting an operative formal child for every RMED Role. Methodology and direct project-local RMED layout/path migration stays in scope; only the R subset enters full/partial formalization. Engine migration, code, Tools, runtime and releases remain outside this Epic. The Current methodology is not changed by this review packet update.
