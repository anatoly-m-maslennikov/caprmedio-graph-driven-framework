---
atom_id: CA-D-545@6
content_role: Delivery
type: Eng Decision
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
status: Archived
author: Anatoly Maslennikov
version: 6
updated_at: 2026-10-24 05:56:25 +0400
subjects:
  governs: Subject/Engineering/Implementation prompt input packet
  depends_on:
  - Subject/Engineering/Prompt
  - Subject/Engineering/Carrier
  - Method
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
relations:
  relates_to:
  - CA-R-1844
  - CA-M-329
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
