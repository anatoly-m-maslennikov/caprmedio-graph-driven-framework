---
subjects:
  governs: "Entity/Continuant/Object/Project.Settings"
  depends_on:
    ["Entity/Continuant/Object/Project", "Entity/Continuant/Object/Project.Settings.Atom Prefix", "Entity/Continuant/Object/Project.Framework Settings", "Entity/Continuant/Projection"]
version: 13
updated_at: "2026-10-15 18:51:34 +0000"
relations:
  child_of:
    - CA-D-364
atom_id: "CA-D-366"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-366-CORE_META_MODEL--serialize-project-settings-content-in-toml.md
  source_atom_id: CA-D-366
  source_atom_revision: 13
  source_sha256: 332bcfd6b54054e2f28df0121adc7f3afb65341166a77f1eb138dbe7a1d2fc21
  original_relations_sha256: 1362486b734d90918b1d2949ab26e315125674e562b6b82d60abc7b3350f9e84
---
# Summary

Serialize Project Settings Content in TOML

## Scope

the Project Settings TOML Carrier.

## Claim

the Project Settings TOML Carrier **must** encode Operator-editable Project initialization inputs through sections **and** fields specified by Standard-tier Atoms under its Core content **and** authority boundaries **and** applicable General settings specifications; it **must not** store Framework Instance choices **or** authoritative Project Structure declarations **or** derived structural values as independently editable settings.

## Details

- the supported current schema **must** use the TOML string `schema_version = "2.0"`. its complete root **must** contain **only** the required `schema_version`, `project`, `artifacts`, **and** `paths` keys **and** optional `project_mcp`.
- `project` **must** be a table containing required `name` **and** optional `obsolete_names`, **and no** other keys. `project.name` **must** be a nonempty TOML string containing the exact lowercase Operator-selected Project Name under CA-D-375.
- **if** present, `project.obsolete_names` **must** be a TOML array of nonempty strings containing the exact registered prior names. an empty array is permitted; absence **and** an empty array **must** remain distinct. preserve their exact values **and** order; do **not** trim, normalize, deduplicate, exclude the canonical name, **or** invent missing prior names. CA-D-392 continues to govern their Projection exposure, **not** this input signature.
- `artifacts` **must** be a table containing **only** the required `identity` table; `artifacts.identity` **must** contain **only** required `project_prefix`. `artifacts.identity.project_prefix` **must** be a nonempty TOML string containing the exact uppercase Operator-selected Atom prefix under CA-D-376 **and** CA-D-378.
- `paths` **must** be a table containing **only** required `control_root`. `paths.control_root` **must** be the TOML string `.caprmedio_<project.name>`, identifying that selected Project's direct-child control root under CA-D-364 **and** CA-D-520; it **must not** override the selected Project **or** declare independently editable Structure.
- **if** present, `project_mcp` **must** be a table containing **only** required `http_port` **and** optional `tool_blacklist`. the selected Project's fixed MCP HTTP port remains governed by CA-D-594. `project_mcp.http_port` **must** be an exact TOML integer, **not** a boolean, **in** `1..65535`. absence of `project_mcp` is permitted for ordinary Settings Read; MCP launch **or** reuse still requires its configured port under CA-D-594.
- **if** present, `project_mcp.tool_blacklist` **must** be a TOML array of nonempty strings naming exact MCP tools whose exposure is disabled for this Project. preserve exact values **and** order without trimming, normalization, deduplication, wildcard matching **or** implicit names. an empty array is permitted; absence **and** an empty array **must** remain distinct when reading **and** serializing, while both mean no blocked tools. a listed tool **must** be absent from discovery **and** refused on invocation before its handler runs; retain its implementation **and** binding for later reuse. this setting controls MCP exposure only **and** does not remove host invocation **or** grant execution authority. no release-specific default is part of this schema.
- validation **must** cover the complete document **and** reject missing required keys, unknown keys **or** sections at **any** level, wrong TOML value types, duplicate TOML keys, unsupported markers, **or** values violating the requirements above. no legacy compatibility section, open extension field, coercion, default, fallback, automatic case conversion, repair, **or** migration is admitted. rejection **must not** authorize changing **or** deleting the existing Carrier.
