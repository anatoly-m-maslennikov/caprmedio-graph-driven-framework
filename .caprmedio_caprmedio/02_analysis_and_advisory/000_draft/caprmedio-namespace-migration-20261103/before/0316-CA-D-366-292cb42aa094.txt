---
subjects:
  active: Project.Settings
  passive:
  - Project
  - Project.Settings.Name
  - Project.Settings.Prefix
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - Projection
version: 30
updated_at: 2026-11-02 19:46:47 +0400
relations:
  child_of:
  - CA-D-364
atom_id: CA-D-366
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 6
role: Delivery
form: Decision
---
## Summary

Serialize Project Settings Content in TOML

## Claim scope

the Project Settings TOML Carrier.

## Claim

the Project Settings TOML Carrier **must** encode Operator-editable Project initialization inputs through sections **and** fields specified by concrete settings-specification Atoms under its foundational content **and** authority boundaries **and** applicable shared settings specifications; it **must not** store Framework Instance choices **or** authoritative Project Structure declarations **or** derived structural values as independently editable settings.

## Details

- the supported current schema **must** use the TOML string `schema_version = "2.0"`. its complete root **must** contain **only** the required `schema_version`, `project`, `artifacts`, **and** `paths` keys **and** optional `project_mcp`.
- `project` **must** be a table containing required `name` **and** optional `obsolete_names`, **and no** other keys. `project.name` **must** be a nonempty TOML string containing the exact lowercase Operator-selected Project Name under CA-D-375.
- **if** present, `project.obsolete_names` **must** be a TOML array of nonempty strings containing the exact registered prior names. an empty array is permitted; absence **and** an empty array **must** remain distinct. preserve their exact values **and** order; do **not** trim, normalize, deduplicate, exclude the canonical name, **or** invent missing prior names. CA-D-392 continues to govern their Projection exposure, **not** this input signature.
- `artifacts` **must** be a table containing **only** the required `identity` table; `artifacts.identity` **must** contain **only** required `project_prefix`. `artifacts.identity.project_prefix` **must** be a nonempty TOML string containing the exact uppercase Operator-selected Project Prefix under the pending [Project Prefix Decision](CA-D-draft-CORE_META_MODEL-DECISION--serialize-project-prefix.md) **and** CA-D-378.
- `paths` **must** be a table containing **only** required `control_root`. `paths.control_root` **must** be the TOML string `.caprmedio_<project.name>`, identifying that selected Project's direct-child control root under CA-D-364 **and** CA-D-520; it **must not** override the selected Project **or** declare independently editable Structure.
- **if** present, `project_mcp` **must** be a table containing **only** required `http_port` **and** optional `tool_blacklist`. the selected Project's fixed MCP HTTP port remains governed by CA-D-594. `project_mcp.http_port` **must** be an exact TOML integer, **not** a boolean, **in** `1..65535`. absence of `project_mcp` is permitted for ordinary Settings Read; MCP launch **or** reuse still requires its configured port under CA-D-594.
- **if** present, `project_mcp.tool_blacklist` **must** be a TOML array of nonempty strings naming exact MCP tools whose exposure is disabled for this Project. preserve exact values **and** order without trimming, normalization, deduplication, wildcard matching **or** implicit names. an empty array is permitted; absence **and** an empty array **must** remain distinct when reading **and** serializing, while both mean no blocked tools. a listed tool **must** be absent from discovery **and** refused on invocation before its handler runs; retain its implementation **and** binding for later reuse. this setting controls MCP exposure only **and** does not remove host invocation **or** grant execution authority. no release-specific default is part of this schema.
- validation **must** cover the complete document **and** reject missing required keys, unknown keys **or** sections at **any** level, wrong TOML value types, duplicate TOML keys, unsupported markers, **or** values violating the requirements above. no legacy compatibility section, open extension field, coercion, default, fallback, automatic case conversion, repair, **or** migration is admitted. rejection **must not** authorize changing **or** deleting the existing Carrier.

### Current source provenance

Current source: `.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-366-CORE_META_MODEL-ENG_DECISION--serialize-project-settings-content-in-toml.md`, CA-D-366@27, SHA-256 `d73dc39767cf56a414f98ea098b2130ec0029cc0287500c8d4fa0e5347d6e4c3`.

The superseded prefix authority remains historical provenance only: `.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-376-CORE_META_MODEL-ENG_DECISION--serialize-the-project-atom-prefix.md`, CA-D-376@25, SHA-256 `3b04a0bd6dfce9eec731a550edcdd86c6fdba8560255477bd4810f3c254bd614`. The pending Project Prefix Decision is a Draft dependency, not Current admission.
