---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Evaluation/Type'
  depends_on: []
version: 34
updated_at: 2026-10-25 17:32:27 +0400
relations:
  depends_on:
  - CA-R-1506
atom_id: CA-R-1662
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
type: Rule
tier: 3
---
# Summary

Register Type Values for Evaluation Atoms

## Scope

internal values of `Atom/Content Role: Evaluation/Type`.

## Claim

Policy, Eval Case, QA Case, **and** Evaluation Control **must** be registered as internal values of `Atom/Content Role: Evaluation/Type`.

## Details

Eval Case is defined by CA-R-2116. QA Case remains registered for existing Atoms pending individually evidenced migration; this registration does not require bulk reclassification. Evaluation Control remains a distinct specific Type.
