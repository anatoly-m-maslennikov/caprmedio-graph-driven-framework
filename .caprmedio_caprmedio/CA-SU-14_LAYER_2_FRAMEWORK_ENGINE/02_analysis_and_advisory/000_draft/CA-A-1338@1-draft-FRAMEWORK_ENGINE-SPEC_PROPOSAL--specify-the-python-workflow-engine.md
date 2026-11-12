---
identity:
  atom_id: CA-A-1338
  ref_id: CA-A-1338@1-draft
context:
  role: analysis_and_advisory
  form: Spec Proposal
  container:
    scope_unit: CA-SU-14
  tier: 3
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution
      Control
state:
  version: 1
  status: draft
  updated_at: '2026-11-12T01:57:49.614430+00:00'
destination:
  file:
    name: CA-A-1338@1-draft-FRAMEWORK_ENGINE-SPEC_PROPOSAL--specify-the-python-workflow-engine.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory/000_draft
---
## Summary

Specify the Python Workflow Engine

## Proposal

Use one reviewed Python entry point in the Workflow Atom's Formal Claim for business logic and Action order. The Engine binds the exact Workflow, Step, and Action revisions and provides typed input, Action invocation, and results. Actions own effectful I/O.

This is the specification packet for [CA-P-3020](../../03_plan/CA-P-3018-EPIC--adopt-the-workflow-engine-and-migrate-cfel-claims-to-python/020_done/CA-P-3020-TASK--specify-the-workflow-engine-in-rmed.md) in Epic CA-P-3018. [CA-A-1337](../../02_analysis_and_advisory/020_done/CA-A-1337-FRAMEWORK_ENGINE-ANALYSIS_REPORT--compare-atom-lifecycle-workflows-with-their-implementation.md) records the six lifecycle comparisons and their verification.

## Rationale

The lifecycle code already has reusable preparation and effect paths. The pilot can reuse those paths and move execution order into a readable Workflow. Explicit Run outcomes make successful writes, partial effects and failures visible through both API and MCP. The Eval Case includes the Operator's recursive Backlog-to-Active rule and a Draft-child regression.

The earlier CFEL-native Workflow proposal is superseded for the choice of executable Workflow language. Its reusable Action and interface ideas can be reviewed independently. CA-P-3022 tracks CFEL schema and expression migration.

## Adopted Engine RMED

| Atom | Role and Form | Contribution |
|---|---|---|
| [CA-R-970308662@1](../../04_requirement/CA-R-970308662-FRAMEWORK_ENGINE-REQUIREMENT--report-workflow-execution-outcomes-and-effects.md) | Requirement / Requirement | Report Workflow execution outcomes and effects |
| [CA-M-1007@1](../../05_method/CA-M-1007-FRAMEWORK_ENGINE-SOLUTION--execute-workflow-business-logic-in-python.md) | Method / Solution | Execute Workflow business logic in Python |
| [CA-E-825@1](../../06_evaluation/CA-E-825-FRAMEWORK_ENGINE-EVAL_CASE--verify-python-workflow-execution-with-lifecycle-cases.md) | Evaluation / Eval Case | Verify Python Workflow execution with lifecycle cases |
| [CA-D-719@1](../../07_delivery/CA-D-719-FRAMEWORK_ENGINE-DECISION--deliver-matching-workflow-and-action-revisions.md) | Delivery / Decision | Deliver matching Workflow and Action revisions |

## Review and adoption

- The separate project-wide Role/Form policy is tracked in [CA-R-3006@10-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-3006@10-draft-CORE_META_MODEL-DECLARATION--declare-scope-delegation.md) and [CA-R-3008@9-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-3008@9-draft-CORE_META_MODEL-REQUIREMENT--establish-project-and-non-project-scope-unit-declarations-and-delegations.md) . This policy would admit every model-valid Role and Form combination and keep Scope Delegations responsible for Main Subjects. The Analysis Report and Spec Proposal use this policy for local admission.
- CA-R-2653@4 admits the Execution Control and Test Design endpoints used by the Engine RMED. The Subject parser resolves their older and compact addresses to the same local expressions. Requirement / Requirement, Evaluation / Eval Case, and Delivery / Decision are local defaults. CA-R-2653@4 explicitly admits Method / Solution.
- CA-R-1519 and CA-R-1525 still govern Workflow conformance and revision binding. CA-R-1528 governs the Journal evidence for Tool calls. The new Requirement specifies what the caller receives.
- Internal calls use the Engine API. The separate CA-R-1111 restriction applies to the direct Markdown Atom Doer executable with `--apply`.
- The Current Status pilot compares accepted behavior with the existing route. Test the recursive activation rule and result reporting against the reviewed contract. Resolve the Version discrepancy before using a version-changing Workflow as a parity case.

All four Engine RMED Atoms are Active. CA-P-3021 carries the Python pilot. The separate model policy remains Draft. Workbench lists the authoritative CA-R-3006 Version 9 and CA-R-3008 Version 8 alongside older installed Version 7 copies. Resolve predecessor selection against the authoritative sources before promoting either model Draft.
