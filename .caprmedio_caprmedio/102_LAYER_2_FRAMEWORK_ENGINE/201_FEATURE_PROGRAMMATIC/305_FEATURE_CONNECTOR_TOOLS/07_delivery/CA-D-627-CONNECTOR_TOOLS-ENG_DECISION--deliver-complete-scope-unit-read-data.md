---
atom_id: CA-D-627
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
relations:
  depends_on:
  - CA-D-625
tier: 3
---
# Summary

Deliver complete Scope Unit read data

## Scope

The operation-specific inner representation of one complete Scope Unit declaration Read, refining CA-D-625-CONNECTOR_TOOLS-ENG_DECISION--deliver-coherent-connector-interface.

## Claim

Scope Unit Read data **must** preserve the common closed interface **and** the logical target, complete declaration **and** exact source-state refinement below. a declared binding property is source data, **not** a public physical target **or** storage protocol.

## Details

### Request refinement

Keep exactly the seven common inner keys. Use `operation = "read"`, `target = {kind: "Scope Unit", identity}`, `query = null` and `delta = null`. Identity is the canonical Scope Unit Name string in the owning Project explicitly bound by context. The canonical Project Name selects its root; no extra ID, physical locator, obsolete-name alias or filename selects the target. A root/child name collision or duplicate declaration is ambiguous, not an invitation to choose.

Context and authorization bind the admitted Project, source view, declaration-schema authority and read permission. `expected_state = null` admits an unpinned current Read with no pre-known token. Otherwise expected_state is the exact existing source-state evidence binding to enforce. Historical selection is explicit in context and requires the exact available historical authority; no new history-retention guarantee or token protocol is introduced.

### Result refinement

Keep exactly `data`, `current_state`, `effects` and `errors`. Available `data = {identity, declaration}`. Declaration is the complete admitted non-Project source row under CA-D-442-CORE_META_MODEL--encode-scope-unit-declaration-fields, or the root's complete governing Project Settings `project` table under CA-R-1484-CORE_META_MODEL-RULE--establish-scope-units-through-project-structure-declarations. Preserve all applicable carried fields and absent optional fields. Root has no duplicate Project Structure row. This reads the one declaration, not the full surrounding configuration, descendants, owned Atoms or folder contents.

`current_state` carries actual bound Project/source view and exact existing source-state evidence, not an invented Scope Unit Version. Current views use current authoritative evidence; pinned/historical views identify the exact requested evidence. Physical Carrier locators stay internal; declared `authority_path`/`delivery_path` values may be returned faithfully as properties of the declaration.

Use exactly the structured common error shape and vocabulary. Missing target is `target_not_found`; duplicate/colliding identity or ambiguous source resolution is `target_ambiguous`; invalid request is `input_invalid`; invalid declaration/schema is `schema_invalid`; stale expected evidence is `stale_state`; denied read permission is `permission_denied`; unavailable/inaccessible backend evidence is `backend_failure`; unsupported operation is `unsupported_operation`. Unavailable full declaration uses null data rather than invented or truncated full-read success. Normal Read has `effects = []`; unexpected actual or unknown effects retain common truthful evidence and fail, including `effect_uncertain` when unknown. Empty errors require verified complete data and state evidence.

CA-O-212-CONNECTOR_TOOLS-ACTION--read-one-complete-scope-unit-declaration is the source operation binding. This representation adds no CLI/MCP/HTTP route, duplicate outer service envelope, database implementation, alias policy, retry/resume or publication mechanism. Current implementation and independent source acceptance remain separate.
