---
atom_id: CA-P-2613@3
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Backlog
version: 3
updated_at: "2026-10-23T00:10:20+0400"
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2582]
  depends_on: [CA-P-2611, CA-P-2612]
  relates_to: [CA-O-016, CA-A-1142, CA-W-09]
---
# Summary

Prepare the detached candidate and registry-drift validation

## Objective

Build a detached candidate from the reviewed source package and validate its
registry/frontier drift before any publication decision. Explicitly account
for A1142 and the W09 old-frontier registry entry; keep the candidate separate
from the actual Project binding.

## Details

At most 15 minutes of own work; one Task per file. Start only after CA-P-2611
is accepted and CA-P-2612 supplies the reviewed source pins. Preserve the
frozen oracle, installed O016@13/CA-O-091 binding, candidate hashes and
current Project identity. Validate candidate graph/source consistency,
connected exceptions and registry drift; report conflicts instead of
repointing the live projection. No actual Project binding write, production
MCP traffic, runtime admission, release, deployment, replay or full-suite
run.

## Definition of Done

Produce a detached candidate plus a bounded validation report showing whether
the reviewed source package can replace the old frontier, including the A1142
/ W09 registry issue. Publication remains a separate reviewed gate and the
visible Project binding stays unchanged.

### Deferred leaf checkpoint — 22 October 2026

Keep this detached-candidate and registry-drift leaf Backlog until CA-P-2612's source package is reviewed. Preserve A1142/W09 as candidate validation concerns and do not repoint the actual Project binding.

### Review-scope decision checkpoint — 23 October 2026

Keep this detached-candidate and registry-drift leaf Backlog. The source package is accepted, but execution awaits the Operator's choice between reviewing all 15 non-target route pins plus both query admissions and retaining the focused hold. Preserve the existing mechanical report, A1142/W09 historical distinction and visible Project binding; do not emit or admit a candidate.
