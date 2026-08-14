---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-165
scope_path: layer:gov
subject_scopes:
  - artifact-catalog
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-GOV-149-register-caprmadio-atom-type-surface
    - CAPRMADIO-REQUIREMENT-GOV-152-register-caprmadio-type-prefixes
---

# Register Delivery subtypes

GOV must register `release_definition` and `environment_definition` as direct subtypes of the internal `delivery` Atom Type.

| Subtype | Governed unit |
|---|---|
| `release_definition` | One independently replaceable rule for packaging, distribution, publication, release, or promotion. |
| `environment_definition` | One independently replaceable rule for a target environment, its topology, or its configuration sourcing. |

Both subtypes use the `DELV` Type prefix and the Delivery Type numbering sequence. A factual release, deployment, or environment state is Ops rather than Delivery.
