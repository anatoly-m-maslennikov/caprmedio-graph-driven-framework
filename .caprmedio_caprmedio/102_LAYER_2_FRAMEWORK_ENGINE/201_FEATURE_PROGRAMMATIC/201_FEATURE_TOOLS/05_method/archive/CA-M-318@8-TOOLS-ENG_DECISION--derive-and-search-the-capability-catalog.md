---
atom_id: CA-M-318@8
content_role: Method
current_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-24 23:19:22 +0400
subjects:
  governs: Subject/Domain/Node/Continuant/Projection
  depends_on:
  - Subject/Engineering/Tool//CAPABILITY_CATALOG
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Engineering/Tool Discovery Binding
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Subject/Domain/Node/Continuant/History/Journal
relations:
  relates_to:
  - CA-R-1810
  - CA-D-520
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
