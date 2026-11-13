---
identity:
  atom_id: CA-D-706
  ref_id: CA-D-706@1
context:
  container:
    scope_unit: CA-SU-15
  role: Delivery
  form: Decision
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Architecture <+ Communication <+ Interface Contracts
  tier: 6
state:
  status: archived
  version: 1
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-D-706@1-DECISION--deliver-the-generic-codex-hook-independently-of-plugins.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/07_delivery/099_archived
relations:
  delivery_for:
  - CA-M-517
author: Anatoly Maslennikov
---

## Summary

Deliver the generic Codex hook independently of plugins

## Claim

### Prose Claim

Keep the generic hook source and its tests in the Project under CODEX_HOOK after that Scope Delegation is adopted. Deliver the host command and configuration independently of the Workbench plugin. Preserve unrelated host hooks.

The hook reads Codex JSON input and changes only the CAPRMEDIO request context. Test the receiving MCP schema and gateway together with the hook payload before enabling the installed host hook. Installation, host activation and a successful runtime call are separate checks.
