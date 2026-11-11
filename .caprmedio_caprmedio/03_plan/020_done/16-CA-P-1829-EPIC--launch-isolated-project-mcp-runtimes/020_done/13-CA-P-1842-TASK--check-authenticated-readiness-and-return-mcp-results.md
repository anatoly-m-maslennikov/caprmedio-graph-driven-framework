---
atom_id: CA-P-1842
ref_id: CA-P-1842
container:
  atom: CA-P-1829
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Gateway
  dependencies:
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Domain/Continuant/Project.Settings
  - Subject/Graph Node/Domain/Continuant/Project.Structure
  - Subject/Graph Node/Domain/Continuant/Project.Framework Settings
  - Subject/Graph Node/Engineering/Continuant/Tool
  - Subject/Graph Node/Engineering/Action
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - Subject/Graph Node/Engineering/Validation
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
tier: 3
relations:
  is_decomposition_of:
  - CA-P-1829
  blocks:
  - CA-P-1843
status: Done
version: 9
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 13-CA-P-1842-TASK--check-authenticated-readiness-and-return-mcp-results.md
    path: .caprmedio_caprmedio/03_plan/020_done/16-CA-P-1829-EPIC--launch-isolated-project-mcp-runtimes/020_done
work_sequence_number: 13
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Check authenticated readiness **and** return MCP results

## Objective

the AI Agent implements the launcher's authenticated readiness gate **and** safe result construction.

## Details

- input: the startup result, result RMED, **and** startup/output golden tests.
- output: a bounded host-side readiness check using the accepted credential source **and** verified published endpoint; ready output includes the actual `/mcp` URL **and** safe instance metadata, while failures expose no success URL.
- verification: exercise correct/wrong/missing credentials, timeout, hostile Host/Origin, unhealthy service, **and** output redaction. an MCP handshake is required **only if** the reviewed readiness contract selects it.
- effort: **`<=15`** minutes for **`=1`** AI Agent; the Epic's decomposition rule applies **before** execution **if** the estimate no longer holds.

### Definition of Done

- completion evidence: all 12 startup test methods passed, covering the 13 safe condition codes, authenticated readiness, failure attribution, metadata **and** token redaction; the default backend uses a bounded host MCP initialization exchange.

the Plan is **not** Done **if** ((a success result precedes the required readiness evidence) **or** (credentials appear **in** URLs, ordinary results, **or** diagnostics) **or** (the readiness/output tests fail)).
