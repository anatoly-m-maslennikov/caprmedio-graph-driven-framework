---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-080
scope_path: layer:meta
subject_scopes:
  - artifact-model
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CARMADIO-REQUIREMENT-META-073
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-META-074
      - CARMADIO-REQUIREMENT-META-075
      - CARMADIO-REQUIREMENT-META-076
      - CARMADIO-REQUIREMENT-META-077
---

# Requirement — Use Atom, Journal, and Projection artifact forms

Every governed artifact has exactly one `artifact_form`:

```toml
artifact_form = "atom" # atom | journal | projection
```

- `atom` is one independently governed unit with a stable identity and one independently replaceable primary claim. An admitted Atom may gain committed revisions only through the governed atomic change and lineage procedures; each committed revision remains immutable and recoverable.
- `journal` is an ordered sequence of admitted records. New records may be appended, while accepted records cannot be edited, reordered, or removed.
- `projection` is a rebuildable view derived from declared governed sources. It may organize, select, or render source meaning but has no independent semantic authority over those sources.

Artifact form states what an artifact is. It does not state how the carrier was created. `append_only`, `generated`, `reasoned`, `manual`, and similar terms describe a change rule or creation procedure, not another artifact form. Journal is intrinsically append-only; a Projection may be generated mechanically or rebuilt through governed reasoning without changing form.

`revision_mode` is retired as a primary classification axis. Content role, Governance locus, and `scope_path` remain independent of Artifact form. Implementation is a Content role and is never an Artifact form.

Draft admission, committed Atom revisions, exact dependency bindings, archive behavior, and lineage impact remain governed by their dedicated requirements. Artifact form does not itself establish truth, authority, priority, or currentness.

## Primary claim

CARMADIO classifies every governed artifact as exactly one Atom, Journal, or Projection according to what the artifact is, independently of its creation mechanism and semantic role.

## Rationale

The predecessor combined atomic identity with a change-oriented Revision-mode taxonomy. Atom, Journal, and Projection expose three different governed structures directly, while append-only and generated describe behavior or production rather than artifact identity.
