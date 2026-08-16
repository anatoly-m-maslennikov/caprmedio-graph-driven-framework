---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-143
scope_path: layer:meta
subject_scopes:
  - scope-topology
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-065-ordered-realization-topology
    - CAPRMADIO-REQUIREMENT-META-096-acyclic-layers-with-ops-feedback
    - CAPRMADIO-REQUIREMENT-META-172-share-canonical-features-across-spec-and-implementation
---

# Use flat Layer-owned Feature scopes

An explicitly structured CAPRMADIO project has one ordered sequence of Layers. Every explicit Feature belongs to exactly one Layer and cannot exist outside a Layer or belong to several Layers.

Layer and Feature scope directories are physical siblings. Their governed numeric addresses encode semantic containment: every Feature address identifies its sole parent Layer and its order within that Layer.
