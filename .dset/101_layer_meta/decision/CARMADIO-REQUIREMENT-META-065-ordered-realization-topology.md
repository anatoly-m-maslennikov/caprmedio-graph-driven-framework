---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-065
scope_path: layer:meta
subject_scopes:
  - topology
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CARMADIO-REQUIREMENT-META-063
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-META-026
      - CARMADIO-REQUIREMENT-META-029
      - CARMADIO-REQUIREMENT-META-057
      - CARMADIO-REQUIREMENT-META-095
      - CARMADIO-REQUIREMENT-META-066
      - CARMADIO-REQUIREMENT-META-067
      - CARMADIO-REQUIREMENT-META-096
---

# Requirement — Define the ordered realization topology

CARMADIO uses six ordered layers:

```text
META → GOV → SPEC → PROFILES → IMPL → OPS
```

| Layer | Canonical responsibility |
|---|---|
| META | Meanings, universal invariants, layer topology, and inter-layer semantics |
| GOV | Governed carriers, identity, settings, provenance, lifecycle, applicability, canonical scope registration, and conflict governance |
| SPEC | Current project behavior, obligations, technical and integration choices, assurance definitions, and cross-scope contracts |
| PROFILES | Selectable implementation profiles, environments, dependency policies, authoring practices, portability and security rules, and profile-specific gates |
| IMPL | Concrete source, skill packages, Test and Eval implementations, configuration, schemas, migrations, adapters, commits, pull requests, and implementation traceability |
| OPS | Post-implementation delivery, release, publication, runtime supportability, investigation, containment, recovery, and hosted evidence |

META owns semantic dimensions, layer boundaries, and the derivation of internal
Atom Type names from Content roles. GOV owns registered external and relational
Type names plus their concrete carrier rules.

## Primary claim

CARMADIO separates universal semantics, governance, required behavior,
selectable profiles, concrete realization, and post-implementation operation
into the ordered META → GOV → SPEC → PROFILES → IMPL → OPS topology.

## Rationale

The predecessor mixed universal layer topology with concrete Type names and a
separately replaceable scope-propagation rule. The narrowed claim keeps one
technology-independent topology while CARMADIO-REQUIREMENT-META-104 owns scope
identity propagation.
