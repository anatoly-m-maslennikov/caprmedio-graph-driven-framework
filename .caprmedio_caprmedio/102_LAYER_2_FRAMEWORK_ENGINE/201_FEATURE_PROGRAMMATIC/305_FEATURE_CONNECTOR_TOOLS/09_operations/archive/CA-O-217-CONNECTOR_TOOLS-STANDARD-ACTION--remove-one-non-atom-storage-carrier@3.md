---
atom_id: CA-O-217
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
version: 3
updated_at: "2026-10-13 23:27:54 +0400"
relations:
  relates_to: [CA-R-1941, CA-M-381, CA-E-633, CA-D-630, CA-D-625, CA-R-1093]
---
# Summary

Remove one non-Atom storage carrier

## Operation

Remove One Non-Atom Storage Carrier **means** the reusable private cleanup Action that removes exactly one explicitly approved non-Atom file **or** empty folder behind an admitted logical connector `modify`. it is **not** an Atom deletion **or** a recursively selected cleanup set.

### Inputs **and** preconditions

require CA-D-630's private remove binding, approved root/parent, exact expected state, positive non-Atom cleanup eligibility **and** explicit permission/context. reject a root/ancestor, escape, symlink/substitution, nonempty folder, current **or** historical Atom carrier, required history, protected source, missing eligibility **or** stale/ambiguous state. do **not** treat an unrecognized **or** absent ID as non-Atom proof.

### Action **and** result

require CA-R-1941's exact staged-cleanup review **and** fresh trusted authorization/window record, including recorded outside-edits-paused confirmation. within that confirmed window, acquire the existing shared Engine lock **and** recheck the exact positive non-Atom eligibility, classification, root/parent, source state, empty-folder evidence, preservation, authority **and** permission frontier **before** the effect; retain the lock through independent readback **and** verification. remove **only** that bound file **or** empty folder; never discover child targets, follow a symlink, accept a wildcard/recursive flag **or** touch a destination, referrer **or** unrelated carrier. independently verify observed absence **and** the unchanged preservation frontier.

return CA-D-625's actual data/current_state/effects/errors. a bound already-absent cleanup state is a no-op **only** **when** absence was explicitly expected, eligibility/permission remains valid **and** unchanged requested state is independently verified. missing expected-present source is a failure, **not** inferred completion. retain known partial effects; unknown effects require `effect_uncertain` **and** errors cannot indicate success.

## Details

Atom removal remains the existing admitted Archive/retire lifecycle with required history; O217 supplies no delete-Atom operation. No automatic set expansion, recovery/retry/resume policy, implementation or runtime route is established.
