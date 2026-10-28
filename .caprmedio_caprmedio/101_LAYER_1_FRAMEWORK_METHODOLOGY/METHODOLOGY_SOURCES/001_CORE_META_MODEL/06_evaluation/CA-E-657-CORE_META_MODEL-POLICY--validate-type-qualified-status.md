---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan.Status'
version: 3
updated_at: 2026-10-27 19:59:38 +0400
relations: {}
atom_id: CA-E-657
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
type: Policy
tier: 2
---
# Summary

Validate Type-Qualified Status

## Scope

Artifacts and their applicable qualified Status model.

## Claim

the Evaluation **must** reject an Artifact **if** **any** applicable condition holds:

- **when** an explicitly defined Status model applies, its Status domain is resolved outside its complete qualified Type **or** Atom Content Role **and** Type path, its current Status cardinality **`!=1`**, its current Status is **not** an allowed value of that domain, a prior transition coexists as current Status metadata, **or** a second disposition axis duplicates Status.

**when** no explicitly defined Status model applies, absence of a Status is **not** a rejection.

the Evaluation **must not** substitute Active **or** Inactive for a missing, invalid, **or** ambiguous Status. an Artifact outside the applicable qualified Status model **must not** fail merely because it has no Status.

## Details
