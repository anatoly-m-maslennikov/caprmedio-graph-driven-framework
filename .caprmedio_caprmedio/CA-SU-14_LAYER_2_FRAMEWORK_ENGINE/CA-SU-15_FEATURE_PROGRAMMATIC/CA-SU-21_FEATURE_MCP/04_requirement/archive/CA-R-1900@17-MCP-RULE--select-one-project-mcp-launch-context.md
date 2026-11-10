---
atom_id: CA-R-1900
ref_id: CA-R-1900@17
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
  - Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Source
    Selection
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component
    Structure
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Runtime
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
tier: 3
status: Archived
version: 17
updated_at: 2026-11-09 21:15:45 +0400
carrier_destination:
  file:
    name: CA-R-1900@17-MCP-RULE--select-one-project-mcp-launch-context.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement/archive
current_scope_unit: MCP
claim_target_scope_unit: MCP
author: Anatoly Maslennikov
relations:
  IS_REPLACEMENT_FOR:
  - CA-M-355
  - CA-D-593
---

## Summary

select one Project MCP launch context

## Claim

### Prose Claim

the Project MCP launcher **must** resolve **=1** safe, explicit Project context from its Project-root path and optional control-root selector, or refuse unchanged without selecting, mounting, or affecting another Project.

## Details

### Scope

project selection and context binding before a Project-local MCP runtime has any Docker, network, Gateway, reload, registry, or query-source effect.

- the default request is `--project-root repo`, where `repo` denotes the command's declared **Project root**. An explicit Project-root path is accepted only when it is an existing canonical directory with **=1** valid local control root. A caller may instead supply `--control-root .caprmedio_name`; it is one direct, normalized, non-symlink child of the selected Project root, has no traversal component, and identifies the control root to use.
- without `--control-root`, the selected Project root must contain **=1** direct valid `.caprmedio_*` control root. Zero or multiple candidates, a control root outside the selected Project root, invalid Project Settings or Project Structure, or an unreadable required Carrier returns an attributable selection refusal. The launcher does not choose a sibling, parent, nested Project, historical default control root, or Git-repository ancestor instead.
- canonical Project identity is the SHA-256 of the canonical host Project-root path, a NUL separator, and the selected control-root path relative to that Project root. It is computed before `/project` container translation and remains the same selected-instance identity there. Thus two Project roots under one Git repository have separate identities even when their control-root names, Engine sources, or image fingerprints match.
- the immutable selected context contains that identity, canonical Project-root path, the selected control-root relative path, and the exact Project-local manifest, registry, and query-source bindings. Gateway construction, hot-reload storage, registry reads, and query-source reads receive that context; they must not fall back to a process-global root or another Project's binding. Local `.git` is not a selection precondition.
- every runtime-owned lock, Gateway context, reload receipt, pending-launch record, and cache is namespaced by the selected Project identity below that Project's installed runtime state. A state entry from another identity is neither reusable input nor a cleanup target. This rule adds no runtime-kind enum and does not change a selected Workflow, queue, worker, or Release boundary.
- an explicit canonical Project root may be nested below the configured host
  projects-root mount when it satisfies the same local-control-root and
  identity checks. Startup candidate discovery remains bounded to direct
  children of that mount; the bounded discovery rule does not prohibit an
  explicitly selected nested Project.
- this record scopes the legacy one-Project launcher mode. A shared per-request
  runtime may serve multiple explicit Projects through one container and
  endpoint under CA-R-2008; that shared mode is not a global one-Project
  restriction.

### Project selection procedure

the launcher **must** construct one immutable `ProjectSelection` from the requested Project-root path and control-root selector before it reads a launch state or performs a Docker effect.


#### Scope

the deterministic Project-selector procedure used by the Project MCP launcher before image or runtime admission.

1. canonicalize the declared Project root and `--project-root`; reject a missing, non-directory, escaping, or symlink-substituted Project path. Interpret `repo` as the declared Project root, not as an ambient current-directory or Git-ancestor search.
2. normalize `--control-root` as one direct relative child when supplied. Otherwise enumerate only direct `.caprmedio_*` control-root candidates of the selected Project root. Require exactly one valid candidate and validate its Project Settings and Project Structure before continuing; a local `.git` directory is not required.
3. calculate `project_identity = sha256(project_root_realpath + NUL + control_root_project_relative_path)`. Build `ProjectSelection` once with the canonical host Project path, container `/project` translation, identity, and selected control-root-relative path; no later component accepts a replacement root.
4. bind the selected manifest, active registry, and admitted query source from that selection only. Mount and pass only that selected Project context to the endpoint Gateway and reload subsystem; a Git-repository ancestor or sibling Project need not be mounted. A missing, changed, foreign, duplicate, or unadmitted binding stops launch before image inspection.
5. derive the Project-scoped installed runtime namespace and per-Project lock from the identity. Store only the selected context's reload receipts, caches, pending-launch evidence, and safe runtime metadata there. Do not read, reuse, delete, or merge a sibling namespace.
6. return the immutable selection or a structured refusal containing the selector error class and no substituted path. This method starts no container, listener, worker, queue, Workflow, Tool call, or Release action.
7. allow an explicitly declared canonical Project root nested below the
   configured host projects-root mount when its local control-root and identity
   checks pass. Keep eager startup discovery bounded to direct children of the
   mount; this does not reject an explicitly selected nested Project.
8. This procedure scopes the legacy one-Project launcher. Shared per-request
   selection uses the host-root/catalog binding and may serve multiple Projects
   through one endpoint; when host and container roots are identical, carry the
   same absolute root without translation.

### Immutable launch context

The launcher **must** carry one explicit ProjectSelection record whose identity and selected bindings are sufficient to isolate the MCP Gateway and launcher state. The record carries the canonical host Project root, selected control root, Project identity, container path mapping and selected manifest, registry and query-source references.

The Codex hook's top-level project_root is an optional assertion for single-Project Tool calls and a required assertion for shared-Project Tool calls. Validate it against the carried ProjectSelection before Tool dispatch. A malformed or mismatched assertion produces a safe refusal with no native Tool execution, source effect or Journal effect. Remove the assertion envelope before a native Tool receives its own arguments. Prompt and Workflow wrappers retain their normal dispatch; initialize and tools/list are protocol operations, not Tool-call envelopes.

tools/list **must** advertise the top-level project_root input as optional for the single-Project service and required for the shared service, without mutating the native Tool descriptors or their input schemas. The advertisement describes the service boundary only; native Tool arguments remain unchanged.

Place launcher-owned Gateway context, hot-reload receipts, cache metadata, pending-launch evidence and the per-Project lock under the selected Project's installed runtime state in an identity-named namespace. Gateway and reload constructors consume the carried selection rather than scanning for a default control root or repository ancestor. A Carrier records safe identifiers and relative references, never credentials or an unselected Project's content.

This Carrier delivers no proxy, listener, worker, queue, Workflow request or Release transition. Shared delivery may serve multiple explicit Projects through one endpoint, but each request remains bound to its validated ProjectSelection.
