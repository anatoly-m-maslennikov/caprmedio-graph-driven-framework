---
atom_id: CA-R-1900
content_role: Requirement
current_scope_unit: MCP
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 00:25:33 +0400"
subjects:
  governs: "MCP/Project launcher/selection boundary"
  depends_on: [Project, Project Settings, Project Structure, MCP, Gateway, Registry, Query Source, Runtime, Operator]
relations:
  relates_to: [CA-R-1884, CA-R-1885, CA-R-1818]
---
# Summary

select one Project MCP launch context

## Scope

project selection and context binding before a Project-local MCP runtime has any Docker, network, Gateway, reload, registry, or query-source effect.

## Claim

the Project MCP launcher **must** resolve **=1** safe, explicit Project context from its Project-root path and optional control-root selector, or refuse unchanged without selecting, mounting, or affecting another Project.

## Details

- the default request is `--project-root repo`, where `repo` denotes the command's declared **Project root**. An explicit Project-root path is accepted only when it is an existing canonical directory with **=1** valid local control root. A caller may instead supply `--control-root .caprmedio_name`; it is one direct, normalized, non-symlink child of the selected Project root, has no traversal component, and identifies the control root to use.
- without `--control-root`, the selected Project root must contain **=1** direct valid `.caprmedio_*` control root. Zero or multiple candidates, a control root outside the selected Project root, invalid Project Settings or Project Structure, or an unreadable required Carrier returns an attributable selection refusal. The launcher does not choose a sibling, parent, nested Project, historical default control root, or Git-repository ancestor instead.
- canonical Project identity is the SHA-256 of the canonical host Project-root path, a NUL separator, and the selected control-root path relative to that Project root. It is computed before `/project` container translation and remains the same selected-instance identity there. Thus two Project roots under one Git repository have separate identities even when their control-root names, Engine sources, or image fingerprints match.
- the immutable selected context contains that identity, canonical Project-root path, the selected control-root relative path, and the exact Project-local manifest, registry, and query-source bindings. Gateway construction, hot-reload storage, registry reads, and query-source reads receive that context; they must not fall back to a process-global root or another Project's binding. Local `.git` is not a selection precondition.
- every runtime-owned lock, Gateway context, reload receipt, pending-launch record, and cache is namespaced by the selected Project identity below that Project's installed runtime state. A state entry from another identity is neither reusable input nor a cleanup target. This rule adds no runtime-kind enum and does not change a selected Workflow, queue, worker, or Release boundary.
