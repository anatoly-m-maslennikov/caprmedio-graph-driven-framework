---
atom_id: CA-O-216
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

Move one private carrier

## Operation

Move One Private Carrier **means** the reusable private Action that realizes one explicitly bound file/folder location change behind an admitted logical connector `modify`, preserving the exact admitted carrier frontier without choosing a lifecycle transition.

### Inputs and preconditions

Require CA-D-630's private move binding, approved source/destination roots and parents, expected source state, explicit destination and expected absence for an actual move, sealed permission/context and complete approved folder inventory. Any basename change must already be explicit. For an Atom carrier, require the already admitted exact lifecycle/currentness/history context; no helper permission substitutes for it.

### Action and result

Apply CA-R-1941/CA-M-381 safety checks and recheck the exact source, destination, parents and inventory before the effect. Perform only the explicitly bound location change. Reject root/ancestor effects, escapes, symlinks/substitution, stale state, collisions, overwrite, merging and unlisted entries. Verify destination contents/modes/inventory, source absence and unchanged unrelated frontier independently.

Return CA-D-625's actual data/state/effects/errors. A same-binding no-op needs verified unchanged requested state; missing expected-present source does not prove an earlier move. Retain known partial effects and mark uncertainty with `effect_uncertain`; errors are not success. No new transaction, retry, resume or concurrent-publication guarantee is implied.

## Details

Archive, retire, upgrade, replacement, identity/Version metadata and history remain owned by their existing admitted operation. This Action supplies only internal carrier movement and never reports lifecycle completion or rewrites references. No executable or runtime admission is established.
