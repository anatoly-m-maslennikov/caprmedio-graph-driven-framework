---
content_role: Method
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
updated_at: "2026-10-20 02:54:48 +0400"
relations: {}
---
# Summary

Bind the caller context and carry Project identity

## Scope

Request or connection/session selection and all dependent work within the shared MCP runtime.

## Claim

Obtain the current-directory/Project selector through the chosen client/server contract; resolve it against the admitted host-to-container root/control-root mapping and current Project identity/prefix declarations. Canonicalize and check paths using that contract, including aliases/symlinks and overlapping roots as relevant, require one unambiguous admitted registration and a retained host-root/control-root-to-container translation, then freeze that binding and its registration/mapping revision for the operation. Accessible mounts alone are not authorization. Load that Project's applicable sources, tool bindings, settings and effective-model generation through the existing admission rules.

## Details

In session-bound mode, supplied request context must resolve to the retained Project binding or be refused until explicit rebind; a directory change not transmitted by the client is not observable by the server. The supported client contract must transmit the change or a Project-context assertion, and may not imply automatic server detection. Carry the binding through tool execution, asynchronous continuation, nested calls, persisted receipts and result attribution. Derive Project-scoped state keys from the validated identity, not prefix text alone; share only resources whose sharing does not erase that identity. Resolve retained Run/receipt/result references under the full binding identity plus local record identity, and verify the retained binding before readback, recovery or continuation. Derive Project filesystem paths below the retained translated root/control-root and apply the declared alias/symlink escape checks; no process working directory supplies fallback. Validate each effect target within the bound Project's admitted boundary. A current-directory change shall produce a new request binding or an explicit session rebind; it shall not mutate another in-flight operation's binding. On selection failure return the condition without exposing another Project's private state. Registration shall not claim filesystem access absent a mount; any required container recreation for changed mounts shall be explicit and distinct from an image rebuild. At existing freshness/effect-admission boundaries, recheck registration/mapping identity as well as source/model freshness. Removal/remapping follows the chosen drain-with-retained-mapping or cancel-before-effects policy; no continuation may silently switch mappings. Use the declared reload/drain policy to manage removed Projects or changed source/model generations; do not invent ambient process-global `current_project` behavior.
