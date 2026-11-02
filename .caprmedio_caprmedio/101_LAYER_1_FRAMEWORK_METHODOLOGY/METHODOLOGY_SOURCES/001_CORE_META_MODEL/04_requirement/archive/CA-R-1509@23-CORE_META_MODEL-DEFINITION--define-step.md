---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Atom/Content Role: Operations/Type: Step'
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Atom/Content Role: Operations/Type: Step >{0+} Atom/Content Role: Operations/Type: Sub-step'
  - Entity/Object/Occurrent/Execution/Step Run
version: 23
updated_at: 2026-10-29 07:32:39 +0400
relations: {}
atom_id: CA-R-1509@23
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Entity Definition
tier: 1
---
## Summary

Define Step

## Claim scope

The reusable Step definition within a Workflow.

## Claim

A Step is a node within exactly one Workflow. A leaf Step specifies one call, with its parameter and input bindings: either a reusable Action or a reusable Workflow. A Step that contains Sub-steps executes those Sub-steps and makes no Action or Workflow call of its own.

A Step cannot exist independently of a Workflow. Each Workflow has at least one Step; a Step may contain zero or more Sub-steps. A Sub-step is a distinct leaf kind and calls an Action only. It cannot call a Workflow or contain further Sub-steps.

A Linear Step has ordered nonconditional Sub-steps and no conditional Sub-steps. A Conditional Step selects exactly one branch from its declared condition and may use Actor input. Result routing belongs to that Step definition.

Bindings identify the sources of required inputs and parameters, including Workflow inputs or earlier results; they need not fix runtime values in the definition.

### Formal claim

```text
Atom/Content Role: Operations/Type: Workflow >{1+} Atom/Content Role: Operations/Type: Step
Atom/Content Role: Operations/Type: Step >{0+} Atom/Content Role: Operations/Type: Sub-step
```

## Semantics

A call refers to a reusable definition; it does not structurally contain or copy that Action or Workflow. Different Steps can call the same definition with different bindings. A leaf Step may call its enclosing Workflow, or another Workflow that calls back to it, under CA-A-1277. Containment of Sub-steps does not imply specialization or inherited Atom properties.

## Details

Agentic Action context follows the applicable invocation rules; a Programmatic Action does not acquire Agent context solely from being called by a Step. This definition remains distinct from its Step Run and from internal Tool calls.

A1262–A1264 settle leaf Sub-steps, Workflow calls by Steps, and Action-only Sub-steps. Exact Type admission remains separate; no new Run kind, engine field or runtime implementation is introduced. CA-A-1277 permits direct and indirect Workflow-call cycles without changing these leaf boundaries.

CA-A-1279 confirms the already-settled container hierarchy; no separate Type-catalog decision is inferred from it.

CA-A-1280 adopts the compact cardinality spelling without changing the counts.
