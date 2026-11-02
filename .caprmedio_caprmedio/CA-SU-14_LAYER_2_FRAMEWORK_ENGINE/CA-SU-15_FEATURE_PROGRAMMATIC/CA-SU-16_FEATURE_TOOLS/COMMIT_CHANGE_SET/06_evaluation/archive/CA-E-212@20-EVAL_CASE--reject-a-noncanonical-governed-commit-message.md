---
subjects:
  governs: Subject/Engineering/Git/Commit
  depends_on: []
version: 20
updated_at: 2026-10-24 22:06:39 +0400
relations:
  evaluation_for:
  - CA-R-805
  - CA-D-417
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-212@20
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Reject a noncanonical governed commit message

## Claim checked

the Git gate accepts a real-change message **only** **when** it is the Initiative-based Projection for its sealed action.

## Test case

For one valid atomic action, present the exact `<initiative-summary> | <CHANGE_CLASS> | <affected-subject>` message **and** variants with a technical parent, changed class, changed subject, extra body line, **or** trailer. Separately present the Journal-batch form for a real-change action.

## Acceptance criteria

**only** the exact real-change Projection succeeds. Every altered **or** Journal-batch form fails **before** the Git effect **without** changing the message carrier, index, working tree, governed source, Journal, refs, **or** runtime state.

## Failure disposition

Reject the delivery **if** a noncanonical message passes, the canonical message fails, **or** message validation mutates project state.
