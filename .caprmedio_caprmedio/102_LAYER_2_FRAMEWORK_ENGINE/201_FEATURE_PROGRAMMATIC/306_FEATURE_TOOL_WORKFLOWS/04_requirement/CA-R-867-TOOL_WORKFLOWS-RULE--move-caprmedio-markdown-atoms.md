---
cce_version: cce_1
cce_form: obligation
atom_id: CA-R-867
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Storage/Directory Layout
  depends_on: []
version: 26
updated_at: 2026-10-27 20:00:11 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
content_role: Requirement
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
status: Active
tier: 3
type: Rule
author: Anatoly Maslennikov
---
# Summary

Move CAPRMEDIO Markdown Atoms

## Scope

Independently admitted relocations of explicitly selected CAPRMEDIO Markdown Atoms.

## Claim

the `ATOM_MOVE` Tool is the canonical Doer for moving CAPRMEDIO Markdown Atom carriers between content-role locations **in** the configured Project control root while preserving their Substance, Summary, Type **and** Atom IDs and applying only the explicit placement change and its required Revision metadata. A sealed `move_atom` request **must** carry one target descriptor with `atom_id`, expected current Version or digest and source evidence, plus one placement object with `destination_path`, `owning_scope_unit` and `claim_target_scope_unit`; the move preserves the Atom ID, Summary, Type, complete body and typed relations. The operation records the actual attempt through the existing Journal when available without making Journal recording a permission or completion gate; an unchanged placement remains a no-op with no Version, Updated At or history change. A changed move archives the exact pre-change carrier bytes at predecessor Version N. it **must** support exact selectors **and** recursive source-subtree selection, preserve the selected subtree by default, flatten **only** **when** explicitly requested, reject collisions **and** invalid destinations, **and** preflight the complete one-Atom operation. An actual changed same-ID Atom move advances Version by **`=1`** and uses actual Updated At; preserve the exact before-Revision bytes as required history. A validated unchanged placement is a no-op without a Version or timestamp change. each Action moves **`=1`** explicit Atom target with its expected Revision or digest. A several-Atom Workflow stops at its first failed Action, retains completed moves and leaves the remaining targets untouched; it does not promise cross-Atom rollback. it **may** use generic rename mechanics but owns Atom placement, identity-preservation, one-Atom storage-effect safeguards, **and** effect semantics. it **must** default **to** a mutation-free dry run **and** accept `--apply` **only** through an authorized project-local MCP delegation with a sealed Initiative action envelope.

## Details

### Check

automated tests **must** prove singular **and** bulk moves, default subtree preservation, explicit flattening, unrelated-byte and identity preservation, required Version/Updated At changes for an actual Atom move, collision **and** destination rejection, mutation-free dry run, MCP-gated apply, **and** verified restoration of the failed Action's source and destination after an apply failure, with earlier completed Atom Actions retained and the remainder untouched.
