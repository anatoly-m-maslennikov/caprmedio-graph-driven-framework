---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom
version: 7
updated_at: 2026-10-24 23:49:48 +0400
relations: {}
atom_id: CA-R-2102@7
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

Every Current Atom **must** carry exactly one of each following base Property:
Content Role, Type, Atom ID (`atom_id`), Status, Updated At (`updated_at`),
Version Number (serialized as `version`), Author (`author`), numeric Tier
(`tier`), effective Label and Summary. Version Number is an integer **>=1**;
Tier follows CA-R-2125, CA-R-2130 and CA-R-2131; Updated At is a datetime with
timezone; Author is an Actor reference. D governs the actual representation.
Effective Label is the explicit Label when present, otherwise the Type name
under CA-R-1594. Do not require a redundant stored Label.

An ordinary Current Atom **must** have exactly one Local Scope Unit. A
Project Goal instead has its registered Operator owner and targets the
Project, with Tier -1 under CA-R-2132. That exception does not waive the
other base Properties or invent an Operator Scope Unit.

Required Content follows the Atom's Content Role and applicable Type:

- R/M/E/D use Content.Claim; an ordinary Current RMED Atom has exactly one
  Claim. A formal R/Type: Graph Rule instead has its operative YAML under
  CA-D-637 and no Claim. Its Summary remains required; Semantics and Details
  remain optional.
- O uses Content.Operation; C uses Content.Concern; P uses Content.Objective.
- A uses Content.Question and Content.Analysis as required by its Type.

The applicable Type defines its precise content contract and may specialize
the Role default. These are logical content names, not a requirement to copy
the same text into redundant physical sections or add empty placeholders.
Their actual Markdown layout remains governed by D. Do not carry a generic
Substance field or invent a duplicate Content-level Substance parent.

Each of these optional base Properties occurs zero or one time: Target Scope
Unit (`claim_target_scope_unit`), the authored Relations collection
(`relations`), the Subjects collection (`subjects`), Content Scope, Details
and Semantics. A Project Goal's required Project target is the stated Type
exception. An optional collection can contain many entries with their own
cardinalities; Subjects has at most one GOVERNS and any number of DEPENDS_ON.
Optional does not waive the applicable Scope or Type conditions.

Content Scope is Content.Scope: the exact applicability boundary of the
role-specific Content. It is not another Local or Target Scope Unit. Keep
useful topic meaning from the retired Atom.Entity property in Subjects and
its applicability boundary in Content Scope; do not recreate Atom.Entity.

A Draft may be incomplete in other required Properties or Content, but
**must** have exactly one Atom ID. Report missing required Properties and
enforce its complete applicable Current contract before promotion. This
rule does not extend the formal Graph Rule YAML schema or replace the
separate per-Property Delivery rules.

## Details
