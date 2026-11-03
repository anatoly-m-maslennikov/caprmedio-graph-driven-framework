---
subjects:
  active: Atom
version: 15
updated_at: 2026-11-02 15:49:28 +0400
relations: {}
atom_id: CA-R-2102
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2102-CORE_META_MODEL-RULE--require-the-base-properties-of-every-current-atom.md
  source_atom_id: CA-R-2102
  source_atom_revision: 15
  source_sha256: 2e3e3185f80908c1fa089cfc9084d81caa734ae8379464e6d371996d00bd8dae
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Require the base properties of every Current Atom

## Claim scope

Every complete Current Atom, with applicable Role and Form conditions.

## Claim

For every complete Current Atom, require one Role, Form, ID, Status, Updated At, Version, Tier, effective Label and Summary, subject to their applicable individual Declarations. Version is a positive integer; Updated At is a datetime with timezone. The effective Label is the explicit Label when present and otherwise the Form name. Author is not an Atom Property.

Subjects is a grouping Property with no direct value. Its active Subject has one reference and its passive Subjects have zero or more references. Resolve the target Scope from the active Subject under the applicable model rules. Carrier compatibility fields do not override that resolution. Encode direct Node-instance Relation facts under Relations.

For RMED, require one Claim as its direct Markdown value. CFEL may provide that value without prose. Do not create a Formal Claim child. Apply the respective content rules for Concern, Analysis & Advisory, Plan and Operations, and preserve their established primary content headings.

A Draft may be incomplete but carries exactly one Atom ID; report missing required Properties and check the complete applicable Current contract before promotion. Each Property's own values and dependent Properties are counted independently.

Legacy carrier spellings remain readable during migration. This transition does not assert additional Atom Properties.
