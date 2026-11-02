# Summary and Active Plan numbering — 2026-11-01

Summary coverage is preserved in the approved authoring Method. Its Declaration is formal-only. The formal ID-to-Summary dependency selects only Current and Archived historical states; Drafts are excluded before tuple resolution. Same ID/different Summary violates that dependency there. Repeated equal pairs and different IDs with equal Summaries do not violate it. Unknown conditions cannot be silently omitted.

Sequence Number is optional and positive when supplied. Uniqueness is checked only for Status Active, within each direct container in the current Project snapshot. Done, Canceled, Backlog, Draft and Archived are excluded from this uniqueness population. A numbered Active Plan must have one known direct typed container. Separate reference-leaf keys support Atom and Scope Unit containers. Task1 and its Subtask1 can coexist because their direct containers differ.

The model contains only Number constraints. Execution order belongs to the Workflow for P execution. The explanatory sentence was removed under the explicit user decision; no extra navigation Method was created.

Both bounded reviews passed. Six Summary-scope cases and ten numbering cases are model examples, not runtime tests. Model, parser, history/reference and Workflow implementation remain separate.

[Summary review](declaration-expansion/summary-accepted-scope-review-20261101.json) · [Number review](declaration-expansion/local-plan-number-review-20261101.json) · [Number scope decision](declaration-expansion/plan-number-scope-decision-20261101.json) · [Remaining prose](remaining-node-claim-prose-20261031.md)

Latest count:19 descendant Declaration Claims retain prose (3 Primary and16 Property).111 Drafts;27 Primary and47 Property Declarations. Structural/hash/link checks pass;750 snapshotted Current Core Requirements and Current Epic38 remain unchanged. No parser or runtime deployment, renumbering, Workflow-instance review or promotion was performed.
