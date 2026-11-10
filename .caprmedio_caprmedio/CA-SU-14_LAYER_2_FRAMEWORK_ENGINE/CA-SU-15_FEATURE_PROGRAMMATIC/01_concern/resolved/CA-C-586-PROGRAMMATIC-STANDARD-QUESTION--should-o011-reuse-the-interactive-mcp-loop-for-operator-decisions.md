---
atom_id: CA-C-586
ref_id: CA-C-586
container:
  scope_unit: CA-SU-15
role: Concern
form: Question
topics:
  main_subject: Entity/Node/Continuant/Implementation
relations:
  concern_about:
  - CA-O-011
  - CA-P-2630
  - CA-C-585
  - CA-C-583
  relates_to:
  - CA-O-016
  - CA-P-2577
  - CA-R-1317
status: Resolved
version: 2
updated_at: 2026-11-10 22:36:14 +0400
carrier_destination:
  file:
    name: CA-C-586-PROGRAMMATIC-STANDARD-QUESTION--should-o011-reuse-the-interactive-mcp-loop-for-operator-decisions.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/01_concern/resolved
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
priority: high
---
# Summary

Should O011 reuse the interactive MCP loop for Operator Decisions?

## Concern

For O011 methodology approval and recovery, should the implementation reuse
the existing interactive MCP loop to obtain and retain an actual
OperatorDecision while keeping Run state and the business Journal record
separate, or should the implementation defer and report this as an unresolved
implementation gap?

## Evidences

CA-C-585 resolves only the Journal boundary: Journal recording is non-blocking
for methodology approvals and recovery, while actual OperatorDecision and
independent Run/effect evidence remain required. The current compiler design
does not yet identify a verified prior non-release O011 recovery reader or an
authoritative decision resolver. The existing operator_authorization mapping
is not accepted as an authoritative caller contract. Proposed trusted evidence
from an executor and public decision references are design candidates only.

## Decision required

Choose one bounded direction:

1. Reuse the admitted interactive MCP loop to obtain the actual OperatorDecision
   and retain the independent Run/effect evidence, with Journal recording kept
   as a separate non-blocking business obligation; or
2. Defer the reuse and report the missing decision/recovery integration as an
   explicit implementation gap before compiler work proceeds.

Neither option creates a universal Journal gate or authorizes a caller-
supplied approval flag.

## Disposition

Keep this Question Active. CA-P-2630 remains a design hold until the Operator
answers; no compiler code, source Atom, runtime binding, release, deployment
or replay is changed by this record.

## Resolution

The Operator canceled CA-P-2630, retiring the old approval-integration plan. The implementation-choice question for that plan is obsolete and is Resolved. No existing MCP approval route or replacement compiler contract is asserted by this resolution.

The governing requirement for an actual Operator decision remains unchanged. No Methodology source, runtime or implementation was changed by this cancellation.
