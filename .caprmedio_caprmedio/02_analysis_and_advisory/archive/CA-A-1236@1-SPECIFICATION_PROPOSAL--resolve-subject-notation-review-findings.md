---
atom_id: CA-A-1236@1
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject
version: 1
updated_at: 2026-10-28 15:55:54 +0400
relations: {}
tier: 3
---
# Summary

Resolve Subject notation review findings

## Question

How should the six Subject operators be defined after the completed SoTA harvest and design challenge, without changing Current sources before decisions are resolved?

## Status and scope

This is the disposition tracker and Specification Proposal for both completed FPF steps: SoTA harvest and design challenge, run `722e48a9-7d60-49c3-a623-e8129eb67005`, plus the explicitly carried Candidate #11 findings. The Plan, both steps and final result passed independent validation. The latest Operator input overrides older Candidate #11 and A1233 grouping notation. This proposal is not adoption, promotion, migration or runtime validation.

The proposed alphabet is `/` specialization with applicable inheritance, `//` named instance, `.` dependent/property, `:` allowed value rather than assignment, `::` organizational membership without inheritance, and `>` structural containment. No `<:` or `>:` replacement is proposed. No new native membership Relation Type is assumed by syntax alone.

Only methodology Drafts and this tracker are edited. Existing Current sources, source Subject selectors, generated Projections, Tools and runtime remain unchanged. Previously prepared successors are refined in place; no competing next-version Draft is created. Governing Subjects retain their current canonical selectors until identity and mixed-path rules are settled.

## Review evidence

The harvest contains 14 primary-source cards in four distinct families: mathematics/types, qualified names, knowledge/constraints, and model/view notation. Precedents do not establish exact equivalence, universal standard status, or empirical readability. Primary references include [Rust paths](https://doc.rust-lang.org/reference/paths.html#canonical-paths), [SKOS collections](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#collections), [SHACL allowed values](https://www.w3.org/TR/2017/REC-shacl-20170720/#InConstraintComponent), and [UML multiplicity](https://www.omg.org/spec/UML/2.5.1/PDF#page=75).

Temporary review artifacts are at `/tmp/fpf-2026-10-28-subject-relation-notation-review-and-sota-harvest-722e48a9-7d60-49c3-a623-e8129eb67005/`: step-001 is the harvest, step-002 is the challenge, and final is their validated consolidation. Their retention is temporary; this document records the durable decisions and work state without copying a large report. The earlier review report is unavailable; its carried finding states come from the retained conversation summary, not a claimed reread.

## Issue and proposal tracker

| Issue | Proposed resolution | State | Drafts / decision |
|---|---|---|---|
| C11-I01 / C11-F01 | Separate structural containment from whether each child requires a container. The Operator's standalone-kind convention may be an explicit schema declaration; it must not be inferred anew from a selected display. | Pending Operator decision | R1931, R2150; Q01 first |
| NT-I01 / NT-F01 | Organizational membership does not duplicate canonical targets. Define how different membership/classification paths reach one target while different same-label targets remain distinct. | Pending Operator decision | R1931, R2209, R2150 |
| NT-I02 / NT-F02 | Treat // and :: as single tokens; preserve qualified Atom kinds, endpoint direction and the separation of parsing from native relation admission. Resolve literal delimiter handling and permitted mixed paths. | Partly Drafted; remaining choices pending | R1931, R2150, R2222 |
| SG3-I02 / SG3-F02 | No inheritance through organizational membership or structural containment; preserve actual specialization inheritance. | Semantics Decided; Drafted; not Applied/Verified | R2209, R2150, R2222 |

Historical/new confidence is as in the validated review: C11-I01 99% / F01 97%; NT-I01 97% / F01 96%; NT-I02 98% / F02 97%; SG3-I02 historical 99% / F02 historical 97%. These are analytical assessments, not proof of an applied repair.

## Draft register

| Current Atom | Proposed Draft | Change | State |
|---|---|---|---|
| CA-R-2209@2 | CA-R-2209@3-draft | Project Model membership uses ::, not > or inheriting /. | Refined Draft |
| CA-R-1931@12 | CA-R-1931@13-draft | Add atomic :: membership; preserve five existing operators and explicitly track unresolved grammar/containment choices. | Refined Draft |
| CA-R-2150@10 | CA-R-2150@11-draft | Render membership separately; preserve source meaning and canonical identity across selected views. | Refined Draft |
| CA-R-2222@1 | CA-R-2222@2-draft | Block inheritance through :: and >; retain actual broader-kind and qualified-kind inheritance. | Refined Draft |

M/E/D sources are being checked for directly relevant successors; do not create a role merely to fill the acronym. Draft existence does not close an issue or authorize promotion.

## Questions and decisions

Ask one non-obvious question at a time, with context and blast radius. Record each answer here and refine the relevant Drafts before the next question. Do not re-ask settled operator meanings or start another FPF review.

### Q01 — more than one permitted container kind

If the complete declared structure contains `X > Y` and `Z > Y`, with no standalone Y, must every Y belong to at least one permitted container kind, or to both kinds? The latest standalone convention settles mandatory versus optional containment but not this combination.

Proposed reading: at least one permitted container; exact numbers and exclusive ownership remain separately governed. This is not accepted yet. It affects Workflow/Step nesting, Packages/Modules and container Atoms. Status: Awaiting answer.

## Evidence gaps and acceptance

| Gap | Handling / next action |
|---|---|
| C11-G01 | Settle the containment declaration and cardinality reading through the question sequence. |
| NT-G03 | Settle canonical identity and mixed grammar through the same sequence. |
| NT-G02 | Readability is unmeasured; no mandatory user study is introduced. |
| NT-G01 | Preserve historical states; recover the prior report only if exact reconciliation becomes necessary. |
| SG3-G02 | Source Drafts are prepared; applied repair and full inheritance checks remain later work. |

Before any promotion, resolve pending choices, read back the final Drafts against those answers, and identify the bounded source/projection checks. No parser implementation, full migration, unrelated graph cleanup or runtime change is included.
