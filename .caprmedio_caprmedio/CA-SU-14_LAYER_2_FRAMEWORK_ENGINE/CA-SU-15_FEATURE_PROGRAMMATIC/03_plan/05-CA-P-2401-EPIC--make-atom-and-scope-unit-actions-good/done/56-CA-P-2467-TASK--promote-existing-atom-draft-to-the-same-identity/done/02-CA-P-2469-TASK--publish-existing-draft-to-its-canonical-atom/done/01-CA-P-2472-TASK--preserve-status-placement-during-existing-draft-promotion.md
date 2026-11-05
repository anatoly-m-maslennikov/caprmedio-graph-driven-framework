---
atom_id: CA-P-2472
ref_id: CA-P-2472
role: Plan
form: Plan
label: Task
work_sequence_number: 1
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Done
topics:
  main_subject: Subject/Graph Node/Domain/Continuant/Atom
relations:
  is_decomposition_of:
  - CA-P-2469
version: 5
updated_at: 2026-10-25 17:32:27 +0400
tier: 3
container:
  atom: CA-P-2469
carrier_destination:
  file:
    name: 1-CA-P-2472-TASK--preserve-status-placement-during-existing-draft-promotion.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/5-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done/56-CA-P-2467-TASK--promote-existing-atom-draft-to-the-same-identity/done/2-CA-P-2469-TASK--publish-existing-draft-to-its-canonical-atom/done
---
# Summary

Preserve Status placement during existing Draft promotion

## Objective

Complete destination-aware canonical publication and verified rollback when a non-Active Current Plan is promoted to Active using a reviewed Draft.

## Details

At most 15 minutes own work; split before extending. P2469 partial checkpoint passed Active same-ID V4 publication/exact V3 archive, no-op preservation and injected Draft-cleanup recovery. Reuse the status/bundle owner, preserve children and source pins, do not copy Draft companion trees or invent relation policy.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.

### Verified execution checkpoint

Done-to-Active canonical placement with existing child preservation and exact predecessor archive passed, as did moved-publication cleanup-failure and native postwrite exact rollback checks. Independent review confirmed moved-path recovery has the expected published-bundle guard. Separate same-path concurrent-edit protection is retained under P2475; parent P2469 remains Active.
