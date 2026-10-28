---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Relation
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection//Stored Governing RMED Relation Occurrences
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Tier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
version: 28
updated_at: 2026-10-27 20:00:11 +0400
relations: {}
atom_id: CA-R-808
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Apply relation direction within its ordering domain

## Scope

declared relations.

## Claim

**every** declared relation **must** satisfy the target position **and** ordering domain registered for its relation family. Stored governing RMED relation occurrences selected by CA-R-2148 **must** use the numeric Tier-and-Scope ordering in CA-R-2149: a same-Scope target **must** have a strictly lower numeric Tier, a target in a strict ancestor Scope Unit is accepted without Tier comparison, the exact one-way Project Configuration-to-Core Meta-Model logical-role prerequisite declared by CA-R-1218 is accepted without Tier comparison, and every other descendant **or** sibling target is forbidden. Temporal relations **must** use lifecycle succession, realization relations **must** use realization order, dependency relations **must** use dependency order, **and** **every** other admitted domain **must** use its own registered order. a universal upstream **or** downstream rule **must not** be inferred across different ordering domains, **and** an inverse-derived view **must not** create another declared edge.

## Details

For selected governing RMED occurrences, CA-D-637 defines the ordering context of a verified Project Goal without treating its Operator owner as a Scope Unit. Ordinary endpoints still use their Local Scope Unit.
