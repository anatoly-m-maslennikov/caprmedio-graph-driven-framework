---
content_role: Delivery
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Draft
subjects:
  governs: PROGRAMMATIC
  depends_on: []
version: 1
updated_at: "2026-10-20 02:56:03 +0400"
relations: {}
---
# Summary

Deliver the multi-Project MCP binding contract

## Scope

The shared runtime's client/server selection contract, Project registration/mount configuration and attributable operational records.

## Claim

Deliver the selected request-bound or session-bound binding contract, its schema/version, supported client context fields, authoritative Project identity/prefix/root/control-root references and host-to-container mappings and their retained registration/mapping revisions. Deliver one-container/one-endpoint configuration plus the Project-scoped state ownership/keying and lifecycle/reload behavior. Binding and diagnostics shall show which Project and source/model generations an operation used without turning the record into source authority.

## Details

State selector precedence, ambiguity and duplicate-prefix behavior, current-directory/context-assertion/rebind semantics including what the server cannot observe without client transmission, qualified record lookup, admitted paths/mounts, adding/removing Projects, shared-resource limits and how receipts/results/Journal writes remain attributable. Include reproducible two-Project acceptance evidence when implementation is authorized, with no stronger isolation claim than demonstrated. The design must not rely on an untransmitted Codex working directory, container-global working directory or prefix-only namespace. Existing per-Project runtime behavior remains the baseline until a separately authorized implementation replaces it. This Draft delivers no deployment, activation or modified MCP tool schema.
