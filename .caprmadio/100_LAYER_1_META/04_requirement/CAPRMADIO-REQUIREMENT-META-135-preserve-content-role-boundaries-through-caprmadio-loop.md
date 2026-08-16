---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-135
scope_path: layer:meta
subject_scope: semantics
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-META-119
  child_of:
    - CAPRMADIO-REQUIREMENT-114-apply-mece-to-canonical-decompositions
    - CAPRMADIO-REQUIREMENT-116-preserve-strict-semantic-distinctions
---

# Requirement — Preserve boundaries through the CAPRMADIO loop

Every transition through Concern, Analysis, Plan, Requirement, Method,
Assurance, Delivery, Implementation, and Ops produces or updates the meaning
owned by the receiving Content role without converting the source meaning into
that role or implying completion of a later role.

In particular:

- Analysis owns findings, alternatives, explanation, and rationale but not the
  action list;
- Plan contains and coordinates action points but does not contain Analysis,
  modify the Specification, or realize the work;
- Requirement states a desired outcome but does not select its Method;
- Method, Assurance, and Delivery specify distinct realization obligations;
- Implementation materially realizes accepted claims but does not prove their
  assurance or operational success; and
- Ops records enacted facts but does not silently rewrite normative authority.

Relations carry meaning between roles while every related artifact retains its
own identity, authority, lifecycle, and owning role.

## Primary claim

CAPRMADIO transitions connect its nine Content roles without allowing a role to
substitute for another or imply that a later role is complete.
