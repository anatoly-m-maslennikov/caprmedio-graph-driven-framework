---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Updated At
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Atom.Status
  - Subject/Engineering/Carrier
  - Subject/Engineering/Carrier.Canonical Address
version: 10
updated_at: 2026-10-24 00:38:25 +0400
claim_target_scope_unit: CORE_META_MODEL
relations:
  child_of:
  - CA-R-1416
atom_id: CA-R-1788@10
content_role: Requirement
current_scope_unit: CORE_META_MODEL
status: Archived
type: Rule
author: Anatoly Maslennikov
tier: 3
---
# Summary

Refresh Updated At whenever an Atom changes

## Scope

accepted Markdown Atom Carrier edits.

## Claim

**every** actual accepted edit **to** an Atom Carrier **must** refresh that Current Atom Revision's `updated_at` **to** the actual Project-time edit instant, including a formatting, lossless serialization, Entity-name, Status, direct-owner, **or** current-Atom local-placement edit. an exact no-op **must** retain Updated At. When a predecessor is archived, its Archive Carrier **must** retain the predecessor's prior Updated At, numeric Version, and unrelated content while carrying the Archived status and version-qualified identity; Git history preserves the exact pre-archive bytes. Archive conversion is not an edit to the historical content and does not require an exact-byte Archive Carrier.

## Details

an ancestor-only move that changes an Atom's repository locator **without** changing its own bytes, metadata, direct owner **or** placement relative **to** that owner is **not** an edit **to** that Atom. retain its Updated At **and** Version under CA-R-1432. this applies **to** **every** Atom, regardless of Content Role; it does **not** exempt an actual Status, filename, ownership **or** local-placement change. Git history retains exact pre-archive bytes.

changing a Current Atom's Status **to** Archived is an actual update governed by CA-R-1432: archive the old-version identity with unchanged numeric Version and Updated At, while the Current successor receives its incremented Version and actual edit time. timestamp encoding follows `CA-D-270-CORE_META_MODEL-DELIVERY--serialize-atom-revision-metadata-in-frontmatter`.
