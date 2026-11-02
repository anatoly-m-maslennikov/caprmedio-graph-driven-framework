---
subjects:
  governs: Subject/Engineering/Carrier.Canonical Address.Segment
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Version Number
version: 17
updated_at: 2026-10-24 09:42:52 +0400
relations: {}
atom_id: CA-D-289@17
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
