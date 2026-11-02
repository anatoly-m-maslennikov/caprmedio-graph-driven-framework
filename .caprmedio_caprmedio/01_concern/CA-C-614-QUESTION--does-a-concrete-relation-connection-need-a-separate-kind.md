---
atom_id: CA-C-614
content_role: Concern
type: Question
current_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
tier: 3
version: 1
updated_at: 2026-10-29 09:39:47 +0400
subjects:
  governs: Entity/Graph Syntax > Relation
relations: {}
---
## Summary

Does a concrete Relation connection need a separate kind?

## Question

Should the chosen continuation below change when a concrete conflicting use is identified?

## Details

For now an actual directed connection remains the tuple (source, Relation Type, target), without a new Connection entity or separate ID. R2247 preserves source/target reference meanings; R1986 and R1987 were retired because those are not reusable Type metadata. Existing direct facts and derived inverses stay governed. A separate endpoint-record kind can be reconsidered only if a concrete operation needs it.

Latest 48-hour input and Current source meanings support this minimal continuation but do not fix every representation detail. The Operator directed choosing the best option, tracking uncertainty and continuing.
