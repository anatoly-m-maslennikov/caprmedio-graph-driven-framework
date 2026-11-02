---
atom_id: CA-O-204@4
content_role: Operations
type: Action
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Engineering/TOML Configuration Modify Operation
  depends_on:
  - Subject/Domain/Node/Continuant/Governing Configuration
  - Subject/Engineering/TOML Configuration Field
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
version: 4
updated_at: 2026-10-23 01:47:30 +0400
relations:
  relates_to:
  - CA-R-1936
  - CA-M-376
  - CA-D-625
  - CA-O-205
  - CA-O-206
  - CA-O-218
  - CA-D-631
---
# Summary

Patch one TOML configuration

## Operation

Patch One TOML Configuration **means** the mechanical TOML `modify` Action through the common connector interface in CA-D-625, CA-R-1936 and CA-M-376. The caller supplies exactly one logical configuration target, its explicit delta, expected_state, authorization/context and selected validation constraints. Storage is private; the connector does not choose a configuration, schema, authority or workflow policy.

Use D625's closed inner request keys `operation`, `target`, `query`, `delta`, `expected_state`, `authorization` and `context`. Exactly one of target or query is non-null; target is `{kind, identity}`, query is `{kind, filters}`. Query/read use null delta; modify receives explicit supplied edits. Modify requires expected current state; Create requires expected absence. An ordinary explicit-ID Read returns its actual exact Version/state token without requiring a pre-known Version; optional pinned/historical Read Version and expected_state must match exactly. Do not invent a Scope Unit Version. Authorization/context reference already bound permission, source and schema evidence, never a new outer protocol or flags. Return only the common result keys `data`, `current_state`, `effects` and `errors`, with precise code/message/field errors and truthful known or unknown effects.

### Action

1. check the common request and its exact explicit target/delta/preconditions/permission. Receiving O205 or O206 owns the configuration-specific target, actual declared schema selection, authority, allowed/protected fields and authorization decision. Require that complete supplied evidence; missing, stale, ambiguous or unsupported evidence returns a structured error before effects.
2. mechanically resolve only the supplied logical target to its private authoritative TOML Carrier. Parse with duplicate-key rejection and check complete source and proposed result against the explicitly supplied schema, declared-version constraints and current authority pins before writing. Never infer a permissive schema or select a fallback configuration.
3. apply only the supplied explicit key add/replace/remove delta and enforce its supplied allowed/protected/generated-field constraints. Preserve every unrelated value and expose the exact effective diff. No-op changes no bytes. Do not decide Atom identity, Version, Status, lifecycle, replacement, reference retargeting or projection/runtime activation.
4. recheck expected_state, supplied schema/authority pins and permission immediately before the safe one-target effect. Independently read back exact bytes, effective values and complete supplied-schema conformance. Retain within-Action safe effects/recovery and truthful partial or unknown results; accepted Run evidence is not discarded.
5. return D625's data/current_state/effects/errors result with exact observed values, actual delta/effects or no-effect evidence, and precise failed checks. A recording blocker does not authorize replay; retry/resume policy is not chosen here.

## Details

CA-O-218 is the separate complete Read Action of this same TOML connector under CA-D-631; this Action remains Modify-only. CA-O-205 **and** CA-O-206 supply different configuration-specific bindings; they are **not** separate connectors. D625 is the common logical inner contract, not a new transport, and D527's outer envelope remains unchanged.

No executable binding or runtime admission is created. Current independently verified realization, definition/source pins, permission and shared Run recording remain required. This source move neither edits either configuration nor activates MCP, Core migration or Subject publication.
