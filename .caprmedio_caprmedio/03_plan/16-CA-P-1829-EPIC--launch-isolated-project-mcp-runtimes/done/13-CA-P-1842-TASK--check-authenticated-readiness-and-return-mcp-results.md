---
atom_id: CA-P-1842
content_role: Plan
type: Plan
label: Task
work_sequence_number: 13
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Done
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 01:12:07 +0400"
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
    - CA-P-1843
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
