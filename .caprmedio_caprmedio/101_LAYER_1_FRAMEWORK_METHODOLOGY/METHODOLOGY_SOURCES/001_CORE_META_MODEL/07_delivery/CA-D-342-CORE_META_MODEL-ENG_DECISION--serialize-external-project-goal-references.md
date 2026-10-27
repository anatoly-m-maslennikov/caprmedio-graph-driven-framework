---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement/Type: Project Goal'
  depends_on:
  - Subject/Graph Node/Carrier/File.Filename
version: 23
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
atom_id: CA-D-342
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Serialize External Project Goal References

## Scope

references to Current and historical external Project Goal Atoms.

## Claim

**every** Reference **to** a Current external Project Goal Atom **must** use its canonical Current Atom ID, not its current Carrier filename stem.

A Reference **to** an Archived external Project Goal Atom **must** use its canonical Atom ID qualified once with its unchanged numeric Version when historical identity is required. A Current Project Goal reference **must not** omit the canonical ID or fall back to a filename stem; this Delivery creates no ID-less Current exception.

## Details
