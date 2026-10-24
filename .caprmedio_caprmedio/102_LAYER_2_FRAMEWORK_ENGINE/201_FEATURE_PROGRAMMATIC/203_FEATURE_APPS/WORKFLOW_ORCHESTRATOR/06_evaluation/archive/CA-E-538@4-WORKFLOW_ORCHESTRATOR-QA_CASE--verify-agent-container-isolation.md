---
atom_id: CA-E-538@4
content_role: Evaluation
type: QA Case
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Archived
author: Anatoly Maslennikov
version: 4
updated_at: 2026-10-24 00:38:25 +0400
subjects:
  governs: Action/execution/isolation evaluation
  depends_on:
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Engineering/Carrier
  - Implementation
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
relations:
  evaluation_for:
  - CA-R-1819
  - CA-M-325
  - CA-D-525
tier: 3
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
