---
atom_id: CA-D-581
content_role: Delivery
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Analysis/Type: FPF Analysis Report'
  depends_on:
  - Subject/Engineering/Carrier/File Carrier.Filename
  - Subject/Engineering/Carrier
version: 6
updated_at: 2026-10-24 01:37:42 +0400
relations:
  delivery_for:
  - CA-R-1888
  relates_to:
  - CA-D-283
  - CA-D-284
  - CA-D-389
  - CA-D-466
tier: 3
type: Eng Decision
---
# Summary

Serialize FPF Analysis Report Type Token

## Scope

the filename Type component of a project-owned FPF Analysis Report Markdown Carrier.

## Claim

a project-owned Analysis Atom with `type: FPF Analysis Report` **must** serialize its Type filename component as `FPF_ANALYSIS_REPORT` within the filename grammar governed by CA-D-283 and CA-D-284.

## Details

This mapping adds the representation of the Type admitted by CA-R-1888. It does not rename another Type, change its filename token or replace the common Analysis body layout. Carrier placement follows the applicable Delivery mapping under CA-D-466 and the canonical Analysis content-role directory under CA-D-324.
