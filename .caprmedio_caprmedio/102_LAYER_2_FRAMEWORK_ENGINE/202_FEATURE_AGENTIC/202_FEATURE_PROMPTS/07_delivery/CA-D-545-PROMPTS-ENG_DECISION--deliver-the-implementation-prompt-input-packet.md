---
atom_id: CA-D-545
content_role: Delivery
type: Eng Decision
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
status: Active
author: Anatoly Maslennikov
version: 13
updated_at: 2026-10-27 19:59:27 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Prompt Authoring
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Serialization
  - Subject/CAPRMEDIO/Carrier
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
relations: {}
tier: 3
---
# Summary

Deliver the implementation prompt input packet

## Scope

the invocation packet passed to one current Implementation Workflow prompt.

## Claim

the packet **must** carry current Workflow/Step/Action pins, P/DoD and owned paths, R/D targets, the verified active-M file, E checks, authority, permissions, confidence, retry accounting, assigned context, retained evidence, and Step-specific input.

## Details

Preparation may begin from a bounded request plus admitted authority, but it must produce or verify the M file before delegated work. A missing field produces the Step's blocked result.
