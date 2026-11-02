---
atom_id: CA-R-2190@3-draft
content_role: Requirement
type: Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
status: Draft
subjects:
  governs: Model::CAPRMEDIO::Continuant/Package>Asset/Configuration
  depends_on:
  - Model::CAPRMEDIO::Continuant/Package>Asset
version: 3
updated_at: 2026-10-29 01:07:23 +0400
relations: {}
tier: 3
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
