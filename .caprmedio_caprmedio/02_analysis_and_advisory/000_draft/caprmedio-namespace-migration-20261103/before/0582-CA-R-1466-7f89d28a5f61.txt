---
subjects:
  active: Aspects <+ Engineering <+ Architecture <+ Component Structure
  passive:
  - Scope Unit//CORE_META_MODEL
  - Journal
  - Projection
  - Scope Unit//PROJECT_CONFIGURATION
version: 23
updated_at: 2026-11-02 18:35:20 +0400
relations: {}
atom_id: CA-R-1466
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Keep Git integration in an Extension

## Claim scope

Git integration in the Core Meta-Model.

## Claim

Git integration **must** be optional Extension authority, **not** a prerequisite of the Core Meta-Model. Git commit policies, commit-message encodings, hooks, **and** event-to-commit references belong **to** that Extension; selecting it **must not** replace the authoritative Journal **or** make Git history an independent source for the same recorded facts. the Core Meta-Model **must** remain applicable **without** Git integration.
