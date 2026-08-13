---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-110
scope_path: layer:meta
subject_scope: framework-boundary
tier: standard
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-109
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-053
---

# Requirement — Isolate runtime state under `.caprmadio_runtime`

Every CAPRMADIO-owned runtime file lives under the current project's
`.caprmadio_runtime/` root whenever the host platform and invoked dependency
permit that location. Runtime files include process state, checkpoints, caches,
temporary materializations, recovery data, generated scratch, and other
reconstructible execution state.

When an operating system or external tool requires its native temporary or
cache location, CAPRMADIO stores only the minimum transient adapter state there,
never treats it as governed authority, and cleans or reconciles it when the
owning operation ends. Runtime placement must not create files in ambient
repository directories.

The complete `.caprmadio_runtime/` tree remains non-authoritative: deleting it
may lose resumable progress or caches, but must not lose any governed artifact.

## Primary claim

CAPRMADIO-owned reconstructible execution state is isolated under
`.caprmadio_runtime/` whenever technically possible.

## Rationale

A single disposable runtime boundary keeps project roots clean and makes cache,
recovery, cleanup, and supportability behavior predictable across tools.
