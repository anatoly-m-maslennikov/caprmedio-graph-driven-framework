---
subjects:
  governs: Artifact.Activity
  depends_on:
  - Subject/Domain/Node/Continuant/Term//Artifact
  - Artifact.Status
version: 18
updated_at: 2026-10-24 12:35:51 +0400
relations: {}
atom_id: CA-R-1307@18
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Limit Artifact Activity to explicit Status models

## Scope

Artifacts to which explicitly defined Status models apply.

## Claim

an Artifact **must** have **`=1`** Activity **in** (Active, Inactive) **if** an explicitly defined Status model applies **to** it, **and** **`=0`** Activity **otherwise**.

## Details
