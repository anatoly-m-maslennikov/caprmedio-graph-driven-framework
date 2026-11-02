---
atom_id: CA-O-031@8
content_role: Operations
type: Action
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Validate And Describe Atom Replacement
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Continuant/Atom
  - Atom/Identifier
  - Atom/Revision
  - Subject/Domain/Node/Continuant/History/Journal.Record
version: 8
updated_at: 2026-10-23 03:14:50 +0400
relations: {}
---
# Summary

Validate and describe one Atom replacement

## Operation

Validate And Describe Atom Replacement **means** the reusable Action that validates and seals one explicit predecessor-to-successor-set intent under CA-R-1041. It owns neither creation nor reference editing; separate independently admitted Atom Actions supply actual successor creation and predecessor archival evidence.

### Action

1. bind one exact predecessor Atom ID and Version and the explicitly supplied distinct successor IDs, Versions and current source evidence. Validate identity/lineage classification and complete content under applicable authority. Reject missing, ambiguous, stale, duplicate or self-referential identities.
2. any Summary-value change, including wording-only, requires a fresh successor Atom ID and predecessor archival; Type-change replacement remains required. Never perform that change as a same-ID edit or infer successor content/identity.
3. return the complete mutation-free replacement description. If predecessor 100 is replaced by 200, preserve the distinct roles: successor creation targets 200 and predecessor archival targets 100. A prepared intent does not claim either effect occurred.
4. accept effect delegation only through the existing admitted Project-local lifecycle route and exact current permission. Verify actual successor activation before the one predecessor archival transition under the applicable CA-R-807 lifecycle authority. The prospective Engine contract preserves exact prior N bytes and gives an actual same-ID predecessor archival Status change Version N+1 and actual Project-time updated_at. CA-O-051's older Version-preserving binding is not an admitted realization of that changed contract; keep effect delegation gated until a compatible independently verified binding exists, without editing Core here. Do not combine a list of replacement mappings into a cross-Atom rollback boundary or roll back independently successful successor creation after a later failure.
5. preserve actual predecessor/successor evidence and governed lineage/Journal recording. Keep replacement history out of Atom frontmatter. No automatic inbound-reference retargeting, Relation invention or implicit Find/Modify Workflow is admitted; requested reference work uses independent explicit-target O201/O202 receiving uses.
6. report prepared, rejected, deferred, applied, failed, partial or unknown only from actual evidence. Creation and archival results retain their respective actual target IDs, not a rewritten alias for the predecessor. Existing recording/intake recovery preserves actual effects and never replays a performed Action.

### Batch and stop boundary

A requested batch is an ordered list of independently authorized Atom Actions. Invoke one Action at a time; advance to the next distinct explicit Atom only after confirmed success. On the first failure, stop, retain all earlier successful effects and their evidence, and leave the remaining targets untouched. Never roll back earlier successful Atoms to simulate a cross-Atom transaction. Validation, stale-source checks, permissions, safe effects and recovery within the failing Atom Action remain required. Automatic retry or resume of this new batch policy is deferred; existing recording-only recovery must not replay a performed Action.

REPLACE_ATOM does not independently append the Journal, create a Git Commit, create a successor or implement archival. Existing COMMIT_TRIGGER intake acknowledgment remains distinct from actual replacement and complete Run recording; absent required intake or recording remains a blocker.

## Details

Bind each actual standalone **or** nested Action Run **to** the shared every-Run contract in CA-P-1117 v3, Done CA-P-1443 J01–J08, independently reviewed by CA-P-1451: exact admitted definition Revision, actual Run identity/lineage, safe input/result/effect references, start, truthful terminal **or** still-pending interruption, **and** durable canonical Journal receipts under CA-R-1720. Workflow-contained bindings also follow CA-R-1525; standalone coverage is the selected Epic obligation, **not** a broadened applicability claim for that Requirement. Reuse the shared recording capability **without** owning another Journal implementation. Preserve accepted events **and** pending evidence; retry failed recording with the same Event identity/payload, **not** the performed Action. No receipt, intake acknowledgment, **or** Git Commit alone proves successful effects **or** complete Run recording.
