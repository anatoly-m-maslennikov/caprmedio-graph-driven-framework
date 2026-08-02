---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-112
scope_path: layer:meta
subject_scopes:
  - artifact-model
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-086
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-META-090
      - CARMADIO-REQUIREMENT-META-102
---

# Requirement — Keep Requirements realization-agnostic

Every Requirement states an outcome, obligation, or externally observable
boundary that the governed product or project must, may, or must not satisfy
without prescribing its internal code or code organization.

A normative choice about programming languages, libraries, algorithms,
functions, classes, modules, source-file structure, or another construction
technique is Method. A normative choice about packaging, release, deployment,
distribution, installation, migration, upgrade, or rollback is Delivery. The
concrete code, configuration, schema realization, executable automation, or
other operative asset is Implementation.

A Requirement may preserve an accepted external interface, protocol, data
shape, or host obligation when conformance to that boundary is itself required.
It does not thereby prescribe the project's internal realization. A candidate
that combines an independently replaceable outcome with a code-facing Method or
Delivery rule must be split before admission.

## Primary claim

Requirements are realization-agnostic; code-facing construction rules belong
to Method, delivery-path rules belong to Delivery, and operative code and
configuration belong to Implementation.

## Rationale

Separating required outcomes from construction, delivery, and concrete
realization lets the same Requirement survive refactoring, language changes,
library replacement, and deployment redesign when its observable obligation is
unchanged.
