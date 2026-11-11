---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Projection
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom.Content
  - CAPRMEDIO <+ MODEL <+ Atom.Content.Summary
  - CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Execution Control <+ Decision Confidence
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Actor/Operator
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan/Type: Plan'
  - CAPRMEDIO <+ MODEL <+ Atom
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
version: 47
updated_at: 2026-11-02 18:35:20 +0400
relations:
  evaluation_for:
  - CA-M-442
  - CA-M-443
  - CA-M-114
  - CA-M-271
  - CA-R-1591
  - CA-R-940
  - CA-R-941
  - CA-R-1273
atom_id: CA-E-241
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 4
role: Evaluation
form: Eval Case
---
## Summary

Validate CCE Claims and derived Projections

## Claim scope

active and draft Atom Claims, their Summaries, and requested Translation and terminology Projections.

## Claim

**every** active **or** draft Atom **contains** **`=1`** human-readable precise CCE Claim **and** a source-faithful Summary. requested Translation **and** terminology Projections preserve their source meaning; their absence **when** **not** requested is **not** an Atom defect.

### Test case

create valid active **and** draft Atom Claims for **every** admitted Content Role. include fixtures with no requested Translation **or** terminology Projection **and** fixtures with requested Projections. derive a candidate Summary during Atom creation, **then** retain it for checks of subsequent Revisions under CA-E-463-CORE_META_MODEL-EVAL_CASE--validate-summary-identity-preservation. derive requested Translation **and** terminology Projections twice **without** regenerating the existing Atom's Summary. **then** introduce ambiguity, an unstated participant, two independent Claims, an added Projection meaning, an independent vocabulary entry, **and** a confidence result below the effective Confidence Threshold resolved according **to** CA-M-271-CORE_META_MODEL-IMPLEMENTATION_METHOD--resolve-confidence-thresholds-by-source-precedence.

### Acceptance criteria

**every** valid fixture has **`=1`** precise interpretation, a source-faithful Summary, **and** reproducible Projections **when** requested. no fixture fails merely because an optional Projection was **not** requested. **every** invalid fixture fails. a confidence result below the effective Confidence Threshold leaves the Atom unchanged **and** requests Operator disposition. changing the applicable Operator input, Plan override, enclosing Hub override, **or** Framework Instance Settings default changes the checked threshold according **to** CA-M-271-CORE_META_MODEL-IMPLEMENTATION_METHOD--resolve-confidence-thresholds-by-source-precedence **without** retaining a fixed percentage gate.

### Failure disposition

record a Concern naming the affected Claim **or** Projection.
