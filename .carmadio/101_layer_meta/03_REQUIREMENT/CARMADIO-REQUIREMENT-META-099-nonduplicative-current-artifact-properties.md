---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-099
scope_path: layer:meta
subject_scope: artifact-model
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CARMADIO-REQUIREMENT-META-038
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-080
      - CARMADIO-REQUIREMENT-META-086
      - CARMADIO-REQUIREMENT-META-089
---

# Requirement — Keep artifact properties nonduplicative

Every governed artifact property has one distinct meaning. A property section contains neither two properties that express the same meaning nor a property whose value is deterministically derived from another canonical property, the registered artifact type and subtype, the current project, or repository placement.

The artifact type and optional direct subtype determine Artifact form, Content role, and Governance locus. Atom carriers therefore do not repeat those derived coordinates or carry an acceptance status: emission follows explicit acceptance, while active versus archived placement identifies whether the Atom participates in current authority.

Project identity and internal project authority are ambient. An external source, issuer, or relation endpoint remains explicit through the precise type-specific property that owns that meaning.

Repeated relations with the same kind, roles, qualifiers, and meaning use one non-empty `targets` list. Relations whose roles, qualifiers, or meanings differ remain separate.

## Primary claim

Artifact properties contain only explicit, non-derived meanings and never duplicate another canonical property, registered type mapping, ambient project fact, or repository-placement fact.

## Rationale

Duplicated or derivable properties create competing writable representations that can disagree.
