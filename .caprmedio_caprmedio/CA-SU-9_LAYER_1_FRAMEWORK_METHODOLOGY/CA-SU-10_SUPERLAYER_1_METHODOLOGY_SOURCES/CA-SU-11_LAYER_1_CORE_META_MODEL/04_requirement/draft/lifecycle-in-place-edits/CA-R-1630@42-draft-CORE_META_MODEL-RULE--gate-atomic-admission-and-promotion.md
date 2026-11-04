---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom
  passive:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework
    Settings
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Governing Configuration
version: 42
updated_at: 2026-11-03 22:29:07 +0400
relations: {}
atom_id: CA-R-1630@42-draft
status: Draft
tier: 3
role: Requirement
form: Rule
---
## Summary

Gate atomic admission and promotion

## Claim

### Prose Claim

CAPRMEDIO **must** admit and promote a Draft only when Project authority and the applicable permissions authorize the requested operation and the selected qualified model accepts the Draft for its intended Scope and target identity.

A valid Draft admission checks ordinary authorization/security, expected source/currentness, owning Scope/Project authority, applicable model, mandatory fields, Claim structure, filename/location consistency, and identity/collision constraints. An unmet or ambiguous check is refused with its diagnostic; no new record or confirmation is required.

Promotion uses the target canonical ID selected during preparation and does not silently change that ID, Tier, or Scope. The Draft marker remains until publication, and target selection stays ordinary operation context/result data. Identity and Version behavior follow CA-R-1432; `updated_at` initialization, refresh, and retention follow CA-R-1788.
