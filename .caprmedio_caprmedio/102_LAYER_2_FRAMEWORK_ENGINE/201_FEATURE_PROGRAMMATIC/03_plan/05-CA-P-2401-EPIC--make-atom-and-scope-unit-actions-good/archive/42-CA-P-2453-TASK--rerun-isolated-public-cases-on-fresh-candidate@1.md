---
atom_id: CA-P-2453
content_role: Plan
type: Plan
label: Task
work_sequence_number: 42
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: [CA-P-2452]
relations:
  is_decomposition_of: [CA-P-2401]
version: 1
updated_at: "2026-10-20T14:30:31.000Z"
---
# Summary

Rerun the isolated public cases on the fresh candidate

## Objective

Run the three selected isolated public cases against the exact new candidate from CA-P-2452 and record production equality without touching production.

## Details

Proceed only after CA-P-2452 supplies the fresh immutable candidate and exact source/image receipt. Bind the isolated harness to that candidate, execute the three public cases, and capture actual pass/failure/skip results, canonical output checks, and `production_equal` evidence. Stop on an isolation or provenance failure; do not fall back to the prior candidate, replay historical requests, or replace production.

At most15minutes ownwork, split before extending. Preserve the exact candidate, fixture, project, port, state namespace, and receipt. No production MCP/Docker replacement, Git mutation, public release, or full-local-release claim is made by this Task.

### Definition of Done

A fresh receipt identifies the exact candidate and records all three isolated public cases, their actual outcomes, canonical-output checks, and production equality. Only a passing receipt can unlock CA-P-2454; this Task does not claim deployment or full-release acceptance by plan alone.
