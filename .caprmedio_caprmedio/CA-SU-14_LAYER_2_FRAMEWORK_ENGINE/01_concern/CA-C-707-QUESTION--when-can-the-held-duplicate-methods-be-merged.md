---
identity:
  id: CA-C-707
  ref_id: CA-C-707
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
  updated_at: 2026-11-09 14:24:58 +0400
destination:
  file:
    name: CA-C-707-QUESTION--when-can-the-held-duplicate-methods-be-merged.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/01_concern
author: Anatoly Maslennikov
relations:
  concern_about:
  - CA-M-284
  - CA-M-425
  - CA-P-2767
---

## Summary

When can the held duplicate Methods be merged?

## Question

When can the held duplicate Methods be merged?

## Details

Resolved after the Operator resumed only E260/E261/E360/E361/E366/E454. Their Draft carriers were normalized mechanically and read through query_run. Independent same-Scope reviews and fresh indexed rechecks preserved unique coverage.

M417@10 was absorbed by M284@30; M426@10 was absorbed by M425@14. The two predecessors are Archived and no longer have Current rows. The surviving policies retain IS_REPLACEMENT_FOR links. M284 needed no extra policy wording; M425 preserves the pure-computation and recording-owner boundary in Details.

All six Evaluations were adopted. E454 now targets only M284. Already-reviewed M399/E648 were also repaired: M399 Tier 5 targets M425 Tier 4; E648 Tier 6 evaluates M399 and M425. No unrelated deferred source was resumed. The remaining prior hold is 69 MED Atoms.

Source retirement initially left stale rows after the watcher reported idle. A Workbench full reread removed them; all ten Current Versions, Tiers and links were then verified. C712 records that implementation defect. No runtime code or native Workflow Run was created here.
