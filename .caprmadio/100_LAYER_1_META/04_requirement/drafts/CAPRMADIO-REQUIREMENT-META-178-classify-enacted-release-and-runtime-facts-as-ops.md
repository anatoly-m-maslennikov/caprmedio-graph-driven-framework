---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-178
scope_path: layer:meta
subject_scopes:
  - semantics
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-091-authority-assurance-and-ops-remain-distinct
    - CAPRMADIO-REQUIREMENT-META-092-analysis-and-ops-fact-boundary
    - CAPRMADIO-REQUIREMENT-META-107-freeze-a-version-only-at-release
    - CAPRMADIO-REQUIREMENT-META-131-nine-content-roles-with-plan
---

# Classify enacted release and runtime facts as Ops

CAPRMADIO must classify successful and failed release or deployment events, deployed environment state, runtime health, and incidents as Ops. Ops records enacted facts and their bounded evidence without establishing or silently changing Plan, Requirement, Method, Assurance, or Delivery authority.
