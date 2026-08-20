---
subject_scopes:
  - provenance
version: 3
updated_at: 2026-08-20 21:27:00
relations:
  delivery_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS_OPS_TOOLS--process-one-file-change
    - CA-R-803-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--emit-only-operational-hook-triggers
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--gather-complete-commit-action-context
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--commit-one-governed-file-action
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--append-governed-file-change-journal-records
---
# Deliver project-local commit automation

Deliver the OPS_TOOLS file-change flow through the shared project-local Tool runtime under `.caprmedio_runtime`. The delivery exposes one opt-in repository Hook adapter that emits `COMMIT_TRIGGER`, one independently invocable `COMMIT_CONTEXT` Finder, the `APPEND_CHANGE_RECORDS` Journal Doer, and the `COMMIT_CHANGE_SET` Git Doer, with the complete flow available in dry-run and apply modes through the common Tool interface. The Hook passes its trigger into the same context-gather, Journal-append, and commit pipeline without classifying or mutating, and suppresses every pipeline-owned Journal append from recursive triggering. Operators may also invoke each Tool manually. Trigger, context, structured Journal record set, ordered receipt set, deterministic message Projection, and result envelopes must be machine-readable, schema-versioned, and sufficient for replay and deterministic diagnostics. Installation and removal of the Hook must preserve any pre-existing repository Hook behavior. No delivery component writes backup copies.
