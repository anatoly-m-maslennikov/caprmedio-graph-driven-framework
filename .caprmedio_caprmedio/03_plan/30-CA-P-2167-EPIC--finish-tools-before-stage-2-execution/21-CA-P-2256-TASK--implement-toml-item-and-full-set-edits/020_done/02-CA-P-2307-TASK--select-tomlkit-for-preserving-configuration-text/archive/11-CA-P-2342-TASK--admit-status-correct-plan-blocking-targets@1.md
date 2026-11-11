---
atom_id: CA-P-2342
content_role: Plan
type: Plan
label: Task
work_sequence_number: 11
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Plan, Relation]
version: 1
updated_at: "2026-10-13 20:54:29 +0400"
relations:
  is_decomposition_of: [CA-P-2307]
---
# Summary

Admit Status-correct Plan blocking targets

## Objective

Proposed-carrier reference admission applies the admitted Plan Status model to typed Plan blocking endpoints instead of requiring every endpoint to be Active.

## Details

Use current D471/R1580/R1539 and existing Plan graph checks. Resolve authenticated explicitly referenced Plan versions across admitted statuses/history where unambiguous; preserve all applicable source/currentness/identity/version/placement constraints. Keep Active-only authority requirements for ordinary RMED references and mixed-role/mixed-relation uses; do not globally allow inactive sources. No Plan edge/status changes, new relation kind or source-rule bypass. Prove the real parent Plan blockers now admit and wrong role, ambiguity, invalid history/placement, mixed relation, stale frontier and missing target still refuse. Reuse existing lookup/history logic where suitable; report ambiguity instead of guessing.

Estimated own work: up to 15 minutes. Split before exceeding this bound. Root owns Plans and Git; implementation and independent tests use disjoint files. Current source authority remains unchanged; C/A legacy migration stays deferred.

### Definition of Done

Exact current source/code/test evidence, actual positive/refusal checks and independent review establish the outcome. No guessed policy, weakened unrelated guard or unsupported runtime claim. Preparation alone is not completion.
