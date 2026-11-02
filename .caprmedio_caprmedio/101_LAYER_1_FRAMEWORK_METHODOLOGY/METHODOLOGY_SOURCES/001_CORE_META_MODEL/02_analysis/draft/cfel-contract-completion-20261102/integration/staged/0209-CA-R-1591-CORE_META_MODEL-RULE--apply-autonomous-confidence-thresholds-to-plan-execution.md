---
subjects:
  active: Atom/(.Role:=Plan).AI Agent Confidence Threshold
  passive:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan/Type: Plan'
  - Entity/Aspect/Engineering/Execution Control/Decision Confidence
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Actor/AI Agent
version: 26
updated_at: 2026-11-02 07:49:21 +0400
relations: {}
atom_id: CA-R-1591
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary

Apply autonomous confidence thresholds to Plan execution

## Claim scope

autonomous continuation of Plan work.

## Claim

autonomous continuation of Plan work **must** satisfy its effective Autonomous Confidence Threshold:

- resolve the value under CA-M-271-CORE_META_MODEL-IMPLEMENTATION_METHOD--resolve-confidence-thresholds-by-source-precedence.
- **if** confidence **in** correct execution is below it, request Operator disposition **before** continuing.
- **otherwise**, continue **only** within existing authority; meeting the threshold does **not** grant additional authority.
