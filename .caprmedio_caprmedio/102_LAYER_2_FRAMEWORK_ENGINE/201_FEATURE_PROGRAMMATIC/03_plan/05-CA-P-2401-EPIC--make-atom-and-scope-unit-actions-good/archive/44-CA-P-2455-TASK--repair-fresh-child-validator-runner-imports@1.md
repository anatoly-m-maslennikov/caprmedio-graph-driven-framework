---
atom_id: CA-P-2455
content_role: Plan
type: Plan
label: Task
work_sequence_number: 44
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
updated_at: "2026-10-20T15:10:43.000Z"
---
# Summary

Repair fresh-child validator runner imports

## Objective

Repair the bounded fresh-child runner/import setup exposed by the nine failing `VALIDATE_ATOMS` modules in the second local-release attempt, without changing validator or production-guard semantics.

## Details

Use the retained failure evidence from `.caprmedio_tmp/simple_local_release/local-20261020-current-target-parser-repair-1438-tests-a71g3vcj.log` and the matching `runtime/reports/runid.md`. Isolate the runner/import repair from the shared frozen-fixture repair in CA-P-2456. Run only the focused affected modules and record actual results; preserve fresh-child isolation, current source provenance and intentional refusals. No production request, image replacement, Git mutation or full-release retry is part of this Task.

At most15minutes ownwork, split before extending. Preserve unrelated concurrent changes and exact predecessor evidence.

### Definition of Done

The nine affected `VALIDATE_ATOMS` fresh-child import paths run with the intended current runner setup and focused checks pass, with the exact source/test boundary recorded. This narrow Task claims neither a production guard fix nor full-suite, deployment or release acceptance.
