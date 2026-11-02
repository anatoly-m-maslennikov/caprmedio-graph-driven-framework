---
atom_id: CA-R-1946@4
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Node/Continuant/Atom.Semantics
relations:
  child_of:
  - CA-R-1746
version: 4
updated_at: 2026-10-24 00:38:25 +0400
tier: 2
---
# Summary

Define Atom.Semantics

## Scope

Meanings expressed in an Atom's content and their applicability.

## Claim

Atom.Semantics **means** the dependent property of an Atom that explains the meanings used in that Atom and their applicability. It is distinct from general Details. Terms Graph Projections derive meanings from source usage and Semantics; their derived definitions do **not** become a separate source of authority.

## Details

The Operator confirmed Semantics is an Atom property represented by a content section. Like a YAML metadata field, a Markdown section represents a property inside the File Carrier. D defines its representation; M governs how it is written. Candidate #6 decision 29 records this distinction without adding a separate Carrier for each property.

Basis: the Operator approved Semantics as meaning-specific Atom content and definitions derived from real uses, not a separate layer of definition Atoms. Candidate #6 decisions 3 and 21 retain that distinction. Different meanings may coexist in different scopes; a Projection flags conflicts where those meanings apply to the same case.

No current R definition of Atom.Semantics was found. Generic uses of the word semantics are not coverage. This draft does not require the section on every Atom, add storage fields, or repair CA-M-114's old Definition-Atom requirement. Corrections belong in source Atoms, followed by rebuilding the derived view.
