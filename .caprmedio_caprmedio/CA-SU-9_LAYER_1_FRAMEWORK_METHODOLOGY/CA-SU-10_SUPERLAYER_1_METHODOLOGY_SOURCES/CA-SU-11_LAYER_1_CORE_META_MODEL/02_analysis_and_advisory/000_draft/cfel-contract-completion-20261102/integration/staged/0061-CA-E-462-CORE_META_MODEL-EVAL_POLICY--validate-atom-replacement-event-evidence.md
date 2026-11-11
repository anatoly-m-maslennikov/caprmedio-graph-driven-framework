---
subjects:
  active: Event Record
  passive:
  - Atom.ID
  - Atom.Version Number
  - Carrier
  - Atom/(.Role := Operations)
  - Journal
  - Atom
  - Project
  - Projection
version: 34
updated_at: 2026-11-02 07:49:21 +0400
relations:
  evaluation_for:
  - CA-R-1491
  - CA-R-807
atom_id: CA-E-462
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Evaluation
form: Eval Policy
---
## Summary

Validate Atom replacement event evidence

## Claim scope

Atom replacement event evidence.

## Claim

an Event Record offered as Atom replacement evidence **must** undergo an actual Evaluation against CA-R-807. Available evidence and Journal acceptance are **not** proof that the replacement is correct.

## Details

### Checks

the Evaluation of that Event Record **must** run and report a passing, failed, or unresolved result. It **must**:

- report a failed replacement result **if** predecessor **or** successor identities are missing, unresolved, duplicate, self-referencing, **or** mismatched;
- verify that **every** named successor was Active **before** the predecessor was archived, that the archived predecessor preserves its body, Summary, identity, numeric Version, and prior Updated At, with only archived Status changed on its Archive Carrier; verify retained exact prior Revision bytes, including the prior Version, Status **and** Updated At, and that **`=1`** authoritative Journal Event Record records that replacement;
- distinguish selected Carrier representation evidence from proof of replacement correctness; and
- treat repeated submission of the same Event Record as non-evidence of another authoritative record.

### Failure disposition

an Event Record whose actual Evaluation reports failure **or** uncertainty **must not** be treated as a conforming replacement merely because the Journal preserves it under CA-R-1491. Its correction disposition **must** route a governed-source change through its authorized Workflow and **must not** rewrite accepted history.

this Evaluation **must not** require a Git Commit **or** a particular Journal serialization. Available evidence without the performed Evaluation and its reported result is **not** a passing result.
