---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step/Execution Kind: Agentic.Execution Context'
  - Subject/Graph Node/Domain/Continuant/Atom
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Graph Node/Domain/Continuant/Atom.Content
version: 24
updated_at: 2026-10-26 17:20:40 +0400
relations: {}
atom_id: CA-R-1508@24
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Definition
---
# Summary

Define Workflow

## Scope

the Workflow entity.

## Claim

a Workflow **means** an Atom with Content Role Operations **and** Type Workflow whose Claim specifies one reusable graph whose nodes are Steps and whose declared control-flow structure is owned by the Workflow graph.

## Details

 - **every** graph node references its Step Atom; that Step owns either its leaf Action reference **and** parameter/input bindings **or** its nested Step structure under CA-R-1509-CORE_META_MODEL-DEFINITION--define-step. the graph owns **only** the scheme under CA-R-1570-CORE_META_MODEL-RULE--keep-workflow-graphs-separate-from-step-bindings **without** copying Step **or** Action definitions.
 - the graph declares its admitted Step order, structural Relations, entry points, **and** terminal outcomes. a Conditional Step definition owns its result-based routing and chooses **exactly one** branch; the Workflow graph does **not** use a separate result-transition Relation.
- the graph preserves its accepted success, retry-budget, **and** escalation conditions; it does **not** itself authorize concurrent execution, arbitrary recursion, **or** unlimited retries.
 - invocation context is selected per Agentic Step under CA-R-1527-CORE_META_MODEL-DEFINITION--define-agentic-step-execution-context; a mixed graph needs no separate Integrated **or** Isolated Workflow identity.
- the reusable graph is distinct from a Workflow Run. doer, finder, checker/test, **and** quality-gate evaluation remain examples of Action responsibilities, **not** a closed Action taxonomy.
