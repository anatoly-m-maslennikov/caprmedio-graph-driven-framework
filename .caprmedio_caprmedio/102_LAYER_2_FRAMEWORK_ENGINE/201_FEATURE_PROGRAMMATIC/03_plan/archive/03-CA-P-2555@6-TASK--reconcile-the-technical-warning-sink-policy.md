---
atom_id: CA-P-2555@6
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Engineering/Logging Policy
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2552
  depends_on:
  - CA-P-2553
version: 6
updated_at: 2026-10-24 13:39:34 +0400
tier: 3
---
# Summary

Reconcile the technical-warning sink policy

## Objective

Apply the answered Logging Policy/configuration choice to the technical warning
boundary without turning warnings into business Journal records: Docker `stderr`
with structured records, a validated Project prefix from the existing bound
Project selection and canonical prefix-field validation, Docker local rotation
`max-size=10m`/`max-file=3`, `mode=non-blocking`, and
`max-buffer-size=1m`.

## Details

This Task is complete at the source, configuration and focused-evidence boundary.
The selected immutable settings view supplies the canonical Project prefix; no
additional settings carrier is introduced and this Task does not claim full
SettingsReader conformance. When the non-blocking buffer is full, new technical
messages may be dropped so primary work cannot stall. Docker logs are removed
with the container. The business Journal remains business-only and no local log
directory is created.

The focused evidence includes six logger checks, 94 AtomSearch tests with no
skips, ten MCP protocol tests in 3.990 seconds after warning-path and malformed
warning-skip updates, and four Docker logging tests plus 21 related checks.
An isolated Docker probe used the existing version 0.4.4.10 image with
read-only new-source and version mounts. It verified two Project prefixes
(CHECK_A and CHECK_B), the Docker environment, token redaction, and Docker local
logging inspection for `max-size=10m`, `max-file=3`,
`mode=non-blocking`, and `max-buffer-size=1m`; it exited 0. This is a
source-mounted configuration check, not acceptance of a newly built image.
Production container 649228a677661439d12d9771d606652525480ab4a2f5ef2131036b451a1cae7e
remained healthy and unchanged.

## Definition of Done

The sink decision, source/configuration contract, and focused evidence are
recorded; technical warnings remain outside business Journal history and do not
expose Atom contents. New-image, deployment, full-suite and public-release
acceptance remain outside this Task and require their own evidence.
