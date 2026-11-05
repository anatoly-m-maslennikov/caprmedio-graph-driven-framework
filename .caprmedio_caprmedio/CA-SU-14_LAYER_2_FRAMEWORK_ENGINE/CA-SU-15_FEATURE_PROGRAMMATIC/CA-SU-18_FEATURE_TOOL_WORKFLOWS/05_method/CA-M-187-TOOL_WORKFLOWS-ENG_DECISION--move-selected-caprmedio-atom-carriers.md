---
atom_id: CA-M-187
ref_id: CA-M-187
container:
  scope_unit: CA-SU-18
role: Method
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Storage/Directory Layout
tier: 4
relations:
  method_for:
  - CA-R-867
  derived_from:
  - CA-A-058
status: Active
version: 24
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-M-187-TOOL_WORKFLOWS-ENG_DECISION--move-selected-caprmedio-atom-carriers.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-18_FEATURE_TOOL_WORKFLOWS/05_method
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
---
# Summary

Move selected CAPRMEDIO Atom carriers

## Scope

use this Method **when** a caller prepares relocation of one exact Atom **or** an explicit sequence of independent Atom Actions while preserving their Substance, Summary, Type and identities and changing only the explicit placement and required Revision metadata. actual relocation is permitted **only** **when** an authorized project-local MCP delegation supplies a sealed Initiative action envelope.

## Claim

1. resolve the exact selector **or** recursive source subtree, retain **only** Atom carriers, **and** capture **every** source path, filename, ID, **and** digest.
   bind one sealed `move_atom` request to one target descriptor with `atom_id`, expected current Version or digest and source evidence, and to placement `{destination_path, owning_scope_unit, claim_target_scope_unit}`; preserve the Atom ID, Summary, Type, complete body and typed relations.
2. derive one destination mapping per selected Atom, preserving selected subtree shape by default **and** flattening **only** **when** the sealed Initiative explicitly requests it.
3. validate destination Scope Unit **and** Content-role placement, source membership, path uniqueness, **and** destination collision freedom without changing unrelated carrier content.
4. freeze the complete move map **and** publish a mutation-free dry-run.
5. on explicit authorized application, invoke one independent move Action per explicit Atom target. Recheck that Action's source digest and permission. If its requested placement already equals its validated current placement, return a no-op with no edit, Version or timestamp effect and continue. Otherwise recheck destination absence before moving; the actual changed same-ID Atom advances Version by **`=1`** and uses actual Updated At, with exact before-Revision bytes retained as required history and the exact pre-change carrier archived at predecessor Version N. Record the actual attempt through the existing Journal when available without making Journal recording a permission or completion gate. Retain that Action's own verified source/destination safeguards and verify its actual result before starting the next Action.
6. For successfully moved targets, verify that their former sources are absent and their mapped destinations are present. For no-op targets, verify unchanged source, destination and Revision metadata. Verify that non-Atom files are untouched, every moved Atom retains its Substance, Summary, Type, complete body, typed relations and Atom ID, all unrelated bytes remain unchanged, and the actual placement and required Revision metadata match the admitted proposal.

## Details

### Outcome

the selected carriers occupy exactly their approved destinations **and** retain their identity and unrelated content with exactly the admitted placement and Revision metadata changes.

### Failure or stop

remain **in** dry-run mode **without** delegated apply authority. Stop at the first Action with an invalid destination, collision, stale source, incomplete mapping, changed destination absence or failed post-move verification. Preserve the failed Action's verified source/destination safeguards, retain earlier completed moves and leave the remainder untouched. An uncertain effect or recording is not success and stops the sequence. Resume and retry policy is deferred.
