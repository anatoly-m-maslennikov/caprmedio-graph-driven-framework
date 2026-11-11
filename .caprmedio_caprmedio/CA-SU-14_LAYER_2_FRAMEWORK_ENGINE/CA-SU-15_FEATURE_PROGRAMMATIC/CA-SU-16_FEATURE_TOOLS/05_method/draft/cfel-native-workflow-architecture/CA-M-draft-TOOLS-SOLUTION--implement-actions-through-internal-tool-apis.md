---
identity:
  atom_id: CA-M-draft
context:
  container:
    scope_unit: CA-SU-16
  role: Method
  form: Solution
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Architecture <+ Communication <+ Interface Contracts
  tier: 0
state:
  status: Draft
  version: 1
  updated_at: 2026-11-11 04:14:10 +0400
destination:
  file:
    name: CA-M-draft-TOOLS-SOLUTION--implement-actions-through-internal-tool-apis.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/05_method/draft/cfel-native-workflow-architecture
author: Anatoly Maslennikov
---

## Summary

Implement Actions through internal Tool APIs

## Claim

### Prose Claim

Implement code-backed Actions through registered internal Tool APIs and adapters. Keep each Action's input/output and business contract distinct from the concrete code that fulfills it. Reuse canonical implementation models at the binding boundary, and let the Workflow Engine invoke that capability through the declared Action contract.

## Semantics

Tools own their implementation behavior and results; Workflow definitions own composition, sequencing and branches, and MCP owns public exposure. A Tool may call libraries or helpers without making every function another public capability. Direct internal API use remains available to Engine components under their applicable contracts; it does not create a public MCP Tool.

Resolve implementations from trusted installed code/configuration and explicitly activated extensions. A Project Workflow can select an admitted Action binding but cannot grant itself a new code entrypoint, effect permission or extension activation. Validate the declared arguments/results at the shared boundary and use the common error-handling mechanism rather than copying wrappers into every Action.

## Details

This proposed TOOLS Method / Solution requires adoption of the companion TOOLS Scope Delegation amendment. The Current delegation does not grant that Form. Tier 0 is the requested architectural placement, not a claim that Current admission or governing-relation ordering has already passed.
