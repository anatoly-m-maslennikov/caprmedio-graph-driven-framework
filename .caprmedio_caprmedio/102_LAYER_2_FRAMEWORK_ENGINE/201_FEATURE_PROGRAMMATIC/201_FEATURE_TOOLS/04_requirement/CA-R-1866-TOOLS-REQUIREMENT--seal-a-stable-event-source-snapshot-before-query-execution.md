---
atom_id: CA-R-1866
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 5
updated_at: 2026-10-24 00:38:25 +0400
subjects:
  governs: Subject/Engineering/Journal Event Query/Stable Source Snapshot
  depends_on:
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Domain/Node/Occurrent/Execution
  - Subject/Domain/Node/Continuant/History/Journal.Record
relations:
  relates_to:
  - CA-O-163
  - CA-M-334
  - CA-E-578
type: Rule
tier: 3
---
# Summary

Seal a stable Event source snapshot before query execution

## Scope

The query-source snapshot.

## Claim

FIND_AND_FETCH_JOURNAL_EVENTS **must** bind an immutable source snapshot before
workflow/action-start execution evidence can append and must not enlarge that
snapshot with its own execution Events.

## Details

The token binds the source root, raw-Journal byte-prefix length and hash, ordered
member references, member byte hashes and actually supplied string Event IDs,
without deduplication or a unique-ID requirement. Capture all decoded rows,
including rows without a string ID; preserve their recorded JSON unchanged.
Before every
continuation it revalidates the source/prefix hashes and captured members:
changed, deleted, unreadable, or truncated members reject continuation; bytes
appended only after the sealed prefix do not. An unavailable, changed, or
incomplete frontier cannot claim complete coverage.
