---
subjects:
  active: Scope Unit//CORE_META_MODEL
version: 37
updated_at: 2026-11-02 19:44:26 +0400
relations:
  child_of:
  - CA-M-447
  - CA-M-261
atom_id: CA-R-1696
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Keep the Core Meta-Model implementation neutral

## Claim scope

CORE_META_MODEL authority and its reusable model invariants and expansion boundaries.

## Claim

CORE_META_MODEL authority **must** define reusable model invariants **and** expansion boundaries **without** hidden dependence on a programming language, LLM provider **or** model, agent host, operating system, repository host, package manager, database, deployment platform, **or** other replaceable implementation mechanism.

mechanism-specific obligations belong **to** the Scope that owns the mechanism. Extensions **and** PROJECT_CONFIGURATION **may** expand the model for their bounded use **without** rewriting its governing Claims.

CORE_META_MODEL **may** name a mechanism **only** **when** the mechanism itself is the explicit Entity governed by the Claim, such as a Carrier format, portability boundary, **or** external constraint; this reference **must not** make that mechanism a hidden prerequisite of unrelated model Claims.
