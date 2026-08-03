---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-119
scope_path: layer:meta
subject_scopes:
  - artifact-model
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-086
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-META-091
      - CARMADIO-REQUIREMENT-META-092
      - CARMADIO-REQUIREMENT-META-093
      - CARMADIO-REQUIREMENT-META-112
      - CARMADIO-REQUIREMENT-META-116
---

# Requirement — Preserve Content-role boundaries through the loop

Every transition through Concern, Analysis, Requirement, Method, Assurance,
Delivery, Implementation, and Ops produces or updates the meaning owned by the
receiving Content role without converting the source meaning into that role or
implying completion of a later role.

In particular:

- Analysis may inform a Requirement but does not establish it without
  acceptance;
- a Requirement states the desired outcome but does not select its Method;
- Method, Assurance, and Delivery specify different realization obligations;
- Implementation materially realizes accepted claims but does not prove that
  they pass Assurance or succeed in operation; and
- Ops records enacted facts but does not silently rewrite normative authority.

Relations carry meaning between roles while every related artifact retains its
own identity, authority, lifecycle, and owning role.

## Primary claim

CARMADIO transitions connect its eight Content roles without allowing any role
to substitute for another or imply that a later role has been completed.

## Rationale

This adapts FPF Role–Method–Work Alignment to the complete CARMADIO loop while
preserving the independently governed contribution of every role.
