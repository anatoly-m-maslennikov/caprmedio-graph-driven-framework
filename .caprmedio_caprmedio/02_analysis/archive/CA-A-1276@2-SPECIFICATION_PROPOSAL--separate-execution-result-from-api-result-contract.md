---
atom_id: CA-A-1276@2
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Model
version: 2
updated_at: 2026-10-29 21:51:04 +0400
relations: {}
tier: 3
---
# Summary

Separate Execution Result from API Result Contract

## Decision

Use Execution.Result for data actually produced by an execution, including returned values and a description of observed changes when provided. The API Result Contract describes the expected result format and meaning under Engineering/API. It is not the actual result.

A Journal Event Record can preserve an actual Execution.Result; the record remains distinct from the execution and its result. No universal recording requirement, exact result count, result datatype, standard response envelope or success status is introduced.

Replace the old Tool.Effect Result concept with this actual-result property, preserving useful effect-outcome meaning. Replace the proposal's undefined Outcome placeholder with Result rather than introducing a second competing field. No existing Engine property is renamed by this proposal update.

## State

New Definition Drafts and the proposal are prepared. R2204 replacement is tracked; Current source retirement and implementation remain pending.
