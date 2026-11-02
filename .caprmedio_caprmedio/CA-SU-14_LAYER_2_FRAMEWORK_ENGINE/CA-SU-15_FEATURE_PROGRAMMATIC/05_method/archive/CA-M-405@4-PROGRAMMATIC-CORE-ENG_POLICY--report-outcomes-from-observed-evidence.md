---
atom_id: CA-M-405@4
content_role: Method
type: Eng Policy
current_scope_unit: PROGRAMMATIC
status: Archived
subjects:
  governs: Subject/Engineering/Outcome Evidence
  depends_on:
  - Subject/Engineering/Statement Authority
version: 4
updated_at: 2026-10-24 00:38:25 +0400
author: Anatoly Maslennikov
tier: 1
---
# Summary

Report outcomes from observed evidence

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and tests.

## Claim

**To** execute PROGRAMMATIC behavior and report its outcome, compare the requested result with observed effects and retained execution evidence, distinguish verified completion, verified no-op, partial effects and uncertain effects, and reuse established evidence rather than blindly replaying completed or uncertain mutations.

## Details

Candidate source: [CA-M-390@2](archive/CA-M-390-PROGRAMMATIC-CORE--report-outcomes-from-observed-evidence@2.md)

- A returned call, scheduler completion or absence of reported errors does not alone establish the requested result.
- A no-op means the requested state was already satisfied and remained unchanged; do not fabricate writes or history.
- Preserve partial results, uncertainty, gaps and blockers honestly. Outcome reporting introduces no automatic retry or recovery policy.

Source basis: CA-M-376, CA-M-323, CA-M-322.
