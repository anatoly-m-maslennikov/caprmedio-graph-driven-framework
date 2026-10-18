---
subjects:
  governs: "Entity/Continuant/Node/Atom/Content Role: Operations/Type: Workflow"
  depends_on:
    ["Entity/Occurrent/Execution/Workflow Run", "Entity/Continuant/Node/Atom/Content Role: Operations/Type: Step", "Entity/Continuant/Node/Atom/Content Role: Operations/Type: Action", "Entity/Continuant/Relation/Type: On Result", "Entity/Continuant/Node/Atom", "Entity/Continuant/Node/Actor/Type: Operator"]
version: 9
updated_at: "2026-10-18 03:34:25 +0400"
relations: {"evaluation_for": ["CA-R-1519", "CA-R-1520"]}
atom_id: "CA-E-489"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/06_evaluation/CA-E-489-CORE_META_MODEL-QA_CASE--validate-workflow-execution-and-handoff-definitions.md
  source_atom_id: CA-E-489
  source_atom_revision: 9
  source_sha256: 738f669753751f30ec9cd81b79afa160ea6a1ad9191ce241bb13cf851f2bac7c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Validate Workflow execution and handoff definitions

## Scope

a Workflow's declared execution **and** handoff behavior.

## Claim

the Evaluation **must** check whether a Workflow's declared execution **and** handoff behavior is well formed under CA-R-1519 **and** CA-R-1520, independently of current executor availability.

## Details

### Cases and expected results

- complete input declarations, resolvable Action references, admitted transitions, explicit terminal outcomes, **and** declared capability requirements: pass this definition check **without** requiring a running executor.
- a missing required input declaration, unresolved definition reference, missing continuation-selection rule, **or** absent applicable approval condition: reject the affected definition.
- a well-formed definition whose selected executor lacks a declared capability, worker, **or** current permission: the definition remains valid; execution admission is blocked under CA-R-1519. do **not** report unavailable execution as malformed authority.
- a missing invocation input **or** runtime resource is an execution-admission problem rather than a definition defect **when** its required binding is correctly declared.
- a terminal handoff declares the target Revision, complete continuation inputs, reason, check evidence, **and** performed-effect account: accept its declared continuation boundary.
- a handoff definition resumes predecessor Steps, claims successor success **before** execution, bypasses approval, resets retries, **or** admits an unbounded continuation cycle: reject.
- a cross-Workflow ON_RESULT Step edge offered as a Run handoff: reject; the two relations have different endpoints **and** responsibilities.

report the exact failing source **and** condition. definition validity **must not** be reported as permission, execution readiness, successful execution, **or** evidence that a Run occurred.
