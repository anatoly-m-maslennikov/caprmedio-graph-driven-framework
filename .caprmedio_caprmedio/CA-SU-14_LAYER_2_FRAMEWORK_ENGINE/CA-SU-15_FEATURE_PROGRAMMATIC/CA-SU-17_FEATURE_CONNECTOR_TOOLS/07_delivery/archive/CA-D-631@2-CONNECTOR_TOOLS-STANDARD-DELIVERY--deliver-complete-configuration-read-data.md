---
atom_id: CA-D-631@2
content_role: Delivery
type: Delivery
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-13 02:50:00 +0400"
subjects:
  governs: "Tool"
  depends_on: ["Project", "Project Structure", "Project Settings", "Workflow"]
relations:
  relates_to: [CA-R-1942, CA-M-382, CA-E-634, CA-O-218, CA-R-1936, CA-M-376, CA-D-625, CA-O-204, CA-M-375]
---
# Summary

Deliver complete configuration read data

## Scope

the Configuration Read refinement of CA-D-625's closed logical interface.

## Claim

Configuration Read **must** use the common request/result keys **and** the complete source representation below. CA-O-218 is its source Action binding on the same shared TOML connector as CA-O-204; separate Actions do **not** create separate connectors.

## Details

### Request refinement

keep exactly `operation`, `target`, `query`, `delta`, `expected_state`, `authorization` **and** `context`. use `operation = "read"`, `target = {kind: "Configuration", identity}`, `query = null` **and** `delta = null`. identity is exactly `Project Structure` **or** `Project Settings` **in** the Project bound by context. a filename, path **or** backend key is **not** a logical identity.

context binds the admitted Project, source view, exact source-authority **and** applicable schema definitions, including declared schema-version constraints. authorization binds read permission for that complete source. the caller selects these bindings; the connector checks them. `expected_state = null` selects an unpinned current Read. a non-null value enforces the supplied exact existing source-state evidence. historical selection is explicit **in** context **and** requires available exact historical source/schema authority; it creates no retention policy.

### Result refinement

keep exactly `data`, `current_state`, `effects` **and** `errors`. successful `data = {identity, source_text, document}` carries complete unchanged UTF-8 TOML text **and** its complete parsed values, including unrelated tables **and** present optional values. preserve source text exactly; do **not** synthesize absent optional fields. the admitted TOML value representation remains that of the existing connector binding; it **must** preserve value types **and** reject a lossy representation rather than stringify typed values silently.

`current_state` carries the logical configuration identity, bound Project/source view **and** exact observed source-state evidence used by the existing common contract. it identifies the same source bytes as `source_text` **and** `document`; no Atom Version is invented for configuration. a subsequent Modify uses this observed evidence as expected current state **and** rechecks it, rather than trusting a prior Read as permission **to** write.

normal Read has `effects = []`. missing source uses `target_not_found`; ambiguous target/source resolution uses `target_ambiguous`; invalid request uses `input_invalid`; malformed TOML, invalid complete schema **or** invalid schema binding uses `schema_invalid`; mismatched evidence uses `stale_state`; denied permission uses `permission_denied`; unavailable historical/backend evidence uses `backend_failure`; unsupported operation uses `unsupported_operation`. retain CA-D-625's exact `{code, message, field}` error shape. unavailable complete data is null, **not** an empty successful document. nonempty errors never mean success; empty errors require verified complete data **and** exact matching state evidence. unexpected actual effects fail Read acceptance **and** remain truthfully reported; unknown effects require `effect_uncertain`.

reuse CA-D-527's existing outer envelope **and** recording rules. this source definition does **not** prove implementation, route admission, installed availability, a new history store **or** stronger publication safety.
