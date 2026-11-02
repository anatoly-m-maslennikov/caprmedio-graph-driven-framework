---
atom_id: CA-M-318@10
content_role: Method
current_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 10
updated_at: 2026-10-26 05:59:45 +0400
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Projection
  depends_on:
  - Subject/Graph Node/Engineering/Continuant/Tool//CAPABILITY_CATALOG
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Engineering/Tool Discovery Binding
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Domain/Continuant/History/Journal
relations: {}
type: Eng Decision
tier: 3
---
# Summary

Derive and search the capability catalog

## Scope

the TOOLS capability for Capability Catalog.

## Claim

**to** derive **and** search the Capability Catalog, the Implementation **must** apply the following method.

## Details

1. read authoritative Project Structure **and** current source Atoms within the configured Project boundary; omit delivered methodology copies **and** historical or draft Carriers.
2. reuse the safe Atom parser; read identity, Content Role, Type, Status **and** Scope Unit from carried Properties.
3. resolve D-owned Tool Binding tables **and** observe admitted entrypoint files without executing them. bind implemented Action Prompts from their existing source manifests.
4. keep duplicate identities **and** unresolved bindings explicit; an observed script with no declaration remains an Implementation candidate.
5. rank matching query words deterministically, apply the requested filters **and** paginate compact results. load full source content only for a selected context.
