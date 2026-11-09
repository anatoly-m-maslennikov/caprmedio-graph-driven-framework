---
identity:
  id: CA-C-710
  ref_id: CA-C-710
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
  updated_at: 2026-11-09 15:56:54 +0400
destination:
  file:
    name: CA-C-710-QUESTION--where-should-the-mcp-release-delivery-live.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/01_concern
author: Anatoly Maslennikov
relations:
  concern_about:
  - CA-D-577
  - CA-P-2767
---

## Summary

Where should the MCP release delivery live?

## Question

Where should the MCP release delivery live?

## Details

D577 concerns project-specific release delivery. Its ownership needs coordination with Project Configuration and release Workflow authority outside this bounded MED correction. Keep the Current source and proposed Draft unchanged pending that handoff. Do not move it merely to satisfy ancestry.

## Resolution

The Operator chose whole-project release ownership in FRAMEWORK_DELIVERY, reusing RELEASES / CA-SU-27 as a direct child of Project. This supersedes the earlier Project Configuration destination. The complete local/public Workflow and release-specific RMED families, including D577 and its recovery authorities, are now Current there. The external Goal remains Project-owned. Query readback verified all 80 moves, the stable Scope Unit ID and unchanged Scope Unit census. Implementation and test relocation is deferred to CA-P-2839 in CA-P-2791; no release execution or code change is claimed.
