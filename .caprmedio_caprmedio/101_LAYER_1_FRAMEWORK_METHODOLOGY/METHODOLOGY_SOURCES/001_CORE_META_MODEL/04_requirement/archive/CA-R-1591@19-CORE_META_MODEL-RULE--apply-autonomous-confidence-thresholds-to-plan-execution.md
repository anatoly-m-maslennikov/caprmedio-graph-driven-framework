---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan.Autonomous Confidence Threshold'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan/Type: Plan'
  - Subject/Graph Node/Engineering/Execution Control/Decision Confidence
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
version: 19
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
atom_id: CA-R-1591@19
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Apply autonomous confidence thresholds to Plan execution

## Scope

autonomous continuation of Plan work.

## Claim

autonomous continuation of Plan work **must** satisfy its effective Autonomous Confidence Threshold:

- resolve the value under CA-M-271-CORE_META_MODEL-IMPLEMENTATION_METHOD--resolve-confidence-thresholds-by-source-precedence.
- **if** confidence **in** correct execution is below it, request Operator disposition **before** continuing.
- **otherwise**, continue **only** within existing authority; meeting the threshold does **not** grant additional authority.

## Details
