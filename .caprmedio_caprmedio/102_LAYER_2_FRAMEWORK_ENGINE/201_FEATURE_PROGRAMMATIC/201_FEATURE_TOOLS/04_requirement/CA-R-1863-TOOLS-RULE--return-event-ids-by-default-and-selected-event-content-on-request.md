---
atom_id: CA-R-1863
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-27 20:00:04 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  depends_on: []
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
