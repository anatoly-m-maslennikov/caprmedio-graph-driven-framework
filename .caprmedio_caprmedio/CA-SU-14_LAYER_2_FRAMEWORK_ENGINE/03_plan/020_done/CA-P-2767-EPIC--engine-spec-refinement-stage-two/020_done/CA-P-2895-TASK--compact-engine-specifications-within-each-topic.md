---
identity:
  id: CA-P-2895
  ref_id: CA-P-2895
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
  status: Done
  version: 3
  updated_at: 2026-11-10 19:14:23 +0400
destination:
  file:
    name: CA-P-2895-TASK--compact-engine-specifications-within-each-topic.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2767-EPIC--engine-spec-refinement-stage-two/020_done
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

- [x] Review same-topic contributions within each Scope Unit. (Repeat batches, each up to 15–20 min.)
- [x] Compare each topic with its broader topics and narrower branches; review shared versus specific contributions, repetition, conflicts and justified placement.
- [x] Review Approach Policy candidates within each branch and their Solution, Decision and Direct Policy cases; check applicability and explicit SPECIALIZES links.
- [x] Review cross-Scope overlap, permissions and justified promotion/demotion.
- [x] Prepare survivor Drafts, obsolete-source dispositions and incoming-reference repairs.
- [x] Independently review and fix coverage, DRY, Roles, Forms and relationships.
- [x] Recheck changed topics, permissions, numeric ordering and combined acceptance before adoption.

## Definition of Done

Each topic has a compact, coherent source set with preserved unique behavior, one clear authority per contribution and recorded merge/retirement decisions. The review covers within-topic and broader-to-narrower relationships. Approach Policy candidates and concrete cases have evidence-backed Form and relation decisions. Supporting MED adds implementation or verification meaning. No merge is justified by topic membership alone.

## Final source checkpoint

Reviewed topic contributions within and across Scope boundaries. Consolidated cache/result ownership, grid and watcher construction, technical logging, source provenance and prompt delivery; repaired duplicate permissions. M222 is the conditional interface Approach with M466 as its concrete frontend Solution; backend containment does not imply that UI case. E792 is reusable Direct Policy. Supporting MED preserves distinct realization or evaluation meaning. Changed sources passed bounded independent rechecks; final combined adoption preparation remains P2857.
