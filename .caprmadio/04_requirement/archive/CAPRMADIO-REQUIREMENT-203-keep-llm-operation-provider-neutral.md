---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-203
subject_scopes:
  - portability
tier: core
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-198-replaceable-substrates
---

# Keep LLM operation provider-neutral

CAPRMADIO canonical authority and workflows remain LLM-provider-neutral, any sufficiently capable modern LLM may operate on canonical artifacts, and enhanced provider-specific behavior is supplied through optional independently versioned Extensions.
