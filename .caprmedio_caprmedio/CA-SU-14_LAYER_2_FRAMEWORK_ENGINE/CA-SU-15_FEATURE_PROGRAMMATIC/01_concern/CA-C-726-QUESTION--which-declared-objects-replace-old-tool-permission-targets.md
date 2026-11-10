---
identity:
  atom_id: CA-C-726
  ref_id: CA-C-726
context:
  container:
    scope_unit: CA-SU-15
  role: Concern
  form: Question
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Scope Unit
  tier: 4
state:
  status: Resolved
  version: 3
  updated_at: 2026-11-10 22:25:42 +0400
destination:
  file:
    name: CA-C-726-QUESTION--which-declared-objects-replace-old-tool-permission-targets.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/01_concern
relations:
  concern_about:
  - CA-R-2655
  - CA-R-2657
  - CA-R-2658
author: Anatoly Maslennikov
---

## Summary

Which declared objects replace old Tool permission targets?

## Concern

The TOOLS, TOOL_WORKFLOWS and PROJECT_TOOLS delegation Drafts still name retired or unverified model objects in their exact target whitelists. Examples include Graph Rule, Tool, Scope Unit.Path and obsolete Atom property paths. An unresolved address grants no permission; substituting a broad parent would change the allowed work.

## Details

Keep these three permission Drafts unadopted and their Current declarations unchanged. Their old Tool implementations and local specifications are already deferred. Resolve their exact targets when those Tools are rebuilt, using established Model declarations rather than aliases or invented entities. Other Engine source work continues.

Blast radius: the permission refresh in R2655, R2657 and R2658 only. No Scope Unit moves, Current source changes or runtime changes.

## Resolution

The Operator clarified that the old Tools are fully retired, not deferred for rebuilding. Withdraw the R2655, R2657 and R2658 permission-update Drafts and preserve their exact bytes in history. No permission-target migration or old-Tool implementation is queued.

This answers the pending permission question. The Operator confirmed that full retirement is already complete. No additional old-Tool retirement, permission migration or rebuilding work is queued by this Question.
