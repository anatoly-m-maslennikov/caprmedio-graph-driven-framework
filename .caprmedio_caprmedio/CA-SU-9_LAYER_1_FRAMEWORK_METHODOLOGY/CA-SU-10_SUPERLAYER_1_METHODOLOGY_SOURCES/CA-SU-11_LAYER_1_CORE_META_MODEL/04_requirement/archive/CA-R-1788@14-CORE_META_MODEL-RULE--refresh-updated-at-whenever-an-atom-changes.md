---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom.Updated At
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Atom.Status
  - Subject/Graph Node/Carrier
  - Subject/Graph Node/Carrier.Canonical Address
version: 14
updated_at: 2026-10-27 06:04:45 +0400
claim_target_scope_unit: CORE_META_MODEL
relations:
  child_of:
  - CA-R-1416
atom_id: CA-R-1788@14
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

**every** actual accepted edit **to** an Atom Carrier **must** refresh that Current Atom's `updated_at` **to** the actual Project-time edit instant, including a formatting, lossless serialization, Entity-name, admitted Current Status, direct-owner, **or** current-Atom local-placement edit. an exact no-op **must** retain Updated At. When a real update publishes a successor and archives its predecessor, the Archive Carrier **must** retain the predecessor's prior Updated At, numeric Version, and unrelated content while carrying the Archived status and version-qualified identity; Git history preserves the exact pre-archive bytes. Standalone archival is not an edit to the Current Atom's content: it only materializes the Archived representation with its version-qualified identity, filename and location, so it does not create a successor or refresh Updated At.

## Details

an ancestor-only move that changes an Atom's repository locator **without** changing its own bytes, metadata, direct owner **or** placement relative **to** that owner is **not** an edit **to** that Atom. retain its Updated At **and** Version under CA-R-1432. this applies **to** **every** Atom, regardless of Content Role; it does **not** exempt an actual Status, filename, ownership **or** local-placement change. Git history retains exact pre-archive bytes.

changing a Current Atom's Status **and** publishing a Current successor is an actual update governed by CA-R-1432: archive the old-version identity with unchanged numeric Version and Updated At, while the Current successor receives its incremented Version and actual edit time. A standalone transition of the Current representation to Archived follows the exception above. timestamp encoding follows `CA-D-270-CORE_META_MODEL-DELIVERY--serialize-atom-revision-metadata-in-frontmatter`.
