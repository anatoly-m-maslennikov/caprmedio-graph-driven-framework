---
artifact_type: requirement
artifact_id: DSET-REQUIREMENT-GOV-114
scope_path: layer:gov
subject_scopes:
  - subject-scope
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - DSET-REQUIREMENT-GOV-071
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-100
  - type: relates_to
    targets:
      - DSET-REQUIREMENT-GOV-113
      - CARMADIO-REQUIREMENT-GOV-144
---

# Requirement — Use expandable scope paths in identities

The canonical artifact identity and filename shape is:

```text
<PROJECT>-<SCOPE_PATH>-<TYPE_PREFIX>-<NNN>[-<SUBTYPE>]--<SUMMARY>.<ext>
```

`PROJECT` is omitted when project-prefix configuration disables it.
`SCOPE_PATH` is omitted at project scope. When present, it contains one or more
registered segments ordered from broader parent to narrower child and may
represent layers, features, either nested inside the other, declared Work
Areas, or future registered scope axes.

Scope does not change numbering. Numeric sequences remain project-wide for
each registered Type prefix. Every scope segment and
parent-child relationship is registered in `.dset/dset_settings.toml`, and a
path must match that registry exactly.

The first implementation and every later vocabulary change perform one
complete lossless migration across active and archived identities, filenames,
relations, Projection and Journal references, settings, Implementation
references, Ops records, and commit provenance.

## Primary claim

Artifact identities use one optional, ordered, registered, and extensible scope
path without restarting their identity-kind numbering.

## Rationale

One structural coordinate supports small flat projects and deeper feature/layer
compositions without hardcoding future scope axes.
