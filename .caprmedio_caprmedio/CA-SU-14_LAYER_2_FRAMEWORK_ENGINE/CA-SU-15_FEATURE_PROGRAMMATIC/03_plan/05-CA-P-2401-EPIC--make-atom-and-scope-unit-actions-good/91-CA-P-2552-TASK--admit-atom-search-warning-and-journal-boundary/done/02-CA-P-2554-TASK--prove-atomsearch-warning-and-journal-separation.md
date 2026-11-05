---
atom_id: CA-P-2554
ref_id: CA-P-2554
container:
  atom: CA-P-2552
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Runtime Failure Classification
tier: 3
relations:
  is_decomposition_of:
  - CA-P-2552
  depends_on:
  - CA-P-2553
status: Done
version: 7
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 2-CA-P-2554-TASK--prove-atomsearch-warning-and-journal-separation.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/5-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/91-CA-P-2552-TASK--admit-the-atomsearch-warning-and-journal-boundary/done
work_sequence_number: 2
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Prove AtomSearch warning and Journal separation

## Objective

Run the bounded focused acceptance for the schema-invalid scan disposition after
CA-P-2553, with exact durable test evidence and no release or deployment claim.

## Details

At most 15 minutes own work. Use a fixture or observed source set containing valid
selected Atoms around one isolated `schema_invalid` Atom. Verify valid matches are
retained, the invalid Atom is skipped, the warning contains repository-relative
path and reason, the result is `complete: false`, and no source or Journal bytes
change. Verify fatal I/O, security, duplicate-identity, stale, ambiguous, and
incomplete-frontier cases still refuse rather than return partial complete data.
Record exact module/case names, Run ID or durable log, counts, skips/failures,
warning fields, and before/after Journal evidence. Preserve the complete-suite
and public-release distinction.

### Definition of Done

Focused proof is independently attributable and shows technical warnings remain
outside business Journal records. The bounded proof is now observed; CA-C-572 remains Active because deployment and sink-policy resolution are not claimed.

### Focused proof evidence

Root's current AtomSearch suite passed 88 tests in 33.896 seconds after
the final code/helper fix. The check preserved valid matches around an isolated
schema-invalid Atom, emitted technical warning path/reason data, returned
`complete: false`, and kept source and business Journal bytes unchanged while
the fatal classes continued to refuse. The result is source/test proof only:
no installed-runtime deployment, release, or sink-path selection is claimed.
