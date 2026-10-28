---
version: 29
updated_at: 2026-10-27 06:04:45 +0400
relations:
  child_of:
  - CA-E-001
  evaluation_for:
  - CA-M-298
  - CA-R-1375
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Scope Unit.Expansion Boundary
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Scope Unit//CORE_META_MODEL
  - Subject/Graph Node/Product/Extension
  - Subject/Graph Node/Domain/Continuant/Scope Unit//PROJECT_CONFIGURATION
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node
  - Subject/Graph Node/Domain/Continuant/Atom.Tier
atom_id: CA-E-249@29
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Policy
tier: 3
---
# Summary

Evaluate methodology expansion mappings

## Scope

methodology expansion mappings.

## Claim

a methodology expansion mapping Evaluation **must** return `fail` **if** a source element, exact canonical target, mapping rule, intended Scope, **or** applicable Core Meta-Model distinction at **any** numeric Tier is missing, canonical ownership is ambiguous, preservation is unproven, **or** the mapping redefines, replaces, shadows, weakens, deletes, contradicts, **or** reinterprets applicable Core Meta-Model authority at **any** numeric Tier; it **must** return `pass` **only** **when** the declared mapping preserves that authority **and** stays within its permitted expansion boundary. an Operator-approved loss **must not** count as conformance; report the failed boundary **and** leave the affected application stopped.

## Details
