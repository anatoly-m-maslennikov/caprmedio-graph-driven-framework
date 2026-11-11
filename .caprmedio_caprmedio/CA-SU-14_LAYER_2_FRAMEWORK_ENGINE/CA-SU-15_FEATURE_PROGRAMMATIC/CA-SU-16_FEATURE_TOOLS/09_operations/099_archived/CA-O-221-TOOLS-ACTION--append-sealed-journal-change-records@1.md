---
atom_id: CA-O-221
content_role: Operations
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
type: Action
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-14 17:00:15 +0400"
subjects:
  governs: "Append Change Records"
  depends_on: [Journal, Journal/Record, Commit Context, Operator]
relations: {}
---
# Summary

Append sealed Journal change records

## Scope

An authorized Project-local APPEND_CHANGE_RECORDS request containing an existing complete sealed context and its observed canonical Journal records.

## Claim

Append Change Records **means** the reusable Action that validates an existing sealed context and appends its exact observed canonical records through the shared Project Journal writer, returning actual storage receipts or truthful failure without changing the recorded Project source or creating a Git commit.

## Action

1. Bind the actual Project and authorized caller; validate the complete supplied context, canonical event fields and digest bindings without inventing missing author, session, Action identity, observation time, predecessor state, replacement references or authorization. Tool parameters express intent and observed data, not independent Operator confirmation.
2. For dry run, return the existing records, safe resolved Journal targets, planned receipts and storage-validation results without mutation.
3. For authorized apply, append the exact event set with the shared writer's event and partition locks and idempotent receipts. Do not acquire a Git-effect lease, alter the Git index, create a Commit or perform the recorded source/lifecycle operation.
4. Return only confirmed receipts as completed recording. Preserve accepted history and actual partial or pending recording evidence on failure; recording retry never replays a source effect. A receipt proves storage integrity, not lifecycle conformance, historical truth beyond the supplied evidence or authority for another effect.

## Details

This Action realizes the existing recording boundary of CA-R-812 and CA-R-1491 and the Carrier serialization of CA-D-009, CA-D-340 and CA-D-435. The context's recorded action_id identifies the observed source-authoring action; it is not silently replaced with this reusable Action definition's Atom ID. No additional WorkflowRun, Session or approval record is created. CA-R-807 and CA-E-462 separately evaluate replacements. An existing recovered baseline is observation evidence only; its preparation and required chronology remain under their existing rules, not a new baseline design in this Action.
