---
atom_id: CA-A-1237
ref_id: CA-A-1237
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: Subject
tier: 3
status: Active
version: 3
updated_at: 2026-11-02 15:49:28 +0400
carrier_destination:
  file:
    name: CA-A-1237-CAPRMEDIO-SPECIFICATION_PROPOSAL--propose-content-field-listing-functions.md
    path: .caprmedio_caprmedio/02_analysis_and_advisory
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Propose Content Field Listing Functions

## Question

Should Content field-listing functions be added, with separate kind-level and instance-level meanings?

## Proposal status and authority

Functions remain proposals only. They are separate from formal claim syntax, relation-notation adoption, and implementation. No Current Atom, tool, parser, runtime, or generated Projection is changed.

## Proposed behavior

Use `atom.content.get_list()` as a read-only proposed function. It returns actual registered Markdown headings, not invented logical keys, values, or function names.

| Proposed receiver | Proposed result |
|---|---|
| `Atom.content.get_list()` | Allowed registered Content headings for the kind, including applicable inherited and optional headings. |
| `Atom/Content Role: Requirement.content.get_list()` | Allowed registered headings for the qualified kind. |
| `atom(atom_id="CA-R-123").content.get_list()` | Registered headings actually present in the selected instance. |

The registered headings are `# Summary`, optional `## Claim scope`, `## Claim`, optional `## Semantics`, and optional `## Details`. `atom.content.details` returns the text/value of the registered Details heading. This proposal does not rename `atom.content.claim`, `atom.version_number`, or any existing YAML field.

Formal and natural claims both use `atom.content.claim`. Version identity remains `atom.version_number` in YAML. No `atom.property`, colon/property-text layer, or additional API is proposed here.

`atom.get_properties()` remains a separate proposal for the full property set, including Content; its exact return shape is unresolved, with a map only a recommendation, not an adopted contract.

All functions remain proposals separate from Formal Claim syntax. Existing Summary content is unchanged.

## Draft Atom register

| Draft | Role / Type | Purpose | State |
|---|---|---|---|
| [List Logical Content Fields](../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2973@1-draft-CORE_META_MODEL-RULE--list-logical-content-fields.md) | R / Rule; `atom_id: CA-R-draft` | Candidate contract for registered Markdown headings at kind and instance level. | Draft; proposed only |
| [Check Content Field Listing](../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/000_draft/CA-E-790@1-draft-CORE_META_MODEL-EVAL_CASE--check-content-field-listing.md) | E / Eval Case; `atom_id: CA-E-draft` | Candidate checks for registered headings versus values and allowed versus present headings. | Draft; proposed only |

These are exactly two candidate Drafts. No numeric identity, typed evaluation link, parser, Tool, runtime, or Current-source change is proposed.

## Disposition

No function decision is adopted. Keep refining this proposal and its Drafts only if requested.
