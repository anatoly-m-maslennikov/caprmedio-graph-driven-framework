---
content_role: Requirement
current_scope_unit: CORE_META_MODEL
status: Draft
subjects:
  governs: "Projection/Type: Entities Graph"
updated_at: "2026-10-15 18:56:34 +0400"
---
# Summary

Requirement for the deferred Entities Graph Construction tree

## Scope

Construction/CONTAINS projection only. Deferred by the Operator on 2026-10-15; this draft is not Active authority.

## Claim

**Construction tree:** use CONTAINS and its inverse-derived IS_CONTAINED_BY, displaying container before contained entity. Do not treat containment as narrower-kind, bearer or allowed-value meaning.

Construction can describe allowed composition of entity kinds, not only existing instances: Plan Atoms containing Plan Atoms; Workflow Atoms containing Steps, each Step containing one Action; and Scope Units containing other Scope Units, Atoms and other admitted Artifacts. Kind-level composition **must not** be presented as an inventory of actual instances. Generation **must** use explicit selected containment declarations and their cardinalities, not infer containment from folder nesting, subtype edges or bearer edges. Missing declarations remain visible as source gaps, not guessed edges.

Display the Construction tree after the Inherency view. Retain canonical identities under every applicable container; repeated placements do not create new identities.

## Origin

Separated from CA-R-1456@10. The active successor retains the Inherency projection. No canonical Atom ID is assigned to this draft.
