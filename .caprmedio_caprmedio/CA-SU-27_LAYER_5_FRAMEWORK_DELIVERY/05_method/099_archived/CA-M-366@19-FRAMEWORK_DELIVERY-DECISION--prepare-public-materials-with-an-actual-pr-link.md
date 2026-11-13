---
atom_id: CA-M-366
ref_id: CA-M-366@19
container:
  scope_unit: CA-SU-27
role: Method
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Documentation
  - Subject/CAPRMEDIO/Carrier/Pull Request
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History
tier: 4
relations:
  method_for:
  - CA-R-1923
status: archived
version: 19
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-M-366@19-FRAMEWORK_DELIVERY-DECISION--prepare-public-materials-with-an-actual-pr-link.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/05_method/099_archived
current_scope_unit: FRAMEWORK_DELIVERY
claim_target_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---
## Summary

Prepare public materials with an actual PR link

## Claim scope

the selected public documentation closure.

## Claim

### Prose Claim

the public-release Tool **must** prepare README, one full PR body, and short Version History bullets from the selected Version. Its one public-writing prompt produces the full PR body with distinct **What's new** and **What's fixed** sections. It discovers an existing matching PR before push and defers a new Version History hyperlink until the remote returns its actual PR URL.

## Details

Version History remains a concise summary plus actual URL. The Tool completes the one fresh public suite after its initial material closure is frozen and before its first publication. If no matching PR exists, it adds that URL through one mechanical metadata-only follow-up commit and push after creation. That follow-up reopens the actual passed initial public-suite and current source/material evidence; it does not rerun the suite, request a separate review or prompt, or change any non-metadata Version/source/material binding.
