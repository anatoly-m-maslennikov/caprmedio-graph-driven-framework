---
atom_id: CA-R-2192@3-draft
ref_id: CA-R-2192@3-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Definition
topics:
  main_subject: Model::CAPRMEDIO::Continuant/Package>Asset/Template
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
