---
atom_id: CA-A-1289
ref_id: CA-A-1289
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: Model::CAPRMEDIO::Graph Syntax
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 15:49:28 +0400
carrier_destination:
  file:
    name: CA-A-1289-CAPRMEDIO-SPECIFICATION_PROPOSAL--prefer-verbose-and-explicit-model-notation-names.md
    path: .caprmedio_caprmedio/02_analysis
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Prefer verbose and explicit Model-notation names

## Decision

Use verbose, self-describing names and explicit structure in Model-notation and operation proposals. Optimize for making the meaning clear at the point of use rather than minimizing characters. Prefer execute_selection() over the tentative materialize() name because it states which operation is performed.

Name the intended operation and result clearly. Do not rely on an unexplained abbreviation or an implicit property projection to save characters. Existing accepted operators and names are not automatically renamed by this style decision; any concrete change belongs in its own proposal or Draft.

## State

The style applies to subsequent proposal writing. CA-A-1288 records the concrete Selection-execution name. This record does not promote the deferred function language or change Current methodology, tools or runtime.
