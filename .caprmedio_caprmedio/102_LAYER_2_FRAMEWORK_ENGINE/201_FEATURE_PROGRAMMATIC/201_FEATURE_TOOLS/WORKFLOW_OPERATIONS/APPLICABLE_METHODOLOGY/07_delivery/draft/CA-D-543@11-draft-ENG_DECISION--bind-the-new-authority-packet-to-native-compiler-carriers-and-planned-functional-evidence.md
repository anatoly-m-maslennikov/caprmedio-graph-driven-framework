---
atom_id: CA-D-543@11-draft
content_role: Delivery
type: Eng Decision
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Draft
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-24 23:55:59 +0400
subjects:
  governs: Subject/Engineering/Carrier
  depends_on:
  - Subject/Engineering/Tool
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/Projection
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Subject/Domain/Node/Occurrent/Execution/Step Run
relations:
  delivery_for:
  - CA-R-1839
  - CA-R-1840
  - CA-R-2118
  - CA-R-1842
  - CA-E-559
  - CA-E-560
  - CA-E-561
  - CA-E-562
tier: 6
---
# Summary

Bind the new authority packet to native compiler carriers and planned functional evidence.

## Scope

The authority-to-native-delivery and planned-evidence boundary for this compiler slice.

## Claim

The Applicable Methodology compiler **must** keep this RMED authority under `WORKFLOW_OPERATIONS/APPLICABLE_METHODOLOGY`, deliver only at its declared native compiler location, and retain functional evidence beside the implementation without duplicating shared Run support.

## Details

Authority carriers are this `04_requirement`, `06_evaluation`, and `07_delivery` packet together with existing construction method CA-M-226. The canonical implementation carrier is `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py`; focused functional tests are its sibling `tests/test_compile_applicable_methodology.py` and any bounded companion test module. Source and output roots are declared by current Project Structure, not by compatibility constants or a caller override.

The delivered tests must implement CA-E-559 through CA-E-562 through the real CLI and any exposed MCP adapter, including one clean activated-Extension pass and the conflict, stale-approval, incomplete, and recovery paths. The compiler returns shared `run_receipt_refs`; it does not write a parallel Journal schema or redefine Workflow/Action/Step Run identities. This RMED packet authorizes no code before independent RMED review and makes no runtime or Docker-success claim.

### Sources

- CA-R-1839, CA-R-1840, CA-R-2118, CA-R-1842; CA-E-559 through CA-E-562; CA-M-226 v6.
- CA-P-1489 v1; CA-P-1117 v3.
