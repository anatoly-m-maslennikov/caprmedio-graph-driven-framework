---
subject_scopes:
  - authority
tier: core
version: 1
updated_at: 2026-08-17 17:27:21
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-230-scale-through-structure
---
# Identify necessary information by confidence

To determine whether project information is necessary, an LLM must inspect every active Atom in its full ancestor and descendant lineage and every other active Atom in the same structural scope. The information is necessary only when its omission would leave the LLM below 95% confidence in the current conclusion.
