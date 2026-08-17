---
subject_scopes:
  - scope-topology
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-192-preserve-bounded-meaning-across-structural-scales
    - CAPRMADIO-REQUIREMENT-META-198-allow-scope-sets-to-vary-by-structural-owner
  replacement_of:
    - CAPRMADIO-REQUIREMENT-META-143-use-flat-layer-owned-feature-scopes
---
# Assign each Feature to one Layer

Every explicit Feature scope belongs to exactly one Layer and cannot exist outside a Layer or belong to multiple Layers. Feature scopes in different Layers remain distinct even when a PROJECT Contract declares them corresponding.
