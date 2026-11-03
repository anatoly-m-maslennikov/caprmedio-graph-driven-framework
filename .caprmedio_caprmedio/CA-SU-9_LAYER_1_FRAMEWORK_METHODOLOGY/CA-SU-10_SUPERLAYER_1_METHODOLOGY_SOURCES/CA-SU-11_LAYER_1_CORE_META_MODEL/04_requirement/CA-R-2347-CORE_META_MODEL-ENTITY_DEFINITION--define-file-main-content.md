---
atom_id: CA-R-2347
current_scope_unit: CORE_META_MODEL
status: Active
tier: 1
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/File.Main Content
relations: {}
version: 2
updated_at: 2026-11-02 00:18:22 +0400
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Entity Definition
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
