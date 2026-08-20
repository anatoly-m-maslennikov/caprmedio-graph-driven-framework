---
subject_scopes:
  - provenance
version: 6
updated_at: 2026-08-20 22:36:00
relations:
  delivery_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS_OPS_TOOLS--process-one-file-change
    - CA-R-803-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--emit-only-operational-hook-triggers
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--gather-complete-commit-action-context
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--commit-one-governed-file-action
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--append-governed-file-change-journal-records
---
# Deliver project-local commit automation

Deliver the OPS_TOOLS file-change flow through the shared project-local Tool runtime under `.caprmedio_runtime`. The delivery exposes one replaceable Hook-adapter interface with explicit install, status, enable, disable, and uninstall controls; one independently invocable `COMMIT_CONTEXT` Finder; the `APPEND_CHANGE_RECORDS` Journal Doer; and the `COMMIT_CHANGE_SET` Git Doer, with the complete flow available in dry-run and apply modes through the common Tool interface. Each enabled adapter must declare its substrate boundary, stable source-event identity semantics, canonical LLM application name, and deterministic host-session UUID resolver; emit the canonical `COMMIT_TRIGGER` without classifying or mutating; and suppress pipeline-owned Journal and runtime-state writes through action correlation. A validated session value supplied by the invoking Skill or operator takes precedence over host discovery. The Codex adapter resolves `CODEX_THREAD_ID` and falls back to `CODEX_SESSION_ID`; every other LLM application adapter must register an equivalent explicit host interface and must fail closed rather than infer a UUID from unrelated process state. Operators may invoke each Tool manually and must be able to observe the enabled adapter, resolved LLM application and session UUID, current repository lease, pending or blocked action, last completed action, and deterministic recovery instruction without specialist Hook or Git knowledge. Trigger, context, structured Journal record set, ordered receipt set, lease token and disposition, deterministic message Projection, and result envelopes must be machine-readable, schema-versioned, and sufficient for replay and deterministic diagnostics. Trigger and context envelopes may carry `llm_session` and `occurred_at` ephemerally, but the delivery persists those values only in Journal events; Atom and Projection carriers receive no copy, and `.caprmedio_runtime` recovery state retains only identifiers and receipts that resolve the canonical Journal record. Installation and removal of an adapter must preserve any pre-existing repository Hook behavior. No delivery component writes backup copies, and no disabled or uninstalled adapter emits a trigger.
