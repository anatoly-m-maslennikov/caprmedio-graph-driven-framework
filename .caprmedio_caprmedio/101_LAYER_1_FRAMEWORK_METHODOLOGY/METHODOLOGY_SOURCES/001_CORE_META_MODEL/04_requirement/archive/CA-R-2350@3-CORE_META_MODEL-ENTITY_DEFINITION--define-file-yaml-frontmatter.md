---
atom_id: CA-R-2350@3
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: Entity/Carrier/File.YAML Frontmatter
relations: {}
version: 3
updated_at: 2026-10-30 03:11:58 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define File YAML Frontmatter

## Claim scope

Optional structured metadata region of a Markdown File Carrier.

## Claim

A Markdown File Carrier YAML Frontmatter is its optional structured metadata region. It has no direct scalar value and is a logical region, not a separate Carrier; its encoding uses economical YAML syntax and keeps uncontrolled prose in Main Content.

### Formal claim

```text
Entity/Carrier/File.YAML Frontmatter{0}
```

## Details

Source meaning: CA-R-2269, CA-D-657, CA-D-277. Scope-specific constraints remain in their governing Rs.
