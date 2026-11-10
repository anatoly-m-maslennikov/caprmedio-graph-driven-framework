---
atom_id: CA-E-538@12
ref_id: CA-E-538@12
container:
  scope_unit: CA-SU-2
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Effect
    Authorization
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
tier: 4
relations:
  evaluation_for:
  - CA-R-1819
  - CA-M-325
  - CA-D-525
status: Archived
version: 12
updated_at: 2026-10-27 19:59:37 +0400
carrier_destination:
  file:
    name: CA-E-538@12-WORKFLOW_ORCHESTRATOR-EVAL_CASE--verify-agent-container-isolation.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-2_APP_WORKFLOW_ORCHESTRATOR/06_evaluation/archive
current_scope_unit: WORKFLOW_ORCHESTRATOR
author: Anatoly Maslennikov
---
# Summary

verify Agent container isolation

## Scope

the Docker Agent service's admission **and** filesystem boundaries.

## Claim

the Evaluation **must** verify that an isolated Agent can return proposals but cannot access host Project Carriers **or** runtime-control capabilities.

## Details

- inspect the resolved configuration: Agent has no Project, host-home **or** Docker socket mount, no published port, no privileged mode **and** no added capabilities.
- test rejected unknown fields, invalid phases, oversized requests, concurrent dispatch **and** invalid structured output.
- verify denied Project write probes **and** absence of credential files from image layers **and** public outputs.
- verify missing credentials produce an explicit readiness failure **without** starting a real Workflow.
