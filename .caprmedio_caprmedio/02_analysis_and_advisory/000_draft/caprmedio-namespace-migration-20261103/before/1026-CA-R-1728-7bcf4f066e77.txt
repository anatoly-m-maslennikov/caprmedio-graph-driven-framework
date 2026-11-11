---
subjects:
  active: Projection
version: 28
updated_at: 2026-11-02 19:44:26 +0400
relations:
  child_of:
  - CA-R-007
atom_id: CA-R-1728
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Record every Projection rebuild in a Journal

## Claim scope

Projection rebuild attempts.

## Claim

**every** Projection rebuild attempt **must** produce append-only Journal provenance from its start through **`=1`** terminal outcome, binding the target Projection, exact source Atom revisions **and** Journal records, generator, configuration, **and** produced revision **when** successful. Programmatic generation **and** LLM generation are provenance facts **only**; the two generation forms grant the Projection no authority.
