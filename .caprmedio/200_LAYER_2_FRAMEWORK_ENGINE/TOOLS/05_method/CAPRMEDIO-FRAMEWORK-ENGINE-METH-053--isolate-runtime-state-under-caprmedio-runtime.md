---
subject_scopes:
  - runtime
tier: core
version: 3
updated_at: 2026-08-19 16:45:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-META-REQU-263--isolate-runtime-state-under-caprmedio-runtime
  child_of:
    - CAPRMEDIO-GOV-REQU-344--all-governed-artifacts-live-under-caprmedio
---

# Isolate runtime state under caprmedio runtime

Place CAPRMEDIO-owned reconstructible execution state under the current
project's caprmedio runtime root whenever the host platform and invoked
dependency permit it. Use native temporary or cache locations only for the
minimum transient adapter state required by that host, never as governed
authority, and reconcile it when the owning operation ends.

Keep the runtime tree non-authoritative: deleting it may lose resumable
progress or caches, but cannot lose a governed artifact.
