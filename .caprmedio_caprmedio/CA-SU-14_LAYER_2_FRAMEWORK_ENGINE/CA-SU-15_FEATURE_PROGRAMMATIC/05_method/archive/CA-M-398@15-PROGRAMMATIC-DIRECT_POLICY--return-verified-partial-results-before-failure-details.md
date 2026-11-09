---
identity:
  atom_id: CA-M-398@15
  ref_id: CA-M-398@15
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Direct Policy
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
      Control/Outcome Reporting
  tier: 2
relations:
  child_of:
  - CA-M-405
state:
  status: Archived
  version: 15
  updated_at: 2026-11-09 07:45:14 +0400
destination:
  file:
    name: CA-M-398@15-PROGRAMMATIC-DIRECT_POLICY--return-verified-partial-results-before-failure-details.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method/archive
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---

## Summary

Return verified partial results before failure details

## Claim

### Prose Claim

When an operation has completed only part of the request, retain and present the verified completed results first, followed by the attributable errors and unfinished or uncertain work, without representing aggregate success.

## Details

### Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and their public operation boundaries.

1. At the operation owner, retain actual completed items and observed effects as work proceeds. A general exception wrapper cannot reconstruct lost local progress or decide business commit boundaries.
2. Return completed data together with errors in the same applicable response contract. Mark incompleteness or partial outcome explicitly and identify failed, skipped, unattempted and uncertain items where known. Do not discard useful verified data because another independent item failed.
3. Results-before-errors is presentation and consumption priority, not a demand for JSON member ordering or a new universal response schema. Preserve each transport's governed result contract while making both available.
4. Do not label an unverified, rolled-back or uncertain effect as completed, leak unsafe/private intermediate data, broaden an effect frontier, or weaken an explicitly atomic operation. If no verified result exists, state that honestly.
5. Do not introduce automatic retry, compensation or replay. Preserve actual recovery information and leave those actions with their declared owner.
