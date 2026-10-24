---
atom_id: CA-R-1863
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: 2026-10-24 00:38:25 +0400
subjects:
  governs: Subject/Domain/Node/Continuant/History/Journal.Record
  depends_on:
  - Subject/Engineering/Journal Event Query/Result Selection
relations:
  relates_to:
  - CA-O-162
  - CA-M-336
  - CA-E-576
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
