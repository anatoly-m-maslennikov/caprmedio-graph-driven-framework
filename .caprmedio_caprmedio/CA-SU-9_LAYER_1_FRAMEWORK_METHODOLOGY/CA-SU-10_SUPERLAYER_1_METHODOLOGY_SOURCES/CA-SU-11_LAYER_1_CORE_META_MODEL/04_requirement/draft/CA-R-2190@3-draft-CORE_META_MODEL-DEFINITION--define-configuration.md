---
atom_id: CA-R-2190@3-draft
ref_id: CA-R-2190@3-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Definition
topics:
  main_subject: Model::CAPRMEDIO::Continuant/Package>Asset/Configuration
  dependencies:
  - Model::CAPRMEDIO::Continuant/Package>Asset
tier: 3
status: Draft
version: 3
updated_at: 2026-10-29 01:07:23 +0400
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
---
# Summary

Define Configuration

## Claim

A Configuration is an Asset supplying technical parameter values used by runtime or evaluations.

### Formal claim

```text
Asset/Configuration
```

## Semantics

This is implementation configuration, distinct from Governing Configuration that governs the Project or methodology.

## Details

CA-A-1278 removes Resources and preserves this useful classification under Asset. This next-version Draft does not promote or retire Current sources.
