---
atom_id: CA-R-2346
current_scope_unit: CORE_META_MODEL
status: Active
tier: 1
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/File.Format
relations: {}
version: 2
updated_at: 2026-11-02 00:18:22 +0400
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Entity Definition
---
## Summary

Define File Format

## Claim

### Prose Claim


Formats applicable to File Carriers.


A File Carrier's Format is the rules for encoding and interpreting its represented content. Core Meta-Model permits registered Markdown, TOML, YAML and JSON formats; Extensions and Project Configuration may register additional Carrier Formats.


```text
Carrier/File.Format[string]{1}
```

## Details

Source meaning: CA-R-1950, CA-D-262. Scope-specific constraints remain in their governing Rs.
