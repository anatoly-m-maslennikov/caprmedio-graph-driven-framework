---
cce_version: cce_1
cce_form: method
subjects:
  governs: "feature-boundary"
  depends_on: []
version: 11
updated_at: "2026-10-12 23:58:28 +0400"
relations:
  method_for:
    - CA-R-1155
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
content_role: Method
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
local_tier: Standard
global_tier: 11
status: Archived
atom_id: CA-M-254@11
---
# Summary

Change one sealed target set

## Scope

use this Method **when** `BULK_CHANGE` **must** compose registered carrier operations over one sealed target set.

## Claim

1. confirm the logical `BULK_CHANGE` Workflow composition binding under TOOL_WORKFLOWS and resolve its explicit admitted executable binding from current context. The existing code path `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/BULK_CHANGE/` is unchanged by this source-authority split; code topology is not Workflow ownership.
2. resolve one sealed target set **and** declared registered create, structured patch, relation change, rename, move, lifecycle, **or** replacement operations.
3. derive a complete mutation-free change plan that identifies **every** explicit target, effect, precondition, collision and required reference rewrite. For Atom operations, bind independent one-Atom Actions and their own storage-effect safeguards; do not create a cross-Atom rollback boundary. Retain rollback actions only where separately governed for generic Artifact operations.
4. require explicit approval of the exact plan digest **and** recheck the target set frontier **and** **every** effect precondition **before** apply.
5. For Atom operations, execute only the unchanged approved one-Atom Actions. Validate each Action's current source and permission before its effect; verify and record its actual outcome. A valid no-op has no edit, Version, timestamp or archive effect and does not stop the sequence. Stop at the first failed Action, retain completed Actions and leave remaining targets untouched. Report the successful, no-op, failed, uncertain and untouched targets truthfully. For separately governed generic Artifact operations, retain the admitted transaction, effect verification and rollback evidence.

## Details

### Outcome

one explicitly approved unchanged `BULK_CHANGE` plan reports the actual outcomes of its explicit targets. Atom Actions remain independent; a several-Atom sequence has no cross-Atom all-or-nothing promise. Separately governed generic Artifact transactions retain their own outcome contract.

### Failure or stop

do **not** mutate **before** an approved complete plan. For Atom operations, stale source, failed precondition, unplanned effect, collision, failed verification or uncertain recording stops the sequence at that Action. Preserve that Action's applicable storage safeguards without reverting earlier completed Atom Actions or executing the remainder. Resume and retry policy is deferred. Separately governed generic Artifact operations retain their admitted stop or rollback behavior.
