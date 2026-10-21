---
atom_id: CA-C-545
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
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-P-2401, CA-O-127, CA-O-145]
version: 3
updated_at: "2026-10-20T19:57:22.658Z"
---
# Summary

Expose the selected update-atom handoff request schema

## Concern

The selected lifecycle handoff does not expose a usable request schema/executable binding through discovery and context. The current CA-O-127 Workflow delegates an ordinary Update request to its first Step CA-O-145, but read-only `get_execution_context` for the selected entry reports `context_complete=true`, `input_schema=null` and no `currentStep`. An advertised `update_atom` preview with `{}` is rejected before target or effect handling with `request route is not the selected MCP route`.

This is only a missing advertised handoff schema/binding observation. It does not prove that a valid Update request is broken, that CA-O-145 lacks its governed Step definition, or that any target/effect route should be guessed.

## Evidences

Read-only discovery for `update_atom` succeeds. Read-only context for CA-O-127 and its first Update Step CA-O-145 both expose a complete context flag but no input schema/current-step executable binding. The current source definitions say that O127 delegates ordinary Update to O145 and that O145 binds the textual target, proposal, authority and assessment evidence while supplying no effect permission. The empty preview was rejected before target/effect selection with the exact route diagnostic above.

No effect request, guessed payload or further route attempt was made. Manual planning fallback records the evidence gap only; it does not publish a native MCP effect or claim a valid-update failure.

## Blast radius

Callers cannot determine the supported selected lifecycle request shape from the advertised discovery/context handoff. Inspect the current-entry O145 context and governed request/schema owner under CA-P-2460, preserving the exact route refusal and refusing to infer a target, proposal or effect. This Concern does not alter validation, routing, Workflow semantics or release status.

### Refined evidence after P2460

Root read-only normal planning lookup by the discovered public route name update_atom succeeds: selected_route=true, context_complete=true, input_schema contains the generic route envelope with operation_route fixed to update_atom. Thus a blanket statement that discovery/context exposes no route schema is superseded. Workflow O127 and Step O145 still return null input_schema and no currentStep; source-only review explains the shared-Workflow ambiguity and omission of Step IDs from selected-route matching. The route envelope leaves parameters as an unstructured object and does not itself expose current-Step inputs, exact effect schema or an executable Step handoff. This narrower gap remains Active; no supported Update effect has been attempted in this follow-up.

A separately inspected old host installation rejects a stale pinned source path. That host artifact test is not evidence that the serving MCP is stale, is not a current production incident, and is not proof that a release fixes this Concern. P2460 diagnosis is Done; implementation of any additional context contract requires a separately reviewed bounded Task. No policy, authority, request fields or route should be guessed.
