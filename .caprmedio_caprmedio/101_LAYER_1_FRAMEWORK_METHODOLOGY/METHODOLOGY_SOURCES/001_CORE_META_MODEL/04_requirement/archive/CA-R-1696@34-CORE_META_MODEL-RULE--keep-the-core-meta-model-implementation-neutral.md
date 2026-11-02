---
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit//CORE_META_MODEL
  depends_on: []
version: 34
updated_at: 2026-10-29 10:13:49 +0400
relations:
  child_of:
  - CA-M-001
  - CA-M-261
atom_id: CA-R-1696@34
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Keep the Core Meta-Model implementation neutral

## Claim scope

CORE_META_MODEL authority and its reusable model invariants and expansion boundaries.

## Claim

CORE_META_MODEL authority **must** define reusable model invariants **and** expansion boundaries **without** hidden dependence on a programming language, LLM provider **or** model, agent host, operating system, repository host, package manager, database, deployment platform, **or** other replaceable implementation mechanism.

mechanism-specific obligations belong **to** the Scope that owns the mechanism. Extensions **and** PROJECT_CONFIGURATION **may** expand the model for their bounded use **without** rewriting its governing Claims.

CORE_META_MODEL **may** name a mechanism **only** **when** the mechanism itself is the explicit Entity governed by the Claim, such as a Carrier format, portability boundary, **or** external constraint; this reference **must not** make that mechanism a hidden prerequisite of unrelated model Claims.
