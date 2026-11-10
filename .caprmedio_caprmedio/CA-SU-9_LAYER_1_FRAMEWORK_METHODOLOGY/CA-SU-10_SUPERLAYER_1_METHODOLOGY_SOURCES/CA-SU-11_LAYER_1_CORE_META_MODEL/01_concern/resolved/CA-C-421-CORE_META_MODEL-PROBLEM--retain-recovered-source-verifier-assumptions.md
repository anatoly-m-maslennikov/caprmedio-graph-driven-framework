---
atom_id: CA-C-421
content_role: Concern
type: Problem
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: resolved
version: 4
updated_at: 2026-10-23 03:14:50 +0400
subjects:
  governs: Source verification evidence
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations'
  - Implementation
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - Subject/Engineering/Carrier
relations:
  concern_about:
  - CA-P-1444
  - CA-P-1445
ref_id: CA-C-421
carrier_destination:
  file:
    name: CA-C-421-CORE_META_MODEL-PROBLEM--retain-recovered-source-verifier-assumptions.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/01_concern/resolved
---
# Summary

Retain recovered source-verifier assumptions

## Concern

Two disposable source completion checks used overly specific incorrect assertions, although the saved carriers did not have those claimed defects.

## Evidences

P1445 assumed fourteen transition rows instead of deriving thirteen from the preserved seven explicit rows plus six wildcard expansions. P1444 expected a literal disclaimer rather than its saved equivalent wording. Both stopped honestly, corrected only the check assumption, and reran the bounded saved gate; source/output meaning was not altered to satisfy a verifier.

## Blast radius

These acquisition/verification incidents remain retained in the owned Plan evidence; they are not runtime failures or evidence of source acceptance. Use actual original structure and semantic disclaimers in the corrected gate. No broad verifier rewrite campaign is required.
