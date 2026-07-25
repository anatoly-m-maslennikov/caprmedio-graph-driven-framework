---
artifact_type: requirement
artifact_id: DSET-REQUIREMENT-META-073
scope_path: layer:meta
subject_scopes:
  - lifecycle
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - DSET-REQUIREMENT-META-041
      - DSET-REQUIREMENT-META-064
  - type: relates_to
    targets:
      - DSET-REQUIREMENT-GOV-125
---

# Requirement — Freeze Atomic Artifacts when another artifact depends on them

DSET has exactly three Revision modes:

```toml
revision_mode = "atomic" # atomic | append_only | maintained
```

- `atomic` identifies one independently governed semantic unit.
- `append_only` identifies a growing sequence whose accepted records cannot be
  edited, reordered, or removed.
- `maintained` identifies a current artifact revised through its registered
  update procedure.

`evergreen` is not a Revision mode or lifecycle term.

Atomicity and immutability are distinct. An Atomic Artifact becomes immutable
only when at least one of these dependency conditions first becomes true:

1. a Git commit lists its ID on the implemented-artifact side of the governed
   commit message; or
2. another governed artifact is created with an explicit relation targeting
   its ID.

The committed carrier version at that first dependency is frozen. Later edits
to its content or meaning are forbidden. A correction requires a new Atomic
Artifact with the applicable typed relation, while the frozen predecessor is
preserved unchanged.

Before the first dependency, an admitted Atomic Artifact is active but
unbound. It has a stable ID and may be revised in place. A commit that produces
a revised unbound version lists the artifact ID on its created-artifact side.

A Draft remains a mutable pre-admission candidate. It has no stable artifact
ID, consumes no sequence number, carries no project authority, and cannot be a
dependency target. Admission assigns the stable ID and creates the active
unbound Atomic Artifact; admission alone does not freeze it.

Draft, active, frozen, and archived conditions are derived from carrier
placement, relations, and Git history. They are not duplicated as frontmatter
status fields. “Created based on” always means an explicit governed relation,
not textual similarity or an inferred dependency.

Append-only records become immutable when appended. Maintained artifacts
remain mutable under their registered procedures.

## Primary claim

An Atomic Artifact is one governed claim and freezes only at its first explicit
implementation or downstream artifact dependency, not when it is admitted.

## Rationale

Unconsumed claims can be corrected without producing replacement chains that
serve no downstream history. Freezing at the first explicit dependency
preserves exactly the version that implementation or another governed artifact
actually relied on.
