---
atom_id: CA-C-524@2
content_role: Concern
type: Problem
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: 2026-10-23 01:47:30 +0400
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.ID
  depends_on:
  - Atom
  - Subject/Engineering/Atom Identity/Concurrent Fresh-ID Allocation and Publication
  - Operator
relations:
  concern_about: [CA-P-2385, CA-P-2387, CA-P-2400]
  relates_to: [CA-A-1215, CA-C-523]
---
# Summary

Native concurrent promotions can duplicate a fresh Atom ID

## Concern

Removing retained Draft-history reservations exposed an ordinary native allocation/publication race. A controlled real two-thread probe let different ID-free Drafts both publish CA-R-1876 at different paths. This was a native regression; the currently serialized connected MCP queue did not demonstrate that race. Journal or retained-history prerequisites must not be restored to resolve it.

This Problem is authored directly in Resolved Status after the actual fix and checks; no prior Concern revision or historical state is invented.

## Evidences

The shared native identity guard uses the existing no-follow filesystem/flock mechanism in Project runtime state. It holds exclusion across fresh allocation and publication; ordinary native Create, direct fresh-identity publication, legacy CLI Create/Promote and explicit identity migration share that guard. Every ID-free promotion still allocates a fresh unused ID. Existing historical files remain identity-collision evidence, not admission permission or an old-ID restoration rule.

Independent review found and verified the repair of an interrupted-acquisition descriptor leak. Reentrancy, exception release and parent/final-lock symlink refusals were checked without weakening the actual mutation assertions.

Final native hashes: atom_operations.py 899dc4293c20156da0bafc88fbf30689888a19b5ff5f61602788cffdd2b77ac8; lifecycle_intents.py c82eb7591684b06aa9598a0c2737e1f6fbb2fb72e51d96b9d70c26b02701984d. All four real concurrency tests passed in disposable Linux in 4.268 seconds on image sha256:0fac136ec9661a8884cbdcf53e0b7da34f5bc24506b71b6d452bc934c8df80a3: different Drafts get distinct IDs; same-ID/different-path Creates publish only once; a child process waits behind the Project lock; interrupted lock acquisition closes its descriptor and preserves the original exception. The incomplete-Journal MCP journey also passed on this image.

## Blast radius

The native regression is resolved at the measured source revisions. No history state machine, Journal gate, restoration exception or host-specific retry was added. The independent host filesystem failures remain Active in CA-C-523; Linux success does not resolve that Problem. This Concern does not claim a full suite, installed-runtime activation, release, or repair of unrelated older Replacement coordination.
