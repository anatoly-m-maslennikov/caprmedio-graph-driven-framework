---
atom_id: CA-D-581
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role := "Analysis & Advisory")/(.Form := FPF Analysis Report)
  passive:
  - CAPRMEDIO <+ MODEL <+ Carrier/File.Filename
  - CAPRMEDIO <+ MODEL <+ Carrier
version: 17
updated_at: 2026-11-02 19:33:47 +0400
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

the filename Form component of a project-owned FPF Analysis Report Markdown Carrier.

## Claim

a project-owned Analysis & Advisory Atom with `form: FPF Analysis Report` **must** serialize its Form filename component as `FPF_ANALYSIS_REPORT` within the filename grammar governed by CA-D-283 and CA-D-284.

## Details

This mapping adds the representation of the Form admitted by CA-R-1888. It does not rename another Form, change its filename token or replace the common Analysis & Advisory body layout. Carrier placement follows the applicable Delivery mapping under CA-D-466 and the canonical Analysis & Advisory Role directory under CA-D-324.

