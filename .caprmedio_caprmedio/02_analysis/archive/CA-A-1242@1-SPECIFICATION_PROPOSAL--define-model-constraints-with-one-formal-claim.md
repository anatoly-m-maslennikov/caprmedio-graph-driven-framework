---
atom_id: CA-A-1242@1
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Formal Model
version: 1
updated_at: 2026-10-28 19:24:50 +0400
relations: {}
tier: 3
---
# Summary

Define model constraints with one formal Claim

## Decision

Formal model constraints are part of the model definitions, not a separate collection of Graph Rule instances. The Requirement Type is Definition, not Graph Rule and not a replacement Rule Type. Each such Atom has one formal content.claim. Optional content.semantics explains the meaning outside the Claim; it contains no additional operative constraints. Optional Details remains support.

Replace the standalone Graph Relation branch with Graph Syntax, which includes Relations and the other constructs of formal Claim notation. Remove the separate Graph Rule branch. The proposed base branches are Continuant, Occurrent, Aspect, Format, Carrier and Graph Syntax. Project Model may still be an organizational view, not another required classification.

## Drafts

- [CA-R-2110@7-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2110@7-draft-CORE_META_MODEL--define-atom-content-role-requirement-type-definition.md): Definition Type structure and the Claim/Semantics distinction.
- [Define Graph Syntax](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-graph-syntax.md): formal syntax declaration and its meaning.
- CA-A-1239@1-draft: primary model and property view, to be refreshed with these branches.

## Superseded preparation

The previously prepared special Graph Rule Type/carrier/authoring packet and its two copied Rule examples are held as superseded Draft material, not promotion candidates. Their useful constraints must be included in the relevant Definition Claims before any Current-source retirement. This decision does not delete Current R1995–R1999, R2001, R2003, R2149, M394 or D637, and does not claim their consumers were migrated. The uniform content.claim layout in CA-A-1241 remains valid. No standalone replacement rule-instance registry is introduced.
