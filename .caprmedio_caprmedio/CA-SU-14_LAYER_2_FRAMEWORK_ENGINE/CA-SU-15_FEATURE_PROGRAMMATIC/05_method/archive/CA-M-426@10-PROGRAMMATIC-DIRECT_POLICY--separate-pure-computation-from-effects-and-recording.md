---
identity:
  atom_id: CA-M-426@10
  ref_id: CA-M-426@10
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Direct Policy
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component
      Structure
    dependencies:
    - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Effect
      Authorization
  tier: 3
state:
  status: Archived
  version: 10
  updated_at: 2026-11-09 00:09:26 +0400
destination:
  file:
    name: CA-M-426@10-PROGRAMMATIC-DIRECT_POLICY--separate-pure-computation-from-effects-and-recording.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method/archive
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
