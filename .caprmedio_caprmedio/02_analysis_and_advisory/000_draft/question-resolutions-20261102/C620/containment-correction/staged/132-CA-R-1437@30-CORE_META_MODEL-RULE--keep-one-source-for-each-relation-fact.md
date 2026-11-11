---
subjects:
  active: CFEL <+ Relation
  passive:
  - CFEL <+ Relation
  - Entity
  - Projection
  - Entity/Aspect/Engineering/Traceability
  - Atom.Content
  - Journal
version: 30
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1437@30
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 1
role: Requirement
form: Rule
---
## Summary

Keep one source for each relation fact

## Claim scope

authoritative source declarations for Relation facts.

## Claim

**every** independently authored Relation fact **must** have **`=1`** authoritative source declaration under Single Source of Truth. its representation **in** multiple CAPRMEDIO Graph views remains a reference **or** derived Projection of that declaration **without** creating another independently maintained source.

a Relation derived under admitted derivation authority **must** remain traceable **to** that authority **and** its authoritative input facts, including through upstream Projections. it does **not** require a fabricated direct source declaration for the derived result. this distinction **must not** weaken a Relation Kind's requirement for an explicit source fact **or** permit unsupported inference.
