---
atom_id: CA-P-2555
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2552]
  depends_on: [CA-P-2553]
version: 2
updated_at: "2026-10-21T18:05:00Z"
---
# Summary

Reconcile the technical-warning sink policy

## Objective

Apply the answered Logging Policy/configuration choice to the technical warning
boundary without turning warnings into business Journal records: Docker `stderr`
with structured records, a validated Project prefix from the existing bound
Project selection and canonical prefix-field validation, and Docker local rotation
`max-size=10m`/`max-file=3` with `mode=non-blocking` and `max-buffer-size=1m`.

## Details

At most 15 minutes own work after the source/test implementation is ready. Reuse
CA-M-163, CA-D-396, CA-D-504 and CA-D-559. Confirm warning records carry the
validated Project prefix, path and reason, preserve `complete: false`, obey
bounded Docker retention/back-pressure/unavailable-sink policy, and leave
historical/business Journal records unchanged. When the non-blocking buffer is
full, new technical messages may be dropped so primary work cannot stall; Docker
logs are removed with the container. Do not create a local log directory. Use the
selected immutable settings view without adding a settings carrier or claiming
full SettingsReader conformance. Root owns any runtime or configuration
implementation and deployment.

### Definition of Done

The explicit sink decision is recorded here. The Task remains Active until focused
logger evidence verifies two Project prefixes, redaction/no Atom contents, bounded
non-blocking buffer/drop behavior, and an observable logging failure that does not
break the primary scan. The pre-existing full SettingsReader conformance gap
remains a separate readiness caveat. No release or deployment claim is allowed
before that evidence.
