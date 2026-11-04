---
atom_id: CA-D-581
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := "Analysis & Advisory")/(.Header.Form := FPF Analysis Report)
  passive:
  - CAPRMEDIO_MODEL <+ Carrier/File
  - CAPRMEDIO_MODEL <+ Carrier
version: 18
updated_at: 2026-11-03 23:25:51 +0400
relations:
  delivery_for:
  - CA-R-1888
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery/CA-D-581-PROJECT_CONFIGURATION-ENG_DECISION--serialize-fpf-analysis-report-type-token.md
  source_atom_id: CA-D-581
  source_atom_revision: 18
  source_sha256: 7a8599c84b594117c9c24c0d0a44348f9b25b252d484ee9a5dd9827022816de9
  original_relations_sha256: e18bb992cc1d06071fe099a8f9861d6a0c2003200626996e045dafc3e3b9ac71
---
## Summary

Serialize FPF Analysis Report Type Token

## Claim

### Prose Claim


the filename Form component of a project-owned FPF Analysis Report Markdown Carrier.


a project-owned Analysis & Advisory Atom with `form: FPF Analysis Report` **must** serialize its Form filename component as `FPF_ANALYSIS_REPORT` within the filename grammar governed by CA-D-283 and CA-D-284.

## Details

This mapping adds the representation of the Form admitted by CA-R-1888. It does not rename another Form, change its filename token or replace the common Analysis & Advisory body layout. Carrier placement follows the applicable Delivery mapping under CA-D-466 and the canonical Analysis & Advisory Role directory under CA-D-324.

