---
atom_id: CA-R-1787
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/Graph Node/Engineering/Verification
  depends_on: []
version: 7
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
tier: 3
type: Rule
---
# Summary

Exclude log prose as sole production-evaluation evidence

## Scope

production evaluation decisions.

## Claim

a production evaluation decision **must not** depend solely on parsing free-form log prose.

## Details

free-form log prose alone is **not** sufficient evidence for a production evaluation decision.
