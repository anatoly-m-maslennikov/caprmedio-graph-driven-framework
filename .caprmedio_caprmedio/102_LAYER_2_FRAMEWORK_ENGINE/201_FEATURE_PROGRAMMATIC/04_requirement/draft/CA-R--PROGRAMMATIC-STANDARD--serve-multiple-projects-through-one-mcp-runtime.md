---
content_role: Requirement
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
updated_at: "2026-10-20 02:54:04 +0400"
relations: {}
---
# Summary

Serve multiple Projects through one MCP runtime

## Scope

One running standalone Docker container and one MCP endpoint serving multiple explicitly bound Projects.

## Claim

The shared runtime shall serve each operation under exactly one retained Project binding without conflating Project identity, applicable methodology/model, mutable state or effects. The caller's current directory shall be an explicit input to the binding contract where that routing mode is used; knowledge of a directory elsewhere in Codex is not an MCP input by itself. A binding shall retain the authoritative Project prefix together with the validated Project instance/root/control-root identity. Prefix identity and path authority shall be checked rather than treated only as a namespace string. A prefix-only selector is usable only when it resolves unambiguously to the retained full Project identity; a duplicate-prefix policy cannot authorize ambiguous routing.

## Details

Only roots made accessible to the container and admitted by its Project registration/configuration contract may be selected. Resolve missing, stale, inconsistent or ambiguous selectors with an attributable refusal or explicit selection request, never silent fallback to another Project. Configuration/model generations, applicable source/tool bindings, indices/caches, locks, workflow/Run state, receipts, Journal/output locations and results shall be scoped to the retained Project binding. Existing lifecycle admission, authorization and uncertain-effect recovery remain applicable after routing. One-container hosting grants no additional cross-Project authority. Request-bound versus session-bound routing, duplicate-prefix admission and adding/removing host mounts remain explicit design choices.
