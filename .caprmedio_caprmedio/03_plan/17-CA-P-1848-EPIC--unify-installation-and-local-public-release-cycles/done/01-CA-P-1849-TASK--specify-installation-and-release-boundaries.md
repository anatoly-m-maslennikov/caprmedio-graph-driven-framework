---
atom_id: CA-P-1849
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Done
author: Anatoly Maslennikov
version: 6
updated_at: "2026-10-12 00:40:01 +0000"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on: [Project, Plan, AI Agent, Operator, Framework Instance Settings, Framework Package, Methodology Source, Applicable Methodology, Project Structure, Requirement, Method, Delivery, Workflow, Action, Journal]
relations:
  is_decomposition_of: [CA-P-1848]
  blocks: [CA-P-1850, CA-P-1851, CA-P-1852, CA-P-1853, CA-P-1854]
---
# Summary

Specify installation **and** release boundaries

## Objective

Define the source, product, reusable package and per-Project runtime boundaries for the direct release workflows.

## Details

- Follow CA-P-1848's current direct happy path. Earlier snapshot, admission, selector, recovery and complete-corpus gate requirements are superseded.
- Commit everything before every release step and at the end, respecting Git ignore rules and secret exclusions.
- Stop and report a failed step for manual handling; no automatic rollback or retry.
- Preserve configuration, Project records and other Projects. Ignore .DS_Store.

- Completion evidence: The direct source/product/package/runtime boundaries are specified and verified by the completed Local Run epic1848-direct-local-20261012-001 and Public Run epic1848-direct-public-20261012-001. Its four decomposing Tasks are complete; final reconciliation is recorded by CA-P-1870.
- Public evidence: Run epic1848-direct-public-20261012-001 completed for 0.4.3; PR https://github.com/anatoly-m-maslennikov/caprmedio-graph-driven-framework/pull/27. Journal started Event 803fbb4b-8b3a-4a2a-9839-a65251d46e02; completed Event 8bdb213a-13be-4f26-9c87-0a44dfc30b34.

- Public completion receipt: .caprmedio_tmp/epic1848/direct-public-completion.md.

## Definition of Done

The Objective is implemented and verified with actual evidence appropriate to this task. Record remaining manual issues. Mock tests do not prove live release, installation, MCP or PR completion.
