---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-088
scope_path: layer:meta
subject_scope: artifact-model
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-082
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-080
      - CAPRMADIO-REQUIREMENT-META-086
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-098
      - CAPRMADIO-REQUIREMENT-META-103
---

# Requirement — Derive internal Atom Types from eight Content roles

For every governed artifact whose Artifact form is `atom` and Governance locus is `internal`, the canonical `artifact_type` name equals its `content_role` value:

```text
atom × concern × internal        → concern
atom × analysis × internal       → analysis
atom × requirement × internal    → requirement
atom × method × internal         → method
atom × assurance × internal      → assurance
atom × delivery × internal       → delivery
atom × implementation × internal → implementation
atom × ops × internal            → ops
```

The equality is exact in canonical machine-readable vocabulary. A direct subtype may refine an internal Atom Type but cannot replace, rename, or introduce another top-level Type for the same Content role.

Stable naming patterns may distinguish recurring domain claims before GOV admits formal subtypes. For example, entity definitions, lifecycle states, status entry criteria, status exit criteria, transition routes, invariants, and events may remain Requirement atoms identified through summaries, relations, and subject scope. A later subtype admission must preserve their top-level `requirement` Type.

This derivation is a META invariant because every conforming CAPRMADIO project can compute it without project policy. GOV owns external and relational Atom Type names, direct subtype vocabularies, identity prefixes, carriers and paths, catalogs and whitelists, schemas and validation, and migrations.

## Primary claim

The canonical Type name of every internal Atom is exactly its Content role name.

## Rationale

The direct equality makes the most common atomic vocabulary predictable and removes a redundant internal naming layer. The pattern applies uniformly to all eight CAPRMADIO roles.
