---
atom_id: CA-R-2345@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: Entity/Carrier/File.Filename.Scope Unit Token
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define File Filename Scope Unit Token

## Claim scope

Scope Unit references serialized in a File Carrier filename.

## Claim

A File Carrier Filename Scope Unit Token is one stable uppercase token for a referenced Scope Unit. A filename may contain zero or more tokens; each serialized Scope Unit reference uses one token selected by Project Configuration.

### Formal claim

```text
Entity/Carrier/File.Filename.Scope Unit Token[string]{0+}
```

## Details

Source meaning: CA-R-2269, CA-D-302. Scope-specific constraints remain in their governing Rs.
