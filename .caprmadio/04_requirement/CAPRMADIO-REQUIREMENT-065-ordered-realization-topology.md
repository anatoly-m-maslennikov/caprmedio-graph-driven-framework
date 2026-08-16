---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-065
subject_scopes:
  - scope-topology
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-114-apply-mece-to-canonical-decompositions
---

# Define the ordered realization topology

CAPRMADIO uses one project scope above six cumulatively ordered Layers:

```text
PROJECT → META
PROJECT + META → GOV
PROJECT + META + GOV → SPEC
PROJECT + META + GOV + SPEC → IMPLEMENTATION
PROJECT + META + GOV + SPEC + IMPLEMENTATION → DELIVERY
PROJECT + META + GOV + SPEC + IMPLEMENTATION + DELIVERY → OPS
```

Each row identifies the complete upstream authority available to its receiving
Layer. It does not require every receiving artifact to repeat relations to
every upstream scope; artifacts store only the direct dependencies they
actually use, and derived reachability remains derived.
