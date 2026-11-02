---
atom_id: CA-R-1863@6
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 6
updated_at: 2026-10-26 05:59:45 +0400
subjects:
  governs: Subject/Graph Node/Domain/Continuant/History/Journal.Record
  depends_on:
  - Subject/Graph Node/Engineering/Journal Event Query/Result Selection
relations: {}
type: Rule
tier: 3
---
# Summary

Return Event IDs by default and selected Event content on request

## Scope

The Event result representation.

## Claim

FIND_AND_FETCH_JOURNAL_EVENTS **must** return canonical Event IDs only unless the caller explicitly requests selected Event fields or complete Events.

## Details

Selected fields retain caller order and values; complete Events retain canonical Event bytes/structure. Missing selected fields are reported per Event and never silently synthesized.
