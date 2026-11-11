---
atom_id: CA-D-581
ref_id: CA-D-581
container:
  scope_unit: CA-SU-13
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := "Analysis & Advisory")/(.Header.Context.Form := FPF Analysis Report)
  dependencies:
  - CAPRMEDIO_MODEL <+ Carrier/File
  - CAPRMEDIO_MODEL <+ Carrier
tier: 3
relations:
  delivery_for:
  - CA-R-1888
status: Active
version: 18
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-D-581-PROJECT_CONFIGURATION-DECISION--serialize-fpf-analysis-report-type-token.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
---
## Summary

Serialize FPF Analysis Report Type Token

## Claim

### Prose Claim


the filename Form component of a project-owned FPF Analysis Report Markdown Carrier.


a project-owned Analysis & Advisory Atom with `form: FPF Analysis Report` **must** serialize its Form filename component as `FPF_ANALYSIS_REPORT` within the filename grammar governed by CA-D-283 and CA-D-284.

## Details

This mapping adds the representation of the Form admitted by CA-R-1888. It does not rename another Form, change its filename token or replace the common Analysis & Advisory body layout. Carrier placement follows the applicable Delivery mapping under CA-D-466 and the canonical Analysis & Advisory Role directory under CA-D-324.

