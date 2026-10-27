---
atom_id: CA-P-2354@8
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Domain/Node/Continuant/Project.Settings
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Project.Settings
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 8
updated_at: 2026-10-24 13:39:34 +0400
relations:
  is_decomposition_of:
  - CA-P-2300
tier: 3
---
# Summary

Align ordinary Settings reader schema and source

## Objective

Align only the complete Project Settings schema and narrow source description used by an ordinary standalone file reader that reads, parses and validates the supplied file.

## Details

Own only the necessary ordinary-reader schema/source alignment and pins. Inspect selected authority before amendments and preserve unrelated policy and existing schema constraints. The reader validates admitted fields and reports missing required fields, unknown fields and invalid supplied types accurately. It does not repair content or migrate existing Settings/callers. Remove the superseded inspection/history/currentness model from this reader's contract: no Journal scan, history/currentness output or gate. Coordinate the accepted schema with CA-P-2355.

Estimated own work: up to 15 minutes. Split before exceeding this bound. Root owns Plans and Git. Parallel workers own disjoint files; preserve unrelated changes. This Task does not authorize changes to existing Settings documents, existing callers, Journal or runtime. Keep Active until final integration.

### Definition of Done

Exact schema/source paths, Versions and digests plus focused valid/invalid schema cases establish this ordinary reader contract. Independent review confirms that no Journal lookup, history/currentness result or admission gate is required and existing schema constraints remain intact. This work does not change existing Settings/callers or Journal/runtime; preserve unrelated pre-existing edits. Broader receiving, parent-wide and runtime completion remain separate.

### Completion checkpoint

Accepted ordinary-reader source alignment is committed with the final reader/schema/tests in `de558c227`. Independent review admits complete closed Settings validation, immutable actual values and physical/schema provenance without a Journal lookup, history/currentness result or gate. D366 v10 admits only optional `[project_mcp] http_port` as an exact integer in `1..65535`; absence stays absent, with no default, migration or MCP startup admission.

Exact changed source bindings:

- `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery/CA-D-366-CORE_META_MODEL--serialize-project-settings-content-in-toml.md`, v10, SHA-256 `93c8eddc61260a52f2b6c708f4e6809a5b1a8a4d12e37dd82b5afe0568b531d2`.
- `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/06_evaluation/CA-E-459-CORE_META_MODEL-EVALUATION_APPROACH--validate-authoritative-project-settings-artifact.md`, v19, SHA-256 `c20f5a68f2d2299e44651f68348605447cad6095b06b898c3cb135994dfc2c38`.
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-284-PROGRAMMATIC-CORE-METHOD--read-engine-settings-through-one-shared-boundary.md`, v14, SHA-256 `511958b7bb1701039215209b3be552a4b25485c48d56d19fab10c5a95564ed98`.

The complete nine-source closure and retained Versions/digests are in `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/project_settings_schema.py::SCHEMA_PINS` at `de558c227`. M284 named-source/header and this ordinary-reader definition are accepted; its deferred legacy carrier-format findings are not a full-carrier conformance claim. Focused author checks passed 8 tests, and final independent reader/Query/Read-receiver checks passed 44 tests in 86.425 seconds; Root's fresh connector regression passed 307 tests in 68.008 seconds.

Reader `e136cbee6424c385d792be7e33e25e33ac8d4e9ec4221f052c21c87bb8357784`; pure schema `a4dc1b8e867468b02a34cae602b13593948e2d233bf152b6bc3f3bb79deee27e`; author tests `131ad22988437b8925986357baf4f5e7d2678636adfd4a82fc4623e26251977c`; independent reader tests `698a8f9f2407d60790213b38245387e7207cc7a20ef23ad600d3bf3fba8cbdb5`.

Existing Settings/callers, Journal and runtime were not changed by this Task. P2300/P2280 receiving/caller integration, parent-wide completion and live runtime remain open.
