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
version: 4
updated_at: "2026-10-21T17:25:04Z"
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
partial successful result. Technical warnings use Docker `stderr` as structured
records, carry the validated Project prefix from Project settings plus path and
reason, and are retained by Docker local rotation `max-size=10m` and
`max-file=3`, with `mode=non-blocking` and a `max-buffer-size=1m`; new technical
messages may be dropped when that buffer is full so the primary scan cannot stall.
The prefix uses the existing bound Project selection and canonical prefix-field
validation. This uses the selected immutable settings view and does not claim full
SettingsReader conformance or add another settings carrier. Docker logs are
removed with the container. They are not business Journal records, must not create
a fake Run, must not create a local log directory, and must not rewrite historical
Journal records. A missing or failed logging stream remains observable without
breaking the primary scan.

## Evidence boundary

The current AtomSearch suite passed 94 tests with no skips. Ten MCP protocol tests
passed in 3.990 seconds after warning-path and malformed-warning-skip updates;
four Docker logging checks and 21 related checks also passed. An isolated Docker
probe against the existing version 0.4.4.10 image, with read-only new source and
version mounts, verified two Project prefixes (CHECK_A and CHECK_B), the Docker
environment, token redaction, and Docker local logging inspection for
`max-size=10m`, `max-file=3`, `mode=non-blocking`, and `max-buffer-size=1m`; it
exited 0. This is source-mounted configuration evidence, not acceptance of a new
image. Production remained unchanged and healthy. CA-R-863, CA-M-370 and CA-E-301
carry the explicit scan disposition; CA-M-163 preserves the technical-diagnostic
versus Journal boundary. Existing query-Journal authorities CA-R-1865, CA-R-1867,
CA-M-337, CA-E-577 and CA-E-580 remain the route for truthful actual-query
evidence and do not authorize a competing log. The selected Docker `stderr`
stream and bounded local rotation are now the sink policy; this Problem does not
add a local log directory or turn technical warnings into business Journal
records. It remains Active pending new-image/deployment acceptance and the
pre-existing full SettingsReader/M284 conformance gap.

## Blast radius

ATOM_SEARCH and related bounded scans, their diagnostic result envelopes, runtime
logging, and the distinction between technical diagnostics and business Journal
history. Preserve all historical Journal bytes, no-effect behavior, fatal guards,
and the complete-suite/public-release gate. No Stage 2 Scope Unit operation,
release, deployment, migration, or whole-Epic closure is implied.
