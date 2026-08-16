---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-030
scope_path: layer:meta
subject_scopes:
  - scope-topology
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-065-ordered-realization-topology
    - CAPRMADIO-REQUIREMENT-META-096-acyclic-layers-with-ops-feedback
---

# Govern Layer extensions

A candidate layer must declare:

- one responsibility not already owned by another layer;
- its predecessor and successor;
- accepted inputs and produced outputs;
- entry, exit, and failure behavior;
- its dependency direction; and
- why a Feature or ordinary scope cannot own the concern.

The candidate is admissible only when the resulting graph remains acyclic and
existing responsibilities remain non-overlapping. Otherwise, model it as a Feature or another governed scope rather than adding a Layer.
