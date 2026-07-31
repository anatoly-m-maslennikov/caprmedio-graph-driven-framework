---
artifact_type: requirement
artifact_id: DSET-REQUIREMENT-META-082
scope_path: layer:meta
subject_scopes:
  - artifact-model
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - DSET-REQUIREMENT-META-080
      - DSET-REQUIREMENT-META-081
  - type: relates_to
    targets:
      - DSET-REQUIREMENT-META-035
      - DSET-REQUIREMENT-META-074
---

# Requirement — Derive internal Atom Types from Content roles

For every governed artifact whose Artifact form is `atom` and Governance locus is `internal`, the canonical `artifact_type` name equals its `content_role` value:

```text
atom × concern × internal        → concern
atom × analysis × internal       → analysis
atom × requirement × internal    → requirement
atom × method × internal         → method
atom × assurance × internal      → assurance
atom × implementation × internal → implementation
atom × observation × internal    → observation
```

The equality is exact in canonical machine-readable vocabulary. A direct subtype may refine an internal Atom Type but cannot replace, rename, or introduce another top-level Type for the same Content role.

Stable naming patterns may distinguish recurring domain claims before GOV admits formal subtypes. For example, entity definitions, lifecycle states, status entry criteria, status exit criteria, transition routes, invariants, and events may remain Requirement atoms identified through summaries, relations, and subject scope. A later subtype admission must preserve their top-level `requirement` Type.

This derivation is a META invariant because every conforming DSET project can compute it without project policy. GOV owns external and relational Atom Type names, direct subtype vocabularies, identity prefixes, carriers and paths, catalogs and whitelists, schemas and validation, and migrations.

## Primary claim

The canonical Type name of every internal Atom is exactly its Content role name.

## Rationale

The direct equality makes the most common atomic vocabulary predictable and removes a redundant internal naming layer. A Requirement atom is a `requirement`, an Assurance atom is an `assurance`, and the same pattern applies uniformly to all seven roles.
