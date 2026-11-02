---
subjects:
  active: Entity/Object/Continuant/History/Journal > Event Record
  passive:
  - Entity/Object/Continuant/History/Journal > Event Record
  - Atom.ID
  - Entity/Object/Continuant/Governing Objects/Atom.Version Number
  - Carrier
  - Atom/(.Role := Operations)
  - Journal
  - Atom
  - Project
  - 'Entity/Object/Continuant/Projection/Type: Applicable Methodology'
version: 31
updated_at: 2026-11-02 00:18:22 +0400
relations:
  evaluation_for:
  - CA-R-1491
  - CA-R-807
atom_id: CA-E-462@31
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 3
role: Evaluation
form: Eval Policy
---
## Summary

Validate Atom replacement event evidence

## Claim scope

Atom replacement event evidence.

## Claim

the Evaluation **must** check whether an Atom replacement satisfies CA-R-807. Journal acceptance is **not** proof that the replacement is correct.

## Details

### Checks

- report a failed replacement Evaluation **if** predecessor **or** successor identities are missing, unresolved, duplicate, self-referencing, **or** mismatched.
- verify that **every** named successor was Active **before** the predecessor was archived, that the archived current predecessor preserves its body, Summary, identity **and** every metadata value except Version, archived Status **and** archive-time Updated At, with Version incremented by exactly **`1`** **and** actual archive-time Updated At. verify retained exact prior Revision bytes, including the prior Version, Status **and** Updated At, **and** that **`=1`** authoritative Journal event records that replacement.
- check event field representation against the selected Delivery authority. a format check alone **must not** be reported as proof of replacement correctness.
- repeated submission of the same event **must not** create another authoritative record.

### Failure disposition

a failed **or** unresolved replacement Evaluation **must not** prevent the Journal from preserving the observed event under CA-R-1491. preserve the supplied identities **and** evidence **without** inventing a conforming replacement **or** claiming that a failed check passed. correction changes the governed source through its authorized Workflow; it does **not** rewrite accepted history.

this Evaluation **must not** require a Git Commit **or** a particular Journal serialization.
