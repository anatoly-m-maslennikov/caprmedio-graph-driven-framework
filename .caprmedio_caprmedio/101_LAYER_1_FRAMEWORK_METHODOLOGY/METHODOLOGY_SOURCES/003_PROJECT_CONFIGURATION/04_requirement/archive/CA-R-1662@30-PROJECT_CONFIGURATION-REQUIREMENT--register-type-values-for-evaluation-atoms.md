---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation/Type'
  depends_on: []
version: 30
updated_at: 2026-10-22 16:34:15 +0000
relations:
  child_of:
  - CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type
  depends_on:
  - CA-R-1506
atom_id: CA-R-1662@30
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
status: Archived
author: Anatoly Maslennikov
global_tier: 11
type: Rule
---
# Summary

Register Type Values for Evaluation Atoms

## Scope

internal values of `Atom/Content Role: Evaluation/Type`.

## Claim

Policy, Eval Case, QA Case, **and** Evaluation Control **must** be registered as internal values of `Atom/Content Role: Evaluation/Type`.

## Details

Eval Case is defined by CA-R-2116. QA Case remains registered for existing Atoms pending individually evidenced migration; this registration does not require bulk reclassification. Evaluation Control remains a distinct specific Type.
