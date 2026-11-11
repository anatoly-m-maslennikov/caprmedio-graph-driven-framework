---
identity:
  id: CA-C-718
  ref_id: CA-C-718
context:
  container:
    scope_unit: CA-SU-45
  role: Concern
  form: Question
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
state:
  status: Resolved
  version: 2
  updated_at: 2026-11-10 22:20:17 +0400
destination:
  file:
    name: CA-C-718-QUESTION--which-body-properties-should-non-rmedo-query-rows-expose.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/01_concern/021_resolved
relations: {}
---

## Summary

Which body properties should non-RMEDO query rows expose?

## Concern

The current compiled Content schema exposes Summary, Claim, Operation, Semantics and Details. It has no primary body column for Concern, Plan or Analysis & Advisory content. Eligible rows can therefore exist in the query index while their substantive role-specific body is unavailable.

## Details

First check whether existing generic Content Declarations already admit these sections and need compiler support, or whether role-specific Declarations are missing. Do not relabel these bodies as RMED Claims or add raw undeclared Content columns. Core model changes need their own reviewed source handoff; structure-only Engine edits cannot invent that authority. Include these Atoms in the refinement inventory rather than restoring a blanket hold.

## Resolution

The Operator approved query access to CAPRMEDO and rebuilding the model from Declarations on every image rebuild, including Roles and Forms. Current R2726, M500, M464, D672 and E675 now carry the requirement, generation/parsing method, delivered asset and acceptance cases. Applicable wildcard Content declarations and more-specific boundaries govern exposed sections; non-RMEDO bodies retain their own sections.

P2866 tracks implementation and tests. This resolves the model/reader specification decision, not runtime query accessibility; no image or service has been rebuilt by this source update.
