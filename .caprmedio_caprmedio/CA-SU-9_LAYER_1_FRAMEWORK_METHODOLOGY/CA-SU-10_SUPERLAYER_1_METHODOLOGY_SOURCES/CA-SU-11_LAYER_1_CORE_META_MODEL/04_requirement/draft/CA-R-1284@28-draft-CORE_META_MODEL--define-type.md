---
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity
  dependencies:
  - 'CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Projection/(.Form: Applicable Methodology)'
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Term//Type
  - CAPRMEDIO_MODEL <+ CFEL
  - CAPRMEDIO_MODEL <+ Node.**
version: 28
updated_at: 2026-11-04 18:25:15 +0400
atom_id: CA-R-1284
ref_id: CA-R-1284@28-draft
status: Draft
tier: 1
role: Requirement
form: Rule
carrier_destination:
  file:
    name: CA-R-1284@28-draft-RULE--define-type.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
container:
  scope_unit: CA-SU-11
---
## Summary

Define Type

## Claim

### Prose Claim


Type Properties and their use in qualified Entity kinds. A Type Property is
optional generally; an applicable governing rule may require it in its context.


Type is a single-valued Property when an Entity admits that Property. It can
be used for classification: `X/(.Type: Z)` identifies a kind narrower than X,
qualified by the Type Property and its admitted value Z. The Type Property
and a Property addressed directly by `X.Y` share the same Property meaning;
classification use does not introduce another Property category.

The applicable allowed-value set is finite at an Applicable Methodology
Revision and expandable through governed Methodology Sources. Admission and
requiredness remain scoped to the qualified Property context.

## Semantics

`X.Y` addresses Property Y. `X.Y: Z` expresses that Z is an allowed value of
that Property. `X/(.Y: Z)` qualifies a narrower kind of X by its own Property Y
and admitted value Z. The leading dot addresses X.Y relative to X; the
qualified X inherits X's applicable features and constraints. Y does not
become a narrower kind of X, and no intermediate X/Y kind is declared. Neither form assigns a
value to an existing instance merely by appearing in an expression.

Atom Form is represented by the YAML `form` key; Atom Role is represented by `role`. Legacy `type` and `content_role` are readable only under the transition rules in CA-D-657. These encodings do not create separate Property kinds.
For example, `Atom/(.Header.Role: Method)` concerns Atoms classified by Content
Role Method; Method is not used as a Type value in this example.

## Details

The latest Operator clarification supersedes the earlier interim statement
that Type is not a Property. Both addressed and classification uses are
Properties. The selected relative Property qualification preserves that
Property meaning without another Property category or qualification operator.

The reviewed CA-D-478@29 says qualified classifications are ordinary
metadata Properties and maps them to `content_role` and `type`. CA-D-657@1
governs the YAML Frontmatter field encodings, with each field also subject
to its applicable Property and Delivery authority. Preserve declared keys,
locations and canonical values; an admitted Property with an unsettled
encoding is a schema gap, not permission to guess. Do not derive a new
YAML structure from a display path. No new
Property kind, intermediate classification object, Carrier per field or
YAML-versus-frontmatter ontology is created. Generic grouping/continuation
syntax and parser effects are not established by this interpretation.
