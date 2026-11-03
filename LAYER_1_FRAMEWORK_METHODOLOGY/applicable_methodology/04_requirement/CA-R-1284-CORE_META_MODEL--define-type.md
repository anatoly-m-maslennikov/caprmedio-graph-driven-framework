---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Entity
  passive:
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Projection/(.Type: Applicable Methodology)'
  - CAPRMEDIO <+ MODEL <+ Scope Unit
  - CAPRMEDIO <+ MODEL <+ Term//Type
  - CAPRMEDIO <+ MODEL <+ CFEL
  - CAPRMEDIO <+ MODEL <+ Entity/Property
version: 27
updated_at: 2026-11-02 19:46:47 +0400
relations: {}
atom_id: CA-R-1284
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1284-CORE_META_MODEL--define-type.md
  source_atom_id: CA-R-1284
  source_atom_revision: 27
  source_sha256: 8bb9cac40eecedf3b9abca9c9a15c0f051ab3814ff4e0f5dae4abbc2ed735030
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Type

## Claim scope

Type Properties and their use in qualified Entity kinds. A Type Property is
optional generally; an applicable governing rule may require it in its context.

## Claim

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
For example, `Atom/(.Content Role: Method)` concerns Atoms classified by Content
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

### Current source pin

Proposed successor of `.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1284-CORE_META_MODEL--define-type.md`, Version 23, SHA-256 `ed846912a5858e8103dfb5189cf574379488dcfde81d52521fafe48a4c7d0622`. This interpretation changes no Current carrier, allocates no identity and performs no promotion.
