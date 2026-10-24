---
atom_id: CA-O-215@6
content_role: Operations
type: Action
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Engineering/Private Carrier Rename Operation
  depends_on:
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/Workflow
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Actor
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
version: 6
updated_at: 2026-10-23 01:47:30 +0400
relations:
  depends_on:
  - CA-R-1941
  - CA-M-381
  - CA-D-630
  - CA-D-625
---
# Summary

Rename one private carrier

## Operation

Rename One Private Carrier **means** the reusable private Action that realizes one explicitly bound same-parent file/folder name change behind an admitted logical connector `modify`, **without** choosing semantic identity **or** rewriting references.

### Inputs **and** preconditions

require CA-D-630's exact private rename binding, current source **and** parent evidence, one explicit destination name with expected absence for an actual name change, sealed permission/context **and** a complete approved inventory for a folder. CA-R-1941 **and** CA-M-381 apply. a root/ancestor, escape, symlink, substitution, stale state, collision, overwrite, merge **or** unapproved entry blocks the Action.

### Action **and** result

require CA-R-1941's exact staged-change review **and** fresh trusted authorization/window record, including recorded outside-edits-paused confirmation. within that confirmed window, recheck the complete bound source/parent/destination, inventory, preservation, authority **and** permission frontier **before** the permitted storage effect. retain independent readback **and** verification. perform **only** the supplied same-parent name change. independently verify the exact destination, old source absence **and** preserved contents/modes/inventory/unrelated frontier, **then** return CA-D-625's common result with actual evidence.

a same-binding request is a no-op **only** **when** requested state is verified already satisfied **and** unchanged. failure retains known partial effects; unknown effects require `effect_uncertain`, **and** nonempty errors are never success. no automatic retry, rollback promise **or** reference discovery/rewrite is implied.

## Details

This is not O040's generic Artifact rename with canonical-reference rewrites. Domain identity, Version, lifecycle and required history remain owned by the admitting Workflow; this Action cannot complete them by storage rename alone. No executable or runtime admission is established.
