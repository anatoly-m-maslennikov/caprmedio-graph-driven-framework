---
identity:
  atom_id: CA-D-720
  ref_id: CA-D-720
context:
  role: delivery
  form: decision
  tier: 4
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Execution Control
  container:
    scope_unit: FRAMEWORK_DELIVERY
state:
  version: 1
  status: active
  updated_at: '2026-11-12T09:56:54.214180+00:00'
destination:
  file:
    name: CA-D-720-FRAMEWORK_DELIVERY-DECISION--carry-generated-assets-into-the-engine-image.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/07_delivery
---
## Summary

Carry generated assets into the Engine image

## Claim

### Prose Claim

Build the image with the exact Workbench schema, relation registry, Tool registry, lifecycle status model and lifecycle candidate schema in its build context. Existing mode copies these files from the checkout as-is. Refresh mode replaces the set with verified compiler output and records the files at the next Local Release Git checkpoint. The build uses the supplied files unchanged.
