---
cce_version: cce_1
cce_form: rationale
subjects:
  declared:
    occurrent:
      - development-flow
subject_scope: artifact-model
priority: high
version: 4
updated_at: 2026-08-23 15:00:38
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: analysis_of
    targets:
      - CAPRMEDIO-META-REQU-254--eight-content-roles-with-delivery-and-ops
      - CAPRMEDIO-META-REQU-255--caprmedio-framework-identity
      - CAPRMEDIO-META-REQU-256--internal-atom-types-equal-eight-content-roles
      - CAPRMEDIO-META-REQU-257--coordinate-artifacts-without-a-72-type-bijection
      - CAPRMEDIO-META-REQU-105--preserve-implementation-traceability-in-journals
      - CAPRMEDIO-META-REQU-265--preserve-content-role-boundaries-through-the-loop
      - CAPRMEDIO-META-REQU-270--use-change-plans-and-implementation-record-projections
---
# Analysis — Plan role and Implementation boundary

## Question

Where does an accepted plan for changing Requirements and their resulting realization belong when it is neither an Analysis finding, a Requirement, a code-writing Method, nor the resulting Implementation?

## Findings

An Analysis explains what was learned and MAY recommend work. A Change Plan accepts and coordinates intended work: which governed artifacts and native project targets will be added, refined, replaced, archived, or reviewed; in what order; and under which completion conditions. The plan does not itself change the normative specification or realize the planned work. It therefore needs a distinct Plan Content role between Analysis and Requirement.

The real Implementation is the project realization outside `.caprmedio/`, including its native code, configuration, executable evaluation mechanisms, packages, documentation, and automation. A Journal or Projection about that realization is not the realization itself. Consequently, the Implementation role remains part of the framework model without requiring an internal Implementation Atom.

The resulting lifecycle is:

```text
Concern -> Analysis -> Plan -> Requirement -> Method -> Evaluation
        -> Delivery -> Implementation -> Ops -> Concern
```

The specification segment remains Requirement, Method, Evaluation, and Delivery. The model can therefore be read as `CAP · RMED · IO`:

- `CAP`: Concern, Analysis, Plan;
- `RMED`: Requirement, Method, Evaluation, Delivery; and
- `IO`: Implementation, Ops.

`CAPSIO` was considered as a shorter name by collapsing `RMED` into Specification. It was rejected because it hides useful specification boundaries and conflicts with the existing public Capsio Technology identity at <https://capsio.com.cn/>.

FPF Role-Method-Work Alignment supports the underlying separation: a plan for intended work, a reusable method, performed work, and a record describing that work have different identities. CAPRMEDIO adapts that distinction by assigning Change Plan to Plan, native project realization to Implementation, and factual execution results to Ops.

## Conclusion

The framework should become CAPRMEDIO, add Plan as a first-class Content role, admit Change Plan as a Plan Atom subtype, and stop requiring an internal Implementation Atom merely to populate every semantic coordinate.

## Open boundary

This analysis does not decide whether an Implementation Journal is mandatory, where a durable Journal MUST live, or which Implementation Projections MUST be committed rather than generated at runtime. Those storage and retention rules require a separate governed decision.
