---
atom_id: CA-E-511
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Target Scope Unit
  passive:
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Local Scope Unit
  - CAPRMEDIO_MODEL <+ Atom.Subjects
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Scope Unit
version: 23
updated_at: 2026-11-02 00:18:22 +0400
relations:
  evaluation_for:
  - CA-D-482
  - CA-D-495
  - CA-R-1271
  - CA-R-1588
  - CA-R-1595@21
  - CA-R-1596
  - CA-R-922
  - CA-R-923
tier: 4
role: Evaluation
form: Eval Case
---
## Summary

Validate Target Scope Unit **and** textual Claim Scope

## Claim scope
the distinction between an Atom's Claim Target Scope Unit **and** its textual applicability.

## Claim

**Claim checked.**

**every** Atom resolves **`=1`** GOVERNS Subject and zero **or** one Claim Target Scope Unit; applicable Goal and Demand rules, including the Operator-owned Project Goal, retain their required target conditions. Claim Scope remains applicability restrictions **in** the body sections registered by CA-D-495, including Claim scope for RMED, **not** another structural target **or** frontmatter Property.

## Details

### Test case

create a Current-scope Atom with its own Scope Unit explicitly carried as target **and** a Claim restricted **to** Python files; repeat with a composite restriction. for RMED, carry those restrictions **in** Claim scope **and** the qualified contribution **in** Claim. create a permitted Demand with a different explicit target, a parent-owned Goal for its direct child, an external Project Goal with its Author's registered Operator name **and** an explicit Project target, **and** a Plan inside nested Container Atoms. **then** omit the internally required target even **when** filename **or** placement identifies its owner, provide two targets, use a Container Atom as a target, leave the target unresolved, duplicate textual applicability **in** frontmatter, **or** infer a target **or** ownership change from the textual restriction alone.

### Acceptance criteria

valid Atoms resolve **to** **`=1`** GOVERNS Subject and zero **or** one Claim Target Scope Unit. authoring defaults select **and** carry the current Scope Unit as target **where** applicable; reading does **not** repair a required omitted target from placement; external Project Goals retain their explicit Project target. narrower **or** composite applicability alone leaves a Current-scope Atom Current-scope. a different permitted target yields an Atom with a distinct Target Scope Unit **without** transferring ownership **or** changing Scope Unit ancestry. Container Atom nesting does **not** create another target. **every** invalid fixture fails with the exact missing, unresolved, duplicate, misclassified, **or** independently duplicated fact identified.

### Failure disposition

report the affected Atom **and** target, ownership, **or** textual-applicability distinction; preserve the source **until** an authorized correction is selected.
