---
atom_id: CA-P-1846
content_role: Plan
type: Plan
label: Task
work_sequence_number: 17
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Done
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 01:23:38 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on:
    - "Project"
    - "Project Settings"
    - "Project Structure"
    - "Framework Instance Settings"
    - "Tool"
    - "Action"
    - "Workflow Run"
    - "Carrier"
    - "Evaluation"
    - "AI Agent"
    - "Operator"
relations:
  is_decomposition_of:
    - CA-P-1829
  blocks:
    - CA-P-1847
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
