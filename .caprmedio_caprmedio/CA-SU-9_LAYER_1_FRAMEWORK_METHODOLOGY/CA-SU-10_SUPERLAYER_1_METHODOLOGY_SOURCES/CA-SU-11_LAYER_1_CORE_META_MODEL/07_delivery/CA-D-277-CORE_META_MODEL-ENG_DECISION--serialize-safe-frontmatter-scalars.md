---
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/File.YAML Frontmatter.Scalar
  passive:
  - CAPRMEDIO_MODEL <+ Carrier/File.Main Content
version: 24
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-277
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
---
## Summary

Serialize Safe Frontmatter Scalars

## Claim scope

YAML Frontmatter of Markdown Atom Carriers.

## Claim

the YAML Frontmatter of a Markdown Atom Carrier **must** serialize registered YAML-safe controlled string values as plain scalars **and** **must** place uncontrolled human prose **in** Main Content.
