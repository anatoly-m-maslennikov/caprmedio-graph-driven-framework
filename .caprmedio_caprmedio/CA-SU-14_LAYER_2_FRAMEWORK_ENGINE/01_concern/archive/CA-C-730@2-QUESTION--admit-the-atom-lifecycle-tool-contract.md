---
identity:
  id: CA-C-730
  ref_id: CA-C-730@2
context:
  container:
    scope_unit: CA-SU-14
  role: Concern
  form: Question
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 3
state:
  status: Archived
  version: 2
  updated_at: 2026-11-11 06:54:38 +0400
destination:
  file:
    name: CA-C-730@2-QUESTION--admit-the-atom-lifecycle-tool-contract.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/01_concern/archive
author: Anatoly Maslennikov
relations:
  concern_about:
  - CA-O-127
  - CA-P-2934
  - CA-O-128
  - CA-R-1093
  - CA-M-374
  - CA-D-623
  - CA-R-1432
  - CA-R-1788
  - CA-E-521
---

## Summary

Admit the Atom Lifecycle Tool contract

## Concern

Which operations and invalid-input behavior should the new MCP Tools expose under P2934? Current O127 admits seven operations in one Workflow, including Move. It waits for an additional input dictionary on a format or allowed-value error and allows cancellation while waiting. The six separate Workflow drafts remain unadopted and omit Move.

## Details

Select the Current combined operation contract or review and adopt the split contracts with a disposition for Move. Decide how a new Tool obtains corrected input when no generic Workflow engine is in scope. The retained MCP provider has transport cancellation but no lifecycle input continuation. An immediate invalid-input result would change the Current waiting behavior.

The retirement removed the old lifecycle effect adapters. Retained metadata, Header, scope and Journal primitives can support new effects. Direct Update of an exactly selected carrier has Current requirements for persisted readback, unchanged ID, Version and Updated At, and preservation of omitted properties. Current R1093, M374 and D623 require every changed same-ID edit to advance Version and Updated At and retain history. O128, R1432, R1788 and E521 require Direct Update to preserve those values. Before implementing a persisted Direct Update, decide which rule governs and reconcile the affected sources. The exact old/new scalar patch shape is already available in R1934 and D623. Prepare disposable fixtures while this decision is open.

The installed MCP SDK supports same-call form elicitation. Native Codex's support is unverified. Check the actual client and decide the unsupported-client response. Cancellation must remain possible while waiting for correction and must preserve the Action boundary.
