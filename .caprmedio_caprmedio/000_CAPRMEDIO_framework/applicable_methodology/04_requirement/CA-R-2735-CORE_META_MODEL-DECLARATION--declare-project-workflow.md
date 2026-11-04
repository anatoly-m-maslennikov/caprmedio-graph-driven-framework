---
atom_id: CA-R-2735
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Workflow/(.Purpose := Project)
version: 1
updated_at: '2026-11-04 00:31:19 +0400'
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2735-CORE_META_MODEL-DECLARATION--declare-project-workflow.md
  source_atom_id: CA-R-2735
  source_atom_revision: 1
  source_sha256: c5d223f5de5d92bfcf97e982c34cc968210e9c6f5d2c01a6d290c67886ae0637
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Project Workflow

## Claim

### Formal Claim

```CFEL
Atom/(.Header.Role: Operations)/Workflow/(.Purpose := Project)
```

## Semantics

A Project Workflow is a Workflow whose Purpose is Project: it develops, validates, maintains or releases a Project's result. Examples include Implementation, Local Release and Public Release.

It inherits Workflow's shared Step, Substep and Action model. Purpose describes use relative to a Project and does not change the canonical definition's owning Scope Unit.
