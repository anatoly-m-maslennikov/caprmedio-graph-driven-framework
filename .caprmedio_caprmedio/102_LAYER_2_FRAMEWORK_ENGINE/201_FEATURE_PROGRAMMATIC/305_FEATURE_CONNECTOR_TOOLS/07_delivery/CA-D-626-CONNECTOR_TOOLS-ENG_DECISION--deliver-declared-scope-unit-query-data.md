---
atom_id: CA-D-626
content_role: Delivery
type: Eng Decision
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
status: Active
author: Anatoly Maslennikov
version: 13
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Scope Unit
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Domain/Continuant/Project.Structure
  - Subject/Graph Node/Domain/Continuant/Project.Settings
relations: {}
tier: 3
---
# Summary

Deliver declared Scope Unit query data

## Scope

The operation-specific inner request/result representation for Scope Unit Query, refining CA-D-625-CONNECTOR_TOOLS-ENG_DECISION--deliver-coherent-connector-interface.

## Claim

Scope Unit Query data **must** use the common closed interface with the concrete logical refinements below. this representation admits no physical backend selector **or** second outer transport.

## Details

### Request refinement

Keep exactly the seven common outer-inner keys; `operation = "query"`, `target = null`, `delta = null`, and `query = {kind: "Scope Unit", filters}`.

`filters` has exactly `frontier`, `predicates` and `result_fields`:

- `frontier = {identity, include_self, include_descendants}`. Identity is the canonical Scope Unit Name in the Project fixed by `context`; both inclusion fields are explicit booleans and at least one is true. The canonical Project Name selects the implicit root; root plus explicit descendants permits a whole-Project frontier. No omitted frontier or physical path is admitted.
- `predicates` is an array of exactly `{field, match, value}` objects, combined conjunctively. Fields are `scope_unit_name`, `scope_unit_type`, `scope_unit_label` or `parent`. Name and Label admit case-sensitive literal `exact`, `prefix`, `suffix` and `contains`; Type and parent admit only `exact`. Values are nonempty strings; Type is `Ordered` or `Unordered`. Parent is a canonical Name in the bound Project, not a path or the private serialized root sentinel. Empty predicates apply only the explicit frontier.
- `result_fields` is an explicit duplicate-free array drawn from those four fields plus `structural_level`, `local_order` and `navigational_order_number`. Identity is always returned. Facts absent under the applicable declaration schema remain absent; missing Type/Label on the root is not invented and does not satisfy a predicate on that field.

Context binds the exact owning Project, source view, applicable schema and source authority. `authorization` binds existing read permission. `expected_state` may be null for an unpinned current view; when supplied, it is the exact existing source-state evidence binding for the selected view, including historical evidence where requested. It is not an Atom Version or a new token protocol. Current versus historical selection is explicit in context, never inferred from filenames.

### Result refinement

Keep exactly `data`, `current_state`, `effects` and `errors`. Available `data = {matches, coverage}`; matches are canonical-name-ordered `{identity, facts}` objects containing only requested facts. `coverage = {frontier, complete}` records the admitted logical frontier and whether all required sources and predicates were checked. A valid empty query has `matches = []`, complete coverage and no errors. Incomplete coverage cannot have empty errors.

`current_state` carries the observed bound Project/source view and exact existing source-state evidence, with no invented Scope Unit Version. Root identity comes from Project Settings; non-Project facts follow CA-D-442-CORE_META_MODEL--encode-scope-unit-declaration-fields. Logical parent facts resolve the declared root sentinel to the actual canonical Project Name. Carried source data and missing optional fields are not repaired.

The error vocabulary and `{code, message, field}` shape are exactly those of CA-D-625-CONNECTOR_TOOLS-CORE-DELIVERY--deliver-coherent-connector-interface: malformed input uses `input_invalid`; unresolved frontier uses `target_not_found`; duplicate or conflicting identity uses `target_ambiguous`; invalid declaration schema/graph uses `schema_invalid`; stale evidence uses `stale_state`; read denial uses `permission_denied`; inaccessible/unavailable backend evidence uses `backend_failure`. Unsupported operation uses `unsupported_operation`. Report available partial matches with incomplete coverage or null data when unavailable, never fabricate complete coverage. Normal Query has `effects = []`; unexpected actual or unknown effects retain the common truthful evidence and fail, with `effect_uncertain` for unknown effects.

CA-D-441-CORE_META_MODEL-ENG_DECISION--encode-the-project-structure-document-schema and CA-R-1484-CORE_META_MODEL-RULE--establish-scope-units-through-project-structure-declarations retain declaration authority. This is an unimplemented source representation pending independent acceptance; CA-O-211-CONNECTOR_TOOLS-ACTION--query-declared-scope-units is its operation definition, not a new CLI/MCP/HTTP route. The existing selected service uses the unchanged common outer envelope where applicable.
