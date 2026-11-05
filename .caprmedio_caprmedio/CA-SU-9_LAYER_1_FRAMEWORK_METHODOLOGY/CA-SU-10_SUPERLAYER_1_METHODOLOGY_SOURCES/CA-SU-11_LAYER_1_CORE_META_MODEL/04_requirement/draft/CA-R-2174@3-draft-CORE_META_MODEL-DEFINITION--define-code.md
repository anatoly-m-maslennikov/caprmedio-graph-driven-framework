---
atom_id: CA-R-2174@3-draft
ref_id: CA-R-2174@3-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Definition
topics:
  main_subject: Formal Model::CAPRMEDIO::Continuant/Implementation>Code
tier: 2
status: Draft
version: 3
updated_at: 2026-10-28 20:57:35 +0400
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
---
# Summary

Define Code

## Claim

### Formal claim

```text
Implementation > Code
Code > Module
Module > Code Unit
Code > Package
Code > Asset
Continuant / @(Code)
```

## Semantics

Code is the Implementation software-material part, with the proposed Module, Package, Code Unit and Asset construction. It has no independent existence outside Implementation. Code Units are parts of Modules; Class and Function specialize Code Unit.

## Details

Prepared from the latest A1246–A1249 decisions; Current predecessor is untouched. A1253 records exactly-one whole for a contained part. Its interaction with alternative Module containers remains pending; this Draft is not ready for promotion.

## Superseded — do not promote

CA-A-1254 removes Code as a separate kind. This older Draft is retained as preparation history only, not an operative migration target. Preserve useful meanings in Package, Module, Prompt and Asset Definitions before retiring Current R2174.
