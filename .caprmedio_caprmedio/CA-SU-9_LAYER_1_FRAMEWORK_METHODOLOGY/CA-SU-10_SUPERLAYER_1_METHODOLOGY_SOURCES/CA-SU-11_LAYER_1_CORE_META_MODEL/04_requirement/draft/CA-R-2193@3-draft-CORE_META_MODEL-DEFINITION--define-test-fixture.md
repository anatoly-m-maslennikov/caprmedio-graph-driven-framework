---
atom_id: CA-R-2193@3-draft
content_role: Requirement
type: Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
status: Draft
subjects:
  governs: Model::CAPRMEDIO::Continuant/Package>Asset/Test Fixture
  depends_on:
  - Model::CAPRMEDIO::Continuant/Package>Asset
version: 3
updated_at: 2026-10-29 01:07:23 +0400
relations: {}
tier: 3
---
# Summary

Define Test Fixture

## Claim

A Test Fixture is a controlled Asset supplying evaluation input, state or expected data.

### Formal claim

```text
Asset/Test Fixture
```

## Semantics

Evaluation Modules and Prompts execute checks; this kind supplies their non-executable input, state or expected data.

## Details

CA-A-1278 removes Resources and preserves this useful classification under Asset. This next-version Draft does not promote or retire Current sources.
