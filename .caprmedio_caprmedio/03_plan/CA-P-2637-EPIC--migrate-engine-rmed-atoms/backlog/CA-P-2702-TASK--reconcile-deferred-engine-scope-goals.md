---
atom_id: CA-P-2702
content_role: Plan
type: Plan
label: Task
current_scope_unit: caprmedio
claim_target_scope_unit: FRAMEWORK_ENGINE
status: Backlog
author: Anatoly Maslennikov
tier: 4
version: 1
updated_at: 2026-10-29 22:52:28 +0400
subjects:
  governs: Entity/Aspect/Engineering/Architecture/Component Structure
relations:
  IS_CONTAINED_BY:
  - CA-P-2637
---
## Summary

Reconcile deferred Engine Scope Goals

## Objective

Resolve four legacy Engine Goals against the Engine Subject and Scope Unit revision, preserving their useful meaning before any change.

## Details

P2701 deliberately leaves CA-R-1186, CA-R-1601, CA-R-1602 and CA-R-1606 unchanged. R1186 names old TOOLS groups CONNECTORS/CAPRMEDIO_TOOLS. The other three refer to ACTION_PROMPTS, OPERATOR_PROMPTS and AGENT_HOST_PLUGINS, which are not registered Scope Units. Decide whether these are still-needed boundaries, ordinary engineering requirements/decisions, renamed existing groups or obsolete content; do not invent units or targets. Current Claims and identities remain authoritative until that review. This is part of the existing Engine methodology migration, not implementation. GIT/FPF Goals R1469/R1474/R1482 remain separately deferred by the Operator and are not reactivated here.
