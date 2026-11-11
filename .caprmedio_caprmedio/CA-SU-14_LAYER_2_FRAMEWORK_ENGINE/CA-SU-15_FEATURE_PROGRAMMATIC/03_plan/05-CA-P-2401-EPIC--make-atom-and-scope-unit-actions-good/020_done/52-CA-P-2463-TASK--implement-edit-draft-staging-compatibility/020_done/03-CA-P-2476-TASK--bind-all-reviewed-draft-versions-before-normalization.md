---
atom_id: CA-P-2476
ref_id: CA-P-2476
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
    name: 3-CA-P-2476-TASK--bind-all-reviewed-draft-versions-before-normalization.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/5-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done/52-CA-P-2463-TASK--implement-edit-draft-staging-compatibility/done
work_sequence_number: 3
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Bind all reviewed Draft Versions before normalization

## Objective

Require carried YAML Version to equal the materialized canonical candidate/explicit Version binding for legacy and ID-free reviewed Subject Drafts, before normalization can erase a mismatch.

## Details

At most 15 minutes own work; split before extending. Independent P2466 review confirmed R866 requires Version-drift refusal for every Draft-backed promotion input. P2473 qualified-marker checks remain correct; extend the shared candidate boundary rather than duplicate normalization. Add legacy and ID-free repinned Version-drift regressions while retaining positive compatibility/no-op coverage.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.

### Verified execution checkpoint

All reviewed formats bind strict positive carried Version to the materialized candidate before normalization. Repinned legacy and ID-free drift regressions and positive/no-op cases passed: focused 16, contract 5, workflow 10. Independent review closed the Version-drift findings with no actionable defect.
