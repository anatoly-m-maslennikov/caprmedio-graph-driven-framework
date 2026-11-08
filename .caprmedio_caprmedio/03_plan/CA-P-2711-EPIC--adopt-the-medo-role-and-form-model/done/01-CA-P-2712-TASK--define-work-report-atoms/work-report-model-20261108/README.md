# CA-P-2712 — P / Work Report model adoption

Status: Done — model sources only.

A Work Report has its own P ID, the same Summary and Container as its reported work Plan, and exactly one direct IS_WORK_REPORT_FOR target using the Plan’s base Atom ID. Task remains the contextual name for that reported Plan; its navigation Label adds no type rule.

The report records actual changes, checks, results and remaining gaps in Markdown Details throughout execution. Its reporting Status is independent from the Task’s Status. Completed reporting can retain explicit gaps.

## Current sources

| Atom | Version | Contribution |
| --- | --- | --- |
| CA-R-2511 | 9 | Declare Atom/(.Role := Plan) |
| CA-R-1575 | 27 | Require work or decomposition in every Plan |
| CA-R-1599 | 24 | Require a Definition of Done for every Plan |
| CA-R-1418 | 30 | Give Every Atom One Summary |
| CA-M-306 | 36 | Author Plan Atoms |
| CA-M-309 | 25 | Write Plan Claims with the Plan CCE Profile |
| CA-D-470 | 31 | Serialize Plan file sections |
| CA-R-3006 | 6 | Declare Scope Delegation |
| CA-R-3008 | 6 | Establish Project and non-Project Scope Unit declarations and delegations |
| CA-R-970308624 | 2 | Declare Work Report Form |
| CA-R-970308626 | 2 | Declare IS_WORK_REPORT_FOR |
| CA-E-802 | 2 | Verify Work Report conformance |

## Verification

Twelve native Drafts were reviewed, repaired, manually promoted and read back. Nine predecessors retain exact bytes. [Source check](post-adoption-check.json) covers 33 exact effects, unchanged reviewed bodies, identities, Versions and removal of consumed Drafts. Promotion uses max(all same-ID Versions, including Drafts) + 1.

[Workbench readback](workbench-readback.json) confirms the new Form, Relation and Evaluation are Current and Active. Grouped Header fields were selected using the live query_schema.

[Worked example](worked-example.json) demonstrates reporting during execution and Task/report completion. It is a virtual model example with assertions, not native report admission.

## Coordination and remaining work

The overlapping Work Report Draft was transferred by CA #8: Workbench and reused under its allocated ID. The direct Relation is IS_WORK_REPORT_FOR. [Consumer contract](consumer-handoff.json) records native authoring, validation, content mapping and projection boundaries.

No actual Work Report instances were created or migrated. Engine, Workbench, Workflows, installed copies, projections and releases were not changed by this task. No native Run or Journal record was fabricated. The parent Epic remains Active for its remaining migration and consumer gates.
