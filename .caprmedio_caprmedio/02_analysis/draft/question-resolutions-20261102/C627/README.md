# C627 — Step invocation and parameter bindings

Applied to Current sources. C627 is Resolved.

A Step has exactly one execution form:

- RUNS one Action.
- RUNS one Workflow.
- CONTAINS one or more leaf Substeps.

A Substep RUNS one Action. Action and Workflow parameter bindings use previous Step outputs, enclosing Workflow Run input, or values fixed by the Step.

## Applied sources

- R2464, R2465, R2466: Workflow, Step, Substep Declarations.
- R2638: RUNS Declaration; replaces retired R2480. R2623 retains IS_RUN_BY as the derived inverse.
- R2639: Bind Step parameters. R1570 keeps the Workflow graph separate from Step bindings.
- R2243, R2487: actual-count test `{>n}`, using admitted numeric comparison.
- E669, E500, E658, D467: aligned source consumers. E658 retains the parallel Role-migration body exactly.
- R1569 and R1992: retired after their effective constraints and incoming consumers were covered. Deferred classification/routing notes remain in `rule-drafts/deferred-classification-and-routing-notes.md`.

The receipt records 14 publications, 15 predecessor archives, and 17 business events. Frozen inputs preserve source and Draft evidence; original Draft carriers were consumed.

## Checks

- Independent semantic review: PASS.
- Independent lifecycle preflight and applied readback: PASS.
- Step truth table: all 64 cases pass.
- Existing graph suite: 358 tests pass.
- Applied selected-source graph: 1,134 RMED sources; 41 Relation Declarations; no new coverage gaps, duplicate Declaration owners, missing Relation Semantics, old RUN bindings, or incoming unversioned references to the three retired sources.

## Pending work

The official graph projections were preserved. Their refresh is blocked by 12 existing parsing/binding gaps from the separate Analysis & Advisory Role migration. The selected-source frontier reflects the applied sources; `projection-refresh-status.json` records the blocker, and `verification/applied-contract-graph.json` retains the source-level result.

Actual Workflow instances, binding syntax, invocation runtime, and full CFEL evaluator conformance remain outside this change. Git publication is pending alongside unrelated in-progress changes; no Git index, commit, or remote was changed for C627.
