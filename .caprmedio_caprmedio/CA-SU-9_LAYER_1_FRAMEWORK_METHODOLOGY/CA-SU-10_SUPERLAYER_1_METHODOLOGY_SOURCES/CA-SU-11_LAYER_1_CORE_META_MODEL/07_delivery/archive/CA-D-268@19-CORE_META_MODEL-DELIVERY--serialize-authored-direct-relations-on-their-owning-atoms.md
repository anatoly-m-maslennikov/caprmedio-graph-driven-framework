---
subjects:
  governs: Subject/Graph/Relation
  depends_on:
  - Subject/Graph/Relation.Source Reference
version: 19
updated_at: 2026-10-23 03:06:32 +0400
relations: {}
atom_id: CA-D-268@19
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
status: Archived
author: Anatoly Maslennikov
global_tier: 11
---
# Summary

Serialize Authored Direct Relations on Their Owning Atoms

## Scope

Authored direct semantic relations.

## Claim

**every** authored direct semantic relation **must** be serialized once under `relations.<RELATION_KIND>` on the Atom that owns its declared direction as a nonempty unordered collection of unique canonical target references; target position **must not** add, remove, **or** alter a direct relation **or** dependency. source-file target order is nonsemantic; validation **must not** require canonical sorting **or** order normalization. each Relation Kind's direction, endpoint validity **and** other declared semantics remain applicable.

## Details

Serialize only the Relation Kind's declared direct direction, never a second declaration for its derived inverse. For containment, the child carries IS_CONTAINED_BY with the parent reference; CONTAINS is a derived parent view and is not serialized on the parent. A change confined to the child does not request a parent-carrier write or a new parent Version. The relation's spelling does not determine which direction is direct.

This policy governs authored relation declarations. When canonical Carrier nesting already supplies a containment fact under CA-D-264, do not add a second independent declaration for the same fact; CA-D-266 governs that derived view. This source contract does not itself register a new runtime relation key.
