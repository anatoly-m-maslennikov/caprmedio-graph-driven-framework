---
atom_id: CA-P-2455
ref_id: CA-P-2455
container:
  atom: CA-P-2401
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Domain/Continuant/Atom
tier: 3
relations:
  is_decomposition_of:
  - CA-P-2401
status: Done
version: 5
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 44-CA-P-2455-TASK--repair-fresh-child-validator-runner-imports.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/5-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done
work_sequence_number: 44
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
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

### Completion checkpoint

The scoped receipt records 13/13 runner checks and 133/133 former fresh-child modules passing with zero skips; independent review is `APPROVE`. This is test-environment evidence only and does not claim installed deployment, production guard repair, full release or Epic completion.
