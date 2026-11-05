---
atom_id: CA-R-865
ref_id: CA-R-865
container:
  scope_unit: CA-SU-18
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.ID
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Version Number
  - Subject/CAPRMEDIO/Carrier
tier: 3
status: Active
version: 29
updated_at: 2026-10-27 20:00:11 +0400
carrier_destination:
  file:
    name: CA-R-865-TOOL_WORKFLOWS-RULE--create-caprmedio-markdown-atoms.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-18_FEATURE_TOOL_WORKFLOWS/04_requirement
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
---
# Summary

Create CAPRMEDIO Markdown Atoms

## Scope

ATOM_CREATE admission and creation of complete new Markdown Atom Carriers within configured Project control-root Content Role locations.

## Claim

the ATOM_CREATE Tool **must** provide admission **and** creation of complete new Markdown Atom Carriers within configured Project control-root Content Role locations:

- accept one explicit logical CreateAtom request with complete admitted Atom content and owning Scope Unit; the Workflow decides admitted identity, metadata, initial Revision and ownership, then supplies the exact content and applicable schema and authority bindings to the connector. The connector maps the logical target to its private storage and mechanically checks supplied placement and preconditions without allocating identity or deciding lifecycle policy.
- reject destination collisions **and** reused assigned Atom IDs, including IDs retained **only** **in** historical authority. identity admission follows CA-D-508; an unassigned Draft does **not** acquire an invented ID.
- create **`=1`** Atom per independently admitted Action. A several-Atom Workflow stops at the first failed Action, retains completed creations and leaves the remainder untouched. Retain each one-Atom Action's complete admission, preflight and storage-effect safeguards; do not promise a cross-Atom all-or-nothing effect.
- permit generic Carrier-construction mechanics while retaining responsibility for Atom admission, identity, Revision, one-Atom storage-effect safeguards, **and** effect semantics.
- default **to** a mutation-free dry run. accept `--apply` **only** through authorized Project-local MCP delegation with a sealed Initiative action envelope.
- admit any requested initial Status allowed by the Atom's applicable Role/Type Status model and transition conditions. Journal append is an independent observation attempt; its absence, incompleteness or failure neither blocks a created Atom nor authorizes replay.

## Details

CA-O-032 defines the operational Action; CA-E-303 supplies its automated conformance cases. exact Carrier syntax remains governed by Delivery authority rather than duplicated here.
