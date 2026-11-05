---
atom_id: CA-P-2709
ref_id: CA-P-2709
container:
  atom: CA-P-2694
role: Plan
form: Plan
label: Task
topics:
  main_subject: CAPRMEDIO_MODEL
  dependencies:
  - CAPRMEDIO_STRUCTURE

tier: 4
status: Done
version: 2
updated_at: 2026-11-03 18:44:41 +0400
current_scope_unit: caprmedio
---
## Summary

Simplify MODEL and STRUCTURE Subject roots

## Objective

Mechanically replace CAPRMEDIO <+ MODEL with CAPRMEDIO_MODEL and CAPRMEDIO <+ STRUCTURE with CAPRMEDIO_STRUCTURE in selected canonical live Subjects.

## Scope

Change only frontmatter subjects.active and subjects.passive string prefixes. Preserve every other source byte, including Claims, IDs, versions, timestamps and relation fields. Use the prior canonical frontier plus actual direct-role Drafts. Preserve historical, delivery, installed, staging and projection snapshots.

## Steps

1. Freeze the exact canonical file list and hashes.
2. Review the simple scalar-preserving script and candidate differences.
3. Apply in place, with no Draft-promotion cycle for this mechanical change.
4. Independently verify the same Subject-only differences and idempotence.

## Definition of Done

Every selected old prefix is replaced; other bytes match the saved preimage; the script is idempotent. Record exact counts and hashes. Keep subsequent Header/Claim/alias Epic work separate.

## Evidence

The root-subject-migration-20261103 packet contains the script, tests, explicit source frontier, application receipt and verification.

## Result

Applied and independently verified: 1,178 canonical live files, 3,685 Subject values (3,280 MODEL and 405 STRUCTURE). Every other source byte was preserved, including IDs, versions, timestamps and bodies. The second apply changed zero files. Six script tests passed. Historical, delivery, installed and staged copies were not selected.

This completion update is a separate Plan lifecycle change after the Subject-only migration proof. The application and independent-verification receipts retain the exact migration-time source hashes.
