---
atom_id: CA-P-1846@6
content_role: Plan
type: Plan
label: Task
work_sequence_number: 17
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
version: 6
updated_at: 2026-10-24 09:20:34 +0400
subjects:
  governs: CAPRMEDIO Framework Instance
  depends_on:
  - Subject/Domain/Node/Continuant/Project
  - Subject/Domain/Node/Continuant/Project.Settings
  - Subject/Domain/Node/Continuant/Project.Structure
  - Subject/Domain/Node/Continuant/Project.Framework Settings
  - Subject/Engineering/Tool
  - Subject/Engineering/Action
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Subject/Engineering/Carrier
  - Subject/Engineering/Evaluation
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
relations:
  is_decomposition_of:
  - CA-P-1829
  blocks:
  - CA-P-1847
tier: 3
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
