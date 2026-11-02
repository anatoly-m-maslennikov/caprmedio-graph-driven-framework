---
subjects:
  governs: Artifact.Activity
  depends_on:
  - Artifact
  - Artifact.Status
version: 14
updated_at: 2026-10-24 00:38:25 +0400
relations: {}
atom_id: CA-R-1307@14
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
---
# Summary

Limit Artifact Activity to explicit Status models

## Scope

Artifacts to which explicitly defined Status models apply.

## Claim

an Artifact **must** have **`=1`** Activity **in** (Active, Inactive) **if** an explicitly defined Status model applies **to** it, **and** **`=0`** Activity **otherwise**.

## Details
