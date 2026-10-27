---
atom_id: CA-P-1636@6
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Archived
subjects:
  governs: Bind minimal status integration touchpoints
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Content Role
  - Subject/Domain/Node/Continuant/Atom.Status
  - Subject/Engineering/Carrier
  - Subject/Engineering/Tool
  - Subject/Engineering/Evaluation
  - Subject/Domain/Node/Continuant/History/Journal
version: 6
updated_at: 2026-10-24 11:01:18 +0400
relations:
  is_decomposition_of:
  - CA-P-1615
  blocks:
  - CA-P-1637
tier: 3
---
# Summary

Bind minimal status integration touchpoints

## Objective

Within <=15 minutes, bind minimal status integration touchpoints.

## Details

Read-only existing dirty lifecycle_intents.py/atom_operations.py, selected Action/Tool/MCP integration and shared Run support. Identify exact minimum touchpoints for source-derived model and D-defined destination integration, preserving existing edits; no code or broad audit.

Inputs: accepted CA-P-1633 source packet and current saved lifecycle inputs; current default role domains, R1825@3/E545@2 and D565@1. Host/image gates C449 and relocation gate C447 remain unchanged. The existing development worker can run focused development tests, not immutable-image proof.

## Definition of Done

Saved bounded integration map covers model derivation, status destinations/archive suffix, Draft, no-op, history/references and shared recording, without a runtime claim.

## Result

Read-only /root/integrate_selected_native_providers preflight identified exact integration touchpoints: lifecycle_intents.py model/no-op/native refusal; atom_operations.py non-Active/Draft locators and D-defined destinations; selected_execution.py freeze/dispatch admission; MCP shared preview preflight and structured diagnostics. Plan Backlog uses D461 local container/001_backlog; new Archived uses D565/@version, preserving legacy archive history. W01–04 source pins remain old and must refresh separately. An identity-less Draft requires a real locator and an explicit accepted identity mapping for promotion; never fabricate ID. Parent P1615 remains incomplete until native effects/recording integration.
