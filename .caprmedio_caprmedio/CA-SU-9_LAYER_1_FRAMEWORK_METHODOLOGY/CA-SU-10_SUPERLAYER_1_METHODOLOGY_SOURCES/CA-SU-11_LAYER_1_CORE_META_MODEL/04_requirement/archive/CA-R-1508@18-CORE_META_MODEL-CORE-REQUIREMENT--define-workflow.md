---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - 'Subject/Graph/Relation/Type: On Result'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step/Execution Kind: Agentic.Execution Context'
  - Subject/Domain/Node/Continuant/Atom
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Domain/Node/Continuant/Atom.Substance
version: 18
updated_at: 2026-10-24 01:37:42 +0400
relations:
  relates_to:
  - CA-R-1570
atom_id: CA-R-1508@18
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

a Workflow **means** an Atom with Content Role Operations **and** Type Workflow whose Claim specifies one reusable graph whose nodes are Steps **and** whose edges are typed, directed Relations owned by the Workflow graph kind.

## Details

 - **every** graph node references its Step Atom; that Step owns its Action reference **and** parameter/input bindings under CA-R-1509-CORE_META_MODEL-CORE-REQUIREMENT--define-step. the graph owns **only** the scheme under CA-R-1570-CORE_META_MODEL-GENERAL-REQUIREMENT--keep-workflow-graphs-separate-from-step-bindings **without** copying Step **or** Action definitions.
 - the typed Relations define admitted control flow, including conditional branches **and** revisits. result-dependent next-Step edges use CA-R-1513-CORE_META_MODEL-GENERAL-REQUIREMENT--define-workflow-result-transition.
- the graph preserves its accepted success, retry-budget, **and** escalation conditions; it does **not** itself authorize concurrent execution, arbitrary recursion, **or** unlimited retries.
 - invocation context is selected per Agentic Step under CA-R-1527-CORE_META_MODEL-GENERAL-REQUIREMENT--define-agentic-step-execution-context; a mixed graph needs no separate Integrated **or** Isolated Workflow identity.
- the reusable graph is distinct from a Workflow Run. doer, finder, checker/test, **and** quality-gate evaluation remain examples of Action responsibilities, **not** a closed Action taxonomy.
