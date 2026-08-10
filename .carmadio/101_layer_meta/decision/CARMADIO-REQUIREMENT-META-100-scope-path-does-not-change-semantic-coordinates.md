---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-100
scope_path: layer:meta
subject_scope: scope-topology
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CARMADIO-REQUIREMENT-META-052
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-089
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-META-011
---

# Requirement — Keep Scope path structural

Scope path is a project-relative, ordered, and extensible structural coordinate. It may address layers, features, feature groups, declared Work Areas, or their configured compositions.

The current project is ambient and never repeated in `scope_path`. Project scope therefore uses an empty path. Scope may govern ownership, applicability, inheritance, and identity, but it never changes Artifact form, Content role, or Governance locus.

## Primary claim

Scope path identifies structural ownership without changing an artifact's semantic coordinate.

## Rationale

Separating structural placement from semantic classification allows the same kind of meaning to apply at different project scales without multiplying semantic types.
