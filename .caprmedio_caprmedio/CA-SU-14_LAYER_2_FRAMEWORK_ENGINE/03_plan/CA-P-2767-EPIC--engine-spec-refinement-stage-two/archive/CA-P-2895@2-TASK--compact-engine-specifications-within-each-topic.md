---
identity:
  id: CA-P-2895
  ref_id: CA-P-2895@2
context:
  container:
    atom: CA-P-2767
  role: Plan
  form: Plan
  label: Task
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
state:
  status: Archived
  version: 2
  updated_at: 2026-11-10 15:36:56 +0400
destination:
  file:
    name: CA-P-2895@2-TASK--compact-engine-specifications-within-each-topic.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2767-EPIC--engine-spec-refinement-stage-two/archive
author: Anatoly Maslennikov
relations:
  IS_BLOCKED_BY:
  - CA-P-2894
---

## Summary

Compact Engine specifications within each topic

## Objective

Review each topic internally and from broader to narrower topics after per-Atom compaction. Merge duplicate contributions, remove repeated detail and keep only useful supporting MED around the outcome Requirements.

## Subtasks

- [ ] Review same-topic contributions within each Scope Unit. (Repeat batches, each up to 15–20 min.)
- [ ] Compare each topic with its broader topics and narrower branches; review shared versus specific contributions, repetition, conflicts and justified placement.
- [ ] Review Approach Policy candidates within each branch and their Solution, Decision and Direct Policy cases; check applicability and explicit SPECIALIZES links.
- [ ] Review cross-Scope overlap, permissions and justified promotion/demotion.
- [ ] Prepare survivor Drafts, obsolete-source dispositions and incoming-reference repairs.
- [ ] Independently review and fix coverage, DRY, Roles, Forms and relationships.
- [ ] Recheck changed topics, permissions, numeric ordering and combined acceptance before adoption.

## Definition of Done

Each topic has a compact, coherent source set with preserved unique behavior, one clear authority per contribution and recorded merge/retirement decisions. The review covers within-topic and broader-to-narrower relationships. Approach Policy candidates and concrete cases have evidence-backed Form and relation decisions. Supporting MED adds implementation or verification meaning. No merge is justified by topic membership alone.
