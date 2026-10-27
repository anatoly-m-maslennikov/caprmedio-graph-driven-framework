---
atom_id: CA-O-066@12
content_role: Operations
type: Action
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
status: Archived
cce_version: cce_1
cce_form: definition
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action//Admit Sealed Drafts as Active Atoms'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Engineering/Continuant/Tool//ATOM_PROMOTE
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Atom.ID
  - Subject/Graph Node/Domain/Continuant/History/Journal.Record
  - Subject/Graph Node/Engineering/Continuant/Carrier
version: 12
updated_at: 2026-10-25 17:32:27 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
tier: 3
---
# Admit sealed drafts as active Atoms

Admit Sealed Drafts as Active Atoms **means** the reusable Action that accepts one explicitly selected Draft into active Atom authority as one independently authorized admission. Earlier successful admissions remain successful when a later target fails.

## Applicable conditions

- select **`=1`** Draft; handle an explicit ordered list as independent Atom Actions under CA-R-869.
- actual promotion requires an authorized Project-local MCP delegation with a sealed Initiative action envelope. preview alone grants no apply authority.
- bind the source to an explicit target. An ID-free or `CA-R-draft` Draft receives an explicitly admitted fresh next-unreused canonical ID under CA-D-378. A `<canonical-ID>@<proposed-version>-draft` Draft binds to that same canonical ID and proposed Version; legacy `<canonical-ID>@draft` remains compatible only with an explicit proposed Version. Do not silently substitute another target or Version.

## Action

1. resolve this one source as a current Draft and retain the exact source path, bytes and digest. Validate that its carried marker is permitted (`CA-R-draft`, `<canonical-ID>@<proposed-version>-draft`, or legacy `<canonical-ID>@draft`) and agrees with the filename; ID-free Drafts remain valid.
2. bind the source to one explicit target and expected state. For an existing marker, require the target canonical ID, exact current predecessor Version/digest, and proposed Version equal to the marker and current Version + 1. For an ID-free/role-draft source, require an explicitly admitted fresh next-unreused canonical ID. No retained Draft history, lineage or Journal append is required; stale or conflicting target/Version evidence leaves admission unresolved.
3. derive one canonical active filename and location. Materialize the canonical ID, admitted Status and proposed Version while preserving Draft body and unrelated metadata; remove only the Draft lifecycle marker/path. Reject non-Drafts, invalid or mismatched markers, collisions and incomplete mappings.
4. freeze this source, identity-admission evidence **and** destination map. return its mutation-free dry run **without** accepting authority.
5. on explicit authorized `--apply`, recheck source digest, explicit target/predecessor Version/digest, marker and destination evidence. A competing admission or changed evidence invalidates the preview. Safely materialize this one Draft within its independent Action boundary, archiving the exact current predecessor for an existing marker.
6. verify exact byte identity, unique active identity, canonical placement, absence from the Draft surface **and** this one target's complete admission.
7. **if** **any** effect **or** postcondition fails, restore only this Action's verified mutable source **and** destination frontier **to** its exact before-state. preserve unrelated Carriers **and** immutable accepted Journal evidence. report the failed attempt **and** recovery result rather than promotion success.

## Outcome

This accepted Draft becomes one canonical active Atom with the explicitly bound identity and Version. An existing-marker promotion updates the same canonical Atom (for example `CA-R-123@4-draft` becomes `CA-R-123` Version 4) and archives the exact current predecessor; a new Draft receives its newly admitted identity. Stop or recover on invalid input, uncertain identity admission, collision, stale Carrier, changed destination or incomplete promotion. Incomplete or unverified restoration is not successful recovery.

Journal records actual observations after the independent mutation attempt. Journal absence or append failure never authorizes replay and never gates an otherwise observed promotion.

For a folder-backed Plan, Workflow or Step Draft, include its matching Directory Carrier in this one target's admitted destination map and retain its nested tree beside the promoted Markdown Carrier with the governed matching stem. Preserve exact older Revision bytes and do not migrate noncanonical legacy archive trees. Relocation does not infer or rewrite descendants' Status or Revision metadata. When this admission is a component of the R1521 containment cascade, the caller separately binds every selected descendant's latest Revision to its own model-admitted Status Action, rechecking its current location after earlier effects. This Action retains the Operator-supplied identity-admission conditions above, selects no other target and proves completion only for its one admission; referenced Atoms outside the tree remain untouched.

## Independent Atom batch boundary

A requested batch is an ordered list of independently authorized Atom Actions. Invoke one Action at a time; advance to the next distinct explicit Atom only after confirmed success. On the first failure, stop, retain all earlier successful effects and their evidence, and leave the remaining targets untouched. Never roll back earlier successful Atoms to simulate a cross-Atom transaction. Validation, stale-source checks, permissions, safe effects and recovery within the failing Atom Action remain required. Automatic retry or resume of this new batch policy is deferred; existing recording-only recovery must not replay a performed Action.
