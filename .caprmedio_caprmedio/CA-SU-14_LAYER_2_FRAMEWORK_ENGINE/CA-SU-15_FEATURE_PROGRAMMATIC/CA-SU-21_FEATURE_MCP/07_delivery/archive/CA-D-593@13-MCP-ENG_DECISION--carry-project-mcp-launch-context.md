---
atom_id: CA-D-593@13
content_role: Delivery
current_scope_unit: MCP
status: Archived
author: Anatoly Maslennikov
version: 13
updated_at: 2026-10-26 05:59:45 +0400
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Project
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Domain/Continuant/Project.Settings
  - Subject/Graph Node/Domain/Continuant/Project.Structure
  - Subject/Graph Node/Engineering/MCP
  - Subject/Graph Node/Engineering/Gateway
  - Subject/Graph Node/Engineering/Occurrent/Runtime
relations:
  delivery_for:
  - CA-R-1900
  - CA-M-355
type: Eng Decision
tier: 5
---
# Summary

carry Project MCP launch context

## Scope

the selected-Project context Carrier and its Project-scoped runtime storage boundary.

## Claim

the launcher **must** carry one explicit Project-selection record whose identity and selected bindings are sufficient to isolate the MCP Gateway and launcher state.

## Details

- carry `ProjectSelection` with exactly the canonical Project-root/control-root facts, the derived Project identity, container path translation, and selected manifest/registry/query-source references. A Carrier records safe identifiers and relative references, never a credential or an unselected Project's content. A Git-repository boundary is neither a selection fact nor required mount.
- place launcher-owned Gateway context, hot-reload receipts, cache metadata, pending-launch evidence, and the per-Project lock under the selected Project's installed runtime state in an identity-named namespace. Runtime metadata includes the Project identity, admitted image digest/fingerprint, Compose project identity, and safe observed publication; it never authorizes a changed Project context.
- Gateway and reload constructors consume the carried selection rather than scanning for a default control root or repository ancestor. The endpoint mount is the selected Project context; sibling Projects are not required. The selected manifest, registry, and query-source bindings are validated again at their established admission boundaries.
- this Carrier delivers no proxy, listener, worker, queue, Workflow request, or Release transition. Its namespace may be created only after successful selection and is not a shared cache.
- this Carrier remains the legacy one-Project launcher context. Shared delivery
  under CA-D-640 carries the outer project root and native request per call for
  multiple Projects; it does not replace this record with a process-global
  Project binding.
