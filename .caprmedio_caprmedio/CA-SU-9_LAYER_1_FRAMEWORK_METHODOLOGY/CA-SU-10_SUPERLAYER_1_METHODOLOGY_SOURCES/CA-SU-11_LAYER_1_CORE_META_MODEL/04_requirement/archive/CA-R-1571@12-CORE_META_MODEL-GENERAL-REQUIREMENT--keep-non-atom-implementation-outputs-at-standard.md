---
subjects:
  governs: Subject/Engineering/Implementation/Output Classification
  depends_on:
  - Artifact
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Engineering/Implementation
  - Subject/Domain/Node/Continuant/Projection
  - Subject/Domain/Node/Continuant/Atom.Tier
version: 12
updated_at: 2026-10-24 00:51:05 +0400
relations:
  relates_to:
  - CA-R-2129
  - CA-R-1568
atom_id: CA-R-1571@12
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
---
# Summary

Keep non-Atom Implementation outputs at Standard

## Scope

non-Atom Implementation Artifacts.

## Claim

a non-Atom Implementation Artifact **must** retain the numeric `tier` of the governed Atom when it is a delivered Projection or other derived output; the output does not acquire an independent Atom tier. The historical Standard label denotes numeric Tier `3` under CA-R-2129, but Content Role and Artifact Type do not impose a tier restriction.

this derived classification does **not** add an Atom Content Role **or** Atom identity **to** the Artifact **and** does **not** change the authority **or** tier of represented source content.

## Details

