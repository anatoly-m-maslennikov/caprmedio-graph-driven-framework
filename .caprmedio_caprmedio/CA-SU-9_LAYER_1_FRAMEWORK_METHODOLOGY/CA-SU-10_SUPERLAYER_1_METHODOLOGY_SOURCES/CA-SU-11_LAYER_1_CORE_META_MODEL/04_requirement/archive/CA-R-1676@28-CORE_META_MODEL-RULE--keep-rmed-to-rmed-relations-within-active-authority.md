---
subjects:
  governs: Subject/Graph/Relation
version: 28
updated_at: 2026-10-24 12:35:51 +0400
relations:
  child_of:
  - CA-R-1051
atom_id: CA-R-1676@28
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Keep RMED-to-RMED Relations within Active Authority

## Scope

direct relations authored by Current RMED Atoms that target RMED Atoms.

## Claim

**if** a direct relation is authored by a Current Atom with Content Role **in** (Requirement, Method, Evaluation, Delivery) **and** targets an Atom with Content Role **in** (Requirement, Method, Evaluation, Delivery), **then** the target Atom **must** be Current.

## Details
