---
subject_scopes:
  - relation-model
tier: core
version: 4
updated_at: 2026-08-19 22:22:41
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-METH-023--typed-artifact-relations
  resolution_of:
    - CAPRMEDIO-SPEC-TOOLS-CONC-056--legacy-relation-sealing
    - CAPRMEDIO-SPEC-TOOLS-CONC-057--atomic-replacement-source
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---

# Use the canonical artifact relations

CAPRMEDIO uses exactly these general forward artifact relations:

| Relation | Exclusive meaning |
|---|---|
| `child_of` | Narrows, decomposes, or specializes an active parent claim while both remain active |
| `analysis_of` | Interprets named inputs without becoming their authority or evidence |
| `projection_of` | Binds a Projection to its declared source-Atom frontier without transferring source authority |
| `implementation_of` | Connects code, configuration, documentation, migration, a commit, or another realized mechanism to the authority it realizes, including a QA Case or Evaluation Control |
| `check_of` | Connects a QA Case or Evaluation Control to the claim, condition, or invariant it checks |
| `evidence_for` | Connects a bounded Ops record to the Evaluation definition, implementation execution, result, or Verification it supports |
| `resolution_of` | Closes a Concern Atom with the `question` or `problem` subtype |
| `solution_for` | Supplies the accepted solution that closes a Conflict |
| `override_of` | Replaces inherited authority only inside a declared narrower scope |
| `replacement_of` | Completely replaces an older immutable atom |
| `recurrence_of` | Links a new Concern Atom to an archived predecessor with the same direct subtype |
| `related_to` | Records an association only in casual mode when no precise relation applies and supplies no authority or coverage |

Every authored edge is stored on its source and names one or more stable target
identities. One source-target pair has one primary relation. Reverse edges,
including `parent_to`, are derived and never authored.

`child_of`, `override_of`, `replacement_of`, and `recurrence_of` are mutually
exclusive for one pair. `solution_for` is reserved for Conflict; other closure
uses `resolution_of`. `related_to` has no authority, evaluation, dependency,
precedence, lifecycle, or coverage semantics. `related_to` is valid only when
the source Artifact's effective `authority_mode` is `casual`.

Rule-registry `depends_on` and `precedence_over` fields remain separate
constitutional controls and are not general artifact relations.
