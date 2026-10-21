---
atom_id: CA-E-306
content_role: Evaluation
type: QA Case
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool/ATOM_ARCHIVE"
  depends_on: ["Atom", "Atom/Revision", "Artifact/Carrier", "Archive Selected Active Atoms", "Journal/Record", "Atom/Revision/Status", "Atom/Revision/Updated At"]
version: 14
updated_at: "2026-10-20T20:29:10.614Z"
relations:
  evaluation_for: [CA-R-868, CA-O-029, CA-D-289, CA-D-303]
  relates_to: [CA-R-1521, CA-R-1788, CA-R-1662]
---
# Summary

Verify archive selected active atoms

## Scope

Workflow admission owns identity, Version/time, lifecycle and complete schema decisions. Connector calls use CA-D-625 only to verify the supplied request, source preconditions and permission and to perform the explicit mechanical operation. A connector does not choose those decisions.

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

7. Archive a file-only Plan with no matching Directory Carrier under the existing currentness, permission, collision and recovery checks. Verify its Archived Plan Markdown Carrier is directly in the owning Scope Unit's shared `03_plan/archived` area, without parent/child Plan directory nesting, with CA-D-289's `@<resulting Version>` suffix. Preserve exact prior Revision bytes, Version and Status.

8. Archive a Plan with an empty or non-Atom-asset-only optional matching Directory Carrier. Verify the Archived Plan Markdown Carrier is flat in `03_plan/archived` and its relocated matching Directory Carrier uses the same versioned stem. No independent current descendant Atom may be implicitly moved. Preserve exact prior Revision bytes, Version and Status. Do not assert a retained-history subtree path while CA-C-549 remains open.

9. Attempt a parent Plan Archive while its matching directory contains a current descendant Atom. If relocating the bundle would implicitly move that descendant, verify pre-effect refusal and unchanged parent, descendant and history bytes/metadata. Then exercise each selected descendant through its own independently admitted single-Atom Action under its own qualified model and ordinary safeguards. After those Actions succeed and no independently current descendant would be moved, archive the parent. Each newly Archived Plan Markdown Carrier is flat in the owning `03_plan/archived` area with its own Version suffix. This does not infer a Status or effect for other descendants or decide C549's retained-history path.

10. Exercise folder-backed Workflow and Step archive fixtures under their admitted model. Verify matching-directory tree placement and unchanged carried descendant metadata; the flat Plan exception does not change this non-Plan behavior.

### Acceptance criteria

Completed Archive preserves one Atom's historical identity/content and reports only verified effects. Earlier completed actions remain after a later failure; rejected preflight and unperformed targets do not mutate. Within-action all-or-nothing and permission/currentness protections remain required. New workflow resume/retry and stronger concurrency/publication guarantees remain deferred.

### Failure disposition

Retain source pins, lifecycle/permission decisions, actual archive state, reference diagnostics, retained successes and untouched remainder. These are future verification requirements, not an implementation or observed test pass.
