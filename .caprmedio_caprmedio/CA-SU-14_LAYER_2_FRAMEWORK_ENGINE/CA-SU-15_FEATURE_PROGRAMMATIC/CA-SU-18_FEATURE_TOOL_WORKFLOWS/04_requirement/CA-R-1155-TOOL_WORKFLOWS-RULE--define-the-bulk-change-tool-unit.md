---
atom_id: CA-R-1155
ref_id: CA-R-1155
container:
  scope_unit: CA-SU-18
role: Requirement
form: Rule
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control"
tier: 3
status: Active
version: 32
updated_at: 2026-11-02 19:46:47 +0400
carrier_destination:
  file:
    name: CA-R-1155-TOOL_WORKFLOWS-RULE--define-the-bulk-change-tool-unit.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-18_FEATURE_TOOL_WORKFLOWS/04_requirement
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
---
# Summary

Define the BULK_CHANGE Tool unit

## Scope

BULK_CHANGE composition of explicitly approved operations, with independent Actions for Atom targets.

## Claim

`BULK_CHANGE` **must** have one Workflow composition owner in TOOL_WORKFLOWS. Its existing executable binding at `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/BULK_CHANGE/` remains unchanged by this authority split and is resolved explicitly from the current execution context; it composes registered create, structured patch, relation change, rename, move, lifecycle, **and** replacement operations over an explicit approved target sequence and emits a complete mutation-free plan. For Atom operations it invokes one independently admitted Action per Atom target, stops at the first failure, retains completed Actions and leaves the remainder untouched; it **must not** promise a cross-Atom rollback or all-or-nothing effect. Preserve each Atom Action's own source, permission, preview and storage-effect safeguards. Resume and retry policy for that sequence is deferred. These Atom rules do not replace separately governed generic Artifact transaction rules.

## Details
