---
atom_id: CA-D-581@14
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
subjects:
  active: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Analysis/Type: FPF Analysis Report'
  passive:
  - Carrier/File.Filename
  - Carrier
version: 14
updated_at: 2026-11-02 00:18:22 +0400
relations:
  delivery_for:
  - CA-R-1888
tier: 3
role: Delivery
form: Decision
---
## Summary

Serialize FPF Analysis Report Type Token

## Claim scope

the filename Type component of a project-owned FPF Analysis Report Markdown Carrier.

## Claim

a project-owned Analysis Atom with `type: FPF Analysis Report` **must** serialize its Type filename component as `FPF_ANALYSIS_REPORT` within the filename grammar governed by CA-D-283 and CA-D-284.

## Details

This mapping adds the representation of the Type admitted by CA-R-1888. It does not rename another Type, change its filename token or replace the common Analysis body layout. Carrier placement follows the applicable Delivery mapping under CA-D-466 and the canonical Analysis content-role directory under CA-D-324.
