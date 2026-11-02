---
atom_id: CA-R-1950@11
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Carrier.Format
relations:
  child_of:
  - CA-R-1174
version: 11
updated_at: 2026-10-29 14:16:32 +0400
tier: 3
type: Entity Definition
---
## Summary

Define Carrier.Format

## Claim scope

Carriers with an applicable representation format.

## Claim

A Carrier's Format **means** the rules for encoding and interpreting its represented content. The registered File Carrier values include Markdown, TOML, YAML and JSON under CA-D-262; representation details remain governed by Delivery.

### Formal claim

```text
Entity/Carrier/File.Format: Markdown
Entity/Carrier/File.Format: TOML
Entity/Carrier/File.Format: YAML
Entity/Carrier/File.Format: JSON
```

## Details

CA-D-262 admits registered File Carrier formats including Markdown, TOML, YAML and JSON; CA-D-507 distinguishes format from identity. This definition does not require a format value for every Directory Carrier.

