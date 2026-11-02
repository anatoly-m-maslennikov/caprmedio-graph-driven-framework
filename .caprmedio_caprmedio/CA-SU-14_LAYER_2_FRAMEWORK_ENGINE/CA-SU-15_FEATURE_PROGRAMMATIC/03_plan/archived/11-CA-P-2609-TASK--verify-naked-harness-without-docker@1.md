---
atom_id: CA-P-2609@1
content_role: Plan
type: Plan
label: Task
work_sequence_number: 11
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
version: 1
updated_at: "2026-10-22T17:26:30Z"
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2581]
  depends_on: [CA-P-2597, CA-P-2607]
  relates_to: [CA-P-2601, CA-P-2602, CA-O-016]
---
# Summary

Verify the Docker-free isolated MCP harness

## Objective

Run the focused interactive-continuation checks in a naked isolated harness
without Docker or the production MCP port. Verify that current-session prompt
return, validated submission, pending/terminal transitions, explicit Project
binding and no-replay behavior remain attributable under the source-first O016
configuration.

## Details

Own work is bounded to 15 minutes. Use disposable frozen Project inputs, a
distinct nonproduction state/port if an HTTP boundary is required, locked uv,
and Project Temporary State. Do not start containers, touch production, replay
uncertain history, rebuild projections as authority, run the full suite, or
publish Git changes. Keep implementation, harness and real-Manifest journey
evidence separate; a Docker-free pass cannot claim runtime admission.

### Definition of Done

The focused naked-harness command passes or returns explicit bounded failures
for prompt/result and source-binding cases, with receipt paths, protected
production equality and the remaining complete real-Manifest gate recorded.
