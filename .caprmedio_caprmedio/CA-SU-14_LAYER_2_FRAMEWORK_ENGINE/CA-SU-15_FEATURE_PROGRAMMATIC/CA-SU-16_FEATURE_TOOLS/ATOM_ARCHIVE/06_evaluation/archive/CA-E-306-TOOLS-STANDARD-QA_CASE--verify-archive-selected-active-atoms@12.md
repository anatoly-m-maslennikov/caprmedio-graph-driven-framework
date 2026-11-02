---
atom_id: CA-E-306
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool/ATOM_ARCHIVE"
  depends_on: ["Atom", "Atom/Revision", "Artifact/Carrier", "Archive Selected Active Atoms", "Journal/Record", "Atom/Revision/Status", "Atom/Revision/Updated At"]
version: 12
updated_at: "2026-10-12 23:13:13 +0400"
relations:
  evaluation_for: [CA-R-868, CA-O-029, CA-D-289, CA-D-303]
  relates_to: [CA-R-1521, CA-R-1788, CA-R-1662]
---
# Summary

Verify archive selected active atoms

## Scope

One admitted Atom Archive action under CA-R-868 and CA-O-029, its retained history and independent sequencing under CA-M-372.

## Claim

Archive withdraws one current Atom while preserving its identity and historical content. No logical Atom deletion operation is admitted.

## Details

### Required test cases

1. Prepare one valid current Atom, a Draft, an already archived Atom and a historical reference. Pin ID, Version, Summary, Properties, sections, source state and the applicable Status/placement model.
2. Reject denied permission, stale source, ambiguous identity, unsupported lifecycle, incomplete validation authority and archive collision before the affected action writes. Dry run changes nothing.
3. Archive the valid Atom. Verify unchanged ID, Summary and governed content, the admitted Status/time transition and Version N+1 for the changed archived Atom state. Preserve exact prior history bytes at N without bumping that history again, and distinguish both observed states. Existing references are not rewritten; Find and Modify reference workflows remain separate.
4. Request ordered independent archives A, B and C. After A completes, make B fail. Retain A's archive and evidence, report B's actual failure and leave C untouched. There is no rollback across Atom actions.
5. Inject failure within one Archive action after its effect or before postcondition verification. Check that action's claimed restoration boundary, including its source/destination, without touching earlier successes or accepted history. Incomplete restoration remains failed or uncertain.
6. Request logical deletion of an Atom. Reject it without losing current or archived content.

### Acceptance criteria

Completed Archive preserves one Atom's historical identity/content and reports only verified effects. Earlier completed actions remain after a later failure; rejected preflight and unperformed targets do not mutate. Within-action all-or-nothing and permission/currentness protections remain required. New workflow resume/retry and stronger concurrency/publication guarantees remain deferred.

### Failure disposition

Retain source pins, lifecycle/permission decisions, actual archive state, reference diagnostics, retained successes and untouched remainder. These are future verification requirements, not an implementation or observed test pass.
