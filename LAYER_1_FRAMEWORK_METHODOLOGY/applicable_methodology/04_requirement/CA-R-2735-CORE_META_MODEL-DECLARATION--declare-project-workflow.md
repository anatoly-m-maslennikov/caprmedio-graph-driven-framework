---
atom_id: CA-R-2735
ref_id: CA-R-2735
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Workflow/(.Purpose := Project)
tier: 3
status: Active
version: 1
updated_at: '2026-11-04 00:31:19 +0400'
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2735-CORE_META_MODEL-DECLARATION--declare-project-workflow.md
  source_atom_id: CA-R-2735
  source_atom_revision: 1
  source_sha256: 0992f8e6799ce59a439f7e33657cd6e4f5d374ab7c67859a3442a26e993d2514
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Project Workflow

## Claim

### Formal Claim

```CFEL
Atom/(.Header.Role := Operations)/Workflow/(.Purpose := Project)
```

## Semantics

A Project Workflow is a Workflow whose Purpose is Project: it develops, validates, maintains or releases a Project's result. Examples include Implementation, Local Release and Public Release.

It inherits Workflow's shared Step, Substep and Action model. Purpose describes use relative to a Project and does not change the canonical definition's owning Scope Unit.
