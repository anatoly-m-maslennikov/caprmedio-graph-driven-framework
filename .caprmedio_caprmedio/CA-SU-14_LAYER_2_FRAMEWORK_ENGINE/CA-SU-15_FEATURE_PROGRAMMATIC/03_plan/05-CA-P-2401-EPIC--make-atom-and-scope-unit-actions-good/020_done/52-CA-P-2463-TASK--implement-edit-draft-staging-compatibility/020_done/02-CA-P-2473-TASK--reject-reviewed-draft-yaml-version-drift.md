---
atom_id: CA-P-2473
ref_id: CA-P-2473
container:
  atom: CA-P-2463
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Domain/Continuant/Atom
tier: 3
relations:
  is_decomposition_of:
  - CA-P-2463
status: Done
version: 5
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 2-CA-P-2473-TASK--reject-reviewed-draft-yaml-version-drift.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/5-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done/52-CA-P-2463-TASK--implement-edit-draft-staging-compatibility/done
work_sequence_number: 2
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Reject reviewed Draft YAML Version drift

## Objective

Close the independent finding that a qualified Draft marker could disagree with carried YAML Version yet be normalized to a valid candidate.

## Details

At most 15 minutes own work; split before extending. Require marker proposed Version to equal carried YAML Version before candidate normalization. Preserve the already reviewed ID-free/empty-number support and exact source/draft bindings. This is a separate bounded follow-up after P2471 ID-free compatibility.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.

### Verified execution checkpoint

Qualified-marker carried-YAML-Version checks now run before normalization. The repinned marker/YAML mismatch regression and focused staging 14/14 passed, with Ruff and diff checks. Independent review accepted this qualified-format fix and separately assigned all-format legacy/ID-free Version binding to P2476. Parent P2463 remains Active.
