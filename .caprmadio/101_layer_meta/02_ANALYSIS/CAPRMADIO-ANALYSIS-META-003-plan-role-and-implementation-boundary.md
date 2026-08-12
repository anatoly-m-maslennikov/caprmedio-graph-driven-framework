---
artifact_type: analysis
artifact_id: CAPRMADIO-ANALYSIS-META-003
scope_path: layer:meta
subject_scope: artifact-model
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: analysis_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-086
      - CAPRMADIO-REQUIREMENT-META-087
      - CAPRMADIO-REQUIREMENT-META-088
      - CAPRMADIO-REQUIREMENT-META-089
      - CAPRMADIO-REQUIREMENT-META-113
      - CAPRMADIO-REQUIREMENT-META-119
      - CAPRMADIO-REQUIREMENT-META-130
---

# Analysis — Plan role and Implementation boundary

## Question

Where does an accepted plan for changing Requirements and their resulting
realization belong when it is neither an Analysis finding, a Requirement, a
code-writing Method, nor the resulting Implementation?

## Findings

An Analysis explains what was learned and may recommend work. A Change Plan
accepts and coordinates intended work: which governed artifacts and native
project targets will be added, refined, replaced, archived, or reviewed; in
what order; and under which completion conditions. The plan does not itself
change the normative specification or realize the planned work. It therefore
needs a distinct Plan Content role between Analysis and Requirement.

The real Implementation is the project realization outside `.caprmadio/`,
including its native code, configuration, executable assurance mechanisms,
packages, documentation, and automation. A Journal or Projection about that
realization is not the realization itself. Consequently, the Implementation
role remains part of the framework model without requiring an internal
Implementation Atom.

The resulting lifecycle is:

```text
Concern -> Analysis -> Plan -> Requirement -> Method -> Assurance
        -> Delivery -> Implementation -> Ops -> Concern
```

The specification segment remains Requirement, Method, Assurance, and
Delivery. The model can therefore be read as `CAP · RMAD · IO`:

- `CAP`: Concern, Analysis, Plan;
- `RMAD`: Requirement, Method, Assurance, Delivery; and
- `IO`: Implementation, Ops.

`CAPSIO` was considered as a shorter name by collapsing `RMAD` into
Specification. It was rejected because it hides useful specification
boundaries and conflicts with the existing public Capsio Technology identity
at <https://capsio.com.cn/>.

FPF Role-Method-Work Alignment supports the underlying separation: a plan for
intended work, a reusable method, performed work, and a record describing that
work have different identities. CAPRMADIO adapts that distinction by assigning
Change Plan to Plan, native project realization to Implementation, and factual
execution results to Ops.

## Conclusion

The framework should become CAPRMADIO, add Plan as a first-class Content role,
admit Change Plan as a Plan Atom subtype, and stop requiring an internal
Implementation Atom merely to populate every semantic coordinate.

## Open boundary

This analysis does not decide whether an Implementation Journal is mandatory,
where a durable Journal must live, or which Implementation Projections must be
committed rather than generated at runtime. Those storage and retention rules
require a separate governed decision.
