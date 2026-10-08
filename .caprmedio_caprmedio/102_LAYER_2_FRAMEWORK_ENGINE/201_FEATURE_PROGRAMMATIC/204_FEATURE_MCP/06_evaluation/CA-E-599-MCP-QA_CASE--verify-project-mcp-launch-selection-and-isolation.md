---
atom_id: CA-E-599
content_role: Evaluation
type: QA Case
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 00:25:33 +0400"
subjects:
  governs: "MCP/Project launcher/selection evaluation"
  depends_on: [Project, Project Settings, Project Structure, MCP, Gateway, Registry, Query Source, Carrier]
relations:
  evaluation_for: [CA-R-1900, CA-M-355]
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
