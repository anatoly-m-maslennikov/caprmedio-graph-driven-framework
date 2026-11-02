---
atom_id: "CA-D-581"
content_role: "Delivery"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Atom/Content Role: Analysis/Type: FPF Analysis Report"
  depends_on:
    - "Project-Owned Markdown Atom Carrier/Filename"
    - "Entity/Carrier"
version: 2
updated_at: "2026-10-19 15:56:25 +0400"
relations:
  delivery_for: ["CA-R-1888"]
  relates_to: ["CA-D-283", "CA-D-284", "CA-D-389", "CA-D-466"]
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-581-PROJECT_CONFIGURATION--serialize-fpf-analysis-report-type-token.md
  source_atom_id: CA-D-581
  source_atom_revision: 2
  source_sha256: 9997cee34b916bd6ebce5ccf56ed7eaacee9df6d1e09821f575a7e08a9e5da6c
  original_relations_sha256: 2b6d8c0ebc6425f06a8771e0fec04a1d53006595d94f07805054d9e0fb3e213d
---
# Summary

Serialize FPF Analysis Report Type Token

## Scope

the filename Type component of a project-owned FPF Analysis Report Markdown Carrier.

## Claim

a project-owned Analysis Atom with `type: FPF Analysis Report` **must** serialize its Type filename component as `FPF_ANALYSIS_REPORT` within the filename grammar governed by CA-D-283 and CA-D-284.

## Details

This mapping adds the representation of the Type admitted by CA-R-1888. It does not rename another Type, change its filename token or replace the common Analysis body layout. Carrier placement follows the applicable Delivery mapping under CA-D-466 and the canonical Analysis content-role directory under CA-D-324.
