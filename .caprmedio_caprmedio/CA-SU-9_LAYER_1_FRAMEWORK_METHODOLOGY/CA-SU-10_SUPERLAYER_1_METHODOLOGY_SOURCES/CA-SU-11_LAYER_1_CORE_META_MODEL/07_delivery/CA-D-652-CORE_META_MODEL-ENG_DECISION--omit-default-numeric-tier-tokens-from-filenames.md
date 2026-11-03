---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Tier
  passive:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Tier
  - CAPRMEDIO_MODEL <+ Projection
version: 13
updated_at: 2026-11-02 00:18:22 +0400
relations:
  delivery_for:
  - CA-R-2504
  depends_on:
  - CA-D-651
  - CA-D-478
atom_id: CA-D-652
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 4
status: Active
role: Delivery
form: Decision
---
## Summary

Omit Default Numeric Tier Tokens from Filenames

## Claim scope

Atom filenames whose registered grammar omits the default numeric Tier token.

## Claim

an Atom filename **may** omit the default Tier `3` token only where the registered filename grammar explicitly defines that omission. The Atom **must** still carry its numeric Tier internally under CA-R-2504; omission **must not** add, remove, or alter an Atom Property, infer a Content Role or Type restriction, or change the represented source Properties in a Projection or other non-Atom Artifact. A Project Goal's explicit Tier `-1` grammar is evaluated before any ordinary default omission.
