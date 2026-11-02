---
atom_id: CA-P-2612@1
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Backlog
version: 1
updated_at: "2026-10-22T19:29:13Z"
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2582]
  depends_on: [CA-P-2611]
  relates_to: [CA-R-1847, CA-R-1848, CA-D-547, CA-E-567, CA-E-568, CA-O-016]
---
# Summary

Align the current Workflow source contract package

## Objective

Prepare one bounded source package for the current Workflow contract:
R1847, R1848, D547, E567 and E568, with their connected current O016
definitions. Identify exact source pins, relations and drift against the
frozen fixture without mutating the visible Project binding.

## Details

At most 15 minutes of own work; one Task per file. Start only after CA-P-2611
is accepted. Preserve the frozen oracle, installed O016@13/CA-O-091 binding,
source hashes, current Project identity and business-only Journal semantics.
Use read-only MCP/source inspection and the locked uv environment. Report
missing, stale or conflicting sources explicitly; do not invent a replacement
route or silently broaden the source frontier. No production MCP traffic,
binding write, runtime admission, release, deployment, replay or full-suite
run.

## Definition of Done

Produce a separately reviewable source package containing exact R1847/R1848,
D547, E567/E568 and connected O016 pins, a bounded drift report and a clear
candidate-versus-current distinction. Leave the live Project projection and
installed runtime unchanged.
