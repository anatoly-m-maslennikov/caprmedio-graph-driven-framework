---
atom_id: CA-P-2685
ref_id: CA-P-2685
container:
  atom: CA-P-2683
role: Plan
form: Plan
label: Task
topics:
  main_subject: Entity
tier: 4
status: Done
version: 40
updated_at: 2026-10-29 07:48:43 +0400
current_scope_unit: caprmedio
author: Anatoly Maslennikov
carrier_destination:
  file:
    name: 02-CA-P-2685-TASK--complete-syntax-rmed-and-markdown-property-contracts.md
    path: .caprmedio_caprmedio/03_plan/020_done/CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/020_done
---
# Summary

Complete syntax RMED and Markdown property contracts

## Objective

Prepare the reviewed plain syntax and Markdown-layout Drafts for adoption with their corrected Subjects.

## Details

Stage 2 support, after the mechanical Subject pass. Reconcile the existing prepared packet against the latest Current predecessors and their migrated Subjects. Use A1301's reviewed repairs; do not reopen the completed design review or invent a new syntax language.

The root is Entity, with Object, Aspect, Graph Syntax and Carrier branches. Continuant/Occurrent specialize Object; Carrier is separate. Graph Syntax includes Relation and value Format. Retain /, //, ., :, ::, >, existing-kind @ references and ((RELATION_TYPE)). Property counts are {n}, {n+}, {n..m}; omitted counts are undefined, explicit {0} forbids direct values without forbidding declared children. Formats describe values, not YAML list/map containers or ref semantics.

RMED top-level sections are sibling ## Summary, optional ## Claim scope, ## Claim, optional ## Semantics and ## Details. R alone may include ### Formal claim below Claim. One direct prose Claim remains required; the formal child's independent optional count cannot satisfy it. Put operative meaning in Claim. YAML null/empty strings count as values; formats and prose conditions govern admissibility.

Confirm each adoption candidate's governs/dependencies against the new paths. Keep advanced formulas, conditions in [], materialization and function proposals outside the packet. Unrelated Drafts and Current sources are not changed by this preparation check.

## Definition of Done

The selected syntax/layout replacements have correct Subjects and a clear adopt/reuse/hold disposition for P2688. Earlier review evidence is linked; no missing-definition/catalog work is disguised as a completed adoption.

## Progress

Reconciled the reviewed packet against the latest Entity-root decisions and actual post-Subject-migration Current versions. Corrected stale paths, YAML quoting, qualified Operations containment and accidental Summary wording. Forty-eight selected Drafts passed adoption readback; the duplicate Terms Projection Draft remains unpromoted under C608/A1305. The advanced-expression and superseded old-Model Drafts were excluded.
