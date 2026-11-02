---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - Subject/Graph Node/Domain/Occurrent/Execution/Step Run
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action/Execution Kind'
  - Subject/Graph Node/Domain/Occurrent/Execution/Step Run.Agentic Step Execution Context
  - Subject/Graph Node/Engineering/Workflow Execution/Tool Call Step Boundary
version: 18
updated_at: 2026-10-26 05:59:45 +0400
relations: {}
atom_id: CA-R-1509@18
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Definition
tier: 1
---
# Summary

Define Step

## Scope

the Step entity.

## Claim

a Step **means** a node **in** a Workflow, defined by **`=1`** Step Atom, that specifies invocation of **`=1`** Action with the parameters **and** inputs for that invocation.

## Details

- the binding identifies the source of **every** required input **or** parameter, including a Workflow input **or** an earlier Step result **when** applicable; it need **not** fix runtime values **in** the definition.
- different Steps **may** reference the same Action with different bindings **without** copying **or** redefining that Action.
- an Agentic invocation selects Integrated **or** Isolated context under CA-R-1527; a Programmatic invocation does **not** acquire an Agent context by this rule.
- the Step definition is distinct from its referenced Action **and** from a Step Run. internal Tool calls remain execution details under CA-R-1528, **not** additional Step definitions.
