---
atom_id: CA-R-2349
current_scope_unit: CORE_META_MODEL
status: Active
tier: 1
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/File.Main Content.Paragraph
relations: {}
version: 2
updated_at: 2026-11-02 00:18:22 +0400
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Entity Definition
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
