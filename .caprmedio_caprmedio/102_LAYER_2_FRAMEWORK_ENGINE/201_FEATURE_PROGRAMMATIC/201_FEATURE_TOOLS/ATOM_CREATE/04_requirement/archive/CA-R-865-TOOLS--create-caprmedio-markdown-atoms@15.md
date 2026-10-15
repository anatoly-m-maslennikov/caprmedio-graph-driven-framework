---
atom_id: CA-R-865
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool/ATOM_CREATE"
  depends_on:
    - "Atom"
    - "Atom/Identifier"
    - "Atom/Revision"
    - "Artifact/Carrier"
version: 15
updated_at: "2026-10-12 23:13:45 +0400"
relations: {}
---
# Summary

Create CAPRMEDIO Markdown Atoms

## Scope

ATOM_CREATE admission and creation of complete new Markdown Atom Carriers within configured Project control-root Content Role locations.

## Claim

the ATOM_CREATE Tool **must** provide admission **and** creation of complete new Markdown Atom Carriers within configured Project control-root Content Role locations:

- accept one explicit logical CreateAtom request with complete admitted Atom content and owning Scope Unit; the storage connector derives or receives the applicable path, directory and filename and enforces placement, filename, metadata and initial Revision authority.
- reject destination collisions **and** reused assigned Atom IDs, including IDs retained **only** **in** historical authority. identity admission follows CA-D-508; an unassigned Draft does **not** acquire an invented ID.
- create **`=1`** Atom per independently admitted Action. A several-Atom Workflow stops at the first failed Action, retains completed creations and leaves the remainder untouched. Retain each one-Atom Action's complete admission, preflight and storage-effect safeguards; do not promise a cross-Atom all-or-nothing effect.
- permit generic Carrier-construction mechanics while retaining responsibility for Atom admission, identity, Revision, one-Atom storage-effect safeguards, **and** effect semantics.
- default **to** a mutation-free dry run. accept `--apply` **only** through authorized Project-local MCP delegation with a sealed Initiative action envelope.

## Details

CA-O-032 defines the operational Action; CA-E-303 supplies its automated conformance cases. exact Carrier syntax remains governed by Delivery authority rather than duplicated here.
