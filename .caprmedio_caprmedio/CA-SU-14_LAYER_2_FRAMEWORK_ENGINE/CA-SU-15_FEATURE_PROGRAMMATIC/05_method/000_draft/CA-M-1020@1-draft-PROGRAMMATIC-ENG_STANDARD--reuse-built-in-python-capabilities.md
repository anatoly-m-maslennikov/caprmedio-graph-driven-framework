---
identity:
  atom_id: CA-M-1020
  ref_id: CA-M-1020@1-draft
context:
  role: method
  form: Eng Standard
  tier: 3
  container:
    scope_unit: CA-SU-15
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Authoring <+ Code Authoring <+ Python Code
state:
  version: 1
  status: draft
  updated_at: '2026-11-13T16:30:09.035081+00:00'
destination:
  file:
    name: CA-M-1020@1-draft-PROGRAMMATIC-ENG_STANDARD--reuse-built-in-python-capabilities.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method/000_draft
---
## Summary

Reuse built-in Python capabilities

## Claim

### Prose Claim

Use built-in Python capabilities and the standard library when they satisfy the applicable requirements. Reuse an existing Project dependency when it covers a gap in the standard library.

For the Model build and validation:

- Use `dataclasses` and ordinary class inheritance for Model classes and fields.
- Use `graphlib.TopologicalSorter` to order class definitions and detect inheritance cycles. Verify that each referenced parent is declared.
- Use `ast.parse()` to inspect Python Formal Claims and `compile()` to check the assembled Python before testing its import.
- Use the Project's existing Pydantic dependency in strict mode for field validation before writing. Read field types, allowed values, and collection bounds from the Model Declarations.
