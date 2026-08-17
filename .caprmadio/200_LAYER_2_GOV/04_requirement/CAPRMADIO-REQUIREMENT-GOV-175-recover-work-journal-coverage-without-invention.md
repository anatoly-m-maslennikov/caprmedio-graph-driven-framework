---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-175
scope_path: layer:gov
subject_scopes:
  - provenance
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-GOV-173-register-the-project-work-journal
---
# Recover Work Journal coverage without invention

Work Journal recovery must append a `recovered` event only for facts established by repository state, Git history, artifact movement, native targets, pull requests, or bounded session state; unresolved actor, time, intent, scope, or outcome must remain explicit uncertainty rather than fabricated history.
