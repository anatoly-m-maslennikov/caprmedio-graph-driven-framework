---
identity:
  id: CA-C-721
  ref_id: CA-C-721@1
context:
  container:
    scope_unit: CA-SU-14
  role: Concern
  form: Question
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering
  tier: 4
state:
  status: Archived
  version: 1
  updated_at: 2026-11-10 05:26:22 +0400
destination:
  file:
    name: CA-C-721@1-QUESTION--how-should-engine-topic-addresses-be-admitted.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/01_concern/archive
relations:
  concern_about:
  - CA-R-2560
  - CA-R-2483
  - CA-R-2653
  - CA-R-2654
---

## Summary

How should Engine topic addresses be admitted?

## Concern

Current Engine sources use CAPRMEDIO_STRUCTURE topic addresses, while the shared Declaration uses PROJECT STRUCTURE under CAPRMEDIO_MODEL. Some local Scope Delegations admit legacy Subject paths exactly. A topic can have the right meaning without an established exact canonical address or matching local admission.

## Details

Preserve the reviewed meanings and prepare source-bound topic Drafts. Before adoption, check each target against Current Declarations and the receiving Scope Delegation. Add only the missing local admissions; do not infer an equality between roots or replace operators globally.

The shared root bridge needs a Methodology decision outside this Engine source pass. Keep API, Workflow Run.Retry, History and UX Discovery and Navigation addresses explicit where an exact replacement remains unresolved. PROGRAMMATIC locally lists Provenance, but that admission does not by itself define a distinct topic or settle whether the shared Traceability topic should remain sufficient.

Proposed treatment: retain justified model and UX subjects, use the existing Engineering group where it fits, and review the bridge or missing declarations separately. Candidate topic Drafts do not establish new Current authority. Independent source review continues.

Blast radius: topic resolution and local permission checks for the changed Engine Drafts. No Claim rewrite, Scope tree change, source promotion, code change or runtime behavior is authorized by this Question.
