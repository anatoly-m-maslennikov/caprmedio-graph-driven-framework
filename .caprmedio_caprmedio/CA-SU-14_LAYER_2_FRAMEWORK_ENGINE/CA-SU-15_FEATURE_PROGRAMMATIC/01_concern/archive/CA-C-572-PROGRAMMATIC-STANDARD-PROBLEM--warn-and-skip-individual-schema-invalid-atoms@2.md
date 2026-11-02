---
atom_id: CA-C-572
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
priority: medium
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  concern_about: [CA-R-863, CA-M-370, CA-E-301, CA-M-163, CA-P-2552]
version: 2
updated_at: "2026-10-21T17:07:21Z"
---
# Summary

Warn and skip individual schema-invalid Atoms during scans

## Concern

Native ATOM_SEARCH observation surfaced 25 `schema_invalid` diagnostics with no
effects. The Operator now requires an isolated schema-invalid Atom to be omitted
with a technical warning carrying its path and reason, while the bounded scan may
continue with `complete: false`. This is a warning disposition for an individual
invalid carrier, not permission to hide an incomplete source frontier or to repair
the source.

## Required disposition

The implementation and acceptance evidence must distinguish an isolated
schema-invalid Atom from fatal I/O, security, duplicate-identity, stale, ambiguous,
or otherwise incomplete-frontier conditions. The former is skipped with valid
matches retained and `complete: false`; the latter remains a refusal/error with no
partial successful result. Technical warnings use the configured runtime
diagnostic logging authority. They are not business Journal records, must not create
a fake Run, and must not rewrite historical Journal records.

## Evidence boundary

The current AtomSearch suite passed 88 tests in 33.896
seconds after the final code helper fix, but this planning record does not claim a
new deployment or installed-runtime acceptance. CA-R-863, CA-M-370 and CA-E-301 now
carry the explicit scan disposition; CA-M-163 preserves the
technical-diagnostic versus Journal boundary. Existing query-Journal authorities
CA-R-1865, CA-R-1867, CA-M-337, CA-E-577 and CA-E-580 remain the route for truthful
actual-query evidence and do not authorize a competing log. Sink selection remains
with the active Logging Policy/configuration; this Problem does not choose a
`.caprmedio_runtime/logs/` default or container-only sink.

## Blast radius

ATOM_SEARCH and related bounded scans, their diagnostic result envelopes, runtime
logging, and the distinction between technical diagnostics and business Journal
history. Preserve all historical Journal bytes, no-effect behavior, fatal guards,
and the complete-suite/public-release gate. No Stage 2 Scope Unit operation,
release, deployment, migration, or whole-Epic closure is implied.
