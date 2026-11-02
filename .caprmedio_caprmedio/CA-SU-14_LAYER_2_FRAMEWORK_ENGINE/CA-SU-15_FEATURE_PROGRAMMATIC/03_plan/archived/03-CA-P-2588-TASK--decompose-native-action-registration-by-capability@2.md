---
atom_id: CA-P-2588
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
version: 2
updated_at: "2026-10-22T10:35:18Z"
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2585]
  depends_on: [CA-P-2578]
  relates_to: [CA-P-2577, CA-E-539]
---
# Summary

Decompose native Action registration by capability

## Objective

Replace the oversized native handler body with cohesive capability-owned adapters and a small composition boundary. Preserve every existing native Action and failure/result contract, including dirty earlier error-boundary work.

## Details

The Operator explicitly refused a source-size exception and selected refactoring legacy files first. Every leaf is at most 15 minutes own work; split before expanding. New or materially changed Python files must meet the applicable <=200 physical-line target and small cohesive unit boundaries; no mixin/namespace class or imported-method facade substitutes for responsibility decomposition. Preserve the pinned C901/format/lint and applicable typing baseline. Use the locked Project virtual environment, disable bytecode writes and keep disposable test state below configured Project Temporary State. Do not revert other workers' changes. One Task per file, exact predecessor history; review/update dependants after each completed Task.

Dependency review: canonical capability extraction depends on reviewed source/test preparation CA-P-2578, not completion of unrelated freeze/dispatch extraction. Creation, replacement, assessed lifecycle update and current-state status leaves are extracted in exclusive worker scopes and reviewed before integration. Corrected mixed-effect selection and exact no-op/terminal mappings are guarded by focused regressions. Keep only canonical owner behavior; remove temporary class-wrapper normalization. Original executor assembly/caller integration remains under one writer.

### Definition of Done

Retain actual before/after focused tests, changed paths, source/unit/complexity measurements and explicit unresolved limits. Preserve frozen test oracle bytes and current public behavior before new shared-context feature work. No production MCP, release, deployment, full suite, source-policy edits or Git publication.
