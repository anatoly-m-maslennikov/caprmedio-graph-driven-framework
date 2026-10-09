---
atom_id: CA-D-602
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-09 21:50:26 +0400"
subjects:
  governs: "Framework Installation contribution/Admitted source catalog"
  depends_on: [Tool, Framework Package, Methodology, Extension, Configuration]
relations:
  delivery_for: [CA-R-1902, CA-R-1908, CA-M-359]
---
# Summary

Encode the admitted package source catalog

## Scope

The package-owned catalog that binds Core, optional extensions, configuration and active Methodology sources to immutable admitted revisions.

## Claim

the INSTALL_TOOLS facade **must** include an admitted `catalog.toml` with a pinned revision and digest for every selected source, and an unknown revision **must** fail before any package, image or target effect.

## Details

Each ordered `[source.<identity>]` record contains `kind`, `revision`, `sha256`, `admission_receipt_sha256`, `visibility`, `selection_default` and package-relative `path`. Core is required; optional extensions and configuration may be catalogued as available. `selection_default = false` and `visibility = private` never cause target autoloading; target selection is an explicit validated target-context choice.

For the explicitly admitted local Core, selected active Methodology and declared support snapshots, `revision` may equal their exact lowercase 64-hex content digest. `admission_receipt_sha256` hashes the actual retained admission record, which binds the Operator command, selected source identity and exact snapshot digest. It is not the source digest repeated as a substitute for an admission record.

The catalog SHA-256 is carried by the package manifest, candidate seal, package-current selector and target installation result. Empty, symbolic, mutable-tag, unresolved, duplicate or content-mismatched revisions are not pins. No caller-provided catalog replaces the sealed catalog.
