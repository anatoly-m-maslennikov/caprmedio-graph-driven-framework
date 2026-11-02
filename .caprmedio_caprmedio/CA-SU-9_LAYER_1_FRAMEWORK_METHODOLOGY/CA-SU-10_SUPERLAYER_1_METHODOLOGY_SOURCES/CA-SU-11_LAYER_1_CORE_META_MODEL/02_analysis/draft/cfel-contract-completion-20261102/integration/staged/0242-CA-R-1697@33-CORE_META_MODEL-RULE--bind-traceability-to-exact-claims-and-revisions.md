---
subjects:
  active: CFEL > Relation
  passive: []
version: 33
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-007
atom_id: CA-R-1697@33
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 1
role: Requirement
form: Rule
---
## Summary

Bind traceability to exact claims and revisions

## Claim scope

CAPRMEDIO traceability assertions.

## Claim

**every** CAPRMEDIO traceability assertion **must** identify the exact governed claim revision on which a receiving artifact, implementation target, evaluation use, delivery action, operational observation, **or** other governed result relies.

## Details

the trace **must** preserve the source identity **and** accepted Revision, the receiving identity **or** stable target locator, the typed relation between them, the bounded scope **and** use, **and** the provenance needed **to** replay that relation. a relation **to** an artifact ID **without** its relied-upon revision is insufficient **after** the Atom has more than one accepted Revision.

Traceability records relationships; it does **not** transfer authority **or** prove correctness, execution, delivery, **or** currentness. secondary storage history **may** preserve Carrier evidence, while governed Journals preserve semantic relationships independently of that secondary history.
