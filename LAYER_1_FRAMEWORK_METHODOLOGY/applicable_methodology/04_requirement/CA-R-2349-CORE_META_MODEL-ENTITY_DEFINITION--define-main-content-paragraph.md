---
atom_id: CA-R-2349
current_scope_unit: CORE_META_MODEL
status: Active
tier: 1
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier/File.Main Content.Paragraph
relations: {}
version: 2
updated_at: 2026-11-02 00:18:22 +0400
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Entity Definition
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2349-CORE_META_MODEL-ENTITY_DEFINITION--define-main-content-paragraph.md
  source_atom_id: CA-R-2349
  source_atom_revision: 2
  source_sha256: 5183be05eca9d5d16d7d34a05a95ee2c4cdc51854ed0dfb9b117a2920921a615
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Main Content Paragraph

## Claim scope

Prose paragraphs within Markdown File Carrier Main Content.

## Claim

A Main Content Paragraph is one prose paragraph in a Markdown File Carrier Main Content; zero or more may occur. Delivery serializes each paragraph on one unwrapped source line with one blank line between adjacent paragraphs.

### Formal claim

```text
Carrier/File.Main Content.Paragraph[string]{0+}
```

## Details

Source meaning: CA-R-2269, CA-D-279. Scope-specific constraints remain in their governing Rs.
