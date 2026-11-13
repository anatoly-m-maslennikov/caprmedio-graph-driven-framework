---
identity:
  atom_id: CA-E-827
  ref_id: CA-E-827
context:
  role: evaluation
  form: Eval Case
  tier: 3
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Atom
  container:
    scope_unit: FRAMEWORK_ENGINE
state:
  version: 1
  status: active
  updated_at: '2026-11-12T12:56:24.915112+00:00'
destination:
  file:
    name: CA-E-827-FRAMEWORK_ENGINE-EVAL_CASE--allocate-normal-atom-ids-with-large-probe-ids-present.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/06_evaluation
---
## Summary

Allocate normal Atom IDs with large probe IDs present

## Claim

### Prose Claim

Verify that new Drafts receive the next in-range ID through both indexed and direct allocation. Include a high-numbered probe, an ordinary Current Atom and an ordinary Archived carrier with leading zeros. The archived number still reserves its place when its body is unloaded. Confirm that the high ID remains selectable by its exact reference and that allocation fails before creating a file when the configured range is exhausted.
