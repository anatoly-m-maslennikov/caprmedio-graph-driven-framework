---
atom_id: CA-E-599
content_role: Evaluation
type: Eval Case
current_scope_unit: MCP
status: Archived
author: Anatoly Maslennikov
version: 14
updated_at: 2026-11-02 19:44:26 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
  - Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Selection
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
  - Subject/CAPRMEDIO/Carrier
relations:
  evaluation_for:
  - CA-R-1900
  - CA-M-355
tier: 5
carrier_destination:
  file:
    name: CA-E-599@14-MCP-EVAL_CASE--verify-project-mcp-launch-selection-and-isolation.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation/archive
---
# Summary

verify Project MCP launch selection and isolation

## Scope

selection, identity, context, and state-isolation checks before Docker runtime effects.

## Claim

the Evaluation **must** prove that the launcher binds only one selected Project context and refuses ambiguous input without an effect or cross-Project state access.

## Details

- exercise separate Project roots with the same control-root name and assert different canonical identities, namespaces, Gateway contexts, manifest/registry/query-source reads, and reload storage.
- exercise two valid Project roots below one Git-repository ancestor. An explicitly selected Project root resolves only its own one local control root; each selection has a different identity and cannot observe or reuse the other's lock, cache, receipt, pending-launch record, or runtime metadata.
- exercise `--project-root repo` with one valid direct control root, missing and invalid roots, an unsafe path, an escaping or symlink control selector, and zero or multiple candidates. Every invalid or ambiguous case returns its selection refusal before Docker image inspection, port allocation, Gateway reload, or state write.
- fixture-bind the selected manifest, registry, and query source to Project A, then supply Project B or a foreign binding. Verify the launcher rejects it rather than selecting the historical/default root, a Git-repository ancestor, or constructing mixed context. Verify a Project root without local `.git` remains admissible.
- verify a selected context is immutable after construction and no selector case starts a worker, queue, Workflow, Tool dispatch, or Release action.
