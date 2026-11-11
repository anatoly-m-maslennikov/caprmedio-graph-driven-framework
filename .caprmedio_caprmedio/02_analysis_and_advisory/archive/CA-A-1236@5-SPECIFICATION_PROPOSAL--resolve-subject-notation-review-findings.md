---
atom_id: CA-A-1236@5
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject
version: 5
updated_at: 2026-10-28 16:22:55 +0400
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
| C11-I01 / C11-F01 | Separate structural containment from whether each child requires a container. The Operator's standalone-kind convention may be an explicit schema declaration; it must not be inferred anew from a selected display. | Partly Decided; Drafted; Q02 pending | R1931, R2150, M232, E383; Q01 decided |
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

| Current Atom | Proposed Draft | Change | State |
|---|---|---|---|
| CA-M-228@28 | CA-M-228@29-draft | Author the six distinct operators without membership inheritance. | New Draft |
| CA-M-232@26 | CA-M-232@27-draft | Render membership separately and preserve source meaning across views. | New Draft |
| CA-E-383@34 | CA-E-383@35-draft | Check atomic ::, qualified kinds and non-inheriting membership/containment. | New Draft |
| CA-D-269@24 | CA-D-269@25-draft | Preserve operator characters in the existing scalar YAML carrier. | New Draft |

These four M/E/D Drafts use the Current sources in `.caprmedio_caprmedio/.../METHODOLOGY_SOURCES/001_CORE_META_MODEL`, not the older root-level copy. Scope remains the notation/semantic correction; unrelated old examples are not a general content migration. Draft existence does not close an issue or authorize promotion.

## Questions and decisions

Ask one non-obvious question at a time, with context and blast radius. Record each answer here and refine the relevant Drafts before the next question. Do not re-ask settled operator meanings or start another FPF review.

### Q01 — more than one permitted container kind

If the complete declared structure contains `X > Y` and `Z > Y`, with no standalone Y, must every Y belong to at least one permitted container kind, or to both kinds? The latest standalone convention settles mandatory versus optional containment but not this combination.

Operator answer: “Yes, each branch here is allowed option”.

Decision: branches are allowed alternatives, not simultaneous obligations. With no standalone Y alternative, each Y requires at least one permitted container kind. A standalone Y alternative permits no container. Exact parent counts and exclusive ownership remain separate cardinality rules; neither “exactly one” nor a ban on multiple parents is introduced by this answer. R1931, R2150, M232 and E383 Drafts are refined accordingly. Status: Decided and Drafted; not Applied or Verified.

### Q02 — vocabulary registration versus standalone containment

An entity kind can have an organizational membership path such as `Project Model::Step` (abbreviated illustration), while Step also has a structural role under Workflow or another Step. Does that organizational registration count as the standalone Y option?

Proposed reading: no. Standalone means a deliberate option in the declared containment structure; `::` membership only registers/organizes the concept. Otherwise registering every kind could accidentally make every containment optional. This proposal is not accepted yet. Blast radius: mandatory containment throughout the model and how membership and containment views are read. Status: Awaiting answer.


### Step and Substep correction

Operator: “No, step and substep are different”. This latest decision supersedes the previous nested-Step-only definition and the assistant's proposed `Workflow > Step >@ Step` rewrite. Preserve `Workflow > Step > Substep` as the structural example. This distinction does not itself decide specialization, property inheritance, Substep nesting, or all Type admission rules.

Prepared CA-R-1509@22-draft from Current CA-R-1509@21, removing the assertion that Substep is a nested Step rather than a separate kind. Prepared `CA-R-draft-CORE_META_MODEL-DEFINITION--define-substep.md` for the minimal distinct Substep definition; its proposed Operations/Type: Substep Subject is not yet promoted. Both are included in this tracker alongside the previous eight Drafts.

The proposed `>@` marker distinguishes an existing-kind reference from a declaration, but remains under discussion. It is not yet added to the operative grammar Draft or treated as a new Relation Type. Q02 must be reconsidered in this declaration/reference context rather than closed by the assistant's recursive-Step example.

### Q03 — reference marker scope

Does the proposed `@` existing-kind reference marker apply only to structural containment (`>@`), or consistently to organizational membership and specialization as well (`::@`, `/@`)?

Illustrative declaration and reference: Project Model `:: Scope Unit` declares its vocabulary entry; Continuant `/@ Scope Unit` points to that same kind and states its specialization, rather than defining another Scope Unit. These are explanatory short labels, not adopted canonical paths.

Proposed reading: use one declaration/reference distinction for these three structural operators. This could make multiple memberships/classifications explicit without duplicating kind identity. The alternative is to keep `@` limited to containment and govern identity of the other paths separately. No `@` syntax, native membership Relation Type, exact reference spelling, instance declaration or escaped-name rule is adopted by this question. Blast radius: Subject identity and grammar across the complete model. Status: Awaiting answer. Q02 remains pending; Q03 informs its declaration/reference interpretation.

## Evidence gaps and acceptance

| Gap | Handling / next action |
|---|---|
| C11-G01 | Settle the containment declaration and cardinality reading through the question sequence. |
| NT-G03 | Settle canonical identity and mixed grammar through the same sequence. |
| NT-G02 | Readability is unmeasured; no mandatory user study is introduced. |
| NT-G01 | Preserve historical states; recover the prior report only if exact reconciliation becomes necessary. |
| SG3-G02 | Source Drafts are prepared; applied repair and full inheritance checks remain later work. |

Before any promotion, resolve pending choices, read back the final Drafts against those answers, and identify the bounded source/projection checks. No parser implementation, full migration, unrelated graph cleanup or runtime change is included.
