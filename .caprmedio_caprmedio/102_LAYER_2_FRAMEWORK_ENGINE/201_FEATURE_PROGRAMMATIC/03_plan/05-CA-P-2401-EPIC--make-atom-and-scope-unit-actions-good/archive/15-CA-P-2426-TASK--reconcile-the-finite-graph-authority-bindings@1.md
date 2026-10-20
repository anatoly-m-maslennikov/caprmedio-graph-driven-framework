---
atom_id: CA-P-2426
content_role: Plan
type: Plan
label: Task
work_sequence_number: 15
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
updated_at: "2026-10-20 15:46:43 +0400"
---
# Summary

Reconcile the finite graph authority bindings

## Objective

Determine whether the remaining approved graph-authority pins can be reconciled to current applicable sources without changing graph behavior or weakening source admission.

## Details

CA-P-2421 repaired the D305 locator, but full finite pin verification reaches another stale binding (CA-D-268). Read only the finite APPROVED_GRAPH_AUTHORITY_IDS and existing graph_authority.json. For each, locate the uniquely declared current authoritative source and the exact historical source matching the old version/hash when retained. Compare Scope/Claim/Details and metadata separately; label unchanged behavior, changed behavior, missing old evidence, ambiguity or unsupported authority. Version/digest drift alone is not permission to refresh a Claim. Source bindings are not governed source Atoms. Do not widen approved IDs or modify sources/pins/code in this investigation.

Use the PROGRAMMATIC M projection and applicable M316 sources. Own only .caprmedio_tmp/mcp-audit-20261020/continuation/graph-binding-review. At most15minutes own work; split before extending it. No MCP/prod56317 calls, workers/scheduler changes, code/Atom/Git mutations, build, replay or cleanup. All source/pin effects remain root-reviewed dependent work.

### Definition of Done

A deterministic per-ID table identifies exact old/current paths, versions, hashes and behavior differences, with a bounded safe-update proposal or specific unsupported/missing evidence. No automatic pin refresh or deployment is claimed.
