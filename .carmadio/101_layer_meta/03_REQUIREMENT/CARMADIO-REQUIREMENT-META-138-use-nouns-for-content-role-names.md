---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-138
scope_path: layer:meta
subject_scope: semantics
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-115
      - CARMADIO-REQUIREMENT-META-131
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-META-132
---

# Requirement — Use nouns for Content-role names

Every canonical CAPRMADIO Content-role name is a noun naming the primary kind
of contribution represented by that role. A role name must not be a verb,
imperative, workflow instruction, status, or activity label.

The canonical labels are Concern, Analysis, Plan, Requirement, Method,
Assurance, Delivery, Implementation, and Ops. Grammatical variants such as
`planning`, `implementing`, or `operating` may appear in explanatory prose but
must not replace the canonical role names in identifiers, schemas, settings,
folder names, diagrams, or public expansions of CAPRMADIO.

Any future role proposal must supply a noun that remains semantically stable
when the workflow, actor, tool, or implementation mechanism changes.

## Primary claim

CAPRMADIO Content-role names are nouns that classify contributions rather than
verbs that prescribe activities.

## Rationale

Noun-based role names keep the classification independent of workflow and make
the framework expansion grammatically and semantically consistent.
