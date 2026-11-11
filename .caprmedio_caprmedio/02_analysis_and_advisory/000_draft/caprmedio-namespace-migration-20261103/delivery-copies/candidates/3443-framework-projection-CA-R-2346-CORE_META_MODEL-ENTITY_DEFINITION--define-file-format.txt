---
atom_id: CA-R-2346
current_scope_unit: CORE_META_MODEL
status: Active
tier: 1
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier/File.Format
relations: {}
version: 2
updated_at: 2026-11-02 00:18:22 +0400
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Entity Definition
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2346-CORE_META_MODEL-ENTITY_DEFINITION--define-file-format.md
  source_atom_id: CA-R-2346
  source_atom_revision: 2
  source_sha256: 2ec456f94325daadab64fdbb90f898e9cf88ff21e53fbfeed441006e65887cd8
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define File Format

## Claim scope

Formats applicable to File Carriers.

## Claim

A File Carrier's Format is the rules for encoding and interpreting its represented content. Core Meta-Model permits registered Markdown, TOML, YAML and JSON formats; Extensions and Project Configuration may register additional Carrier Formats.

### Formal claim

```text
Carrier/File.Format[string]{1}
```

## Details

Source meaning: CA-R-1950, CA-D-262. Scope-specific constraints remain in their governing Rs.
