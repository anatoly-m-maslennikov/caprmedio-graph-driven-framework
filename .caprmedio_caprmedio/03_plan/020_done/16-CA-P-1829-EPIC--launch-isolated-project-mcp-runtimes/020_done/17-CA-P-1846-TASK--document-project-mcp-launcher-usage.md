---
atom_id: CA-P-1846
ref_id: CA-P-1846
container:
  atom: CA-P-1829
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/MCP
  dependencies:
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Domain/Continuant/Project.Settings
  - Subject/Graph Node/Domain/Continuant/Project.Structure
  - Subject/Graph Node/Domain/Continuant/Project.Framework Settings
  - Subject/Graph Node/Engineering/Continuant/Tool
  - Subject/Graph Node/Engineering/Action
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - Subject/Graph Node/Engineering/Evaluation
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
tier: 3
relations:
  is_decomposition_of:
  - CA-P-1829
  blocks:
  - CA-P-1847
status: Done
version: 8
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 17-CA-P-1846-TASK--document-project-mcp-launcher-usage.md
    path: .caprmedio_caprmedio/03_plan/020_done/16-CA-P-1829-EPIC--launch-isolated-project-mcp-runtimes/020_done
work_sequence_number: 17
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Document Project MCP launcher usage

## Objective

the AI Agent documents the implemented launcher so the Operator can obtain **and** use the selected Project's MCP endpoint.

## Details

- input: the integrated command **and** reviewed input/output, authentication, compatibility, **and** lifecycle boundaries.
- output: short usage **and** connection examples **in** the Docker runtime README **and** a discoverable root README link; cover Project selection, returned URL, separate credential configuration, healthy reuse, **and** truthful startup failures.
- verification: check the examples against the actual command. distinguish MCP readiness from worker/Workflow execution **and** explain URL changes **after** explicit recreation; provide no live credentials.
- effort: **`<=10`** minutes for **`=1`** AI Agent; the Epic's decomposition rule applies **before** execution **if** the estimate no longer holds.

### Definition of Done

the Plan is **not** Done **if** ((a documented command differs from the implemented interface) **or** (the connection example omits required authentication) **or** (documentation implies automatic Workflow execution **or** unverified readiness)).

- completion evidence: root README **and** Docker README document the actual Project root, direct control folder, separately explicit Framework source, JSON/URL output, bearer-header authentication, safe reuse, failure conditions, **and** HTTP-only boundary.
- verification: CLI help agrees with documented flags; **`=3`** CLI tests passed; documentation diff checks passed. no release **or** installed runtime change is claimed.
