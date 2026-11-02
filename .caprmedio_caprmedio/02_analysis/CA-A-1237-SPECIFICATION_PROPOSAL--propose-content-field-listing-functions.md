---
atom_id: CA-A-1237
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject
version: 2
updated_at: 2026-10-28 19:24:50 +0400
relations: {}
tier: 3
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
| [List Logical Content Fields](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-RULE--list-logical-content-fields.md) | R / Rule; `atom_id: CA-R-draft` | Candidate contract for registered Markdown headings at kind and instance level. | Draft; proposed only |
| [Check Content Field Listing](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/06_evaluation/draft/CA-E-draft-CORE_META_MODEL-EVAL_CASE--check-content-field-listing.md) | E / Eval Case; `atom_id: CA-E-draft` | Candidate checks for registered headings versus values and allowed versus present headings. | Draft; proposed only |

These are exactly two candidate Drafts. No numeric identity, typed evaluation link, parser, Tool, runtime, or Current-source change is proposed.

## Disposition

No function decision is adopted. Keep refining this proposal and its Drafts only if requested.
