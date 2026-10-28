---
subjects:
  governs: Subject/CAPRMEDIO/Carrier.Canonical Address.Segment
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Version Number
version: 20
updated_at: 2026-10-27 19:59:23 +0400
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
