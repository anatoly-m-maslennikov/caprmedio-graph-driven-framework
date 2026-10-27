---
atom_id: CA-E-306@27
content_role: Evaluation
type: Eval Case
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Atom.Version Number
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action//Archive Selected Active Atoms'
  - Subject/Graph Node/Domain/Continuant/History/Journal.Record
  - Subject/Graph Node/Domain/Continuant/Atom.Status
  - Subject/Graph Node/Domain/Continuant/Atom.Updated At
version: 27
updated_at: 2026-10-26 00:46:35 +0400
relations:
  evaluation_for:
  - CA-R-868
  - CA-O-029
  - CA-D-289
  - CA-D-303
  relates_to:
  - CA-R-1521
  - CA-R-1788
  - CA-R-1662
tier: 4
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

8. Archive a Plan with an empty or non-Atom-asset-only optional matching Directory Carrier. Verify flat Archived Plan Markdown and the same versioned matching directory stem. Retained-history subtrees and non-Atom assets move byte-for-byte with the matching directory without rewriting old Version, Status, Updated At or content; no asset receives an invented Status Action.

9. Request one Archive of a folder-backed Plan, Workflow or Step container with nested latest Atoms, including Done Plans. Verify the calling Workflow selects all contained latest Atoms recursively and composes independently admitted single-Atom Actions under each qualified model, without an optional descendant mode or additional per-child human confirmation. Newly Archived Plan Markdown is flat in the owning shared area with its own Version suffix. Referenced Atoms outside containment and older Revision bytes remain unchanged. On a later failure, preserve earlier successful Actions and stop with truthful partial results, without cross-Atom rollback.

10. At the low-level single-Atom boundary, attempt parent carrier relocation while an independent current descendant would be implicitly moved. Verify pre-effect refusal and unchanged parent, descendant and history bytes. Then let the calling Workflow complete the selected descendant Actions first and archive the parent under ordinary safeguards. This safety precondition must not become blanket refusal of the authorized recursive request.

11. Exercise folder-backed Workflow and Step fixtures under their admitted models. Verify their matching-directory placement remains parent-governed and each changed descendant has its own actual Status/Revision effect. The flat Plan exception does not change non-Plan placement. Archive of a container whose source Status is Done still archives its descendants; CA-R-1521's cancel-unfinished-Plans exception applies only when the requested parent Status is Done, not when the requested parent Status is Archived.

### Acceptance criteria

Completed Archive preserves one Atom's historical identity/content and reports only verified effects. Earlier completed actions remain after a later failure; rejected preflight and unperformed targets do not mutate. Within-action all-or-nothing and permission/currentness protections remain required. New workflow resume/retry and stronger concurrency/publication guarantees remain deferred.

### Failure disposition

Retain source pins, lifecycle/permission decisions, actual archive state, reference diagnostics, retained successes and untouched remainder. These are future verification requirements, not an implementation or observed test pass.
