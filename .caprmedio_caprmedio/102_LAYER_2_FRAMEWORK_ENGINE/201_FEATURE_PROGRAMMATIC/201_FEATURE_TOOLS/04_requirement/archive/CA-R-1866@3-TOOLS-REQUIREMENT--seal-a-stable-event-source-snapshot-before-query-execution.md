---
atom_id: CA-R-1866@3
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-14 18:44:20 +0400"
subjects:
  governs: "FIND_AND_FETCH_JOURNAL_EVENTS/source snapshot"
  depends_on: [Journal, Event, Workflow Run, Action Run, Tool]
relations:
  relates_to: [CA-O-163, CA-M-334, CA-E-578]
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
