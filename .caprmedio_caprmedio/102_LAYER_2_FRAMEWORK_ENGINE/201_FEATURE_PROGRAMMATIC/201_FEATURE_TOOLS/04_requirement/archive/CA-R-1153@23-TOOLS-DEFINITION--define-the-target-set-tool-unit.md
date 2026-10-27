---
subjects:
  governs: Subject/Engineering/Tool//TARGET_SET
  depends_on: []
version: 23
updated_at: 2026-10-24 11:58:20 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1153@23
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Definition
tier: 1
---
# Define the TARGET_SET Tool unit

`TARGET_SET` **must** be one Finder Tool owned immediately by `TOOLS` as an `unordered_unit` at Structural level `4`, addressed by `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/TARGET_SET`, **and** realized under `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/TARGET_SET/`; it resolves explicit identities **and** composable governed selectors into one stably ordered target set with its complete membership, source frontier, **and** content digest **before** another Tool evaluates **or** changes those targets.
