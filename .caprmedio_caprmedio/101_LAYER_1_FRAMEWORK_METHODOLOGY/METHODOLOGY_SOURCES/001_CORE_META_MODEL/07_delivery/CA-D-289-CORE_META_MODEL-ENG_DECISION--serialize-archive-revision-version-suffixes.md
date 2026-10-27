---
subjects:
  governs: Subject/Graph Node/Carrier.Canonical Address.Segment
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom.Version Number
version: 19
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
atom_id: CA-D-289
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
type: Eng Decision
author: Anatoly Maslennikov
tier: 3
---
# Summary

Serialize Archive Revision Version Suffixes

## Scope

Archive Carrier basenames for Archived Atom versions.

## Claim

**every** Archived Atom Carrier basename **must** serialize the archived Atom's canonical ID with exactly one `@<version>` marker, where `<version>` is the unchanged numeric Version Number of that Archived Atom version. The marker **must** occur in the filename's Atom-ID segment under CA-D-283; do **not** append a second `@<version>` to a basename that already carries the marker. Existing legacy archive basenames are not normalized automatically.

## Details
