---
atom_id: CA-R-1972
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Occurrent
relations:
  child_of:
  - CA-R-1174
version: 1
updated_at: "2026-10-17 17:07:48 +0400"
---
# Summary

Define Entity/Occurrent

## Scope

actual occurrences.

## Claim

an Occurrent **means** an actual occurrence, such as an Event, Execution or Session. a stored record describes the occurrence; it is **not** the occurrence itself.

## Details

Candidate #6 separates runs from definitions and historical records. CA-R-1510 and CA-R-1511 define particular Run kinds; CA-R-1745 distinguishes Journal records from events. These support the distinction but do not define the general Occurrent kind. This draft adds no Run or Session lifecycle.
