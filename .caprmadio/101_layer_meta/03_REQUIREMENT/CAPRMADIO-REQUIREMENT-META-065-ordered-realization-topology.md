---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-065
scope_path: layer:meta
subject_scope: scope-topology
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-063
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-026
      - CAPRMADIO-REQUIREMENT-META-029
      - CAPRMADIO-REQUIREMENT-META-057
      - CAPRMADIO-REQUIREMENT-META-095
      - CAPRMADIO-REQUIREMENT-META-066
      - CAPRMADIO-REQUIREMENT-META-067
      - CAPRMADIO-REQUIREMENT-META-096
---

# Requirement — Define the ordered realization topology

CAPRMADIO uses six ordered layers:

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

CAPRMADIO separates universal semantics, governance, required behavior,
selectable profiles, concrete realization, and post-implementation operation
into the ordered META → GOV → SPEC → PROFILES → IMPL → OPS topology.

## Rationale

The predecessor mixed universal layer topology with concrete Type names and a
separately replaceable scope-propagation rule. The narrowed claim keeps one
technology-independent topology while CAPRMADIO-REQUIREMENT-META-104 owns scope
identity propagation.
