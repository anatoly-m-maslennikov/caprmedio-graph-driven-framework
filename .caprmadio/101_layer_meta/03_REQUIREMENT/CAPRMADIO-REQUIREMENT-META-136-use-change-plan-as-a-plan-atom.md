---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-136
scope_path: layer:meta
subject_scope: lifecycle-traceability
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-130
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-131
      - CAPRMADIO-REQUIREMENT-META-133
  - type: relates_to
    targets:
      - CAPRMADIO-ANALYSIS-META-003
      - CAPRMADIO-REQUIREMENT-META-090
      - CAPRMADIO-REQUIREMENT-META-101
---

# Requirement — Use Change Plan as a Plan Atom

`change_plan` is a direct subtype of the internal `plan` Atom Type. It is an
accepted operative statement of intended project change, not an Analysis
finding, normative specification claim, code-writing Method, or realized
Implementation.

A Change Plan identifies the governed artifacts and native project targets to
add, refine, replace, archive, or review; their ordering and dependencies; and
the completion conditions for the bounded change. It may span Requirement,
Method, Assurance, Delivery, Implementation, and Ops consequences without
changing the authority owned by any of those roles.

A draft Change Plan may evolve before admission. Once execution or another
governed artifact depends on its admitted revision, ordinary Atom refinement
and replacement rules apply.

Projects may omit a Change Plan for a trivial direct change. A Change Plan is
expected when work spans multiple governed artifacts, Content roles,
`scope_path` values, or native implementation targets.

## Primary claim

CAPRMADIO represents an accepted cross-artifact change plan as a `change_plan`
subtype of the internal Plan Atom Type.

## Rationale

An accepted plan is a stable governed claim about intended work. Atomic
admission gives execution an exact parent revision without pretending the plan
is the resulting specification or implementation.
