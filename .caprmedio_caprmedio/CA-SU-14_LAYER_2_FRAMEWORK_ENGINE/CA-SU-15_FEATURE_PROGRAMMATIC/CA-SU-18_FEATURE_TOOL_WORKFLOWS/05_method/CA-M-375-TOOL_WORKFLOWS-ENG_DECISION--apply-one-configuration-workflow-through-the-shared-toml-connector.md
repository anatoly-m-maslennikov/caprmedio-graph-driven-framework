---
atom_id: CA-M-375
content_role: Method
type: Eng Decision
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
status: Active
author: Anatoly Maslennikov
version: 13
updated_at: 2026-10-27 19:59:42 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Governing Configuration
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
relations: {}
tier: 3
---
# Summary

Apply one configuration Workflow through the shared TOML connector

## Scope

One explicit update of a TOML-backed Project configuration.

## Claim

**To** update Project configuration, its distinct configuration Workflow **must**:

1. Select the explicit logical configuration and requested delta under that configuration's meaning and applicable schema. Use the same TOML connector used by the other TOML configuration Workflows through the coherent logical interface; keep backend locations and serialization private to that binding.
2. read the complete current source through CA-O-218 under CA-D-631 on that same connector. CA-O-205 uses CA-O-219; CA-O-206 uses CA-O-220. require complete data, matching observed current_state, no errors **and** no mutation effects. bind that document **and** source evidence as explicit inputs **to** the later patch Step **before** deriving **or** validating its proposal. a failed **or** incomplete Read stops **without** Modify. derive **only** the explicit proposed delta **and** preserve unrelated configuration.
3. Validate the complete proposal against the selected configuration's applicable schema before any write. Missing or ambiguous schema authority, invalid values or unresolved required references fails closed.
4. Produce a mutation-free preview and obtain the applicable exact permission. A verified unchanged configuration is a no-op without a write or fictitious revision or timestamp.
5. Recheck current source and permission before supplying the exact logical modify request, complete proposed content or explicit delta, expected current state and bound schema and authorization context to the connector. Verify the actual resulting complete configuration and return its actual effects and recording state. The connector performs mechanical checks of the supplied bindings, not schema selection or configuration policy.

For CreateScopeUnit, use the declared Project Structure change through this shared connector; do not infer a Scope Unit declaration from a filesystem folder. Preserve applicable storage and concurrent-edit safeguards. This Method adds no configuration schema, connector-specific Workflow duplicate or resume/retry policy.

## Details

This is a required design contract. Current implementation, acceptance and any deferred publication concurrency/access decision remain separate.
