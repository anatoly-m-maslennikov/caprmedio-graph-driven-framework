---
artifact_type: method
artifact_id: CAPRMADIO-METHOD-TOOL-006
scope_path: feature:tools
subject_scopes:
  - runtime
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-META-110
  child_of:
    - CAPRMADIO-REQUIREMENT-GOV-180
---

# Isolate runtime state under caprmadio runtime

Place CAPRMADIO-owned reconstructible execution state under the current
project's caprmadio runtime root whenever the host platform and invoked
dependency permit it. Use native temporary or cache locations only for the
minimum transient adapter state required by that host, never as governed
authority, and reconcile it when the owning operation ends.

Keep the runtime tree non-authoritative: deleting it may lose resumable
progress or caches, but cannot lose a governed artifact.
