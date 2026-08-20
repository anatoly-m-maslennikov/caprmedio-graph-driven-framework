---
subject_scopes:
  - feature-boundary
version: 10
updated_at: 2026-08-21 00:01:00
relations:
  child_of:
    - CA-R-802-REQUIREMENT-FR_ENGN_TOOLS--define-flat-auto-commit-tool-topology
    - CAPRMEDIO-GOV-REQU-309--revision-bound-parent-child-commit-messages
    - CAPRMEDIO-GOV-REQU-339--register-work-journal-events
---
# Gather complete commit action context

`COMMIT_CONTEXT` must be independently invocable and strictly read-only. From one Hook trigger, it validates the adapter, source-event, trigger, repository, and structured LLM-session candidate identities; deterministically resolves exactly one governed subject identity and its `ADD`, `MOVE`, `UPDATE`, `MOVE+UPDATE`, or `REMOVE` change set; reads the applicable staged, working, committed, Journal, graph, and repository apply-lease states; and gathers the complete direct typed upstream relation set from the canonical relation registry, paths, filenames, versions, content and frontier digests, Git base, and validation results required by the Doers. The same trigger and unchanged source frontier must yield the same action and event identities. Before-state data may exist inside this sealed ephemeral context only to classify and validate the change; it must not be copied into the Work Journal event.

The Finder seals the canonical schema-version `2` structured change event: stable event and action identities, adapter and source-event provenance, structured `llm_session` with canonical `app` and host `uuid`, author, one timezone-qualified `occurred_at` and local calendar date, configured timezone, `action_type`, ordered `sources`, singular resulting `result`, and `previous_result_event` when one exists. It resolves LLM-session values through the registered application adapter, preferring an explicit validated invocation value, and fails closed rather than guess when required provenance is absent or ambiguous. It resolves the author and event time exactly once; all downstream Tools must use these sealed author, timezone, `occurred_at`, and local-date values without recomputing them. The sealed values and event identity must remain unchanged on retry; `<app>:<uuid>:<occurred_at>` is only a derived presentation.

When a non-`ADD` subject has no accepted prior result event, the Finder also seals a candidate `recovered` baseline record and the exact evidence required by the recovery rule. It predicts the complete ordered Journal sidecar record set, every target partition, repository lease availability, and the Git message Projection governed by the canonical commit-message rule without storing that message as Journal authority. An explicit author must be a full GitHub username; when omitted, the Finder resolves the current operator's full GitHub username and fails closed if it cannot do so unambiguously. It derives `MOVE` from a Structural-location change and `UPDATE` from a content, filename, or other governed carrier-state change, emitting `MOVE+UPDATE` when both flags are true. It must not edit governed files, copy LLM-session event provenance into Atoms or Projections, append Journals or Projections, acquire an apply lease, change the Git index, or create or rewrite Git history. Context gathering is mandatory, but `COMMIT_CHANGE_SET` may invoke the same deterministic logic internally instead of requiring a separate standalone call.
