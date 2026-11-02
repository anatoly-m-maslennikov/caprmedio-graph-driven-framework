---
atom_id: CA-P-2686@4
content_role: Plan
type: Plan
label: Task
current_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity
version: 4
updated_at: 2026-10-29 07:57:52 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2683
tier: 4
---
# Summary

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

Done: all six used primitive Formats have Current R/Entity Definition authority. See formats-verification.json and the refreshed Definition coverage for exact IDs/Versions. The adopted Format structure retains direct-value cardinality semantics and separates YAML containers/Carrier representation formats from value Formats. No precision, uniqueness expression, functions or advanced bracketed conditions were added.
