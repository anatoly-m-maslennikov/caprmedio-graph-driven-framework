---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Substance
  - Implementation
version: 9
updated_at: 2026-10-23 03:20:06 +0400
relations: {}
atom_id: CA-R-1503@9
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
status: Archived
author: Anatoly Maslennikov
global_tier: 9
---
# Summary

Keep Evaluation Atoms mechanism-neutral

## Scope

Evaluation Atom check definitions and their implementation mechanisms.

## Claim

an Evaluation Atom **must** define the checked Claim, applicable conditions, acceptance criteria, **and** disposition rule **without** prescribing the mechanism that realizes its check.

## Details

automated tests, model-judged evaluations, statistical assessments, rubrics, manual reviews, **and** other implementation mechanisms **may** realize that check. choosing a mechanism does **not** change the governing Evaluation Atom's Claim.
