---
atom_id: CA-R-1514
ref_id: CA-R-1514
container:
  scope_unit: CA-SU-13
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Architecture <+ Component Structure
  dependencies:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//CORE_META_MODEL
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)
  - CAPRMEDIO_MODEL <+ Package/Implementation
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Action)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)'
  - CAPRMEDIO_MODEL <+ Package
tier: 2
relations:
  depends_on:
  - CA-R-1519
status: Active
version: 27
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-R-1514-PROJECT_CONFIGURATION-RULE--keep-implementation-specifications-independent-of-production-workflows.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1514-PROJECT_CONFIGURATION-RULE--keep-implementation-specifications-independent-of-production-workflows.md
  source_atom_id: CA-R-1514
  source_atom_revision: 27
  source_sha256: f88d90ea88b3b2a9b57ad54c0f3795ebd7f6358ff1957ae66845a4faa24ad0d8
  original_relations_sha256: 445b79cc5d5c1583b960c0e86c52c0d7693990df1711ccc5f5c5e6aa3a0dd35e
---
## Summary

Keep Implementation specifications independent of production Workflows

## Claim

### Prose Claim


the CAPRMEDIO Project's governing RMED for an Implementation.


**in** the CAPRMEDIO Project, governing RMED **must** fully specify the required Implementation independently of the Workflow used **to** produce it.

## Details

- conformity depends on the resulting Implementation satisfying its RMED, **not** on following a particular production Workflow. different Workflows, **or** work **without** a formally defined Workflow, **may** produce a conforming Implementation.
- ordinary implementation RMED **must not** leave required behavior specified **only** **in** an O Atom **or** require an O Atom as its production procedure.
- the permitted authority references are the Tool realization binding under CA-R-1800-PROJECT_CONFIGURATION-RULE--bind-every-tool-to-one-methodology-action **and** CA-R-1517-PROJECT_CONFIGURATION-RULE--keep-tool-operational-authority-outside-its-own-subtree, **and** methodology checks of Action **and** Workflow definitions under CA-R-1518-PROJECT_CONFIGURATION-RULE--separate-methodology-and-tool-evaluation-responsibilities. neither exception makes the Workflow used **to** build the Implementation part of its specification.
- a generic executor **may** consume applicable O definitions as runtime inputs under CA-R-1519-CORE_META_MODEL-RULE--require-conforming-workflow-execution. its RMED **must** fully specify how it interprets those inputs; the selected Workflow is **not** its production procedure **or** an independently copied part of its Spec.

these are CAPRMEDIO Project Configuration boundaries, **not** a change **to** the reusable Core Meta-Model Content Roles.
