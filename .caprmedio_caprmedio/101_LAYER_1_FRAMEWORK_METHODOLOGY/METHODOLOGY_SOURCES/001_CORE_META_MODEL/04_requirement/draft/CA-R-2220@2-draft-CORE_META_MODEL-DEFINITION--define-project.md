---
atom_id: CA-R-2220@2-draft
content_role: Requirement
type: Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
subjects:
  governs: Model::CAPRMEDIO::Continuant/Structural Unit/Scope Unit/Project
version: 2
updated_at: 2026-10-29 00:04:17 +0400
relations: {}
tier: 1
---
# Summary

Define Project

## Claim

Project is the single root Scope Unit. It has no parent Scope Unit and contains the Project's top-level Scope Units. Scope Unit properties apply through specialization, with that explicit root-parent exception. Existing Project Goal Operator ownership remains unchanged.

### Formal claim

```text
Scope Unit/Project
Project > @(Scope Unit)
Project.Parent{0}
```

## Semantics

The slash defines what Project is; the containment relation defines its parts. A child Scope Unit is not a subtype of Project merely because Project contains it.

## Details

CA-A-1258 records this correction. Current predecessor remains unchanged.
