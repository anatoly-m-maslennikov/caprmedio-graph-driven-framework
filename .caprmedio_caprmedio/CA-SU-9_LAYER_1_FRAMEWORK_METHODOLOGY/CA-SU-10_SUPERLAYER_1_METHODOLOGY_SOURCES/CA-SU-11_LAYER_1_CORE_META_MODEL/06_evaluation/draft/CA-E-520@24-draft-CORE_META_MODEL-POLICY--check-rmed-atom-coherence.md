---
atom_id: CA-E-520@24-draft
ref_id: CA-E-520@24-draft
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Policy
topics:
  main_subject: Model::CAPRMEDIO::Continuant/Governing Objects/Atom.content
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Subjects
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Target Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Details
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Summary
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Property
  - Subject/CAPRMEDIO/Graph/Node
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Controlled English
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - 'Subject/caprmedio/Product: CAPRMEDIO Framework'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
tier: 5
relations:
  evaluation_for:
  - CA-D-269
  - CA-D-478
  - CA-D-479
  - CA-D-495
  - CA-M-113
  - CA-M-125
  - CA-R-1269
  - CA-R-1270
  - CA-R-1271
  - CA-R-1273
  - CA-R-1465
  - CA-R-1624
  - CA-R-1799
status: Draft
version: 24
updated_at: 2026-10-29 00:04:17 +0400
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
---
# Summary

Check RMED Atom coherence

## Claim scope

Local review of an individual complete RMED Atom against its carried text and applicable rules.

## Claim

A complete RMED Atom passes this local Evaluation only when it has one source-faithful Summary under # Summary, exactly one content.claim under ## Claim, and optional Claim scope, Semantics and Details in the registered order. Its one Type-defined Claim contains prose, an optional formal_claim child, or both; they must agree rather than supply unrelated or contradictory contributions. Assess the independently replaceable contribution, applicable boundary, support and Summary from that one Claim.

## Details

Check Properties against CA-D-479 and the applicable Type. Do not fail absent optional sections; fail an omitted Claim scope only when the full-applicability omission condition is not met. For a formal part parse its declared expression under the applicable Definition and Graph Syntax, check its admitted fields/schema and absence of a duplicate frontmatter Claim. Do not infer a defined schema, fulfilled rule, actual run or semantic correctness merely from parsing.

CCE applies to authored prose; formal content follows its declared syntax. Semantics explains meaning, Details supports the Claim, and neither supplies another normative Claim. Report concrete local source evidence for findings and retain unresolved evidence as gaps. This remains the atom_local profile: it does not silently add model-wide conflict, Subject completeness, target existence, Tier hierarchy or Principle audits. Existing Operator authority remains applicable. A local pass is not whole-methodology conformance.

R-only scope refinement (CA-A-1244): the optional ### Formal claim / content.claim.formal_claim is admitted only for Requirement Atoms for now. Method, Evaluation and Delivery have prose Claims with no operative formal child; code examples remain examples. Any earlier generic optional-formal wording in this Draft is limited by that Role condition. The complete one-Claim contract and optional supporting sections remain unchanged.
