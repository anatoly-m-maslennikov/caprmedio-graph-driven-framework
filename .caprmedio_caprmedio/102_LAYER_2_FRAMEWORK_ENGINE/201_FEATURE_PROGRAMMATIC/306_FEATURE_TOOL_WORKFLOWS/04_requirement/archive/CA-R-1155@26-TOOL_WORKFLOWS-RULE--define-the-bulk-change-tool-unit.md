---
subjects:
  governs: Subject/Engineering/Tool//BULK_CHANGE
  depends_on: []
version: 26
status: Archived
updated_at: 2026-10-24 12:35:51 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
content_role: Requirement
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
atom_id: CA-R-1155@26
tier: 3
type: Rule
author: Anatoly Maslennikov
---
# Summary

Define the BULK_CHANGE Tool unit

## Scope

BULK_CHANGE composition of explicitly approved operations, with independent Actions for Atom targets.

## Claim

`BULK_CHANGE` **must** have one Workflow composition owner in TOOL_WORKFLOWS. Its existing executable binding at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/BULK_CHANGE/` remains unchanged by this authority split and is resolved explicitly from the current execution context; it composes registered create, structured patch, relation change, rename, move, lifecycle, **and** replacement operations over an explicit approved target sequence and emits a complete mutation-free plan. For Atom operations it invokes one independently admitted Action per Atom target, stops at the first failure, retains completed Actions and leaves the remainder untouched; it **must not** promise a cross-Atom rollback or all-or-nothing effect. Preserve each Atom Action's own source, permission, preview and storage-effect safeguards. Resume and retry policy for that sequence is deferred. These Atom rules do not replace separately governed generic Artifact transaction rules.

## Details
