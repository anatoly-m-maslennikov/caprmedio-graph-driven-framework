---
identity:
  atom_id: CA-E-826
  ref_id: CA-E-826
context:
  role: evaluation
  form: eval_case
  tier: 5
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality
      <+ Verification <+ Dynamic Testing
  container:
    scope_unit: MCP
relations:
  evaluation_for:
  - CA-R-1105
state:
  version: 4
  status: active
  updated_at: '2026-11-12T16:59:54.242192+00:00'
destination:
  file:
    name: CA-E-826-MCP-EVAL_CASE--measure-live-atom-lifecycle-tools.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation
---
## Summary

Measure live Atom Lifecycle Tools

## Claim

### Prose Claim

Measure each of the six live MCP Atom Lifecycle Tools from request to response on twenty randomized Atoms in one temporary Scope Unit. Verify the effects through Workbench. Record the running image, individual durations, median, maximum, and cleanup.

## Details

Include same-ID and replacement Update. Check that Create Draft without a source Version copies Current and an explicit Version copies exactly that revision. Check that fields absent from the request are preserved. Include distinct padded and unpadded decimal Atom IDs and verify selection preserves the exact spelling. Check independent Archive and Promote Draft batches for result order, stopping on the first failure, and accurate completed and remaining targets. Confirm grouped publication with no missing changed rows.

Check that a Current Epic can change from Backlog to Active with a Draft child. Verify that direct and nested Current Tasks become Active and the Draft child stays a Draft. Run a content-only Update of an Epic with children and verify that the children’s content and Status are unchanged.

Check independent copying separately. Copy a Current Atom, an Archived revision and a Draft through Create Draft. Verify that each copy starts at Version 1 with a new ID, preserves fields and Relations not supplied in the request, including inherited IS_REPLACEMENT_FOR, and leaves the source unchanged. Promoting the copy must leave the source in place.
