---
atom_id: CA-P-2342
ref_id: CA-P-2342
container:
  atom: CA-P-2307
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Continuant/Tool
  dependencies:
  - Subject/Graph Node/Domain/Continuant/Atom
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
  - Subject/Graph Relation
tier: 3
relations:
  is_decomposition_of:
  - CA-P-2307
status: Done
version: 6
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 11-CA-P-2342-TASK--admit-status-correct-plan-blocking-targets.md
    path: .caprmedio_caprmedio/03_plan/30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/21-CA-P-2256-TASK--implement-toml-item-and-full-set-edits/done/2-CA-P-2307-TASK--select-tomlkit-for-preserving-configuration-text/done
work_sequence_number: 11
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
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

### Accepted outcome — 2026-10-13

The final connected implementation is independently accepted in contained-status-and-plan-admission-acceptance.md under the Stage-2 Tools-first derived receipts. Full validator: 433/433. Independent real publication/placement: 33/33. Reference lifetime/closure: 28/28, including actual post-lookup mutation and namespace refusals. Real P2264 v6, P2256 v6 and P2272 v7 passed finite PRMEDO admission with exact bytes unchanged. This Task's bounded implementation/check scope is complete; selected lifecycle rebinding, cascade execution, Draft identity, runtime activation and live migration remain separate.
