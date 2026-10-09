---
atom_id: CA-R-1908
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Source catalog admission"
  depends_on: [Tool, Framework Package, Methodology, Extension, Configuration]
relations:
  relates_to: [CA-D-602, CA-E-604]
---
# Summary

Require a pinned admitted package source catalog

## Scope

the source identity proof carried by a reusable package.

## Claim

the INSTALL_TOOLS facade **must** seal every selected package source with an admitted immutable revision and digest, and an unknown revision **must** fail **before** package, image, selector or target effects.

## Details

The catalog binds Core, selected active Methodology source, declared support and any available optional extension/configuration. Mutable tags, blank revisions, duplicate identities, mismatched source digest or caller replacement catalog refuse. The catalog digest is re-bound in candidate, package, image proof and activation evidence.
