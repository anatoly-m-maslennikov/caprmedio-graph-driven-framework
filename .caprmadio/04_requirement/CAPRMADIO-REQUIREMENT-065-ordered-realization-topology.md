---
subject_scopes:
  - scope-topology
tier: core
version: 1
updated_at: 2026-08-17 17:26:21
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-114-apply-mece-to-canonical-decompositions
---
# Ordered realization topology

CAPRMADIO defines the Project as one root scope with six cumulatively ordered Layers. Each Layer receives authority from the Project and every preceding Layer:

```text
PROJECT → META
PROJECT + META → GOV
PROJECT + META + GOV → SPEC
PROJECT + META + GOV + SPEC → IMPLEMENTATION
PROJECT + META + GOV + SPEC + IMPLEMENTATION → DELIVERY
PROJECT + META + GOV + SPEC + IMPLEMENTATION + DELIVERY → OPS
```
