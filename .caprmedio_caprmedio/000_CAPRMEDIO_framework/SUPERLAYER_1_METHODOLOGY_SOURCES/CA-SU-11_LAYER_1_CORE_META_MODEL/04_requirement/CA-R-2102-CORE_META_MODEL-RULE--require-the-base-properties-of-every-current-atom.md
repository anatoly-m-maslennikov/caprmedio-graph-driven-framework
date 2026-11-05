---
atom_id: CA-R-2102
ref_id: CA-R-2102
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom
tier: 1
status: Active
version: 17
updated_at: 2026-11-03 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-2102-CORE_META_MODEL-RULE--require-the-base-properties-of-every-current-atom.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Require the base properties of every Current Atom

## Claim

### Prose Claim

Applicability: Every complete Current Atom, with applicable Role and Form conditions.

For every complete Current Atom, require one Role, Form, ID, Status, Updated At, Version, Tier, effective Label and Summary, subject to their applicable individual Declarations. Version is a positive integer; Updated At is a datetime with timezone. The effective Label is the explicit Label when present and otherwise the Form name. Author is not an Atom Property.

Subjects is a grouping Property with no direct value. Its active Subject has one reference and its passive Subjects have zero or more references. Resolve the target Scope from the active Subject under the applicable model rules. Carrier compatibility fields do not override that resolution. Encode direct Node-instance Relation facts under Relations.

For ordinary RMED, require one Claim grouping with no direct value and one or both uniquely named Formal Claim and Prose Claim children. Formal Claim contains a CFEL-labelled code fence; Prose Claim contains ordinary Markdown. Apply the respective content rules for Concern, Analysis & Advisory, Plan and Operations, and preserve their established primary content headings.

A Draft may be incomplete but carries exactly one Atom ID; report missing required Properties and check the complete applicable Current contract before promotion. Each Property's own values and dependent Properties are counted independently.

Legacy carrier spellings remain readable during migration. This transition does not assert additional Atom Properties.

