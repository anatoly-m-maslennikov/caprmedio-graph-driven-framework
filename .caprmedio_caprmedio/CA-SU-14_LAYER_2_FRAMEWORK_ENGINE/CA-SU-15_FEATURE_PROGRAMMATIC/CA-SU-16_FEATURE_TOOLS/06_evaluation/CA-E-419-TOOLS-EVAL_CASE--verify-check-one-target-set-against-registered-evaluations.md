---
atom_id: CA-E-419
ref_id: CA-E-419
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Static Analysis"
tier: 3
relations:
  evaluation_for:
  - CA-M-253
status: Active
version: 23
updated_at: 2026-11-02 19:46:47 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Verify check one target set against registered Evaluations

## Claim checked

CA-M-253 returns stable attributable registered-Evaluation verdicts for one unchanged sealed target set **without** mutating **any** governed carrier.

## Applicable when

apply whenever `GRAPH_CHECK` target-set verification, criterion application, verdict ordering, **or** no-mutation boundary changes.

## Test case

inspect the registered `GRAPH_CHECK` unit, **then** use one sealed target set with two targets **and** two registered criteria yielding satisfied, unsatisfied, **and** inapplicable outcomes. execute the check, **then** alter the target-set source frontier **and** execute it again. separately exercise an unresolved target set **and** a registered criterion that reports an execution error. retain the exact registered criterion identity **and** failure evidence; error **or** blocked is **not** satisfied, unsatisfied **or** inapplicable.

## Acceptance criteria

`GRAPH_CHECK` has prefix `GRAPH_CHECK`, immediate `TOOLS` owner, `unordered_unit` kind, Structural level `4`, address `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/GRAPH_CHECK`, **and** realization path `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/GRAPH_CHECK/`. the unchanged case returns **every** attributable verdict, issue, **and** evidence **in** stable target-and-criterion order with no governed carrier change. the altered-frontier case is blocked **and** performs no evaluation **or** mutation. an unresolved target set returns the declared blocked **or** error disposition **without** criterion application; a criterion execution error remains explicitly attributable as error rather than an omitted **or** successful verdict. **all** cases preserve governed Atoms, Journals, native Implementation **and** derived outputs unchanged under CA-M-253.

## Failure disposition

reject the realization **and** preserve target set, criteria, expected verdicts, ordered result, source-frontier comparison, **and** no-mutation evidence.
