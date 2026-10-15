---
atom_id: CA-O-066
content_role: Operations
type: Action
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Admit Sealed Drafts as Active Atoms"
  depends_on:
    - "Action"
    - "Tool/ATOM_PROMOTE"
    - "Atom"
    - "Atom/Identifier"
    - "Atom/Revision"
    - "Artifact/Carrier"
    - "Journal/Record"
version: 3
updated_at: "2026-10-12 23:49:24 +0400"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Admit sealed drafts as active Atoms

Admit Sealed Drafts as Active Atoms **means** the reusable Action that accepts one explicitly selected Draft into active Atom authority as one independently authorized admission. Earlier successful admissions remain successful when a later target fails.

## Applicable conditions

- select **`=1`** Draft; handle an explicit ordered list as independent Atom Actions under CA-R-869.
- actual promotion requires an authorized Project-local MCP delegation with a sealed Initiative action envelope. preview alone grants no apply authority.
- the Operator supplies the stable Project Atom IDs. validate their admission under CA-D-450 **and** CA-D-378; do **not** silently substitute another ID.

## Action

1. resolve this one source as a current Draft **and** bind it **to** **`=1`** Operator-supplied stable Atom ID. retain the exact source paths **and** bytes, digests, assigned IDs **and** expected active destinations.
2. validate role matching, uniqueness within the request **and** the next unreused Project-wide numbers for the applicable Content Roles. use current authority **and** preserved assignment/history evidence; absence from active files alone does **not** establish non-use. archived, replaced **or** absorbed Atoms do **not** release their IDs. missing **or** conflicting evidence leaves admission unresolved.
3. derive **`=1`** canonical active filename **and** location for this Draft. remove **only** the `drafts` lifecycle path segment **and** change the Carrier filename under the applicable Delivery grammar; preserve the complete Draft bytes. reject non-Drafts, invalid **or** mismatched IDs, collisions **and** incomplete mappings.
4. freeze this source, identity-admission evidence **and** destination map. return its mutation-free dry run **without** accepting authority.
5. on explicit authorized `--apply`, recheck source digests, identity-admission evidence **and** destination absence. a competing admission **or** changed evidence invalidates the preview. safely move this one Draft within its independent Action boundary.
6. verify exact byte identity, unique active identity, canonical placement, absence from the Draft surface **and** this one target's complete admission.
7. **if** **any** effect **or** postcondition fails, restore only this Action's verified mutable source **and** destination frontier **to** its exact before-state. preserve unrelated Carriers **and** immutable accepted Journal evidence. report the failed attempt **and** recovery result rather than promotion success.

## Outcome

This accepted Draft becomes **`=1`** byte-identical active Atom with its admitted Operator-supplied identity. remain **in** dry-run mode **without** delegated apply authority. stop **or** roll back on invalid input, uncertain identity admission, collision, stale Carrier, changed destination absence **or** incomplete promotion. incomplete **or** unverified restoration is **not** successful recovery.

A first identity admission preserves the Draft-byte rule above; it does not invent a prior same-ID Atom Revision. Any actual change to an already identified Atom follows Version N+1 and actual Project-time updated_at, with exact prior N history retained; no-op retains Version/time.

## Independent Atom batch boundary

A requested batch is an ordered list of independently authorized Atom Actions. Invoke one Action at a time; advance to the next distinct explicit Atom only after confirmed success. On the first failure, stop, retain all earlier successful effects and their evidence, and leave the remaining targets untouched. Never roll back earlier successful Atoms to simulate a cross-Atom transaction. Validation, stale-source checks, permissions, safe effects and recovery within the failing Atom Action remain required. Automatic retry or resume of this new batch policy is deferred; existing recording-only recovery must not replay a performed Action.
