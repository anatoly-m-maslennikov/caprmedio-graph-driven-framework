---
subjects:
  governs: Tool/ATOM_PROMOTE
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Atom/Identifier
  - Atom/Revision
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/History/Journal.Record
atom_id: CA-R-869@15
author: Anatoly Maslennikov
status: Archived
version: 15
updated_at: 2026-10-23 03:14:50 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
content_role: Requirement
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
local_tier: Standard
global_tier: 11
---
# Summary

Promote drafts to active Atoms

## Scope

Independently admitted promotion of one explicitly selected CAPRMEDIO Markdown Draft per Action.

## Claim

the `ATOM_PROMOTE` Tool **must** provide canonical promotion of CAPRMEDIO Markdown Drafts into active Atom authority. promotion is **not** archival **or** upgrade.

the capability **must**:

- admit **`=1`** explicit Draft per independently admitted Action; a several-Draft Workflow stops at its first failed Action, retains completed promotions and leaves the remainder untouched;
- accept ID-free Drafts, `CA-R-draft`/`<PREFIX>-<ROLE>-draft` new-Atom markers, version-qualified `<canonical-ID>@<proposed-version>-draft` edit markers, and legacy `<canonical-ID>@draft` compatibility. Require the marker and filename to agree;
- bind every promotion to an explicit target and expected source state. Existing-marker promotion updates the same canonical Atom at the carried/requested Version and archives the exact current predecessor; ID-free/role-draft promotion uses an explicitly admitted fresh next-unreused ID under CA-D-378;
- preserve Draft body/unrelated metadata, derive the canonical active filename and placement, and materialize the canonical ID, admitted Status and Version;
- reject non-Drafts, missing/invalid/mismatched markers or targets, Version/digest drift, historical ID reuse, destination collisions, stale preconditions and partial operations. Do not require retained Draft history, lineage or Journal append;
- default **to** a mutation-free dry run **and** accept `--apply` **only** through an authorized Project-local MCP delegation with a sealed Initiative action envelope;
- restore the failed one-Draft Action's verified mutable before-state after an effect or postcondition failure without changing earlier completed Actions, unrelated Carriers or immutable accepted Journal evidence.

CA-O-066 owns the admission Action. CA-E-307 checks the capability **and** recovery conditions; failed **or** unverified restoration is **not** successful recovery.

For `CA-R-123@4-draft`, the admitted target is canonical `CA-R-123` and the exact current predecessor must be Version 3; promotion writes Version 4. Legacy `CA-R-123@draft` requires the same proposed Version explicitly in the request. A changed target, source digest, predecessor Version or marker refuses before effects. Journal is post-effect observation only and its absence or append failure never gates promotion or authorizes replay.

## Details
