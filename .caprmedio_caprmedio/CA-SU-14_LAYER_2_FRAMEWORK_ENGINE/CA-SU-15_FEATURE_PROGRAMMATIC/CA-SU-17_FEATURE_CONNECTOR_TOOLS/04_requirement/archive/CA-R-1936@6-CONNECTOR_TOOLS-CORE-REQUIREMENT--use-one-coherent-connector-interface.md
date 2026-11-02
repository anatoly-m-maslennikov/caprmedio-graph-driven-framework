---
atom_id: CA-R-1936@6
content_role: Requirement
type: Requirement
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
status: Archived
author: Anatoly Maslennikov
version: 6
updated_at: 2026-10-24 00:51:05 +0400
subjects:
  governs: Subject/Engineering/Tool
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Term//Property
relations:
  relates_to:
  - CA-M-376
  - CA-D-625
  - CA-E-628
  - CA-R-1093
tier: 1
---
# Summary

Use one coherent connector interface

## Scope

All connectors in CONNECTOR_TOOLS, independently of their storage backend and supported operation subset.

## Claim

Every connector **must** use the coherent logical interface represented by CA-D-625-CONNECTOR_TOOLS-CORE-DELIVERY--deliver-coherent-connector-interface. A connector declares its supported subset of `query`, `read`, `create` and `modify` and the admitted payload schema for each supported operation. An unsupported operation or invalid payload **must** be rejected without effects; do not emulate it by composing a hidden Workflow. The common interface does not require every connector to support every operation.

The request roles are `operation`, `target`, `query`, `delta`, `expected_state`, `authorization` and `context`. Supply exactly one logical target or query as applicable, with explicit entity kind and identity or explicit filters. Query and Read have no delta; Create and Modify receive complete explicit content or edits under the admitted schema. Context and authorization bind existing source-view, schema and permission authority, not ambient permission or a new Boolean approval. A connector mechanically validates these supplied bindings and required preconditions; it does not choose target-selection defaults, domain schema, identity, Version, lifecycle, reference-retargeting or Workflow sequence.

Read by explicit logical ID **must** return actual exact Version where the entity has one and its actual source-state evidence without requiring a pre-known Version. A supplied pinned or historical expectation **must** match exactly; the explicit target and context distinguish the current source view from the requested historical view. Missing or ambiguous resolution fails rather than selecting another view or adding a hidden Status filter. Modify requires expected current state and Create requires expected absence. Do not invent an Atom Version for a Scope Unit or configuration that has no such Property.

Backend locations, filenames, database tables, serialization, query languages and internally computed list positions remain private connector bindings, not logical target or delta selectors. Workflows use logical entities and this interface; swapping storage changes the connector binding or implementation, not Workflow meaning or sequencing. Query and Read remain mutation-free. Create and Modify perform only the supplied admitted storage delta after required currentness, permission and preview checks; they do not allocate domain identity, advance Version, decide lifecycle, select replacement or retarget incoming references. The Workflow supplies those decisions and the resulting exact content or edits.

The result roles are `data`, `current_state`, `effects` and `errors`. Return actual observed data and source-state evidence and truthful known or unknown effect evidence. Errors are structured by code, message and affected field. Unknown effects **must** include `effect_uncertain`; nonempty errors **must not** be reported as success even if some effects are known. Empty errors require independent verification of the operation's declared result, not merely absence of an exception. A true no-op requires verification that the requested state is already satisfied and unchanged; it creates no fictitious write, history, Version or timestamp. Preserve applicable per-operation storage safeguards and any known partial effects without claiming a cross-Atom transaction or automatic recovery.

## Details

### Direct Subject lookup exception

Only the direct read-only ATOM_SEARCH Subject lookup declared by CA-D-424 may receive its closed explicit logical criteria without the seven-member request envelope or caller-supplied authorization/context references. Its canonical provider is bound to the admitted Project root and must validate the exact applicable definition, grammar, Project boundary and selected-source evidence itself. This named exception introduces no approval flag, fabricated reference, permission system or implicit target-selection policy. It creates no Session, Action Run or Journal record and grants no mutation permission. When used within an actual Workflow, the caller retains its applicable Tool-call recording responsibility. All other connector operations and the existing Session-based realization retain their request, admission and recording rules unchanged.

CA-M-376-CONNECTOR_TOOLS-CORE-METHOD--execute-one-explicit-connector-operation defines the minimal adapter procedure; CA-E-628 defines conformance and CA-D-625 owns exact representation. CA-D-527 remains the existing outer selected-operation service envelope where used; this contract adds no transport, database implementation, whole-Project default query, retry or resume protocol. Workflow semantic ownership remains under CA-R-1093-TOOL_WORKFLOWS-CORE-REQUIREMENT--separate-generic-and-atom-specific-tool-authority. Source authoring is not runtime implementation, connected-MCP acceptance or admission of deferred Subject publication.
