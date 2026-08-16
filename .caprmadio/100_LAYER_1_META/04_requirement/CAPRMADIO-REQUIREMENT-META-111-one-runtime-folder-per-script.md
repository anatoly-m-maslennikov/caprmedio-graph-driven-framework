---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-111
scope_path: layer:meta
subject_scope: framework-boundary
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-109-all-governed-artifacts-live-under-caprmadio
---

# Requirement — Give every runtime-writing script one folder

Each CAPRMADIO script or executable tool that persists runtime files owns one
dedicated directory below `.caprmadio_runtime/`. All runtime files created by
that script stay inside its directory. Concurrent invocations may use bounded
run-specific descendants of the same script directory.

A script must not scatter runtime files across `.caprmadio_runtime/`, write into
another script's directory, or depend on an unowned shared directory. A shared
runtime service is treated as its own executable owner with its own directory;
clients access it through the service contract rather than its files.

## Primary claim

One runtime-writing script or executable tool owns exactly one dedicated
`.caprmadio_runtime/` directory namespace.
