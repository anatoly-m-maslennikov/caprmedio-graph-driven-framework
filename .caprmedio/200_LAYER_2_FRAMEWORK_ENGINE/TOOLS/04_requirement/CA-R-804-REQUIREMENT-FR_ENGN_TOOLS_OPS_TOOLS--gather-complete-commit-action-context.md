---
subject_scopes:
  - feature-boundary
version: 1
updated_at: 2026-08-20 19:16:46
relations:
  child_of:
    - CA-R-802-REQUIREMENT-FR_ENGN_TOOLS--define-ops-tools-feature-group
---
# Gather complete commit-action context

`COMMIT_CONTEXT` must be one optional Finder Tool owned immediately by `OPS_TOOLS`. From one Hook trigger, it deterministically resolves exactly one affected file identity and its `ADD`, `UPDATE`, or `REMOVE` action; reads the applicable staged, working, committed, and graph states; gathers the complete direct typed upstream relation set, filenames, versions, content and frontier digests, Git base, and validation results required by the commit Doer; and returns one sealed context envelope. It must not edit governed files, write Journals or Projections, change the Git index, or create or rewrite Git history. When this standalone Finder is skipped, the Doer must invoke the same context-gathering logic internally.
