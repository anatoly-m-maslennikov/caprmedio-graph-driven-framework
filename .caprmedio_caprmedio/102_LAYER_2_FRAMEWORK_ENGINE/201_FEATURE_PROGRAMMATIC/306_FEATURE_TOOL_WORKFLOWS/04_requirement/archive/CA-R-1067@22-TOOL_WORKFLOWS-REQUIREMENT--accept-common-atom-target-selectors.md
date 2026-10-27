---
subjects:
  governs: Subject/Engineering/Tool//TARGET_SET
  depends_on: []
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 22
status: Archived
updated_at: 2026-10-24 11:29:41 +0400
content_role: Requirement
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
atom_id: CA-R-1067@22
tier: 1
type: Rule
author: Anatoly Maslennikov
---
# Summary

Accept common Atom target selectors

## Scope

Independent logical Find, Read and Modify selection of Atom targets.

## Claim

Atom Find **must** accept composable Scope Unit, Content Role, Type and Subject filters, including direct `governs` and `depends_on` matching under the selected exact, prefix, suffix or contains mode. A connector **may** resolve canonical filenames or locations internally; logical operation targets are Atom identities. Find **must** return matching identities and matching facts without granting effect permission.

Read and Modify **must** accept explicit selected identities independently of Find. Read returns the complete source and exact identity, Version and source pin; Modify binds its explicit target and expected source before its own preview and authorized effect. The Workflow owns supplied selection defaults, source-view and lifecycle criteria and applicable schema and authorization bindings; the connector executes only the explicit resulting request. An explicit logical-ID Read requires no pre-known Version and returns actual exact Version and source-state evidence; an optional pinned or historical expectation must match exactly. Modify requires expected current state and Create requires expected absence. The selector contract supplies no permission or Atom operation semantics. Each Atom Doer owns one target's preflight and effect; a several-target Workflow follows independent Action sequencing. Generic Artifact Tools **may** use selectors **only** as helpers and **must not** become public substitutes for logical Atom operations.

## Details
