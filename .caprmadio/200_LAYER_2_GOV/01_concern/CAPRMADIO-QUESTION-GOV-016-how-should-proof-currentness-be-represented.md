---
artifact_type: concern
artifact_subtype: question
artifact_id: CAPRMADIO-QUESTION-GOV-016
scope_path: layer:gov
subject_scopes:
  - provenance
priority: medium
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-QUESTION-GOV-006
      - CAPRMADIO-OPPORTUNITY-GOV-001
---

# Question — How should proof currentness be represented?

Should CAPRMADIO keep proof dependencies and stale-closure triggers as prose reviewed
by judgment, or register enough structured dependency and frontier data to
derive a non-authoritative proof-currentness view?

The resolution must preserve proof records as the authority for their
observations, keep any generated view non-authoritative, identify the smallest
affected proof closure after change, and avoid claiming currentness from
timestamps alone.

This Question combines the former representation question and its dependent
view opportunity into one unresolved choice.
