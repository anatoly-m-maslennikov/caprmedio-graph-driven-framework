---
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Workflow"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Entity/Occurrent/Execution/Workflow Run", "Entity/Continuant/Object/Relation/Type: On Result", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step/Execution Kind: Agentic.Execution Context", "Entity/Continuant/Object/Atom", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Workflow", "Entity/Continuant/Object/Atom.Substance"]
version: 10
updated_at: "2026-10-16 12:08:29 +0000"
relations: {"relates_to": ["CA-R-1570"]}
atom_id: "CA-R-1508"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1508-CORE_META_MODEL-CORE-REQUIREMENT--define-workflow.md
  source_atom_id: CA-R-1508
  source_atom_revision: 10
  source_sha256: ab4d6fe0b37830c025444fabdf2b56cb1b1a4303745a52cae8d7c5bd4f425cc1
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
