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
version: 4
updated_at: "2026-10-13 23:51:12 +0400"
relations:
  depends_on: [CA-R-1941, CA-M-381, CA-D-630, CA-D-625]
---
# Summary

Move one private carrier

## Operation

Move One Private Carrier **means** the reusable private Action that realizes one explicitly bound file/folder location change behind an admitted logical connector `modify`, preserving the exact admitted carrier frontier **without** choosing a lifecycle transition.

### Inputs **and** preconditions

require CA-D-630's private move binding, approved source/destination roots **and** parents, expected source state, explicit destination **and** expected absence for an actual move, sealed permission/context **and** complete approved folder inventory. **any** basename change **must** already be explicit. for an Atom carrier, require the already admitted exact lifecycle/currentness/history context; no helper permission substitutes for it.

### Action **and** result

require CA-R-1941's exact staged-change review **and** fresh trusted authorization/window record, including recorded outside-edits-paused confirmation. within that confirmed window, acquire the existing shared Engine lock, apply CA-R-1941/CA-M-381 safety checks **and** recheck the complete bound source, destination, parents, inventory, preservation, authority **and** permission frontier **before** the effect; retain the lock through independent readback **and** verification. perform **only** the explicitly bound location change. reject root/ancestor effects, escapes, symlinks/substitution, stale state, collisions, overwrite, merging **and** unlisted entries. verify destination contents/modes/inventory, source absence **and** unchanged unrelated frontier independently.

return CA-D-625's actual data/state/effects/errors. a same-binding no-op needs verified unchanged requested state; missing expected-present source does **not** prove an earlier move. retain known partial effects **and** mark uncertainty with `effect_uncertain`; errors are **not** success. no new transaction, retry, resume **or** concurrent-publication guarantee is implied.

## Details

Archive, retire, upgrade, replacement, identity/Version metadata and history remain owned by their existing admitted operation. This Action supplies only internal carrier movement and never reports lifecycle completion or rewrites references. No executable or runtime admission is established.
