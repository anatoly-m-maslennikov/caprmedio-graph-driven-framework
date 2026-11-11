---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Entity
  passive:
  - CAPRMEDIO <+ MODEL <+ Projection
  - CAPRMEDIO <+ MODEL <+ Atom
  - CAPRMEDIO <+ MODEL <+ Atom.Content
  - CAPRMEDIO <+ MODEL <+ Entity
  - CAPRMEDIO <+ MODEL <+ Journal
  - CAPRMEDIO <+ MODEL <+ CFEL > Relation
version: 27
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1471
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Keep secondary graphs derived from source authority

## Claim scope

secondary CAPRMEDIO Graphs.

## Claim

secondary CAPRMEDIO Graphs **must** be Projections derived from their selected authoritative sources **or** source-traceable upstream Projections. their nodes **and** Relations **must** preserve source identities **and** traceability **to** the governing derivation authority **and** source facts.

storing, composing, filtering, **or** rebuilding a secondary graph **must not** make its contents another source of authority. a represented source fact is corrected **at** its authoritative source; an incorrect derivation is corrected under its governing methodology. neither case is resolved by independently editing the projected fact **or** fabricating source history.
