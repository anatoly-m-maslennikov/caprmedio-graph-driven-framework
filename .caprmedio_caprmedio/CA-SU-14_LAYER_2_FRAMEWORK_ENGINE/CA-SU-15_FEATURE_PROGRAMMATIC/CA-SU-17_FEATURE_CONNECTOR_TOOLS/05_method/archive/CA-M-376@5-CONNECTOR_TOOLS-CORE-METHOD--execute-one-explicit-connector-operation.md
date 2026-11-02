---
atom_id: CA-M-376@5
content_role: Method
type: Eng Decision
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
status: Archived
author: Anatoly Maslennikov
version: 5
updated_at: 2026-10-24 00:38:25 +0400
subjects:
  governs: Subject/Engineering/Connector Operation Dispatch
  depends_on:
  - Subject/Domain/Node/Continuant/Workflow
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
relations:
  relates_to:
  - CA-R-1936
  - CA-D-625
  - CA-E-628
  - CA-R-1093
tier: 1
---
# Summary

Execute one explicit connector operation

## Scope

One explicit admitted storage operation through the coherent connector interface.

## Claim

**To** execute a connector request, the adapter **must**:

1. Validate the requested operation against this connector's declared supported subset and payload schema under CA-R-1936-CONNECTOR_TOOLS-CORE-REQUIREMENT--use-one-coherent-connector-interface and CA-D-625-CONNECTOR_TOOLS-CORE-DELIVERY--deliver-coherent-connector-interface. Reject an unsupported operation or invalid shape without effects, emulation or hidden Workflow composition.
2. Bind the supplied logical target or query, source-view and schema context, authorization and required expected state. Resolve the storage mapping privately and uniquely. Do not add filters, choose domain schema or permission, infer identity or lifecycle, or silently substitute targets. Reject missing, ambiguous, stale or unauthorized bindings before effects.
3. For Query or Read, keep the operation mutation-free and return only the admitted requested data and actual source-state evidence. Explicit-ID Read does not require a pre-known Version; return actual exact Version where applicable. Enforce an optional pinned or historical expectation exactly and do not silently change the requested source view.
4. For Create or Modify, require the supplied explicit content or edits and respectively expected absence or expected current state. Mechanically validate the supplied schema, bound permission and required preview evidence, recheck source preconditions before effects and perform only the admitted exact storage delta. Domain identity, Version, lifecycle, replacement, default selection and reference decisions remain Workflow-owned; retain applicable storage-effect safeguards.
5. Independently verify the declared result against observed after-state and return `data`, `current_state`, `effects` and structured `errors`. Preserve known partial effects truthfully. An unknown effect requires `effect_uncertain`; nonempty errors are not success. Empty errors require verified declared postconditions, not merely a completed call. A true no-op verifies requested state already satisfied and unchanged and creates no fictitious write, history, Version or timestamp.

Do not turn these mechanics into a cross-Atom all-or-nothing promise, hidden lifecycle Action or automatic retry, resume or recovery policy. A storage-backend swap replaces this connector's implementation or binding without changing Workflow meaning or sequencing.

## Details

### Direct Subject lookup procedure

For only the direct read-only ATOM_SEARCH Subject subset declared by CA-D-424, validate its closed explicit criteria instead of demanding caller authorization/context references or the seven-member envelope. Bind the Project root through the registered canonical provider; verify current definition, grammar, settings/structure and selected-source evidence before returning. Do not manufacture execution references or start a Session, Action Run or Journal event. Return the same four result roles with no effects; refuse incomplete, ambiguous or stale observation. Applicable recording remains with an actual enclosing Workflow caller. The existing Session-based realization and every other connector's admission and recording are unchanged.

The exact request and result representation belongs to CA-D-625. Existing CA-D-527 outer service transport remains unchanged where applicable. This Method introduces no database implementation or new transport and does not prove current code conformance, connected-MCP execution or deferred Subject publication readiness.
