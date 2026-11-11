---
atom_id: CA-R-2734
ref_id: CA-R-2734
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Workflow/(.Purpose := Runtime)
tier: 3
status: Active
version: 1
updated_at: '2026-11-04 00:31:19 +0400'
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2734-CORE_META_MODEL-DECLARATION--declare-runtime-workflow.md
  source_atom_id: CA-R-2734
  source_atom_revision: 1
  source_sha256: 542bb5d57c52558df43d10e2b4b949db5e43df56525f6024f5c3caac4972c086
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Runtime Workflow

## Claim

### Formal Claim

```CFEL
Atom/(.Header.Role := Operations)/Workflow/(.Purpose := Runtime)
```

## Semantics

A Runtime Workflow is a Workflow whose Purpose is Runtime: it provides behavior through a Project's delivered result during its operation. In CAPRMEDIO, examples include Create Draft, Promote Draft and Archive Atom.

It inherits Workflow's shared Step, Substep and Action model. Purpose describes use relative to a Project and does not change the canonical definition's owning Scope Unit.
