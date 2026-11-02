---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Atom/Content Role: Operations/Type: Step'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Atom/Content Role: Operations/Type: Step >{0+} Atom/Content Role: Operations/Type: Sub-step'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - Entity/Object/Occurrent/Execution/Workflow Run
version: 27
updated_at: 2026-10-29 07:32:39 +0400
relations: {}
atom_id: CA-R-1508@27
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Entity Definition
---
## Summary

Define Workflow

## Claim scope

the Workflow entity.

## Claim

a Workflow **means** an Atom with Content Role Operations **and** Type Workflow whose Claim specifies one reusable graph whose nodes are Steps and whose declared control-flow structure is owned by the Workflow graph.

- **every** graph node references its Step Atom; that Step owns either its leaf Action-or-Workflow reference **and** parameter/input bindings **or** its Sub-step structure under CA-R-1509-CORE_META_MODEL-DEFINITION--define-step. the graph owns **only** the scheme under CA-R-1570-CORE_META_MODEL-RULE--keep-workflow-graphs-separate-from-step-bindings **without** copying Step **or** Action definitions.
 - the graph declares its admitted Step order, structural Relations, entry points, **and** terminal outcomes. a Conditional Step definition owns its result-based routing and chooses **exactly one** branch; the Workflow graph does **not** use a separate result-transition Relation.
- the graph preserves its accepted success, retry-budget, **and** escalation conditions. It permits direct and indirect recursive Workflow calls through leaf Steps; it does not itself authorize concurrent execution or unlimited retries.
 - invocation context is selected per Agentic Step under CA-R-1527-CORE_META_MODEL-DEFINITION--define-agentic-step-execution-context; a mixed graph needs no separate Integrated **or** Isolated Workflow identity.
- the reusable graph is distinct from a Workflow Run. doer, finder, checker/test, **and** quality-gate evaluation remain examples of Action responsibilities, **not** a closed Action taxonomy.

CA-A-1256 records the containment declaration and counts. This next-version Draft does not promote the change.

A1263 permits a leaf Step to call a reusable Workflow with parameters. A containing Step has no own call, and its leaf Sub-steps call Actions only under A1264. Referenced Workflows remain independent reusable definitions, not contained copies.

A Workflow may call itself directly or indirectly through other Workflows. Its call graph need not be acyclic. CA-A-1277 records this decision; no mandatory recursion-depth limit or termination proof is introduced.

### Formal claim

```text
Atom/Content Role: Operations/Type: Workflow >{1+} Atom/Content Role: Operations/Type: Step
Atom/Content Role: Operations/Type: Step >{0+} Atom/Content Role: Operations/Type: Sub-step
```

## Details

A1262–A1264 record the accepted call-target and leaf-boundary decisions. This remains a next-version Draft; Current source and concrete Workflow instances are unchanged.

CA-A-1279 confirms the already-settled container hierarchy; no separate Type-catalog decision is inferred from it.

CA-A-1280 adopts the compact cardinality spelling without changing the counts.
