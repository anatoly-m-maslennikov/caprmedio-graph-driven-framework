---
identity:
  atom_id: CA-P-3048
  ref_id: CA-P-3048
context:
  role: plan
  form: Plan
  label: Epic
  tier: 3
  container:
    scope_unit: CA-SU-14
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//PROGRAMMATIC
state:
  version: 1
  status: active
  updated_at: '2026-11-13T15:12:55.531245+00:00'
destination:
  file:
    name: CA-P-3048-EPIC--establish-the-programmatic-model.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan
---
## Summary

Establish the Programmatic Model

## Objective

Establish the MODEL Scope Unit directly under PROGRAMMATIC. It contains FORMAL_MODEL_ENGINE and GENERATED_MODEL. This Epic ends at the generated Model package. Adopting that package in Tools and Apps is separate work.

## Work

1. Update the Scope Unit Declarations and Delegations. Move FORMAL_MODEL_ENGINE under MODEL with its existing ID.
2. Review the RMEDO against the Model and Project Structure Projection specifications.
3. Compare the reviewed RMEDO with the current implementation.
4. Discuss what can be removed and what needs to remain before changing implementation.

## References

Scope Unit Atoms: CA-R-2654, CA-R-3090, CA-R-3091, CA-R-3133, CA-R-3134, CA-R-3135, CA-R-3136.

CA-P-3022 tracks CFEL retirement. The Model Declaration and error specifications are CA-R-2721, CA-R-3081, CA-R-3082, CA-R-3131, and CA-R-3137.
