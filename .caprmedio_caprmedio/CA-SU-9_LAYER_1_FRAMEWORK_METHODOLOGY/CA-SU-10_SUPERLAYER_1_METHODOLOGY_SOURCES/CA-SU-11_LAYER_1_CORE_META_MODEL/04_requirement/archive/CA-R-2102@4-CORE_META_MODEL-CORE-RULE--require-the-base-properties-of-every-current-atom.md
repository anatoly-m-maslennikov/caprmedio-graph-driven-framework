---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom
version: 4
updated_at: 2026-10-24 00:38:25 +0400
relations: {}
atom_id: CA-R-2102@4
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Rule
tier: 1
---
# Summary

Require the base properties of every Current Atom

## Scope

Every Current Atom.

## Claim

Every Current Atom **must** carry exactly one of each following base Property: Content Role, Local Scope Unit (`current_scope_unit`), Type, Atom ID (`atom_id`), Status, Updated At (`updated_at`), Version Number (serialized as `version`), Author (`author`), numeric Tier (`tier`), effective Label, and Summary. Version Number is an integer **>=1**; Tier is an integer admitted by the owning Scope Unit under CA-R-2125, CA-R-2130 and CA-R-2131; Updated At is a datetime with timezone; Author is an Actor reference. Their serialization details remain governed by the applicable Delivery authority. Every ordinary Current Atom **must** also carry exactly one Substance. The effective Label is the explicit Label Property when present; otherwise it is the Atom's Type name, as defined by CA-R-1594. A derived effective Label does not require a redundant stored copy.

A formal Graph Rule Atom is the bounded exception to the Substance requirement: it has no Substance Property or Substance section and instead carries its operative YAML block under CA-D-637. This Rule does not define or extend that block's schema; the applicable formal Graph Rule authority remains separate.

Each of these optional base Properties may occur zero or one time: Target Scope Unit (`claim_target_scope_unit`), the authored Relations collection (`relations`), the Subjects collection (`subjects`), Substance Scope, Details, and Semantics. Optional collection-valued Properties have at most one collection occurrence; collection members retain their independently governed cardinality and values. In particular, Subjects is one collection with at most one GOVERNS Subject and any number of DEPENDS_ON Subjects.

An Atom Draft may be incomplete in other required Properties or body content, but **must** carry exactly one Atom ID. Its missing required Properties must be reported; it must satisfy the full Current Atom contract before promotion to Current. This Rule does not prescribe a separate Graph Rule YAML schema or replace per-Property serialization authority.

## Details
