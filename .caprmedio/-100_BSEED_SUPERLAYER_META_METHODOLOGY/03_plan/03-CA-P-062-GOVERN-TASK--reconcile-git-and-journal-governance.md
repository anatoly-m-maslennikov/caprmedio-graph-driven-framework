---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    continuant:
      - provenance
    occurrent:
      - version-control
  prerequisite:
    continuant:
      - work-journal
version: 3
updated_at: 2026-08-23 15:24:07
autonomous_confidence_threshold: 98
---
# Reconcile Git and Journal governance

THE Assignee MUST replace or revise the conflicting BSEED Governance authority for governed Git commits and Project Work Journal records so that it states only mechanism-neutral constraints compatible with their independent provenance responsibilities.

## Scope

`(Atom ID IN (CAPRMEDIO-GOV-REQU-309--use-direct-typed-relation-change-set-commit-messages))`

## Definition of Done

THE Task is NOT DONE IF (the active BSEED Governance authority still requires one governed subject per Git commit OR derives the complete Git commit message from one Journal event OR makes Git history and Journal history one coupled transaction OR duplicates PROGRAMMATIC mechanism authority OR the exact Task Scope Resolution and replacement disposition are not recorded).

## Details

Preserve the higher-order requirements that Git and the Project Work Journal provide durable provenance and that Journal carriers are versioned through Git. Remove BSEED commitments to the current `governed_file_change` schema, direct-relation commit-message rendering, one-file commit cardinality, and journal-sidecar commit coupling. Leave repository concurrency, Initiative projection, batching, queueing, leases, and concrete Tool topology to Project-local PROGRAMMATIC authority.
