---
subjects:
  governs: Subject/Engineering/Carrier/Filename/Atom.Tier
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Atom.Tier
  - Subject/Domain/Node/Continuant/Projection
version: 4
updated_at: 2026-10-24 01:50:12 +0400
relations:
  delivery_for:
  - CA-R-2124
  depends_on:
  - CA-D-651
  - CA-D-478
atom_id: CA-D-652@4
content_role: Delivery
type: Eng Decision
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 3
status: Archived
author: Anatoly Maslennikov
---
# Summary

Omit Default Numeric Tier Tokens from Filenames

## Scope

Atom filenames whose registered grammar omits the default numeric Tier token.

## Claim

an Atom filename **may** omit the default Tier `3` token only where the registered filename grammar explicitly defines that omission. The Atom **must** still carry its numeric Tier internally under CA-R-2124; omission **must not** add, remove, or alter an Atom Property, infer a Content Role or Type restriction, or change the represented source Properties in a Projection or other non-Atom Artifact. A Project Goal's explicit Tier `-1` grammar is evaluated before any ordinary default omission.

## Details
