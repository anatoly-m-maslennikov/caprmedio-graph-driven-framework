---
atom_id: CA-E-579
content_role: Evaluation
type: Eval Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Implementation/Code/Tool
  depends_on:
  - Subject/Graph Node/Engineering/Execution Control/Effect Authorization
  - Subject/Graph Node/Engineering/Data Handling/Source Retrieval
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Evaluation'
relations:
  evaluation_for:
  - CA-R-1864
tier: 4
---
# Summary

Verify Journal query read-only and secret exclusion

## Claim

The Tool rejects mutation, credential, secret, arbitrary SQL, and arbitrary-code requests without reading protected values or changing Journal data.

## Test case

Submit each forbidden parameter against a before/after Journal digest and protected-value sentinel.

## Acceptance criteria

Each request is rejected with a boundary diagnostic; the Journal digest and sentinel access count are unchanged.

## Failure disposition

Reject any mutation authority, protected-value read, or executable interpretation.
