---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-117
scope_path: layer:meta
subject_scopes:
  - artifact-model
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-META-030
      - CARMADIO-REQUIREMENT-META-089
      - CARMADIO-REQUIREMENT-META-098
      - CARMADIO-REQUIREMENT-META-114
---

# Requirement — Admit only materially distinct framework constructs

Before CARMADIO admits a new Artifact Type, subtype, relation kind, semantic
axis, scope kind, structural layer, lifecycle state, or other durable framework
construct, the proposal must attempt to express the needed meaning through the
existing model.

The new construct is admitted only when composition would lose a reviewable
distinction and the construct has:

- a non-overlapping primary meaning;
- a one-sentence inclusion and exclusion boundary;
- an action-facing use that changes what a user or tool may claim, check,
  implement, route, stop, or rely upon; and
- a condition under which its necessity must be reconsidered.

Naming convenience, local vocabulary, source prestige, carrier shape, or tool
implementation alone cannot justify a new framework construct. Parsimony also
cannot reject a construct when the existing model materially hides a required
distinction.

## Primary claim

CARMADIO admits a durable framework construct only when existing composition
causes material semantic loss and the addition has a sharp, action-facing
boundary.

## Rationale

This adapts FPF Ontological Parsimony to CARMADIO's artifact, relation, scope,
layer, and lifecycle model.
