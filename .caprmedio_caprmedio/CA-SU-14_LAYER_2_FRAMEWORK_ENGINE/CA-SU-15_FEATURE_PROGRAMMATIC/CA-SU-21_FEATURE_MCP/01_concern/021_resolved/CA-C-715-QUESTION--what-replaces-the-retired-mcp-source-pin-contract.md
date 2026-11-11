---
identity:
  id: CA-C-715
  ref_id: CA-C-715
context:
  container:
    scope_unit: CA-SU-21
  role: Concern
  form: Question
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Execution Control
  tier: 4
state:
  status: Resolved
  version: 2
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-C-715-QUESTION--what-replaces-the-retired-mcp-source-pin-contract.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/01_concern/021_resolved
author: Anatoly Maslennikov
---

## Summary

What replaces the retired MCP source-pin contract?

## Concern

Current R1894 requires exact source-pin refresh and explicitly names D588. D588 has Archived carriers but no Current carrier or established replacement in the checked source set. Which Current delivery contract should R1894 use, or should this old selected-route refresh behavior retire?

## Details

Preserve the current R1894 Claim until this is decided. Its structural Draft does not choose a successor, restore retired tools or implement refresh behavior. This is a source-authority gap, not evidence of a running-service failure.

## Proposed resolution

Retire the obsolete finite selected-source refresh specified by CA-R-1894 and CA-M-350, whose exact CA-D-588 registration is Archived and has no Current replacement or accepted RMEDO callers. This decision does not retire generic source validation or publication. Resolve this Concern only after both Current sources CA-R-1894 and CA-M-350 are archived and both successor Drafts are withdrawn. No runtime behavior is established by this source decision.
