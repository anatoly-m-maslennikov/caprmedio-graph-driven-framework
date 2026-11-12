---
identity:
  atom_id: CA-P-3018
  ref_id: CA-P-3018
context:
  role: plan
  form: Plan
  label: Epic
  tier: 3
  container:
    scope_unit: CA-SU-14
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
state:
  version: 1
  status: active
  updated_at: '2026-11-12T01:46:36+00:00'
destination:
  file:
    name: CA-P-3018-EPIC--adopt-the-workflow-engine-and-migrate-cfel-claims-to-python.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan
---
## Summary

Adopt the Workflow Engine and migrate CFEL Claims to Python

## Objective

Use ordinary Python for Workflow business logic. Migrate CFEL Formal Claims to readable Python declarations and expressions with minimal boilerplate. Keep the existing Topic notation and addresses.

## Work

1. Compare the Current Atom Lifecycle O Atoms with the code. Record verified behavior and gaps.
2. Draft and review Workflow Engine RMED. Workflows own business decisions and action order. The Engine provides inputs, invokes Actions, and handles I/O, results, and failures.
3. Pilot a Python Workflow on Atom Lifecycle. Check parity with the baseline.
4. Migrate CFEL Claims and their consumers. Start with schemas, inherited constraints, and overrides. Use ordinary Python syntax with minimal boilerplate. Use functions and classes with descriptive names and named parameters. Add a linter for formal expressions. Compare representative Claims with and without a small expression engine before deciding whether to add one.

## Definition of Done

Workflow Engine RMED is adopted. The Python lifecycle pilot matches the verified baseline. Migrated declarations preserve schema inheritance and validation. Affected consumers pass parity checks. The linter checks admitted syntax and model references. Short Python examples show the chosen approach and the evidence for the expression-engine decision.
