---
subject_scopes:
  - provenance
version: 4
updated_at: 2026-08-20 22:04:00
relations:
  delivery_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS_OPS_TOOLS--process-one-file-change
    - CA-R-803-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--emit-only-operational-hook-triggers
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--gather-complete-commit-action-context
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--commit-one-governed-file-action
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--append-governed-file-change-journal-records
---
# Deliver project-local commit automation

Deliver the OPS_TOOLS file-change flow through the shared project-local Tool runtime under `.caprmedio_runtime`. The delivery exposes one replaceable Hook-adapter interface with explicit install, status, enable, disable, and uninstall controls; one independently invocable `COMMIT_CONTEXT` Finder; the `APPEND_CHANGE_RECORDS` Journal Doer; and the `COMMIT_CHANGE_SET` Git Doer, with the complete flow available in dry-run and apply modes through the common Tool interface. Each enabled adapter must declare its substrate boundary and stable source-event identity semantics, emit the canonical `COMMIT_TRIGGER` without classifying or mutating, and suppress pipeline-owned Journal and runtime-state writes through action correlation. Operators may invoke each Tool manually and must be able to observe the enabled adapter, current repository lease, pending or blocked action, last completed action, and deterministic recovery instruction without specialist Hook or Git knowledge. Trigger, context, structured Journal record set, ordered receipt set, lease token and disposition, deterministic message Projection, and result envelopes must be machine-readable, schema-versioned, and sufficient for replay and deterministic diagnostics. Installation and removal of an adapter must preserve any pre-existing repository Hook behavior. No delivery component writes backup copies, and no disabled or uninstalled adapter emits a trigger.
