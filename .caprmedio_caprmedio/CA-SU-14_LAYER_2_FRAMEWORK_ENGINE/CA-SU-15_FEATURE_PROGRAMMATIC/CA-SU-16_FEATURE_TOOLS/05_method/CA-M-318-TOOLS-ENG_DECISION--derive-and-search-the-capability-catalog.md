---
atom_id: CA-M-318
ref_id: CA-M-318
container:
  scope_unit: CA-SU-16
role: Method
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  dependencies:
  - "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Data Transformation"
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
status: Active
version: 12
updated_at: 2026-10-27 19:59:42 +0400
carrier_destination:
  file:
    name: CA-M-318-TOOLS-ENG_DECISION--derive-and-search-the-capability-catalog.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/05_method
current_scope_unit: TOOLS
author: Anatoly Maslennikov
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
