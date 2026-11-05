---
atom_id: CA-R-1873
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Package/Implementation
  passive:
  - CAPRMEDIO_MODEL <+ Projection
  - CAPRMEDIO_MODEL <+ Journal
  - CAPRMEDIO_MODEL <+ Carrier
version: 20
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 1
role: Requirement
form: Rule
---
## Summary

Derive Implementation and use its actual state as source

## Claim

### Prose Claim


native Implementation production and subsequent use as a source.


Implementation production **must** derive I from current applicable RMED using governed Operations: **RMED → using O → I**. native I **may** subsequently act as source truth for its actual realized content, structure, dependencies, **and** behavior. a further view derived from I using O, including a dependency graph, **must** remain a non-authoritative Projection: **I → using O → Projection**.

## Details

Generation need not be deterministic. Derivation is a relation to governing intent, not perpetual loss of actual-state authority. Actual code may predate CAPRMEDIO authority; its observations support adoption, reconciliation, and continuation without automatically accepting inferred CRMED drafts or changing governing RMED. Existing I is not a prerequisite for reconstructing I from current RMED. Ordinary view Projections never replace the authority of their represented sources.
