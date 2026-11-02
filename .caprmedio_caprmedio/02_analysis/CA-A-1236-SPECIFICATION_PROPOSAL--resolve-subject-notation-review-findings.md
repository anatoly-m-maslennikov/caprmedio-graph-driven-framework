---
atom_id: CA-A-1236
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject
version: 13
updated_at: 2026-10-28 17:16:26 +0400
relations: {}
tier: 3
---
# Summary

Resolve Subject notation review findings

## Question

How should the six Subject operators be defined after the completed SoTA harvest and design challenge, without changing Current sources before decisions are resolved?

## Status and scope

This is the disposition tracker and Specification Proposal for both completed FPF steps: SoTA harvest and design challenge, run `722e48a9-7d60-49c3-a623-e8129eb67005`, plus the explicitly carried Candidate #11 findings. The Plan, both steps and final result passed independent validation. The latest Operator input overrides older Candidate #11 and A1233 grouping notation. This proposal is not adoption, promotion, migration or runtime validation.

The proposed alphabet is `/` specialization with applicable inheritance, `//` named instance, `.` dependent/property, `:` allowed value rather than assignment, `::` organizational membership without inheritance, and `>` structural containment. No `<:` or `>:` replacement is proposed. The separately defined `@` modifier marks existing-kind references after `::`, `/` and `>`; it is not another relation operator. No new native membership Relation Type is assumed by syntax alone.

Only methodology Drafts and this tracker are edited. Existing Current sources, source Subject selectors, generated Projections, Tools and runtime remain unchanged. Previously prepared successors are refined in place; no competing next-version Draft is created. Governing Subjects retain their current canonical selectors until identity and mixed-path rules are settled.

## Review evidence

The harvest contains 14 primary-source cards in four distinct families: mathematics/types, qualified names, knowledge/constraints, and model/view notation. Precedents do not establish exact equivalence, universal standard status, or empirical readability. Primary references include [Rust paths](https://doc.rust-lang.org/reference/paths.html#canonical-paths), [SKOS collections](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#collections), [SHACL allowed values](https://www.w3.org/TR/2017/REC-shacl-20170720/#InConstraintComponent), and [UML multiplicity](https://www.omg.org/spec/UML/2.5.1/PDF#page=75).

Temporary review artifacts are at `/tmp/fpf-2026-10-28-subject-relation-notation-review-and-sota-harvest-722e48a9-7d60-49c3-a623-e8129eb67005/`: step-001 is the harvest, step-002 is the challenge, and final is their validated consolidation. Their retention is temporary; this document records the durable decisions and work state without copying a large report. The earlier review report is unavailable; its carried finding states come from the retained conversation summary, not a claimed reread.

## Issue and proposal tracker

| Issue | Proposed resolution | State | Drafts / decision |
|---|---|---|---|
| C11-I01 / C11-F01 | Separate structural containment from whether each child requires a container. The Operator's standalone-kind convention may be an explicit schema declaration; it must not be inferred anew from a selected display. | Semantics Decided; Drafted; not Applied/Verified | R1931, R2150, M232, E383; Q01/Q02 decided |
| NT-I01 / NT-F01 | Organizational membership does not duplicate canonical targets. Define how different membership/classification paths reach one target while different same-label targets remain distinct. | Canonical migration Decided; remaining declaration interpretation pending | R1931, R2209, R2150; Q03/Q05/Q06 decided |
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

### Q02 — independent declaration and required containment

Operator: “Yes, and for step it's false, for module is true”, clarified as “Module can be not in a package, step can't be not in a wf”.

Decision: the independent-declaration reading is selected. Module can exist outside Package; Step cannot exist outside Workflow. In a governing declaration structure an uncontained declaration permits independence; @ references do not declare another independent kind. Selection, indentation or deduplication of a derived view does not change the source permission. R1931, R2150, M232 and E383 Drafts are refined; R1509@22 makes the required Workflow explicit; R2177@3 and R2178@3 record the optional Module case. Status: Decided and Drafted; not Applied/Verified.

### Step and Substep correction

Operator: “No, step and substep are different”. This latest decision supersedes the previous nested-Step-only definition and the assistant's proposed `Workflow > Step >@ Step` rewrite. Preserve `Workflow > Step > Substep` as the structural example. This distinction does not itself decide specialization, property inheritance, Substep nesting, or all Type admission rules.

Prepared CA-R-1509@22-draft from Current CA-R-1509@21, removing the assertion that Substep is a nested Step rather than a separate kind. Prepared `CA-R-draft-CORE_META_MODEL-DEFINITION--define-substep.md` for the minimal distinct Substep definition; its proposed Operations/Type: Substep Subject is not yet promoted. Both are included in this tracker alongside the previous eight Drafts.

The `@` existing-kind modifier is now decided in Q03 and added to the grammar Draft for `::@`, `/@` and `>@`; it is not another Relation Type. Q02 is resolved by the confirmed Module/Step distinction. The assistant's recursive-Step example remains withdrawn.

### Q03 — reference marker scope

Does the proposed `@` existing-kind reference marker apply only to structural containment (`>@`), or consistently to organizational membership and specialization as well (`::@`, `/@`)?

Illustrative declaration and reference: Project Model `:: Scope Unit` declares its vocabulary entry; Continuant `/@ Scope Unit` points to that same kind and states its specialization, rather than defining another Scope Unit. These are explanatory short labels, not adopted canonical paths.

Operator: “Yes, we can define @ separately”.

Decision: define `@` as an existing-kind reference modifier, separately from the base relation operator, consistently for `::@`, `/@` and `>@`. The base operator retains its relation and inheritance meaning; `@` creates no duplicate kind, new Relation Type or automatic independent-existence permission. Unmarked kind declarations and marked existing-kind references are schema statements, not runtime instantiation. This supersedes the old blanket ban on @ in the R1931 and E383 Drafts only; Current sources remain unchanged. Exact reference spelling, literal-name handling and remaining containment interpretation are not decided by this answer. Status: Decided and Drafted; not Applied/Verified.


### Q04 — literal operator characters in names

Operator considered quoting and backslash escaping, then accepted backslash-only Subject escaping with “Okay, next”.

Decision: a backslash makes the next character literal; examples `CI\/CD`, `Release 0\.4`, and `\\` for one literal backslash. A final unmatched backslash is invalid. YAML single/double quoting remains a separate carrier concern, not additional Subject quoting syntax. R1931, R2150, M228, E383 and D269 Drafts are refined. Status: Decided and Drafted; not Applied/Verified.

### Q05 — full-path reference boundary

Operator selected the first option: “First”.

Decision: `@(canonical Subject path)` delimits an existing-kind reference; `::@(path)`, `/@(path)` and `>@(path)` preserve their base relation meanings. The matching unescaped close ends the reference; following properties or other admitted components continue outside it. Short display labels do not replace stored full canonical spelling or create aliases. The existing backslash rule handles literal parentheses in names. R1931, R2150, M228, M232, E383 and D269 Drafts are refined; the Substep Draft's old proposal-only reference wording is aligned. Status: Decided and Drafted; not Applied/Verified.

### Q06 — canonical path changes

If a kind is moved or renamed and its canonical Subject path changes, should its existing `@(...)` references be migrated to the new full path, or should old paths remain accepted aliases?

Operator: “First”, followed by “No also aliases for now”.

Decision: keep one canonical declaration path and migrate its Current references when that path changes. Keep no aliases or alias registry for now; do not guess targets by leaf-name matching. Preserve historical archived source versions under the existing history rules. This is a methodology decision and Draft refinement, not execution of any path migration. R1931, M228, M232, E383 and D269 Drafts are refined. Status: Decided and Drafted; not Applied/Verified.

### Scope Unit parts — latest correction

Operator's final structure: Scope Unit; Scope Unit >@ Scope Unit; Scope Unit >@ Atom; Scope Unit >@ Projection. Clarification: “Yes, it's not a vocabulary, it's parts”. This supersedes the intervening proposal to use :: for Scope Unit–Atom/Projection links. Keep :: for organizational membership elsewhere, such as Project Model grouping; do not generalize this correction to every grouping.

Prepare R1757@29-draft for these three structural endpoint kinds. The generic Relation pair R1368 already separates endpoint permissions from Relation Type meaning and needs no change for this permission. Local Scope assignments, immediate ownership/cardinality and the Operator-owned Project Goal exception remain separate rules.

### Additional Definition Draft register

| Current source | Draft | Scope | State |
|---|---|---|---|
| CA-R-1509@21 | CA-R-1509@22-draft | Step distinct from Substep and always in a Workflow. | Refined Draft |
| New definition | CA-R-draft — define-substep.md | Distinct Substep contained in Step; further nesting/type details pending. | New Draft |
| CA-R-2177@2 | CA-R-2177@3-draft | Module independently permitted outside Package. | New Draft |
| CA-R-2178@2 | CA-R-2178@3-draft | Package may contain the existing Module kind. | New Draft |
| CA-R-1757@28 | CA-R-1757@29-draft | Scope Unit structural parts: Scope Unit, Atom, Projection. | New Draft |

Thirteen successor/new Definition and RMED Drafts are now tracked in total. Current source versions remain unchanged.

### Similar-case inventory — bounded source investigation

Four read-only lanes inspected authoritative Core/Project Configuration definitions and relevant Drafts. Absence of a required-parent rule is not treated as proof of independent permission. No external implementation facts or root-level replica material establish methodology here.

| Kind / link | Classification | Evidence / disposition |
|---|---|---|
| Workflow > Step | Required containment for Step; no independent Step. | Operator Q02; R1509@22 Draft. |
| Step > Substep | Required containing Step in the new distinct-kind Draft; further nesting unresolved. | Operator distinction; new Substep Draft. |
| Package >@(Module) | Optional for Module; independently allowed. | Operator Q02; R2177@3/R2178@3 Drafts. |
| Plan >@(Plan) | Optional nesting; independent/naked Plan Atoms remain possible. | Current R1990 explicitly makes nesting optional. |
| Step referencing Action | Reusable Action definition, not structural Step > Action. | Current R1452; don't turn invocation/reference into containment. |
| Scope Unit >@(Scope Unit) | Structural child hierarchy; parent exceptions/counts need existing Scope rules. | Operator correction; Current R1756/R1757; R1757@29 Draft. |
| Scope Unit >@(Atom), >@(Projection) | Structural parts; no subtype/property inheritance. | Operator correction; R1757@29 Draft; Project Goal ownership exception remains. |
| Git Repository > Git Branch | Required repository ownership stated by the definition. | Current Project Configuration R2200/R2203. |
| Document/Section > Section | Section is defined as subdivision of Document or Section; strongest required-parent candidate, exact admission/counts not formalized here. | Current R2182; no automatic new policy. |
| Journal > Event Record | Record containment is explicit; the actual Event is not part of Journal. Universal record-parent cardinality not established by this read. | Current R1745; keep event vs record distinct. |
| Workflow Run / Step Run | Step Run belongs to one Workflow Run; execution-definition binding is not automatically > containment. | Current R1510/R1511; relation nature must remain explicit. |
| File/Directory/Database, Docker Image, Git Commit/Index, Pull Request | No universal containing Carrier established by these definitions. | R1955–R1957, R2198–R2203; representation/context is not blanket containment permission. |
| Function/Class and Documentation units/resources | Definitions do not establish every possible outer container or independent-existence permission. | R2175/R2176, R2181–R2193; avoid inventing a part relation from category or storage wording. |

### Q07 — unique primary names and short references

Operator asked whether primary Subject parts should be unique, excluding properties, to make @ references unambiguous. Proposed interpretation: each distinct primary-kind declaration has a unique name across the effective Subject model; repeated references to that same kind are not duplicates. Property names may repeat under different bearers. Existing same-label primary kinds, such as Aspect Documentation versus actual Implementation Documentation, would need distinct names if this is adopted; no such renames are performed yet.

Operator answered the quoted Q07 recommendation with “Yes”.

Decision: distinct primary-kind declaration names are unique across the effective Subject model. Permit `@(Module)` without requiring its full path inside the reference. Property names may repeat; repeated @ references do not declare duplicate kinds. This refines Q05/Q06: branch moves preserve references using an unchanged unique primary name; primary-name renames require reference migration. A current full-path reference remains valid but needs path migration when its path changes. No aliases. Ordinary full Subject paths still express graph structure. Existing naming collisions are not automatically renamed. Six notation Drafts and a new Rule Draft are prepared. Status: Decided and Drafted; not Applied/Verified.

### Additional naming Rule Draft

`CA-R-draft-CORE_META_MODEL-RULE--require-unique-primary-kind-names.md` records Q07. Fourteen total Drafts are now tracked. Conflicting primary labels need naming correction before promotion; exact collision inventory remains bounded follow-up, not a new generic identity layer.

### Functions moved to a separate proposal

The Operator explicitly kept functions as a proposal. The earlier Q08 Decided/Drafted wording is superseded. [CA-A-1237 — Content field-listing functions](CA-A-1237-SPECIFICATION_PROPOSAL--propose-content-field-listing-functions.md) now tracks the proposed `content.get_list()` behavior and exactly two candidate R/E Drafts.

Functions are not adopted and are excluded from relation-notation acceptance, promotion and implementation scope. Fourteen notation/structural/name Drafts remain tracked here; the two function Drafts belong to A1237. Historical versions preserve the earlier discussion without making it current authority.

## Evidence gaps and acceptance

Containment interpretation Q01/Q02 is decided at the proposal level. Q07 name scope is decided; the remaining naming collisions and Substep definition details are follow-ups; functions are separately proposed in A1237 and do not block notation disposition; earlier pending wording is historical context, not a new blocker.

| Gap | Handling / next action |
|---|---|
| C11-G01 | Settle the containment declaration and cardinality reading through the question sequence. |
| NT-G03 | Settle canonical identity and mixed grammar through the same sequence. |
| NT-G02 | Readability is unmeasured; no mandatory user study is introduced. |
| NT-G01 | Preserve historical states; recover the prior report only if exact reconciliation becomes necessary. |
| SG3-G02 | Source Drafts are prepared; applied repair and full inheritance checks remain later work. |

Before any promotion, resolve pending choices, read back the final Drafts against those answers, and identify the bounded source/projection checks. No parser implementation, full migration, unrelated graph cleanup or runtime change is included.
