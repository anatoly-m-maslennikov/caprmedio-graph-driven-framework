---
identity:
  atom_id: CA-M-421
  ref_id: CA-M-421
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Direct Policy
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Authoring <+ Code Authoring
    dependencies: []
  tier: 3
state:
  status: Active
  version: 13
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-M-421-PROGRAMMATIC-DIRECT_POLICY--reuse-suitable-established-solutions.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method
current_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---

## Summary

Reuse suitable established solutions

## Claim



### Prose Claim
**To** implement declared PROGRAMMATIC behavior, prefer well-adopted, well-suited existing libraries, approaches and tools over reimplementing their mechanics; use custom mechanics **when** existing solutions cannot meet a declared requirement **or** the custom choice provides a concrete benefit.

At the real library boundary, verify the selected solution's public API, actual defaults and event behavior; do not let assumed local behavior contradict the system contract.

## Details

### Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and tests.


- Check existing Project capabilities and established solutions for actual fit, not popularity alone.
- Consider the complexity and dependency cost introduced by the choice.
- Keep custom work limited to the unmet requirement or demonstrated benefit. This Method selects no mandatory product or technology. A library default is not evidence of contract conformance: verify the real boundary for behavior such as sorting scope or popup theme and zoom, then configure or adapt it when the default conflicts with the declared behavior.

The Operator explicitly selected reuse of well-adopted and suitable libraries, approaches and tools instead of reinventing the wheel on 2026-10-15.
