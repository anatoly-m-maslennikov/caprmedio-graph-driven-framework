---
artifact_type: requirement
artifact_id: DSET-REQUIREMENT-GOV-129
scope_path: layer:gov
subject_scopes:
  - relation-model
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-077
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-META-078
      - DSET-REQUIREMENT-GOV-127
      - DSET-REQUIREMENT-GOV-128
---

# Requirement — Record one Lineage Impact Analysis per changed atom revision

Every `refinement`, `semantic_revision`, or `replacement` of an admitted
Atomic Artifact produces one atomic Analysis Report whose primary conclusion
is the impact state of that exact changed parent revision.

The report records:

- the changed artifact ID and exact previous and new Git revisions;
- the assigned change class and the observed basis or rationale for the change;
- the responsible operator and session provenance already required for the
  report carrier;
- the expected impact radius;
- every directly examined child and the exact child revision examined;
- one `compatible`, `update_required`, `replacement_required`, or `uncertain`
  disposition for each child;
- the evidence or reasoning supporting each disposition;
- every resulting child revision, successor, Question, or Problem; and
- the recursive branch result and overall fixed-point conclusion.

One report may contain many child rows because those rows support the single
primary conclusion that the changed parent revision's impact review is
complete or blocked. The report does not replace the children, their evidence,
or their own semantic claims.

A compatible disposition is durably recorded in the report without rewriting
the child. An updated or replaced child continues the review recursively. An
uncertain disposition names its blocking Question or Problem and leaves that
branch incomplete.

The report is Analysis, not evidence of its own correctness. Material evidence
remains claim-bound through explicit evidence relations. A release or
downstream gate that requires the revised atom must not pass until the report
concludes that every affected branch has reached a fixed point.

`carrier_only` changes require lossless-recoding verification but do not
require a Lineage Impact Analysis.

## Primary claim

One atomic Lineage Impact Analysis makes every non-carrier Atomic Artifact
revision's downstream disposition and fixed-point result durable.

## Rationale

A single change-bound report avoids per-child artifact explosion while keeping
each disposition tied to exact revisions, supporting evidence, resulting work,
and a replayable completion boundary.
