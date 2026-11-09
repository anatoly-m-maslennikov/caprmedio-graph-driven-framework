---
identity:
  id: CA-C-706@1
  ref_id: CA-C-706@1
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
  version: 1
  updated_at: 2026-11-09 05:53:06 +0400
destination:
  file:
    name: CA-C-706@1-QUESTION--how-should-unexposed-engine-med-content-be-reviewed.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/01_concern/archive
author: Anatoly Maslennikov
relations:
  concern_about:
  - CA-P-2768
  - CA-P-2767
---

## Summary

How should unexposed Engine MED Content be reviewed?

## Question

Should the additional 35 Current MED Atoms with no query-exposed Content be migrated after declared legacy Content is made readable, or be retired after a separate source review?

## Details

The selected Engine corpus has110 MED Atoms with no exposed Summary,Claim,Semantics orDetails.64 arePROGRAMMATIC-local and11APPS-local, already covered by the prior legacy deferral. The expanded scope adds30MCP,4WORKFLOW_ORCHESTRATOR and1PROMPTS sources.

Continue with the213 readable MED Atoms. Keep all110 unavailable sources unchanged and marked Held in the inventory. Do not infer their Claims from filenames or metadata, treat them as passed, substitute raw-source analysis, or implement a reader change in this specification Epic. The follow-up Epic will carry a scoped Content-exposure prerequisite and a subsequent source-review task for the additional holds. The existing78-RMEDO deferral remains in effect; its other Role members are not part of the323-MED review count.

The exact source IDs, owner and reviewed versions are recorded in CA-P-2767/inventory.tsv. This Question records the safe continuation and the remaining migration choice; it does not grant retirement or reader implementation authority.
