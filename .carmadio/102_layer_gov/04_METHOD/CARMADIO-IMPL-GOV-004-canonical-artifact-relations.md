---
artifact_type: method
artifact_subtype: technical_decision
artifact_id: CARMADIO-IMPL-GOV-004
scope_path: layer:gov
subject_scopes:
  - relation-model
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CARMADIO-DECISION-GOV-013
  - type: resolution_of
    targets:
      - CARMADIO-DEFECT-TOOL-002
      - CARMADIO-DEFECT-TOOL-003
---

# Technical Decision — Use the canonical artifact relations

CARMADIO uses exactly these general forward artifact relations:

| Relation | Exclusive meaning |
|---|---|
| `child_of` | Narrows, decomposes, or specializes an active parent claim while both remain active |
| `analysis_of` | Interprets named inputs without becoming their authority or evidence |
| `projection_of` | Binds a Projection to its declared source-Atom frontier without transferring source authority |
| `implementation_of` | Connects code, configuration, documentation, migration, a commit, or another realized mechanism to the authority it realizes, including a QA Case or Assurance Control |
| `check_of` | Connects a QA Case or Assurance Control to the claim, condition, or invariant it checks |
| `evidence_for` | Connects a bounded Ops record to the Assurance definition, implementation execution, result, or Verification it supports |
| `resolution_of` | Closes a Concern Atom with the `question` or `problem` subtype |
| `solution_for` | Supplies the accepted solution that closes a Conflict |
| `override_of` | Replaces inherited authority only inside a declared narrower scope |
| `replacement_of` | Completely replaces an older immutable atom |
| `recurrence_of` | Links a new Concern Atom to an archived predecessor with the same direct subtype |
| `relates_to` | Records an association only when no precise relation applies and supplies no authority or coverage |

Every authored edge is stored on its source and names one or more stable target
identities. One source-target pair has one primary relation. Reverse edges,
including `parent_to`, are derived and never authored.

`child_of`, `override_of`, `replacement_of`, and `recurrence_of` are mutually
exclusive for one pair. `solution_for` is reserved for Conflict; other closure
uses `resolution_of`. `relates_to` has no authority, assurance, dependency,
precedence, lifecycle, or coverage semantics.

Rule-registry `depends_on` and `precedence_over` fields remain separate
constitutional controls and are not general artifact relations.

## Primary claim

CARMADIO uses twelve precise forward relations with derived inverses, exclusive
closure semantics, and type/scope `projection_of` frontiers.

## Rationale

The earlier ten-relation decision predated archive recurrence and explicit
Conflict-solution semantics. Keeping those meanings implicit would overload
resolution and historical linkage, while a small bounded extension preserves
the anti-explosion rule and makes each edge reviewable.
