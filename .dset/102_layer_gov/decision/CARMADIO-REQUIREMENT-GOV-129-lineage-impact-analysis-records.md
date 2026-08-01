---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-GOV-129
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
      - CARMADIO-REQUIREMENT-META-097
      - CARMADIO-REQUIREMENT-GOV-127
      - CARMADIO-REQUIREMENT-GOV-128
---

# Requirement — Record one Lineage Impact Analysis per changed atom revision

Every `refinement`, `semantic_revision`, or `replacement` of an admitted
Atom produces one Analysis Atom whose primary conclusion
is the impact state of that exact changed parent revision.

The report records:

- the changed artifact ID and exact previous and new Git revisions;
- the assigned change class and the observed basis or rationale for the change;
- the responsible operator and session provenance already required for the
  Analysis carrier;
- the expected impact radius;
- every directly examined child and the exact child revision examined;
- one `compatible`, `update_required`, `replacement_required`, or `uncertain`
  disposition for each child;
- the evidence or reasoning supporting each disposition;
- every resulting child revision, successor, or blocking Concern Atom; and
- the recursive branch result and overall fixed-point conclusion.

One report may contain many child rows because those rows support the single
primary conclusion that the changed parent revision's impact review is
complete or blocked. The report does not replace the children, their evidence,
or their own semantic claims.

A compatible disposition is durably recorded in the Analysis Atom without
rewriting the child. An updated or replaced child continues the review
recursively. An uncertain disposition names its blocking Concern Atom and
leaves that branch incomplete.

The Analysis Atom is not Ops evidence of its own correctness. Material Ops
evidence remains claim-bound through explicit evidence relations. A release or
downstream gate that requires the revised atom must not pass until the report
concludes that every affected branch has reached a fixed point.

`carrier_only` changes require lossless-recoding Verification but do not
require a Lineage Impact Analysis Atom.

## Primary claim

One Lineage Impact Analysis Atom makes every non-carrier Atom
revision's downstream disposition and fixed-point result durable.

## Rationale

A single change-bound report avoids per-child artifact explosion while keeping
each disposition tied to exact revisions, supporting evidence, resulting work,
and a replayable completion boundary.
