---
subject_scopes:
  - feature-boundary
version: 4
updated_at: 2026-08-20 20:13:00
relations:
  child_of:
    - CA-R-802-REQUIREMENT-FR_ENGN_TOOLS--define-ops-tools-feature-group
---
# Gather complete commit context

`COMMIT_CONTEXT` must be one independently invocable Finder Tool owned immediately by `OPS_TOOLS`. From one Hook trigger, it deterministically resolves exactly one affected file identity and its `ADD`, `MOVE`, `UPDATE`, `MOVE+UPDATE`, or `REMOVE` change set; reads the applicable staged, working, committed, and graph states; and gathers the complete direct typed upstream relation set from the canonical relation registry, before and after paths, filenames, versions, content and frontier digests, Git base, and validation results required by the Doers. It also seals one stable Journal event identity, the event author, occurrence time and local calendar date, configured timezone, canonical `action_message`, and predicted Journal partition. An explicit author must be a full GitHub username; when omitted, the Finder resolves the current operator's full GitHub username and fails closed if it cannot do so unambiguously. It derives `MOVE` from a Structural-location change and `UPDATE` from a content, filename, or other governed carrier-state change, emitting `MOVE+UPDATE` when both flags are true. It must not edit governed files, append Journals or Projections, change the Git index, or create or rewrite Git history. Context gathering is mandatory, but an orchestrating Doer may invoke the same logic internally when the standalone Finder interface is skipped.
