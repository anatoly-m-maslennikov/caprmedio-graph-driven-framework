---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Relation/Type: evaluation_for'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Delivery'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Tier
version: 30
updated_at: 2026-10-27 19:59:49 +0400
relations: {}
atom_id: CA-R-1018
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Definition
---
# Summary

Register Evaluation targets

## Scope

direct `evaluation_for` relations.

## Claim

`evaluation_for` **means** a direct relation owned by an Evaluation Atom **and** directed **to** an Atom whose Content Role is **in** (Requirement, Method, Evaluation, Delivery, Operations) **and** whose authority the Evaluation checks;

- an Evaluation Atom of Type Eval Case **must** own **`>=1`** such target relations,
- while an Evaluation Atom of Type Policy **may** state a representation-independent evaluation policy **without** an artificial list of individual targets.

**every** supplied target relation **must** retain the same checked-authority qualification regardless of the Evaluation's numeric Tier.

## Details
