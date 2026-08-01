---
artifact_type: requirement
artifact_id: DSET-REQUIREMENT-GOV-133
scope_path: layer:gov
subject_scopes:
  - carrier-format
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - DSET-REQUIREMENT-GOV-130
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-083
      - CARMADIO-REQUIREMENT-META-084
  - type: relates_to
    targets:
      - DSET-REQUIREMENT-GOV-102
      - DSET-REQUIREMENT-GOV-116
      - DSET-REQUIREMENT-GOV-126
---

# Requirement — Govern Catalog, Map, and Hub Projections

GOV registers three internal Projection Types:

| Projection Type | Permitted contribution |
|---|---|
| `catalog` | A selected inventory of source Atom IDs grouped and ordered by declared coordinates, scope, subject, entity, lifecycle state, or another governed key |
| `map` | A rendered topology of already-governed relations among declared source Atom IDs |
| `hub` | A navigation entry point to scoped Atoms, Catalogs, Maps, or other governed surfaces |

Catalog, Map, and Hub are Types within Artifact form `projection`; they are not Content roles or creation mechanisms. Every Projection still declares one Content role and one Governance locus. A role-specific Projection may link to artifacts of other roles for navigation but cannot absorb or restate their semantic claims.

A Projection uses Markdown with YAML frontmatter and has a stable governed identity. Its canonical filename follows the registered Type-prefix grammar:

```text
<PROJECT>-<SCOPE_PATH>-<TYPE_PREFIX>-<NNN>--<SUMMARY>.md
```

Frontmatter declares `artifact_form: projection`, the applicable `artifact_type`, `content_role`, `governance_locus`, `artifact_id`, `scope_path`, and only other non-derived properties admitted by the catalog. The Projection declares its exact source frontier through the governed provenance and relation model.

The body may contain headings, grouping and ordering labels, direct Atom IDs and links, source titles, and rendered governed relations. It must not introduce a normative paraphrase needed to understand or satisfy a source Atom. Any independently meaningful explanation, conclusion, requirement, method, assurance rule, implementation claim, or observation is emitted as its own Atom and then linked from the Projection.

A Projection may be rebuilt mechanically or through governed reasoning. Generated and reasoned describe creation procedures, not Artifact forms. Creation and every rebuild are committed as new or updated children under the exact source revisions consumed.

A Projection is current only when its declared source frontier and rebuild procedure reproduce the committed view. A source change triggers lineage-impact review. A compatible result may preserve the existing Projection revision; an affected result requires a rebuild before a gate that requires the Projection may pass.

`specification` is retired as an independent maintained Type. A current view of the distributed normative specification is represented by a `requirement`-role Catalog, Map, Hub, or bounded combination of those Projections.

## Primary claim

Catalog, Map, and Hub are thin internal Projection Types with direct atomic provenance, no independent semantic authority, and no normative restatement of their sources.

## Rationale

These three Types preserve inventory, topology, and navigation without recreating a second prose specification. The view can be rebuilt whenever its source frontier changes, while each semantic claim remains governed by its owning Atom.
