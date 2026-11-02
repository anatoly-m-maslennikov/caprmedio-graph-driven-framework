---
atom_id: CA-R-1946@14
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Content.Semantics
relations:
  child_of:
  - CA-R-1746
version: 14
updated_at: 2026-10-29 14:12:43 +0400
tier: 2
type: Entity Definition
---
## Summary

Define Atom.Semantics

## Claim scope

Meanings expressed in an Atom's content and their applicability.

## Claim

Atom.Semantics **means** the dependent property of an Atom that explains the meanings used in that Atom and their applicability. It is distinct from general Details. Terms Graph Projections derive meanings from source usage and Semantics; their derived definitions do **not** become a separate source of authority.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom.Content.Semantics[string]{0..1}
```

## Details

The Operator confirmed Semantics is an Atom property represented by a content section. Like a YAML metadata field, a Markdown section represents a property inside the File Carrier. D defines its representation; M governs how it is written. Candidate #6 decision 29 records this distinction without adding a separate Carrier for each property.

Basis: the Operator approved Semantics as meaning-specific Atom content and definitions derived from real uses, not a separate layer of entity-definition Atoms. Candidate #6 decisions 3 and 21 retain that distinction for entity semantics. The later CCE decision separately admits exactly one dedicated Term Definition Requirement Atom as the authoritative meaning owner of a Governed Term. Semantics explains the applicability of entity content without replacing that lexical authority or changing the referent of a complete canonical entity name. Scope-specific entity semantics may coexist; a Projection flags conflicts where those meanings apply to the same case.

Shared lexical `Package`, `Unit`, and `ID` meanings remain stable across their uses, including `atom.id` and `projection.id`. Complete qualified names, not terminal labels, distinguish those property entities. No dictionary Projection, extractor, or lookup is required. A concrete Term Definition retains the canonical GOVERNS obligation; explicit defining authority, not word occurrence or parsing, may introduce its lexical target under CA-R-1194 and CA-R-1931.

Generic uses of the word semantics are not coverage. This requirement does not require the section on every Atom or add storage fields. Corrections belong in source Atoms, followed by rebuilding an applicable derived view. Existing Terms Graph statements apply when such an optional view is selected; this does not implement the deferred Terms Graph.
