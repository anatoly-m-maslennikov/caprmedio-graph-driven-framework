---
role: Analysis
form: Specification Proposal
tier: 3
subjects:
  active: CAPRMEDIO_MODEL
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
atom_id: CA-A-1317
version: 1
status: Draft
updated_at: 2026-11-05 01:59:03 +0400
carrier_destination:
  file:
    name: CA-A-1317@1-draft-CORE_META_MODEL-SPECIFICATION_PROPOSAL--declare-occurrent-nodes-and-execution-event-relations.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/02_analysis/draft
---
## Summary

Declare Occurrent Nodes and execution-event Relations

## Proposal

Declare the Occurrent hierarchy and its execution-event Relations.

- Execution has Workflow Run, Step Run and Action Run kinds.
- Runtime has Internal Local, Internal Remote, External Local and External Remote Runtime kinds.
- Session is narrower than External Remote Runtime.
- Local means on the Operator's machine.
- Internal means part of the CAPRMEDIO application.
- Each Event Record records one Event. Its existing fields remain in place.
- Executions produce Events and run in Runtimes.
- Step is recursive. Each Step uses exactly one execution form: RUNS one Action, RUNS one Workflow, or CONTAINS one or more Steps.
- Retire the separate Substep kind. Step Run executes Step at any nesting level. Actual Workflow instances remain with their owners.

## Rationale

Declarations define the model kinds and their permitted Relations. Occurrences and their records have distinct identities. Reusable definitions admit actual Runs. Parent rules apply through inheritance. Recursive Steps preserve the same execution choice at every structural depth, without a separate Substep kind.

## Relation contracts

| Relation | Source | Target | Constraint |
| --- | --- | --- | --- |
| IS_EXECUTION_OF | Workflow Run, Step Run, Action Run | Matching definition | One definition per Run |
| HAS_EXECUTION | Reusable definition | Matching Runs | Zero or more |
| RECORDS | Event Record | Event | Exactly one |
| IS_RECORDED_BY | Event | Event Record | Zero or more |
| PRODUCES | Execution | Event | Zero or more |
| IS_PRODUCED_BY | Event | Execution | One or more; no maximum specified |
| EXECUTES | Runtime | Execution | Zero or more |
| IS_EXECUTED_BY | Execution | Runtime | One or more; no maximum specified |

## Draft Atoms

- CA-R-2749@1-draft — Declare Execution
- CA-R-2750@1-draft — Declare Workflow Run
- CA-R-2751@1-draft — Declare Step Run
- CA-R-2752@1-draft — Declare Action Run
- CA-R-2753@1-draft — Declare Runtime
- CA-R-2754@1-draft — Declare Session
- CA-R-2755@1-draft — Declare Event
- CA-R-2756@1-draft — Declare Internal Local Runtime
- CA-R-2757@1-draft — Declare Internal Remote Runtime
- CA-R-2758@1-draft — Declare External Local Runtime
- CA-R-2759@1-draft — Declare External Remote Runtime
- CA-R-2760@1-draft — Declare PRODUCES
- CA-R-2761@1-draft — Declare IS_PRODUCED_BY
- CA-R-2464@6-draft — Declare Workflow
- CA-R-2465@5-draft — Declare Step
- CA-R-2467@3-draft — Declare Action
- CA-R-2245@9-draft — Define IS_EXECUTION_OF Relation
- CA-R-2417@6-draft — Define HAS_EXECUTION Relation
- CA-R-2246@9-draft — Define RECORDS Relation
- CA-R-2421@6-draft — Define IS_RECORDED_BY Relation
- CA-R-2557@5-draft — Declare Event Record
- CA-R-2255@10-draft — Define EXECUTES Relation
- CA-R-2420@6-draft — Define IS_EXECUTED_BY Relation

## Adoption

Review the complete source packet. Promote accepted Drafts atomically with their prerequisite declarations. Rebuild the seven MODEL projections from the accepted sources. CA #3 owns implementation, data conversion, fixtures and test execution.

The Term registry remains. Entity is a general Term without an Entity root; Property has its reviewed Term meaning. IS_BLOCKED_BY / BLOCKS are already Current.

The recursive Step source packet is prepared separately in the Epic evidence. Existing native Drafts must be merged rather than replaced. Containment-cycle policy, carrier recursion and all affected endpoint permissions remain review gates; no new recursive Step source is claimed Current here.
