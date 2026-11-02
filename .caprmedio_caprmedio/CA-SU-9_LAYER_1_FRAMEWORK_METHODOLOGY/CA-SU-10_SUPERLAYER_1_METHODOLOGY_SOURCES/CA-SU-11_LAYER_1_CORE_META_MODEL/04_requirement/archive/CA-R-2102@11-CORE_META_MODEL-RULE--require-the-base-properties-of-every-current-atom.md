---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom
version: 11
updated_at: 2026-10-29 07:32:39 +0400
relations: {}
atom_id: CA-R-2102@11
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Rule
tier: 1
---
## Summary

Require the base properties of every Current Atom

## Claim scope

Every complete Current Atom, with the stated Role and Type exceptions.

## Claim

Every Current Atom **must** carry exactly one of each following base Property:
Content Role, Type, Atom ID (`atom_id`), Status, Updated At (`updated_at`),
Version Number (serialized as `version`), Author (`author`), numeric Tier
(`tier`), effective Label and Summary. Version Number is an integer **>=1**;
Tier is an integer >=-1 and follows the more-specific prose conditions in CA-R-2125, CA-R-2130 and CA-R-2131; Updated At is a datetime with
timezone; Author is an Actor reference. D governs the actual representation.
Effective Label is the explicit Label when present, otherwise the Type name
under CA-R-1594. Do not require a redundant stored Label.

An ordinary Current Atom **must** have exactly one Local Scope Unit. A
Project Goal instead has its registered Operator owner and targets the
Project, with Tier -1 under CA-R-2132. That exception does not waive the
other base Properties or invent an Operator Scope Unit.

Required Content follows the Atom's Content Role and applicable Type:

- R/M/E/D use atom.content.claim, exactly once. This includes Model Definitions. Every complete RMED Atom has one direct prose Claim value. For R, an optional formal_claim child has its own zero-or-one count and cannot satisfy the prose requirement; M/E/D keep prose Claims; it is never duplicated in frontmatter atom.claim or atom.formal_claim. Its Summary remains required; Claim scope, Semantics and Details remain optional.
- O uses Content.Operation; C uses Content.Concern; P uses Content.Objective.
- A uses Content.Question and Content.Analysis as required by its Type.

The applicable Type defines its precise content contract and may specialize
the Role default. These are logical content names, not a requirement to copy
the same text into redundant physical sections or add empty placeholders.
Their actual Markdown layout remains governed by D. Do not carry a generic
Substance field or invent a duplicate Content-level Substance parent.

Target Scope Unit (`claim_target_scope_unit`), Content Scope, Details and Semantics each have zero or one direct value, subject to the applicable Scope/Type conditions. A Project Goal's required Project target remains the stated exception.

Entitys is a grouping property with zero direct values: subjects{0}. Its governs property has exactly one reference and its dependency property has zero or more references. The YAML dependency key remains subjects.depends_on. Relations and Content also group declared child properties without direct values. Child values and nested keys do not count toward their parent cardinality. A zero-direct-value group does not prohibit its children. Each property's own count is independent; YAML lists carry multiple values under one unique key rather than introducing a list value Format.

For RMED, Content Scope is atom.content.claim_scope: the exact applicability boundary of the
role-specific Content. It is not another Local or Target Scope Unit. Keep
useful topic meaning from the retired Atom.Entity property in Entitys and
its applicability boundary in Content Scope; do not recreate Atom.Entity.

A Draft may be incomplete in other required Properties or Content, but
**must** have exactly one Atom ID. Report missing required Properties and
enforce its complete applicable Current contract before promotion. This
rule does not itself define every formal syntax or replace the
separate per-Property Delivery rules.

For RMED, use the exact body headings in CA-D-479: ## Summary, optional ## Claim scope, required ## Claim, optional ## Semantics, optional ## Details, in that order. This changes no C/A/P/O primary-content headings. The canonical access convention remains atom.version_number for a YAML property and atom.content.claim for a Markdown property; no property/text grouping layer is introduced.

## Details

CA-A-1241 records the superseding RMED layout decision. Drafts may remain incomplete under their existing admission rules.

R-only scope refinement (CA-A-1244): the optional ### Formal claim / content.claim.formal_claim is admitted only for Requirement Atoms for now. Method, Evaluation and Delivery have prose Claims with no operative formal child; code examples remain examples. Any earlier generic optional-formal wording in this Draft is limited by that Role condition. The complete one-Claim contract and optional supporting sections remain unchanged.
