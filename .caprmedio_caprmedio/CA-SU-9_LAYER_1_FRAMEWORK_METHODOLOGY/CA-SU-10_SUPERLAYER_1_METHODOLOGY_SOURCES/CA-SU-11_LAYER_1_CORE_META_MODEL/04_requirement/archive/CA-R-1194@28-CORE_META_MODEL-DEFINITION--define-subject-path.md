---
subjects:
  governs: Entity
  depends_on:
  - Entity
  - Entity/Graph Syntax > Relation
  - Entity/Object/Continuant/Term
version: 28
updated_at: 2026-10-29 07:45:26 +0400
relations: {}
atom_id: CA-R-1194@28
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Entity Definition
---
## Summary

Define Subject Path

## Claim scope

a Subject Path.

## Claim

A Subject Path means a full canonical Subject Expression used by a Subject Relation to identify exactly one canonical Subject Target through its named Term components and registered qualifications. Bare Subject is a valid umbrella. A more-specific path names its namespace immediately after Subject: `Subject/CAPRMEDIO/...` for shared framework vocabulary or `Subject/<Project Name>/...` for project-specific concepts.

Within CAPRMEDIO, Graph contains Node, Relation and Rule as siblings; Node contains Project Model and Aspect; Carrier is outside Graph at `Subject/CAPRMEDIO/Carrier`. These path branches and namespaces do not create an extra entity or target identity. A qualification retains its registered endpoint constraints; the path identifies the target without becoming the Subject Relation itself.

## Details

The logical canonical path remains complete, including its namespace. A concise display label is not a substitute for that path in target identity, comparison or provenance. Namespaces are not entity kinds or Scope Units, and the Atom's owning Scope Unit does not determine its namespace.

A Subject Path may identify a classification axis without reifying it. Within the shared Atom branch, `Atom/Content Role` identifies that axis; `Atom/Content Role: Plan` identifies a narrower Atom kind that inherits Atom properties. The axis and the narrower kind retain distinct Subject meanings.
