---
topics:
  main_subject: Model::CAPRMEDIO::Continuant/Governing Objects/Atom.content.claim_scope
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Target Scope Unit
  - Subject/CAPRMEDIO/Carrier/File
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role
version: 21
updated_at: 2026-10-29 00:04:17 +0400
atom_id: CA-D-495@21-draft
ref_id: CA-D-495@21-draft
role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
tier: 1
form: Eng Decision
container:
  scope_unit: CA-SU-11
---
# Summary

Carry applicability in the registered body sections

## Claim scope

Applicability restrictions carried by Markdown Atoms.

## Claim

For RMED, carry any separate applicability boundary once in atom.content.claim_scope under ## Claim scope, before ## Claim. Its count is zero or one; require it when the full-applicability omission condition does not hold. Claim, Semantics and Details are read within that boundary. Do not repeat the same boundary as an independently maintained frontmatter, Claim or Details value.

## Details

For a formal model Definition any formal applicability expression remains in the optional formal_claim child of that one Claim, with complementary prose in the parent section. Optional prose Claim scope may clarify its boundary without copying or overriding the operative selector or condition. No extra prose scope is required solely because the Claim is formal. Local Scope Unit and Target Scope Unit remain structural references, not replacements for applicability. Other Content Roles retain their registered applicability arrangements. CA-D-479 supplies the exact headings and order.

R-only scope refinement (CA-A-1244): the optional ### Formal claim / content.claim.formal_claim is admitted only for Requirement Atoms for now. Method, Evaluation and Delivery have prose Claims with no operative formal child; code examples remain examples. Any earlier generic optional-formal wording in this Draft is limited by that Role condition. The complete one-Claim contract and optional supporting sections remain unchanged.
