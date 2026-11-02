---
atom_id: CA-R-2191@3-draft
content_role: Requirement
type: Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
status: Draft
subjects:
  governs: Model::CAPRMEDIO::Continuant/Package>Asset/Schema
  depends_on:
  - Model::CAPRMEDIO::Continuant/Package>Asset
version: 3
updated_at: 2026-10-29 01:07:23 +0400
relations: {}
tier: 3
---
# Summary

Define Schema

## Claim

A Schema is an Asset defining a machine-readable structural or validation shape used by runtime or evaluations.

### Formal claim

```text
Asset/Schema
```

## Semantics

A document explaining the schema is Documentation; the schema used as a structural or validation input is an Asset.

## Details

CA-A-1278 removes Resources and preserves this useful classification under Asset. This next-version Draft does not promote or retire Current sources.
