---
atom_id: CA-A-1276
ref_id: CA-A-1276
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: Model
tier: 3
status: Done
version: 3
updated_at: 2026-11-02 15:49:28 +0400
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Separate Execution Result from API Result Contract

## Decision

Use Execution.Result for data actually produced by an execution, including returned values and a description of observed changes when provided. The API Result Contract describes the expected result format and meaning under Engineering/API. It is not the actual result.

A Journal Event Record can preserve an actual Execution.Result; the record remains distinct from the execution and its result. No universal recording requirement, exact result count, result datatype, standard response envelope or success status is introduced.

Replace the old Tool.Effect Result concept with this actual-result property, preserving useful effect-outcome meaning. Replace the proposal's undefined Outcome placeholder with Result rather than introducing a second competing field. No existing Engine property is renamed by this proposal update.

## State

New Definition Drafts and the proposal are prepared. R2204 replacement is tracked; Current source retirement and implementation remain pending.
