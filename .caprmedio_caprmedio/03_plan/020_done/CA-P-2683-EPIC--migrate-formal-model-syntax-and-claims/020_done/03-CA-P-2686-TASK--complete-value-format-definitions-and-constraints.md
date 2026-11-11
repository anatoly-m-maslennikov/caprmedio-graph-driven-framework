---
atom_id: CA-P-2686
ref_id: CA-P-2686
container:
  atom: CA-P-2683
role: Plan
form: Plan
label: Task
topics:
  main_subject: Entity
tier: 4
status: Done
version: 5
updated_at: 2026-10-29 11:24:13 +0400
current_scope_unit: caprmedio
author: Anatoly Maslennikov
carrier_destination:
  file:
    name: 03-CA-P-2686-TASK--complete-value-format-definitions-and-constraints.md
    path: .caprmedio_caprmedio/03_plan/020_done/CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/020_done
---
## Summary

Complete value Format definitions and constraints

## Objective

Fill missing primitive value Format Definitions and their relevant property/cardinality meanings.

## Details

Stage 3 specialist lane under P2691. Reuse existing governing R definitions and accepted usage first. Complete the used primitive Formats in the scoped Model; the prepared vocabulary is string, int, bool, datetime, decimal and float, without assuming an unreviewed closed catalog or precision policy.

Formats describe direct values. list/map are YAML carrier structures, and identifying values use string rather than ref. Cardinality counts direct values at the addressed path, not nested keys; {0} permits a group with declared children, while an omitted count is undefined. Follow YAML value interpretation; null and an empty string are each one value, with admissibility governed by format/prose.

Put operative definitions in required prose Claims and add settled simple formal parts where useful. Do not require unique(selection), ID composition, functions, materialization, conditions in [] or a new evaluation engine. Do not gate the earlier mechanical Subject migration or reviewed-Draft adoption on this specialist completeness task.

## Definition of Done

Every used in-scope primitive Format has adopted defining R authority and the coverage record cites it. No representation container is reintroduced as a Format; advanced expression design is not smuggled into completion.

## Progress

Completed seven primitive Value Formats: bool, datetime, decimal, float, int, scalar and string. Each has adopted R authority. list/map remain carrier structures, ref is not a primitive Format, and advanced conditions/functions stay in their separate proposal.
