---
version: 36
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-E-001
  evaluation_for:
  - CA-M-298
  - CA-R-1375
subjects:
  active: Scope Unit
  passive:
  - Scope Unit//CORE_META_MODEL
  - Scope Unit
  - Scope Unit//PROJECT_CONFIGURATION
  - Entity/Object/Continuant/Actor/Operator
  - Entity
  - Atom.Tier
atom_id: CA-E-249
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Evaluation
form: Eval Policy
---
## Summary

Evaluate methodology expansion mappings

## Claim scope

methodology expansion mappings.

## Claim

a methodology expansion mapping Evaluation **must** return `fail` **if** a source element, exact canonical target, mapping rule, intended Scope, **or** applicable Core Meta-Model distinction at **any** numeric Tier is missing, canonical ownership is ambiguous, preservation is unproven, **or** the mapping redefines, replaces, shadows, weakens, deletes, contradicts, **or** reinterprets applicable Core Meta-Model authority at **any** numeric Tier; it **must** return `pass` **only** **when** the declared mapping preserves that authority **and** stays within its permitted expansion boundary. an Operator-approved loss **must not** count as conformance; report the failed boundary **and** leave the affected application stopped.
