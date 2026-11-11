---
atom_id: CA-M-426
ref_id: CA-M-426@9
container:
  scope_unit: CA-SU-15
role: Method
form: Eng Policy
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component
    Structure
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization
tier: 3
status: Archived
version: 9
updated_at: 2026-10-27 19:59:43 +0400
carrier_destination:
  file:
    name: CA-M-426@9-PROGRAMMATIC-ENG_POLICY--separate-pure-computation-from-effects-and-recording.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method/archived
current_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Separate pure computation from effects and recording

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and tests.

## Claim

**To** construct a result, keep pure computation independent of persistence and Run or Journal writes, leaving those effects with their declared execution owners.

## Details

Candidate source: [CA-M-392@2](archive/CA-M-392-PROGRAMMATIC-CORE--separate-pure-computation-from-effects-and-recording@2.md)

- Construct from bound inputs and return results and diagnostics without hidden writes.
- Persist an output only through its applicable authorized effect boundary.
- Actual execution recording remains with its declared executor; generated output alone does not establish durable terminal completion.

Source basis: CA-M-330, CA-M-259.
