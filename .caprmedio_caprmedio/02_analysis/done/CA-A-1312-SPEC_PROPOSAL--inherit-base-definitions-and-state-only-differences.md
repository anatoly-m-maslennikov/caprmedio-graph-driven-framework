---
atom_id: CA-A-1312
content_role: Analysis & Advisory
type: Spec Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Done
author: Anatoly Maslennikov
tier: 3
version: 3
updated_at: 2026-11-02 15:49:28 +0400
subjects:
  governs: Entity
relations: {}
---
## Summary

Inherit base Definitions and state only differences

## Proposal

Definitions inherit through / specialization and // instantiation. A narrower kind reuses the broader Definition and states only its differences. An instance follows its kind Definition and states only instance facts. Common meaning, properties and constraints are reused, not copied. Containment > adds no inheritance. Atom/Content Role: Method is an Atom with Content Role Method; it does not repeat the Atom Definition.

## Status

Accepted Operator decision. P2696 applies it to the Definition template, ownership rule and seven Content Role Definitions. This adds no new notation or Type hierarchy.
