---
atom_id: CA-R-2230@2
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Aspect/Engineering/Architecture/Communication/API/Result Contract
  depends_on:
  - Entity/Aspect/Engineering/Architecture/Communication/API
  - Entity/Object/Occurrent/Execution.Result
version: 2
updated_at: 2026-10-29 10:28:51 +0400
relations: {}
tier: 1
---
## Summary

Define API Result Contract

## Claim

An API Result Contract defines the expected format and meaning of results for an API operation. It describes what callers can expect under its applicable conditions, rather than the data produced by a particular execution.

## Semantics

The operation-specific contract may describe returned values, errors or effect summaries. This Definition prescribes no common envelope or mandatory field set across all APIs. API Self Documentation can expose the contract, while Execution.Result supplies an actual result to assess against it.

## Details

CA-A-1276 records the Operator decision. The defining identity and simple schemas are adopted; this does not implement a result envelope or Journal writer.
