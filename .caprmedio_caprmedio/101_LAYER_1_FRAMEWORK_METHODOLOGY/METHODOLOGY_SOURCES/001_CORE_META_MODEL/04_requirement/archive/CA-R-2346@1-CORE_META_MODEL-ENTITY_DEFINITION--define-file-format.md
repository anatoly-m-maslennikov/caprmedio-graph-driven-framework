---
atom_id: CA-R-2346@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: Entity/Carrier/File.Format
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define File Format

## Claim scope

Formats applicable to File Carriers.

## Claim

A File Carrier's Format is the rules for encoding and interpreting its represented content. Core Meta-Model permits registered Markdown, TOML, YAML and JSON formats; Extensions and Project Configuration may register additional Carrier Formats.

### Formal claim

```text
Entity/Carrier/File.Format[string]{1}
```

## Details

Source meaning: CA-R-1950, CA-D-262. Scope-specific constraints remain in their governing Rs.
