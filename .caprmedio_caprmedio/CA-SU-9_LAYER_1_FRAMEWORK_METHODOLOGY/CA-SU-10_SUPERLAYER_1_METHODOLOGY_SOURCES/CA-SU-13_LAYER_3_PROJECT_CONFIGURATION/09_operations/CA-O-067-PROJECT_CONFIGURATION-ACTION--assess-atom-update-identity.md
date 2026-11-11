---
atom_id: CA-O-067
ref_id: CA-O-067
container:
  scope_unit: CA-SU-13
role: Operations
form: Action
topics:
  main_subject: Subject/caprmedio/Action//Assess Atom Update Identity
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Summary
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Header.State.Version Number
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
tier: 3
status: Active
version: 22
updated_at: 2026-10-27 19:59:45 +0400
carrier_destination:
  file:
    name: CA-O-067-PROJECT_CONFIGURATION-ACTION--assess-atom-update-identity.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
---
# Summary

Assess Atom update identity

## Operation

This read-only Action reports whether a proposed Summary or Content Role differs from the selected Atom. A changed Draft Summary or Content Role results in a new identity promoted at Version 1; an existing Draft with unchanged Summary and Content Role retains its Version. This observation is not a semantic change-class assessment or a prerequisite for Update, direct editing, or promotion. The Action does not persist changes or select a Workflow continuation.
