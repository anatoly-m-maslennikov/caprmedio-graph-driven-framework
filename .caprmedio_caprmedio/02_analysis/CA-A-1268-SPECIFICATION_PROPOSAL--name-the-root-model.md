---
atom_id: CA-A-1268
ref_id: CA-A-1268
role: Analysis & Advisory
form: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
topics:
  main_subject: Model
version: 2
updated_at: 2026-11-02 15:49:28 +0400
tier: 3
container:
  scope_unit: CA-SU-00
carrier_destination:
  file:
    name: CA-A-1268-CAPRMEDIO-SPECIFICATION_PROPOSAL--name-the-root-model.md
    path: .caprmedio_caprmedio/02_analysis
---
# Summary

Name the root Model

## Decision

The root is Model, not Formal Model. Rename the root label and proposed canonical selectors from Formal Model::... to Model::..., preserving their structure and meaning. The storage fields subjects.governs and subjects.depends_on retain their names. The existing Subject definition is not silently turned into the new Model definition. Historical proposal records and the completed FPF report retain their recorded wording.

## State

Proposal and prepared Draft updates only. Current methodology, governing configuration, historical reports and implementation are unchanged.
