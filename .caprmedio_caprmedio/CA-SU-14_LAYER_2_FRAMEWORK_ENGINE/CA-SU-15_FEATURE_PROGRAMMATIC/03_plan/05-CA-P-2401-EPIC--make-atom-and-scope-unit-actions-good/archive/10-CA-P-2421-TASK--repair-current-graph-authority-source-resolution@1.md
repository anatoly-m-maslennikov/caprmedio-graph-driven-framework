---
atom_id: CA-P-2421
content_role: Plan
type: Plan
label: Task
work_sequence_number: 10
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2401]
version: 1
updated_at: "2026-10-20 15:36:17 +0400"
---
# Summary

Repair current graph-authority source resolution

## Objective

Advance the bounded Epic repair or evidence-reconciliation responsibility for CA-C-525 without broadening deployment or historical effects.

## Details

Own graph_authority_refresh.py, graph_authority.json only if a supported binding update is required, and dedicated graph authority tests. Reuse current declared authoritative source resolution; preserve finite approved IDs, unique active source/provenance checks, and fail-closed behavior for missing, ambiguous, projected or unsafe carriers. Do not move governed sources or silently expand authority. Golden fixture must model D305 at its declared owner without live source coupling.

Use the current mrt_programmatic_methods_compact.projection.md and applicable current source RMEDO; the projection is not authority. Use Luna workers, preserve other edits, keep one owner per file and leave Git/index/commit integration to root. Before changing behavior, inspect callers and current source authority. At confidence below95percent, stop the affected behavior and ask the Operator rather than inventing policy.

Estimated own work: at most15minutes. Split further before exceeding that bound. After each completion, review and update dependent Tasks before execution. Prefer frozen public-interface/functional evidence over implementation-shaped tests. Run Project Python only in the selected uv-managed environment. No production MCP test, restart, reload, deployment, or uncertain effect replay. User-authorized manual fallback applies if MCP cannot do the job; retain exact predecessors and actual Journal provenance.

### Definition of Done

A concrete bounded deliverable has inspected sources/callers, reproducible checks and truthful outcomes/limitations. Code repairs retain all applicable safeguards; evidence-only work makes no effect or deployment claim. Any blocker or unresolved choice is recorded as a Concern.
