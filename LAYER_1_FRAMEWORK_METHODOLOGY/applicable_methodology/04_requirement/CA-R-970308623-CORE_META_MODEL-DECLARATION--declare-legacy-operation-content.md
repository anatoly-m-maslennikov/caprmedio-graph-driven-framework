---
identity:
  id: CA-R-970308623
  ref_id: CA-R-970308623
context:
  container:
    scope_unit: CA-SU-11
  role: Requirement
  form: Declaration
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations).Content.Operation
  tier: 4
state:
  status: Active
  version: 1
  updated_at: 2026-11-08 18:59:53 +0400
destination:
  file:
    name: CA-R-970308623-CORE_META_MODEL-DECLARATION--declare-legacy-operation-content.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
author: Anatoly Maslennikov
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-970308623-CORE_META_MODEL-DECLARATION--declare-legacy-operation-content.md
  source_atom_id: CA-R-970308623
  source_atom_revision: 1
  source_sha256: 5054d12aacee36d594d66f324a9b4fcc5b73f617ae13f1c3397652d590eab2b6
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare legacy Operation content

## Claim

### Prose Claim

An Operations Atom may retain its legacy Operation section during migration. Operation is a Markdown Content Property. Its presentation subheadings, lists and code blocks remain part of its value.

### Formal Claim

```CFEL
# model
Atom/(.Header.Role := Operations).Content.Operation:: [markdown]{::0..1};

Atom/(.Header.Role := Operations).Content.Operation.*[]{::0}
```

## Semantics

Operation is the operation text carried by the legacy Operations Atom. This declaration describes that existing section; it does not decide whether a later Form must use Operation or Claim.
