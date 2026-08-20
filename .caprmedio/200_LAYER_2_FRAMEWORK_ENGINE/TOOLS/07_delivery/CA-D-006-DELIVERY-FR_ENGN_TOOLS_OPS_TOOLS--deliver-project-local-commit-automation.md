---
subject_scopes:
  - provenance
version: 1
updated_at: 2026-08-20 19:44:00
relations:
  delivery_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS_OPS_TOOLS--process-one-file-change
    - CA-R-803-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--emit-only-operational-hook-triggers
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--gather-complete-commit-action-context
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--commit-one-governed-file-action
---
# Deliver project-local commit automation

Deliver the OPS_TOOLS commit flow through the shared project-local Tool runtime under `.caprmedio_runtime`. The delivery exposes one opt-in repository Hook adapter that emits `COMMIT_TRIGGER`, one independently invocable `COMMIT_CONTEXT` Finder, and one `COMMIT_CHANGE_SET` Doer available in dry-run and apply modes through the common Tool interface. The Hook passes its trigger to the same Tool flow without classifying or mutating; operators may also invoke either Tool manually. Trigger, context, and result envelopes must be machine-readable, schema-versioned, and sufficient for replay and deterministic diagnostics. Installation and removal of the Hook must preserve any pre-existing repository Hook behavior. No delivery component writes backup copies.
