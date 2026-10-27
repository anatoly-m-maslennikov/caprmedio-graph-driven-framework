---
atom_id: CA-M-355
content_role: Method
current_scope_unit: MCP
claim_target_scope_unit: MCP
status: Active
author: Anatoly Maslennikov
version: 15
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Project
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Domain/Continuant/Project.Settings
  - Subject/Graph Node/Domain/Continuant/Project.Structure
  - Subject/Graph Node/Engineering/Architecture/Component Structure
  - Subject/Graph Node/Engineering/Data Handling/Source Selection
  - Subject/Graph Node/Carrier
relations:
  method_for:
  - CA-R-1900
type: Eng Decision
tier: 4
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
7. allow an explicitly declared canonical Project root nested below the
   configured host projects-root mount when its local control-root and identity
   checks pass. Keep eager startup discovery bounded to direct children of the
   mount; this does not reject an explicitly selected nested Project.
8. This procedure scopes the legacy one-Project launcher. Shared per-request
   selection uses the host-root/catalog binding and may serve multiple Projects
   through one endpoint; when host and container roots are identical, carry the
   same absolute root without translation.
