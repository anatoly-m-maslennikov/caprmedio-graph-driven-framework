---
atom_id: CA-E-538
content_role: Evaluation
type: Eval Case
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Active
author: Anatoly Maslennikov
version: 12
updated_at: 2026-10-27 19:59:37 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
relations:
  evaluation_for:
  - CA-R-1819
  - CA-M-325
  - CA-D-525
tier: 4
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
