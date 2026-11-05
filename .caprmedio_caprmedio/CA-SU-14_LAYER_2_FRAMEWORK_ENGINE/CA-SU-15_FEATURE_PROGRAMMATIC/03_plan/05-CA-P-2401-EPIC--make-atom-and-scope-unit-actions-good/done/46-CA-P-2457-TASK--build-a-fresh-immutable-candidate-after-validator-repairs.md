---
atom_id: CA-P-2457
ref_id: CA-P-2457
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
version: 8
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 46-CA-P-2457-TASK--build-a-fresh-immutable-candidate-after-validator-repairs.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/5-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done
work_sequence_number: 46
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Build a fresh immutable candidate after validator repairs

## Objective

Build a fresh immutable candidate from the repaired current source after CA-P-2455 and CA-P-2456 pass, with exact provenance for the next isolated gate.

## Details

Do not start until both Active repair Tasks supply their focused receipts. Build from the current source and approved fixtures, record exact source/image fingerprints and admission/production guard evidence, and preserve rollback identity. Do not reuse the failed candidate, replay either failed release attempt, replace production or infer full-suite readiness from a build receipt.

The repair dependencies are now recorded Done. Preserve the exact build/admission receipt and do not infer isolated success, deployment or release acceptance from a build alone.

At most15minutes ownwork, split before extending. Preserve the source/Git/runtime boundary and unrelated concurrent changes. No deployment, public release or Git mutation is authorized by this preparation Task.

### Definition of Done

A fresh immutable candidate is built after both repair receipts pass, with reproducible source/image provenance and protected production state unchanged. This Task does not claim isolated-case, deployment or release acceptance.

### Completion checkpoint

Admission receipt `.caprmedio_tmp/mcp-audit-20261020/isolation/execute/p2410-20261020T151202Z-628773a0/admission-receipt.json` records image `sha256:a26b88751f9e8eb57132f648e114f0af4d0c25ff5acf66a6f891f7d05fb4fab3`, source fingerprint `b95525f5be4b87c9b342f52199cd8f9260ff4206c2f130090cf63f4cc3e38f76`, unchanged prelaunch source/image/compose inputs, and production snapshot equality `true`. Independent fixture review is `APPROVE` with no findings. This closes candidate build provenance only; isolated public-case, deployment and full-release acceptance remain separate gates.
