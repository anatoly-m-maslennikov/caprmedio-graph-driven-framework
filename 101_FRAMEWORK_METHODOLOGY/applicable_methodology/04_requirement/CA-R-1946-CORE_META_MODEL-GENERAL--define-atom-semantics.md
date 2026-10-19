---
atom_id: CA-R-1946
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: General
global_tier: 10
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Continuant/Node/Atom.Semantics"
relations:
  child_of:
  - CA-R-1746
version: 2
updated_at: "2026-10-18 03:34:01 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1946-CORE_META_MODEL-GENERAL--define-atom-semantics.md
  source_atom_id: CA-R-1946
  source_atom_revision: 2
  source_sha256: 31c9002ff676c22a9ddd7693d128ff4421e13462ed41e891b3da33374ccd9435
  original_relations_sha256: cf9cb3753811b7df14cb3d6471a1dbb7c105ba4c7887af180d314140d5f5514f
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
