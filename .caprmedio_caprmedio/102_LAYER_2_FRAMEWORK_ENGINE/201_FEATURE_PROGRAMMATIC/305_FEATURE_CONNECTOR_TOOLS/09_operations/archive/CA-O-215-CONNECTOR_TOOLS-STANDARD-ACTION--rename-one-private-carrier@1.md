---
atom_id: CA-O-215
content_role: Operations
type: Action
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool"
  depends_on: ["Artifact/Carrier","Action","Workflow","Atom","Operator"]
version: 1
updated_at: "2026-10-13 01:46:23 +0400"
relations:
  relates_to: [CA-R-1941, CA-M-381, CA-E-633, CA-D-630, CA-D-625, CA-R-1093]
---
# Summary

Rename one private carrier

## Operation

Rename One Private Carrier **means** the reusable private Action that realizes one explicitly bound same-parent file/folder name change behind an admitted logical connector `modify`, without choosing semantic identity or rewriting references.

### Inputs and preconditions

Require CA-D-630's exact private rename binding, current source and parent evidence, one explicit destination name with expected absence for an actual name change, sealed permission/context and a complete approved inventory for a folder. CA-R-1941 and CA-M-381 apply. A root/ancestor, escape, symlink, substitution, stale state, collision, overwrite, merge or unapproved entry blocks the Action.

### Action and result

Recheck the bound source/parent/destination and inventory before the permitted storage effect. Perform only the supplied same-parent name change. Independently verify the exact destination, old source absence and preserved contents/modes/inventory/unrelated frontier, then return CA-D-625's common result with actual evidence.

A same-binding request is a no-op only when requested state is verified already satisfied and unchanged. Failure retains known partial effects; unknown effects require `effect_uncertain`, and nonempty errors are never success. No automatic retry, rollback promise or reference discovery/rewrite is implied.

## Details

This is not O040's generic Artifact rename with canonical-reference rewrites. Domain identity, Version, lifecycle and required history remain owned by the admitting Workflow; this Action cannot complete them by storage rename alone. No executable or runtime admission is established.
