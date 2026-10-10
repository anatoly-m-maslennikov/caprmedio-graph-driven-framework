---
content_role: Delivery
type: Delivery
current_scope_unit: MCP
claim_target_scope_unit: MCP
local_tier: Standard
author: Anatoly Maslennikov
status: Draft
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "MCP/adapter declaration Carrier"
  depends_on:
    - "Atom/Content Role: Implementation"
    - "Carrier"
    - "Tool"
version: 2
updated_at: "2026-10-11 01:16:51 +0400"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"delivery_for": ["CA-R-1116"], "relates_to": ["CA-D-049", "CA-M-159", "CA-M-166", "CA-R-1111", "CA-R-1117", "CA-R-1118", "CA-R-1119"]}
---
# Summary

Publish versioned MCP adapter declarations

## Claim

an MCP adapter delivered within FRAMEWORK_ENGINE **must** carry a version-bound interface declaration at its declared MCP Delivery location. It consumes the transport-neutral Tool description from `CA-R-1930-TOOLS-CORE-REQUIREMENT--require-uniform-tool-self-description` without duplicating Tool authority.

- consume the exact Tool self-description defined by `CA-D-621-TOOLS-DELIVERY--encode-uniform-tool-self-description`; the adapter adds no duplicate literal descriptor schema. Model symbols remain the sole schema source and the adapter accepts no caller-provided descriptor schema.
- project each valid descriptor through one uniform provider invoke wrapper; the wrapper adds MCP protocol representation and diagnostics only. Effect hints are non-authorizing behavior metadata. Missing, stale, or incoherent descriptor fields make only that projection unavailable with attributable diagnostics.
- identify the supported protocol revision **and** admitted capability declarations owned by CA-R-1116; do **not** select another protocol revision here. Registration, schema derivation, projection, and refresh do not invoke a Tool, start a Workflow, infer approval, or cause an effect.
- represent admitted progress, cancellation, correlation, and resource-bound fields according to CA-R-1117 and preserve result meanings under CA-R-1119. Credentials **must not** be embedded in the declaration, generated schemas, or published examples.

CA-D-049 owns the MCP Delivery binding; the version-bound declaration belongs **to** that adapter distribution rather than an independent FRAMEWORK_ENGINE-wide interface authority.
