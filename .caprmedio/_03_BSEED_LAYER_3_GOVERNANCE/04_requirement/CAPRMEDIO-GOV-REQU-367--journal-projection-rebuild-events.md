---
subject_scopes:
  - provenance
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 1
updated_at: 2026-08-17 07:48:34
relations:
  child_of:
    - CAPRMEDIO-META-REQU-169--record-every-projection-rebuild-in-a-journal
---
# Journal Projection rebuild events

Each Projection rebuild is one Work Journal action with operation `projection_rebuild`: its `started` event binds the target Projection, exact source frontier, governed generator, and configuration; exactly one terminal event records the outcome; and a `completed` event additionally binds the published Projection `updated_at`, output carrier, and content digest. A rebuilt Projection becomes current only after its `completed` event is accepted.
