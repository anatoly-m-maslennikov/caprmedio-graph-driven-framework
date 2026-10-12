---
atom_id: CA-O-204
content_role: Operations
type: Action
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool"
  depends_on: ["Tool","Project Configuration","Property","Action"]
version: 1
updated_at: "2026-10-12 23:17:22 +0400"
relations:
  relates_to: [CA-R-1935, CA-M-375, CA-O-205, CA-O-206, CA-R-1143, CA-D-441]
---
# Summary

Patch one TOML configuration

## Operation

Patch One TOML Configuration **means** the one shared TOML Action used by the distinct Project Structure and Project Settings Workflows. Public selection is an explicitly authorized logical configuration identity and key patch; private storage resolution is not another connector.

### Action

1. bind exactly one selected logical configuration, explicit add/replace/remove key operation and current values where required, its source pin, actual declared schema version, current applicable schema/authority and exact permission from its receiving Workflow. Reject mixed configurations, unknown targets, malformed operations, stale pins or missing/ambiguous authority before effects.
2. resolve the private exact authoritative TOML target. Parse without normalizing unrelated values; reject duplicate keys, unknown/disallowed schema fields and unsupported declared versions. Validate both complete source and proposed result against the selected configuration's actual declared schema and current authority before writing. Do not invent a schema file or accept a permissive fallback.
3. preserve all unrelated values and protected/generated settings under CA-R-1143. Expose the exact mutation-free effective diff; a no-op changes no bytes or metadata. Do not update projection/runtime manifests, perform Atom replacement or delete Atoms as an inferred TOML effect.
4. only after the configuration-specific Workflow's current checks and an admitted exact permission, recheck source/schema/authority pins and safely write this one configuration. Independently read back exact bytes, effective values and complete schema conformance.
5. report prepared, rejected, applied, failed, partial or unknown only from actual evidence. Within-Action recovery remains scoped to its verified mutable frontier; preserve unrelated configuration and accepted Run evidence. Failed recording does not authorize replay.

## Details

O205 and O206 reuse this same Action with different fixed private targets and schema/authority selection. Their configuration-specific validations do not create separate connectors. This definition neither chooses a new retry/resume policy nor claims a runnable TOML route.

These are normative source definitions, not executable bindings or live admission. Before any actual Run, resolve and independently verify the selected realization, current definition pins, applicable permissions and shared Run recording under CA-R-1525/CA-R-1720. Missing, stale, unsupported or incompatible bindings stop before dispatch. No new retry/resume decision, MCP activation, runtime manifest change, Core adoption or Subject publication is authorized.
