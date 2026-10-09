---
atom_id: CA-M-355
content_role: Method
current_scope_unit: MCP
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 00:42:28 +0000"
subjects:
  governs: "MCP/Project launcher/selection method"
  depends_on: [Project, Project Settings, Project Structure, Gateway, Registry, Query Source, Carrier]
relations:
  method_for: [CA-R-1900]
  relates_to: [CA-M-341, CA-M-342]
---
# Summary

resolve one Project MCP launch context

## Scope

the deterministic Project-selector procedure used by the Project MCP launcher before image or runtime admission.

## Claim

the launcher **must** construct one immutable `ProjectSelection` from the requested Project-root path and control-root selector before it reads a launch state or performs a Docker effect.

## Details

1. canonicalize the declared Project root and `--project-root`; reject a missing, non-directory, escaping, or symlink-substituted Project path. Interpret `repo` as the declared Project root, not as an ambient current-directory or Git-ancestor search.
2. normalize `--control-root` as one direct relative child when supplied. Otherwise enumerate only direct `.caprmedio_*` control-root candidates of the selected Project root. Require exactly one valid candidate and validate its Project Settings and Project Structure before continuing; a local `.git` directory is not required.
3. calculate `project_identity = sha256(project_root_realpath + NUL + control_root_project_relative_path)`. Build `ProjectSelection` once with the canonical host Project path, container `/project` translation, identity, and selected control-root-relative path; no later component accepts a replacement root.
4. bind the selected manifest, active registry, and admitted query source from that selection only. Mount and pass only that selected Project context to the endpoint Gateway and reload subsystem; a Git-repository ancestor or sibling Project need not be mounted. A missing, changed, foreign, duplicate, or unadmitted binding stops launch before image inspection.
5. derive the Project-scoped installed runtime namespace and per-Project lock from the identity. Store only the selected context's reload receipts, caches, pending-launch evidence, and safe runtime metadata there. Do not read, reuse, delete, or merge a sibling namespace.
6. return the immutable selection or a structured refusal containing the selector error class and no substituted path. This method starts no container, listener, worker, queue, Workflow, Tool call, or Release action.
