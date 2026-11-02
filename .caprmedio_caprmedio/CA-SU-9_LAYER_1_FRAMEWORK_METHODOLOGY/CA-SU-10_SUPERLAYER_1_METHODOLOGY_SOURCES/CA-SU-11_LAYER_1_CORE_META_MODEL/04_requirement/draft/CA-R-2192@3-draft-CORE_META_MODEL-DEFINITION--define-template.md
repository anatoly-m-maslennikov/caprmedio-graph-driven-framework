---
atom_id: CA-R-2192@3-draft
content_role: Requirement
type: Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
status: Draft
subjects:
  governs: Model::CAPRMEDIO::Continuant/Package>Asset/Template
  depends_on:
  - Model::CAPRMEDIO::Continuant/Package>Asset
version: 3
updated_at: 2026-10-29 01:07:23 +0400
relations: {}
tier: 3
---
# Summary

Define Template

## Claim

A Template is a parameterized, non-executable Asset used by runtime or evaluations to construct a result.

### Formal claim

```text
Asset/Template
```

## Semantics

Instructions executed by an LLM are Prompts rather than Assets. Parameterization alone does not make a Prompt an Asset.

## Details

CA-A-1278 removes Resources and preserves this useful classification under Asset. This next-version Draft does not promote or retire Current sources.
