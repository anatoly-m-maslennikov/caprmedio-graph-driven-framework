---
atom_id: CA-R-2347
current_scope_unit: CORE_META_MODEL
status: Active
tier: 1
subjects:
  active: Carrier/File.Main Content
relations: {}
version: 2
updated_at: 2026-11-02 00:18:22 +0400
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Entity Definition
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2347-CORE_META_MODEL-ENTITY_DEFINITION--define-file-main-content.md
  source_atom_id: CA-R-2347
  source_atom_revision: 2
  source_sha256: 58441faae498e22167aaa6e8003cf80e509e1668180efe19492bf24fe75ac04a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define File Main Content

## Claim scope

Main Content of a Markdown File Carrier.

## Claim

A Markdown File Carrier Main Content means the content after its YAML Frontmatter and is its Markdown body. It is optional, may contain Paragraph and CCE Operator occurrences as content parts, and is not a separate File.

### Formal claim

```text
Carrier/File.Main Content[string]{0..1}
```

## Details

Source meaning: CA-R-2269, CA-D-357, CA-D-279, CA-D-280, CA-D-479. Scope-specific constraints remain in their governing Rs.
