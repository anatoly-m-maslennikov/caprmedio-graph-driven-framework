---
subject_scopes:
  - provenance
version: 9
updated_at: 2026-08-21 01:09:53
relations:
  delivery_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS--process-one-file-change
    - CA-R-802-REQUIREMENT-FR_ENGN_TOOLS--define-flat-auto-commit-tool-topology
    - CA-R-803-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_TRIGGER--emit-only-operational-hook-triggers
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CONTEXT--gather-complete-commit-action-context
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--commit-one-governed-file-action
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_APPEND_CHANGE_RECORDS--append-governed-file-change-journal-records
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-520--own-deterministic-scripts-in-tools
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-602--use-a-common-tool-cli-interface
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-603--use-one-project-local-tool-runtime
---
# Deliver project-local commit automation

Deliver the file-change flow through four peer Tool units: `COMMIT_TRIGGER`, `COMMIT_CONTEXT`, `APPEND_CHANGE_RECORDS`, and `COMMIT_CHANGE_SET`. Their canonical source carriers and shared libraries live under `.caprmedio/200_LAYER_2_FRAMEWORK_ENGINE/TOOLS`. Installation publishes one content-addressed, digest-verified, self-contained release under `.caprmedio_runtime/installed/tools/auto_commit`; installed Tools import code and read the relation registry only from that release. Runtime state, cache, Hook configuration, logs, and retained operational history occupy separate directories under `.caprmedio_runtime`. A host-required `.codex/hooks.json` carrier may be a pointer to the runtime Hook configuration but contains no framework implementation. `COMMIT_CHANGE_SET` exposes the complete dry-run and apply flow and composes the other peer interfaces without becoming their structural owner. The standalone interfaces remain available for deterministic inspection, bounded execution, and retry.

The integrated delivery exposes a replaceable Hook-adapter interface with explicit install, status, enable, disable, and uninstall controls. Each enabled adapter must declare its substrate boundary, stable source-event identity semantics, canonical LLM application name, and deterministic host-session UUID resolver; emit the canonical `COMMIT_TRIGGER` without classifying or mutating; and suppress pipeline-owned Journal and runtime-state writes through action correlation. A validated session value supplied by the invoking Skill or operator takes precedence over host discovery. The Codex adapter resolves `CODEX_THREAD_ID` and falls back to `CODEX_SESSION_ID`; every other LLM application adapter must register an equivalent explicit host interface and fail closed rather than infer a UUID from unrelated process state.

Operators may invoke each Tool manually and must be able to observe the enabled adapter, resolved LLM application and session UUID, current repository lease, pending or blocked action, last completed action, and deterministic recovery instruction without specialist Hook or Git knowledge. Trigger, context, structured Journal record set, ordered receipt set, lease token and disposition, deterministic message Projection, and result envelopes must be machine-readable, schema-versioned, and sufficient for replay and deterministic diagnostics. Trigger and context envelopes may carry `llm_session` and `occurred_at` ephemerally, but the delivery persists those values only in Journal events; Atom and Projection carriers receive no copy, and `.caprmedio_runtime` recovery state retains only identifiers and receipts that resolve the canonical Journal record. Installation and removal of an adapter must preserve any pre-existing repository Hook behavior. No delivery component writes backup copies, and no disabled or uninstalled adapter emits a trigger.
