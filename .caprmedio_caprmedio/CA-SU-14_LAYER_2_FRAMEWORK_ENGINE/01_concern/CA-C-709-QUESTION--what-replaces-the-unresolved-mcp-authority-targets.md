---
identity:
  id: CA-C-709
  ref_id: CA-C-709
context:
  container:
    scope_unit: CA-SU-14
  role: Concern
  form: Question
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 3
state:
  status: Resolved
  version: 2
  updated_at: 2026-11-09 15:11:21 +0400
destination:
  file:
    name: CA-C-709-QUESTION--what-replaces-the-unresolved-mcp-authority-targets.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/01_concern
author: Anatoly Maslennikov
relations:
  concern_about:
  - CA-R-1847
  - CA-D-547
  - CA-P-2767
---

## Summary

What replaces the unresolved MCP authority targets?

## Question

What replaces the unresolved MCP authority targets?

## Details

D576 and E582 link to M339 and R1882, neither of which resolves to a Current authority in the reviewed graph. Keep the two Current sources and proposed Drafts unchanged. Identify an admitted replacement authority or explicitly retire the contract after reviewing its meaning; do not invent target IDs.

### Resolution

Resolved by the Operator-approved withdrawal of D576@14 and E582@15 without replacements. Their retired authorities M339/R1882 are not rebound or recreated. The obsolete 15-to-16-route Release-admission publisher and refresh gate are not part of the Current direct local/public Release contracts under R1847/D547. C470 is closed as obsolete; resolved historical C496/C497 remain byte-for-byte unchanged. Actual release Workflows, runtime code and stored history were not modified by this cleanup.
