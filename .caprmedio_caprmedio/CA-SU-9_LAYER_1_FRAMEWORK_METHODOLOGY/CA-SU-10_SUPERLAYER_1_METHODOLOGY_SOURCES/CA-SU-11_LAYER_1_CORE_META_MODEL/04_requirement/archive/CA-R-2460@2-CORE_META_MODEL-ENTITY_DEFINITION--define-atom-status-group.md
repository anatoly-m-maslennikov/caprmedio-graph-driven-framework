---
atom_id: CA-R-2460@2
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
version: 2
updated_at: 2026-10-30 14:24:16 +0400
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Status >| Status Group
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom.Status
  - Entity/Graph Syntax <+ Relation//HAS_CLASSIFICATION
  - Entity/Graph Syntax <+ Relation//IS_CONTAINED_BY
relations: {}
---
## Summary

Define Atom Status Group

## Claim scope

Status Group classification of admitted Atom Statuses, across all Content Roles.

## Claim

Atom Status Group is a Classification of Atom Statuses, not a Property.
It has three groups: Draft, Archived and Current. Status Draft
belongs to Draft; Status Archived belongs to Archived; every other admitted
Status belongs to Current. These cases are exhaustive and mutually exclusive,
so each admitted Status determines exactly one Status Group and each Atom
with its required single Status selects exactly one group through that Status.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom.Status >| Status Group: Draft <+ Draft
Entity/Object/Continuant/Governing Objects/Atom.Status >| Status Group: Archived <+ Archived
Entity/Object/Continuant/Governing Objects/Atom.Status >| Status Group: Current <+ * not in (Draft, Archived)
```

## Semantics

The three Formal claim lines declare each Status Group and its Status parts.
`Whole <+ Part` means Whole has Part; `Part +> Whole` means Part is part of
Whole. The pointer faces the Whole in both directions. The group on the
left contains the Status values on the right. The underlying direct fact is
Part IS_CONTAINED_BY Whole, with CONTAINS as its derived inverse.
These are containment expressions, not numeric comparisons or narrower-kind
inheritance. They do not classify every Status into all three groups at once.
The Claim's mapping determines exactly one group for each admitted Status.

In the Current line, `*` ranges only over admitted Atom Status values, and
`not in (Draft, Archived)` excludes those two values. It does not include
unadmitted names, missing values or arbitrary Entity instances.

In the proposed notation, `Atom.Status >| Status Group` references the
Classification axis applicable to Atom Statuses through HAS_CLASSIFICATION.
`Status Group |< Atom.Status` is the reverse written view of that fact. The
following colon declares an allowed group in the qualified context. The
generic `X: Y` rule means Y is an allowed value of X regardless of the
preceding path or Entity kind; it does not make Status Group a Property.

Backlog, Active, Done and Canceled are examples of Current-group Statuses
where those Status values are admitted. They do not form a closed list:
another admitted Status is Current unless it is Draft or Archived. The
grouping does not admit a new Status value or replace an applicable Status
admission check.

Status remains a Property represented by the existing `status` field. Status
Group classifies its admitted Status values using that mapping; it is not a second
Property and does not require a stored `status_group` field. The mapping itself establishes
exactly-one membership; no additional Rule Atom or Property cardinality is
needed for that result.

### Delivery rule applicability

The Status Group condition selects rules for the Atom or its Carrier, as
specified by each rule's Subject, Claim scope and Claim. It does not attach
a filename template or folder-placement requirement to the Status value
entity itself. `Atom.Status >| Status Group` classifies Atom Statuses across
Content Roles; the common group-based filename template is the
base across Content Roles. The Operator explicitly selects a more-specific
P/Plan filename-template override, retaining its optional Work Sequence
Number prefix. A Content Role token in the base template remains a parameter
value; the P override is an explicit exception, not a template per Role.
Draft and Archived identity markers remain governed by their identity rules
within the override's Atom-ID segment.

A D Atom with Subject `Atom.Status >| Status Group: Archived` may define the filename
template for Carriers of Atoms whose Status belongs to that group. Its Claim
scope and Claim specify that Carrier effect. A D Atom with Subject
`Atom.Status` may define the folder location of an Atom Carrier according to
its Status. The two contributions compose: one determines the filename and
the other its directory. They do not change the Status or its group mapping.

This clarifies conditional Delivery applicability without deciding generic
classification inheritance beyond the pending Relation Definitions. It adds
no inference engine, stored group fact or automatic Carrier mutation.
The Formal claim expresses the Status values as parts of their groups. It
does not make the Atom or its Carrier a structural part of a group or rename
the Atom's Status to Current.

## Details

The Operator explicitly corrects the former separate-Property interpretation
and supplies the complete mapping: Draft to Draft, Archived to Archived,
and Current for everything else, including Backlog, Active, Done and Canceled.
This semantic correction changes no Current source, Carrier field or runtime.

### Proposed classification target and pending grammar dependencies

The Operator's latest clarification selects `Atom.Status >| Status Group` and
the three group-to-Status containment declarations above. The Governs target now uses the full Entity-rooted
classification expression. It replaces the former Property-shaped
`Atom.Status Group`, supersedes the explored `..` spelling, and supersedes
the earlier direct Atom classification `Atom :: Status Group`.

The Operator approved HAS_CLASSIFICATION for the classification-axis
Relation. Its sibling Draft `CA-R-draft-CORE_META_MODEL-RELATION_DEFINITION--define-has-classification.md`
defines that meaning, distinct from historical organizational membership and
IS_CLASSIFIED_BY membership in a particular classifier. It remains pending adoption.

The current R1245/R1436 colon contracts cover Property allowed values only;
their Draft successors and R1931/M228/E383 need reconciliation for allowed
generic allowed values and the selected `>|` / `|<` notation. No separate
Classification Entity kind is required: the Operator identifies the named
HAS_CLASSIFICATION and IS_CLASSIFIED_BY Relation instances under Graph Syntax.
A standalone Classification word definition, if needed, belongs to the Term
branch. Relative Property qualification replaces the separate Classification
Property category. This
Draft is therefore not ready for promotion. No new Property, stored field,
Current operator, parser or runtime behavior is admitted by these examples.

The Operator selected `Part +> Whole / Whole <+ Part` and
`something >| its classification / its classification |< something`.
These spellings supersede bare `>` / `<` containment and the `::` axis spelling.
The `* not in (...)` value selection
need coordinated grammar and evaluation support before adoption. Recording
the Formal claim is not evidence of an executable set-expression parser.
