---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-100
scope_path: layer:meta
subject_scope: scope-topology
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-META-052
  child_of:
    - CAPRMADIO-REQUIREMENT-116-preserve-strict-semantic-distinctions
    - CAPRMADIO-REQUIREMENT-120-preserve-bounded-meaning-across-structural-scales
---

# Requirement — Keep Scope path structural

Scope path is a project-relative, ordered, and extensible structural coordinate. It may address layers, features, feature groups, declared Work Areas, or their configured compositions.

The current project is ambient and never repeated in `scope_path`. Project scope therefore uses an empty path. Scope may govern ownership, applicability, inheritance, and identity, but it never changes Artifact form, Content role, or Governance locus.

## Primary claim

Scope path identifies structural ownership without changing an artifact's semantic coordinate.
