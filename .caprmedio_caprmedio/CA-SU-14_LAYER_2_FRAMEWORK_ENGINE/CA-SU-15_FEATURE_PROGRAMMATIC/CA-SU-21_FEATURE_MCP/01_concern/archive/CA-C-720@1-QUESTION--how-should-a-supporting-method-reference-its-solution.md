---
identity:
  id: CA-C-720
  ref_id: CA-C-720@1
context:
  container:
    scope_unit: CA-SU-21
  role: Concern
  form: Question
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
state:
  status: Archived
  version: 1
  updated_at: 2026-11-10 04:16:47 +0400
destination:
  file:
    name: CA-C-720@1-QUESTION--how-should-a-supporting-method-reference-its-solution.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/01_concern/archive
relations:
  concern_about:
  - CA-M-167
  - CA-R-1105
  - CA-R-1017
---

## Summary

How should a supporting Method reference its Solution?

## Concern

M519 replaces the internal R1105 contract as a Method/Solution. Current M167 is a distinct one-request delegation Method and currently has method_for R1105. R1017 defines method_for from Method to Requirement, so that relation cannot simply target the new Method.

## Details

Keep the distinct claims; the scoped DRY review found that merging would require a broad umbrella Summary. Choose a model-admitted support or reference relation, or remove an unnecessary link after checking governing coverage. Do not invent a relation, revive R1105 as a false Requirement, or alter Core in this Engine pass. Current M167 and R1105 remain unchanged pending adoption.
