---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-175
scope_path: layer:gov
subject_scopes:
  - provenance
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-GOV-174-register-work-journal-events
---

# Recover Work Journal coverage without invention

Work Journal recovery must append a `recovered` event only for facts established by repository state, Git history, artifact movement, native targets, pull requests, or bounded session state; unresolved actor, time, intent, scope, or outcome must remain explicit uncertainty rather than fabricated history.
