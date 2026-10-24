---
subjects:
  governs: "Subject/Domain/Node/Continuant/Selection//Stored Governing RMED Relation Occurrences"
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Atom/Content Role
  - 'Subject/Graph/Relation/Type: method_for'
  - 'Subject/Graph/Relation/Type: evaluation_for'
  - 'Subject/Graph/Relation/Type: delivery_for'
  - 'Subject/Graph/Relation/Type: depends_on'
  - 'Subject/Graph/Relation/Type: child_of'
version: 2
updated_at: 2026-10-23 23:13:47 +0400
relations: {}
atom_id: "CA-R-2148@2"
content_role: "Requirement"
type: "Definition"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
tier: 1
status: "Archived"
author: "Anatoly Maslennikov"
---
# Summary

Define Endpoint-Constraint Source Selection

## Scope

the named Selection `Subject/Domain/Node/Continuant/Selection//Stored Governing RMED Relation Occurrences`.

## Claim

the named Selection `Subject/Domain/Node/Continuant/Selection//Stored Governing RMED Relation Occurrences` **means** exactly the stored Current Atom Relation occurrences whose registered Relation Kind is one of the following source-declared kinds:

| Registered Relation Kind | Defining Requirement |
|---|---|
| `method_for` | CA-R-1017 |
| `evaluation_for` | CA-R-1018 |
| `delivery_for` | CA-R-1019 |
| `child_of` | CA-R-879 |
| `depends_on` | CA-R-1026 |

Membership additionally requires both the Relation source and target to be Current Atoms with Content Role in (Requirement, Method, Evaluation, Delivery). The stored governing direction is the source-to-target direction declared by the defining Relation Requirement. Derived inverse views, including `required_by`, are excluded; no inverse occurrence is added to the Selection. Relation names or aliases not registered by the five cited Requirements are excluded.

This is a named Selection instance, not a new Domain Entity or Relation Kind. Membership comes from the complete registered source declarations and Current Atom state, independently of whether a matching edge appears in a filtered graph or Projection. Unknown or incomplete source membership remains unresolved; it is not treated as an empty passing Selection.

## Details
