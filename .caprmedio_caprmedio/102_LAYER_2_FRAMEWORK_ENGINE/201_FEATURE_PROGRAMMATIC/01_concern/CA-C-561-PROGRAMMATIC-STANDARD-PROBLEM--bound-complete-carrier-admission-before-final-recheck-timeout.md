---
atom_id: CA-C-561
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
priority: high
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  concern_about: [CA-C-560, CA-P-2521]
version: 1
updated_at: "2026-10-21T09:06:55Z"
---
# Summary

Bound complete-carrier admission before final recheck timeout

## Concern

A bounded new Concern could not be published through the existing native writer because complete-carrier validation exhausted its read-I/O time budget before the final Project-declaration recheck.

## Evidences

One C560 native create attempt under .caprmedio_tmp/image-tags-20261021-ABiLEA/create_problem.py failed with read_io.LimitReached(timeout_seconds), then ProjectSelectionError(Declaration boundary evidence is unavailable or unsafe), ProposedCarrierError(selected Project inputs are unavailable), and ToolError(complete-carrier-invalid). The traceback reached proposed_carrier.validate_proposed_carrier line606 final _current check; no C560 target was published. Earlier new Plan creation succeeded in the same checkout. The failure does not prove schema invalidity, declaration drift, a general writer outage or a production incident. Root checked the target/identity absence and used the Operator's standing manual fallback. No automatic retry or timeout/guard change occurred.

## Blast radius

Postpone this separate diagnosis while completing the explicitly prioritized image naming work. Reproduce only in an isolated representative corpus and identify actual read/validation cost, budget and final-currentness behavior before a fix. Preserve required complete validation, currentness and identity safety; do not raise a timeout blindly, waive a check, replay an uncertain effect or use live source Atoms as the test oracle. No repair or acceptance is claimed by this record.
