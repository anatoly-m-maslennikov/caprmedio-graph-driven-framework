---
atom_id: CA-R-2345
current_scope_unit: CORE_META_MODEL
status: Active
tier: 1
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier/File.Filename.Scope Unit Token
relations: {}
version: 2
updated_at: 2026-11-02 00:18:22 +0400
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Entity Definition
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2345-CORE_META_MODEL-ENTITY_DEFINITION--define-file-filename-scope-unit-token.md
  source_atom_id: CA-R-2345
  source_atom_revision: 2
  source_sha256: 968ef5ad3f09feffee4401a70472d21168cce0be67934a444eac00701a1dad96
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define File Filename Scope Unit Token

## Claim scope

Scope Unit references serialized in a File Carrier filename.

## Claim

A File Carrier Filename Scope Unit Token is one stable uppercase token for a referenced Scope Unit. A filename may contain zero or more tokens; each serialized Scope Unit reference uses one token selected by Project Configuration.

### Formal claim

```text
Carrier/File.Filename.Scope Unit Token[string]{0+}
```

## Details

Source meaning: CA-R-2269, CA-D-302. Scope-specific constraints remain in their governing Rs.
