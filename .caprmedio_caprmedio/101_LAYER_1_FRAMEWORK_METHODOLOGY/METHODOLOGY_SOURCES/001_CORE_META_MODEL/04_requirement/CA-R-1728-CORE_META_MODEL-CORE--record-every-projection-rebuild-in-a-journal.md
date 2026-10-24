---
subjects:
  governs: Subject/Domain/Node/Continuant/Projection
  depends_on: []
version: 20
updated_at: 2026-10-24 04:38:42 +0400
relations:
  child_of:
  - CA-R-007
atom_id: CA-R-1728
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Record every Projection rebuild in a Journal

## Scope

Projection rebuild attempts.

## Claim

**every** Projection rebuild attempt **must** produce append-only Journal provenance from its start through **`=1`** terminal outcome, binding the target Projection, exact source Atom revisions **and** Journal records, generator, configuration, **and** produced revision **when** successful. Programmatic generation **and** LLM generation are provenance facts **only**; the two generation forms grant the Projection no authority.

## Details
