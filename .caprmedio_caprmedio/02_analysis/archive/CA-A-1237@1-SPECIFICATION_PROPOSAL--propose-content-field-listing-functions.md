---
atom_id: CA-A-1237@1
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject
version: 1
updated_at: 2026-10-28 17:16:26 +0400
relations: {}
tier: 3
---
# Summary

Propose Content Field Listing Functions

## Question

Should Content field-listing functions be added, with separate kind-level and instance-level meanings?

## Proposal status and authority

Functions remain a proposal only. The Operator instructed: “Let's keep the functions as proposal. Separate A/spec proposal with the list of draft atoms”. The two linked Drafts are candidates for discussion, not accepted methodology, promotion approval, or implemented capabilities. This Analysis being Active means the proposal is being tracked; it does not make the proposed functions Active rules.

This document owns the functions discussion formerly recorded as Q08 in CA-A-1236. Functions are separate from relation-notation adoption and must not be included in a notation-only promotion or migration. No Current Atom, tool, parser, runtime or generated Projection is changed.

## Proposed behavior

Use `get_list()` rather than `titles()` or `list()`. It returns logical Content field names, not Markdown headings, field values, or function names.

| Proposed call | Proposed result |
|---|---|
| `Atom.content.get_list()` | Fields allowed by the Atom model, including applicable inherited and optional fields. |
| `Atom/Content Role: Requirement.content.get_list()` | Fields allowed by the qualified Requirement model. |
| `atom(atom_id="CA-R-123").content.get_list()` | Fields actually present in that selected Atom. |

Illustrative field names are `claim_scope`, `claim`, and `details`. This example does not globally rename the existing Content Scope property, establish a complete universal field schema, or assert what CA-R-123 actually contains. Existing field definitions and carrier mappings remain authoritative until separately changed.

The result would be derived information. The proposal does not add a primary function entity or Relation Type. Whether such expressions may occur in stored Subjects is not decided here. Transport, implementation, ordering and any broader function family remain outside this bounded proposal.

## Draft Atom register

| Draft | Role / Type | Purpose | State |
|---|---|---|---|
| [List Logical Content Fields](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-RULE--list-logical-content-fields.md) | R / Rule; `atom_id: CA-R-draft` | Candidate contract for direct logical fields, kind-level allowed fields and instance-level present fields. | Draft; proposed only |
| [Check Content Field Listing](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/06_evaluation/draft/CA-E-draft-CORE_META_MODEL-EVAL_CASE--check-content-field-listing.md) | E / Eval Case; `atom_id: CA-E-draft` | Candidate checks for keys versus headings/values and allowed versus present fields. | Draft; proposed only |

These are exactly two candidate Drafts. Their generic Draft IDs are not used as ambiguous typed relation targets; numeric identity and an evaluation_for link would be assigned only during later promotion preparation. No separate Method or Delivery Atom is invented to fill a role without an established need.

## Disposition

No function decision is adopted. Keep refining this proposal and its Drafts only if requested. Any later adoption must be explicit and remains separate from implementation. The normative wording inside a Draft states a candidate contract, not an already active rule.

## Source of discussion

The Operator proposed Content property listing, distinguished what may exist for a kind from what actually exists in an Atom, preferred `get_list()`, and then explicitly kept the entire functions idea as a proposal. The latest instruction overrides the earlier Decided wording in CA-A-1236.
