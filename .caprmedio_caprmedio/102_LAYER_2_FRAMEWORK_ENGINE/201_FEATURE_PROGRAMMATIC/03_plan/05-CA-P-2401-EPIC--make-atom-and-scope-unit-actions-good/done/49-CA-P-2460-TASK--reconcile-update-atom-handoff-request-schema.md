---
atom_id: CA-P-2460
content_role: Plan
type: Plan
label: Task
work_sequence_number: 49
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2401
version: 7
updated_at: 2026-10-25 17:32:27 +0400
tier: 3
---
# Summary

Reconcile the update-atom lifecycle handoff request schema

## Objective

Perform one bounded read-only reconciliation of the selected `update_atom` discovery/context handoff and its first Update Step, without attempting an effect or inventing a request payload.

## Details

Use the retained observations for CA-O-127 and its ordinary Update entry CA-O-145: discovery succeeds, `get_execution_context` reports `context_complete=true` with `input_schema=null` and no `currentStep`, and an empty `update_atom` preview is rejected before target/effect handling with `request route is not the selected MCP route`. Read the current governed O145 definition and the selected current-entry context, identify the authoritative owner of any supported request schema/executable binding, and preserve the distinction between a missing advertised handoff and a valid Update implementation failure. Do not guess a payload, retry the rejected route, send an effect, weaken validation, or modify Workflow/Step semantics.

At most15minutes ownwork, split before extending. Preserve exact evidence and unrelated changes. No production request, historical replay, source publication, runtime replacement, Git mutation or Journal/report write is authorized by this Task.

### Definition of Done

Record the exact selected current-entry context and governed O145 binding, identify whether a usable request schema/executable handoff is advertised, and retain any unresolved gap with its precise owner. A missing schema remains a bounded discovery/context limitation; it is not relabeled as a valid-update product failure or fixed by a guessed request.

### Dependency and scope checkpoint

CA-C-545 records the narrow handoff observation. The approved release is separate and does not resolve this discovery/context gap. This Task is Backlog pending the next read-only handoff review.

### Dependency review

Independent local source investigation may proceed using retained O127/O145 context (input_schema=null) while P2478 executes. No new production call, guessed effect packet, source fix, Git or Journal write by the investigator. Root separately owns planning publication and records actual evidence. This is the next dependency-reviewed read-only queue item, not permission to change Workflow semantics.

### Verified execution checkpoint

Read-only source diagnosis and a root normal-planning context lookup establish the supported route-name lookup: get_execution_context({id: update_atom}) returns selected_route=true, context_complete=true and a generic selected-route envelope schema with operation_route fixed to update_atom. The live Workflow CA-O-127 and Step CA-O-145 lookups each returned input_schema=null and no currentStep. Source service.py exposes one schema only for a single selected route; O127 serves five routes, and Step IDs are not included in route matching. The envelope parameters remain an unstructured object; this is not a complete current-Step input/effect contract. No effect, guessed request, preview, replay, release or deployment was performed. C545 remains Active for that narrower handoff gap.

The investigator also reproduced a stale-path loader failure in an older host-installed package. That counterfactual artifact test is not evidence about the actually serving runtime and does not prove that deployment fixes the handoff. Route-name source-only lookup was reproduced; only root performed the live read-only route context call. No code/schema change is needed merely to choose the already supported route-name context lookup; do not invent per-Workflow schemas or broaden the contract without its own governed Task.
