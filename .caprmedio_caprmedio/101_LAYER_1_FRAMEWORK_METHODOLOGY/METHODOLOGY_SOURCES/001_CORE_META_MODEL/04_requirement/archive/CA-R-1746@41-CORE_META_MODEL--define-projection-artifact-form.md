---
subjects:
  governs: Entity/Object/Continuant/Projection
  depends_on:
  - Entity/Object/Continuant/Term//Artifact
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Governing Objects/Atom.Content
  - Entity/Object/Continuant/Structural Unit/Scope Unit
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
  - Entity/Object/Continuant/History/Journal
version: 41
updated_at: 2026-10-29 10:03:18 +0400
relations: {}
atom_id: CA-R-1746@41
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Entity Definition
---
## Summary

Define Projection Artifact form

## Claim scope

Projections and their authoritative sources.

## Claim

A Catalog is a Projection that organizes a selected set of source-backed entries for lookup or review. Vocabulary-diagnostic and proof-currentness Catalog policies govern their specific selections and judgments; the generic Type itself creates no Term, proof result or authority.

A Projection is a non-authoritative output produced from a declared selection of sources through a Workflow:

source of truth → Workflow → Projection.

A Projection is not edited directly. Changes are made in its authoritative sources, then the Projection is rebuilt through its Workflow. Its sources may include other Projections; represented facts remain traceable through them to the appropriate source of truth under CA-R-1470. Multiple views of the same facts do not create independent authority.

The declared selection identifies the sources actually used. A Projection need not consume every source kind, and its generation need not be byte-deterministic.

The ID, named selection and source-of-truth properties follow CA-R-1943; CA-D-635 defines their Markdown field encodings. Source references identify the contributing sources, including Atom Versions. No mandatory Workflow metadata field is introduced by this definition.

### Formal claim

```text
Projection.ID[string]{1}
Projection.Type[string]{1}
Projection.Updated At[datetime]{1}
Projection.Sources[string]{0+}
Projection.Named Selection[string]{1}
Projection.Source Of Truth[string]{1}
Projection/Type: Catalog
```

## Semantics

Implementation is not a Projection merely because it realizes RMED. Code, tests, prompts, configuration and documentation can be edited directly and can be authoritative for actual implementation. A generated view of Implementation is a Projection when changes belong in its sources and the view is rebuilt.

## Details

The Workflow defines how the selected sources produce the Projection. Carrier materialization remains separate from that derivation under CA-R-1460.
