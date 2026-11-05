---
atom_id: CA-A-1269
ref_id: CA-A-1269
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: Model
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 15:49:28 +0400
carrier_destination:
  file:
    name: CA-A-1269-CAPRMEDIO-SPECIFICATION_PROPOSAL--specialize-packages-for-runtime-and-tests.md
    path: .caprmedio_caprmedio/02_analysis
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Specialize Packages for runtime and tests

## Decision

Package has Runtime Package and Test Package specializations. Project Implementation remains the root Package specialization. The common structure remains recursive Package containment, Module containing Code Unit (Class/Function), Asset File, Prompt and Documentation. These Package specializations describe use; they add no new Module or Asset File Types, no mandatory usage property and no rule making the listed specializations a closed catalog.

## State

Proposal and prepared Draft updates only. Current methodology, governing configuration, historical reports and implementation are unchanged.
