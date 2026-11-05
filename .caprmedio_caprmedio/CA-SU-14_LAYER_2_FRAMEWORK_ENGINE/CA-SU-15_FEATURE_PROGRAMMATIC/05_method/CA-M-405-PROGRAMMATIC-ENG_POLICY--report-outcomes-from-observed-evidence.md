---
atom_id: CA-M-405
ref_id: CA-M-405@10-draft
role: Method
form: Eng Policy
current_scope_unit: PROGRAMMATIC
status: Active
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Output Publication
version: 10
updated_at: 2026-11-05 23:05:59 +0400
author: Anatoly Maslennikov
tier: 1
container:
  scope_unit: CA-SU-15
carrier_destination:
  file:
    name: CA-M-405-PROGRAMMATIC-ENG_POLICY--report-outcomes-from-observed-evidence.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method
---
# Summary

Report outcomes from observed evidence

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and tests.

## Claim

**To** execute PROGRAMMATIC behavior and report its outcome, compare the requested result with observed effects and retained execution evidence, distinguish verified completion, verified no-op, partial effects and uncertain effects, and reuse established evidence rather than blindly replaying completed or uncertain mutations.

Resume is allowed only where the existing lifecycle or operation contract already admits it. Before a dependent step, preserve successful partial steps; on resume, read the actual observed state and continue from it without overwriting or replaying completed work. This policy does not require new receipts, retry or recovery machinery for every operation.

## Details

Candidate source: [CA-M-390@2](archive/CA-M-390-PROGRAMMATIC-CORE--report-outcomes-from-observed-evidence@2.md)

- A returned call, scheduler completion or absence of reported errors does not alone establish the requested result.
- A no-op means the requested state was already satisfied and remained unchanged; do not fabricate writes or history.
- Preserve partial results, uncertainty, gaps and blockers honestly. Outcome reporting introduces no automatic retry or recovery policy. Do not infer that a resume is admitted from ordinary error text; use the existing lifecycle state and contract. When resume is admitted, retain successful partial work and do not replay completed steps.

Source basis: CA-M-376, CA-M-323, CA-M-322.
