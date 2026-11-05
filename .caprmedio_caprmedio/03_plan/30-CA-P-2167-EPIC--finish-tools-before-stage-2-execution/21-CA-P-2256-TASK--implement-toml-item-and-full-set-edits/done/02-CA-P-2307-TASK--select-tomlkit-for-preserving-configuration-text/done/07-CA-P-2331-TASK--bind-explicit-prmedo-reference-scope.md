---
atom_id: CA-P-2331
ref_id: CA-P-2331
role: Plan
form: Plan
label: Task
work_sequence_number: 7
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
topics:
  main_subject: Subject/Graph Node/Engineering/Continuant/Tool
  dependencies:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
version: 6
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-2307
tier: 3
container:
  atom: CA-P-2307
carrier_destination:
  file:
    name: 7-CA-P-2331-TASK--bind-explicit-prmedo-reference-scope.md
    path: .caprmedio_caprmedio/03_plan/30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/21-CA-P-2256-TASK--implement-toml-item-and-full-set-edits/done/2-CA-P-2307-TASK--select-tomlkit-for-preserving-configuration-text/done
---
# Summary

Bind explicit PRMEDO reference scope

## Objective

Let the private complete-carrier validator honor an explicit declared Content Role reference scope, including the Operator-selected PRMEDO scope, without changing its default complete frontier.

## Details

Estimated own work: up to 15 minutes. Use the existing source-bound role-directory map and admitted-container inventory. Validate a nonempty unique tuple of canonical admitted roles and require the candidate role inside it. Limit traversal only; preserve every finite carrier, Type, Status, source-pin, graph, placement, duplicate and currentness check.

For explicit scope, resolve every carried relation even when existing relations would otherwise be allowed. A required off-scope reference must refuse, never disappear or be satisfied from unrelated authority-source records. Report the exact selected role scope as finite evidence, never whole-Project admission. Default callers remain unchanged; no public request, receiver, writer or new dependency is added.

Independently test selected-scope success, invalid scope, off-scope candidate/reference refusal, stale-source refusal and default behavior. Run actual admission on the four current TOML packet carriers after their separately approved header repairs. Report further blockers; do not weaken checks.

### Acceptance

Independent frozen review passed 58/58 reference tests, including 12 independent controls. Actual current PRMEDO admission passed P2307 and truthfully refused M383/D632/E635 on separate canonical-ordering/relates_to authority gaps. See .caprmedio_caprmedio/_projection/core-entity-review/stage2/tools-first/explicit-prmedo-reference-scope-acceptance.md. This closes only explicit scoped admission behavior; no whole-Project or TOML implementation acceptance is inferred.

### Definition of Done

The Plan is not Done if scope is implicit, a required dependency is skipped, default behavior changes, current authority is unverified, focused refusal and success checks lack independent acceptance, or finite admission is presented as whole-Project validity.
