---
atom_id: CA-D-625@5
content_role: Delivery
type: Eng Decision
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
local_tier: Core
global_tier: 9
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Engineering/Connector Interface Contract
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Workflow
  - Subject/Domain/Node/Continuant/Governing Configuration
version: 5
updated_at: 2026-10-23 23:34:06 +0400
relations:
  delivery_for:
  - CA-R-1936
  relates_to:
  - CA-M-376
  - CA-D-527
  - CA-O-046
  - CA-O-047
  - CA-O-204
  - CA-O-218
  - CA-D-631
---
# Summary

Deliver coherent connector interface

## Scope

The concrete logical API representation required by CA-R-1936 and CA-M-376 for every connector under CONNECTOR_TOOLS. API means one coherent caller contract, not a new MCP, HTTP, CLI or other transport.

## Claim

Connectors use the same request/result roles for explicit query, read, create and modify operations. Each connector declares only its supported subset and target kinds; the common vocabulary does not require every connector to implement all four operations.

## Details

### Named direct Subject lookup exception

Only CA-D-424's direct read-only ATOM_SEARCH Subject lookup uses its separately closed public criteria instead of the seven-member inner request. It accepts no caller root, physical selector, authorization/context reference, approval flag or Session ID. The canonical root-bound provider validates the actual definition, grammar, Project boundary and selected-source evidence; no synthetic references or new authorization protocol substitute for those checks. It returns the same four logical result roles with no effects. This direct observation creates no Session, Action Run or Journal record and is not a recorded Action execution; an actual enclosing Workflow retains applicable Tool-call recording. This exception does not change the existing Session-based realization, D527's envelope within the selected service, any other connector operation, or staging/publication admission and recording.

### Logical request

The inner request is one JSON object with exactly `operation`, `target`, `query`, `delta`, `expected_state`, `authorization` and `context`.

- `operation` is exactly `query`, `read`, `create` or `modify`, and must belong to that connector's admitted subset.
- Exactly one of `target` and `query` is non-null. Query uses `query = {kind, filters}` and null target; the other operations use `target = {kind, identity}` and null query. The admitted operation schema fixes supported logical kinds, identity and filter shapes. Physical filenames, paths, indexes or backend keys cannot substitute for logical identity.
- `delta` is null for query/read. Create supplies the complete explicitly admitted content; Modify supplies the explicitly admitted edits or proposed content. Its operation-specific shape is fixed by the bound schema; it is not an untyped permission to change anything.
- `expected_state` is null for an unpinned Read or carries the exact supplied Version/source-state evidence for pinned or historical Read. Explicit full-ID Atom Read needs no pre-known Version and returns the actual exact Version/state. Target/context fixes the source view; ambiguity fails rather than invoking Find. Modify requires exact expected current state; Create requires expected absence. Query carries its applicable bound source-view evidence, without inventing an Atom Version for a Scope Unit or configuration.
- `authorization` and `context` are references to existing bound permission and execution/source/schema context, not ambient flags, secret payloads or a second authorization protocol. Verify them against the admitted surrounding contract. Preview does not acquire effect permission.

For example, this illustrative unpinned Read contains no authority by itself:

```json
{
  "operation": "read",
  "target": {"kind": "Atom", "identity": "CA-R-863"},
  "query": null,
  "delta": null,
  "expected_state": null,
  "authorization": "bound-permission-reference",
  "context": "bound-context-reference"
}
```

Workflow admission owns schema/domain validation, identity allocation, initial and changed Version/time, Status/lifecycle and replacement decisions. The connector mechanically checks the supplied shape, currentness, permission and validation bindings, then performs only the explicit requested operation. It does not choose defaults, allocate an ID, bump Version, archive/delete an Atom, infer a replacement or rewrite references. The workflow supplies every admitted metadata/content delta. Reject unknown fields, unsupported subsets, unresolved references, stale state and widened scope before the affected operation writes.

Query returns matches, not full content; Read returns the complete identified state. Neither implicitly invokes the other or a mutation. List-entry replacement uses the unique exact current value, not a caller index; whole-set replacement and add/remove use their separately admitted explicit deltas. CA-O-218 supplies complete Configuration Read under CA-D-631; CA-O-204 supplies Modify on the same shared TOML connector. configuration Workflows choose schema **and** source authority.

### Logical result

The inner result is one JSON object with exactly `data`, `current_state`, `effects` and `errors`.

- `data` is the operation's actual matches, complete read state or observed write result; use null when unavailable. Proposed data is explicitly labelled and never reported as an observed effect.
- `current_state` carries the exact observed logical identity, actual Version where applicable and source-state evidence; use null where state is unavailable. An unpinned Atom Read returns its actual exact Version/state token.
- `effects` is an array of attributable descriptors `{operation, target, state, evidence}`. `state` is `known` or `unknown`; evidence binds actual observations or the unresolved boundary, never a proposed effect. Query, Read and truthful no-op have no mutation effects.
- `errors` is an array of `{code, message, field}`; `field` is the affected logical request field or null. Stable codes are `input_invalid`, `unsupported_operation`, `target_not_found`, `target_ambiguous`, `stale_state`, `permission_denied`, `schema_invalid`, `backend_failure` and `effect_uncertain`. Empty matches are not errors. A failure never erases an earlier observed effect or converts an unknown effect into success. Every unknown effect requires an `effect_uncertain` error. Nonempty errors never indicate success, even when known effects occurred; empty errors require a verified declared result, not merely absence of an exception. A true no-op must verify the requested state unchanged.

Within the existing selected service, place the logical request in CA-D-527's typed parameters and the logical result in its route-owned outcome/result payload. Reuse its parameters/target/effect/definition/currentness/authorization bindings and outer disposition/recording rules unchanged. This carrier introduces no second outer request/result, Run/Event schema, execution engine or admitted route.

### Delivery status

This is an unimplemented required contract awaiting functional verification. Existing individual executable paths remain explicit adapter bindings; the new FEATURE Delivery root is future/unmaterialized and does not relocate code. A replaceable backend contract is not a DB implementation or a guarantee stronger than observed file/TOML behavior. No new retry/resume, concurrency or publication design is admitted. Old fixtures, source pins, installed copies and receipts are historical evidence, not proof of this revision.
