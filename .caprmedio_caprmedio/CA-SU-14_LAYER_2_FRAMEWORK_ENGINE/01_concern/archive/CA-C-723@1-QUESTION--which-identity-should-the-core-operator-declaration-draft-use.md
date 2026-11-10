---
identity:
  id: CA-C-723
  ref_id: CA-C-723@1
context:
  container:
    scope_unit: CA-SU-14
  role: Concern
  form: Question
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
state:
  status: Archived
  version: 1
  updated_at: 2026-11-10 09:17:30 +0400
destination:
  file:
    name: CA-C-723@1-QUESTION--which-identity-should-the-core-operator-declaration-draft-use.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/01_concern/archive
relations:
  concern_about:
  - CA-R-2953
  - CA-P-2858
author: Anatoly Maslennikov
---

## Summary

Which identity should the Core Operator Declaration Draft use?

## Concern

CA-R-2953 is already a Current Workbench Requirement for read-only result sorting, filtering and grouping. A separate Core Draft uses the same Atom ID for the Operator Declaration Form. They define different contributions; the Core Draft is not a new Version of the Workbench Requirement.

## Details

Preserve the existing Workbench identity. The proposed treatment is to give the unrelated Core Draft an unused canonical ID in its owning source lane and repair only its actual references. Do not let a global Draft-preference lookup shadow the Engine Requirement.

Current: `.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/CA-R-2953-WORKBENCH-SOLUTION--query-results-support-read-only-sorting-filtering-and-grouping.md`.

Unrelated Draft: `.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/CA-R-2953@1-draft-CORE_META_MODEL-DECLARATION--declare-operator-declaration-as-a-requirement-form.md`.

Blast radius: this pair's identity and its actual consumers. The Core Draft is outside this Engine refinement pass, and neither source is renamed, promoted or retired by this Question. The scoped candidate inventory keeps the existing Workbench contribution.
