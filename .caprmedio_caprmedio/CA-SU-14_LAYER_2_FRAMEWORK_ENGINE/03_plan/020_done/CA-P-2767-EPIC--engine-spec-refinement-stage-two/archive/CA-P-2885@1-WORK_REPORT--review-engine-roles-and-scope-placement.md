---
identity:
  id: CA-P-2885
  ref_id: CA-P-2885@1
context:
  container:
    atom: CA-P-2767
  role: Plan
  form: Work Report
  label: Work Report
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
state:
  status: Archived
  version: 1
  updated_at: 2026-11-10 07:12:26 +0400
destination:
  file:
    name: CA-P-2885@1-WORK_REPORT--review-engine-roles-and-scope-placement.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2767-EPIC--engine-spec-refinement-stage-two/archive
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2871
---

## Summary

Review Engine Roles and Scope placement

## Details

Role/Scope review is in progress, using one Scope Unit per read-only lane. Current sources remain unchanged; corrections use Drafts.

Prepared Core-owned Drafts for the existing Workspace and View definitions without changing their Claims or identities. R2998 retains its visible diagnostic result and report semantics; M525 holds the existing profiler realization. Added the missing frontend-topic authority to M492, removed M167's obsolete method_for R1105 link, and supplied the explicit Engine owner for the AGENTIC delegation.

Independent corrected-batch review is pending. Later MECE/DRY, Forms, relations, policy alignment and Tiers remain separate gates. No Draft has been promoted and no runtime code has changed. P2883 requires rebuilding, checking and fixing the main-subject graph after adoption and before implementation.
