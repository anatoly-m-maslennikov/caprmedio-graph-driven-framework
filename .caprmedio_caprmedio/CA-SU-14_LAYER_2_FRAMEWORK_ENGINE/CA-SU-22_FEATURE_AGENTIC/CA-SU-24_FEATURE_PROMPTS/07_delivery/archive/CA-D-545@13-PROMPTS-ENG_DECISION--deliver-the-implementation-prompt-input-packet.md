---
atom_id: CA-D-545@13
ref_id: CA-D-545@13
container:
  scope_unit: CA-SU-24
role: Delivery
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Authoring/Prompt
    Authoring
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Serialization
  - Subject/CAPRMEDIO/Carrier
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
tier: 3
status: Archived
version: 13
updated_at: 2026-10-27 19:59:27 +0400
carrier_destination:
  file:
    name: CA-D-545@13-PROMPTS-ENG_DECISION--deliver-the-implementation-prompt-input-packet.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-24_FEATURE_PROMPTS/07_delivery/archive
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
author: Anatoly Maslennikov
---
# Summary

Deliver the implementation prompt input packet

## Scope

the invocation packet passed to one current Implementation Workflow prompt.

## Claim

the packet **must** carry current Workflow/Step/Action pins, P/DoD and owned paths, R/D targets, the verified active-M file, E checks, authority, permissions, confidence, retry accounting, assigned context, retained evidence, and Step-specific input.

## Details

Preparation may begin from a bounded request plus admitted authority, but it must produce or verify the M file before delegated work. A missing field produces the Step's blocked result.
