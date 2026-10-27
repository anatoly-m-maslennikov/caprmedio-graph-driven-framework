---
atom_id: CA-E-545
content_role: Evaluation
type: Eval Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Atom.Status
  - Subject/Graph Node/Carrier
version: 14
updated_at: 2026-10-27 06:04:45 +0400
relations:
  evaluation_for:
  - CA-R-1825
tier: 4
---
# Summary

Verify model-driven status dispatch

## Scope

Current status-model resolution for one selected Atom.

## Claim

Use fixtures with distinct admitted Content Role status models. Verify Create accepts each requested model-admitted initial Status and Tool-side Change Status and Archive derive only the actual carried Role and optional Type's current authoritative model, exact source/revision and destination mapping. Verify a manually created Draft with no retained history can perform an otherwise admitted explicit Status update. A request with caller-forged Role/Type/model identity, unavailable, ambiguous, stale, mismatched or unadmitted authority/status is rejected with its diagnostic and no write. Verify that no fixed status list makes an otherwise valid model-specific request succeed or fail, and that Journal absence or append failure does not change an observed admitted Status effect or authorize replay.

## Details

### Acceptance criteria

Each result identifies the resolved model source/revision, operation and authoritative destination decision. Prove Role/Type precedence, exact status casing, source-currentness, destination creation and collision handling, and same-status no-op. Rejected and preview cases leave all Carriers and history unchanged.
