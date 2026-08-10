---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-111
scope_path: layer:meta
subject_scope: framework-boundary
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-110
---

# Requirement — Give every runtime-writing script one folder

Each CARMADIO script or executable tool that persists runtime files owns one
dedicated directory below `.carmadio_runtime/`. All runtime files created by
that script stay inside its directory. Concurrent invocations may use bounded
run-specific descendants of the same script directory.

A script must not scatter runtime files across `.carmadio_runtime/`, write into
another script's directory, or depend on an unowned shared directory. A shared
runtime service is treated as its own executable owner with its own directory;
clients access it through the service contract rather than its files.

## Primary claim

One runtime-writing script or executable tool owns exactly one dedicated
`.carmadio_runtime/` directory namespace.

## Rationale

Per-script ownership makes cleanup, retention, collision diagnosis, and runtime
supportability deterministic without requiring one folder per invocation.
