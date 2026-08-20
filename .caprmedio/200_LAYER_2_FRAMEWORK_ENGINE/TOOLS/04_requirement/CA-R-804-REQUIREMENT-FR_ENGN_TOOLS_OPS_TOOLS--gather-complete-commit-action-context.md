---
subject_scopes:
  - feature-boundary
version: 5
updated_at: 2026-08-20 21:23:00
relations:
  child_of:
    - CA-R-802-REQUIREMENT-FR_ENGN_TOOLS--define-ops-tools-feature-group
    - CAPRMEDIO-GOV-REQU-309--revision-bound-parent-child-commit-messages
    - CAPRMEDIO-GOV-REQU-339--register-work-journal-events
---
# Gather complete commit context

`COMMIT_CONTEXT` must be one independently invocable Finder Tool owned immediately by `OPS_TOOLS`. From one Hook trigger, it deterministically resolves exactly one governed subject identity and its `ADD`, `MOVE`, `UPDATE`, `MOVE+UPDATE`, or `REMOVE` change set; reads the applicable staged, working, committed, Journal, and graph states; and gathers the complete direct typed upstream relation set from the canonical relation registry, paths, filenames, versions, content and frontier digests, Git base, and validation results required by the Doers. Before-state data may exist inside this sealed ephemeral context only to classify and validate the change; it must not be copied into the Work Journal event.

The Finder seals the canonical schema-version `2` structured change event: stable event and action identities, author, occurrence time and local calendar date, configured timezone, `action_type`, ordered `sources`, singular resulting `result`, and `previous_result_event` when one exists. When a non-`ADD` subject has no accepted prior result event, it also seals a candidate `recovered` baseline record and the exact evidence required by the recovery rule. It predicts the complete ordered Journal sidecar record set, every target partition, and the Git message Projection governed by the canonical commit-message rule without storing that message as Journal authority. An explicit author must be a full GitHub username; when omitted, the Finder resolves the current operator's full GitHub username and fails closed if it cannot do so unambiguously. It derives `MOVE` from a Structural-location change and `UPDATE` from a content, filename, or other governed carrier-state change, emitting `MOVE+UPDATE` when both flags are true. It must not edit governed files, append Journals or Projections, change the Git index, or create or rewrite Git history. Context gathering is mandatory, but an orchestrating Doer may invoke the same logic internally when the standalone Finder interface is skipped.
