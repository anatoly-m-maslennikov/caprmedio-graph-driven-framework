## Task, scope, and boundaries

Review [Candidate #10, A1218@2](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/02_analysis/CA-A-1218-SPECIFICATION_PROPOSAL--subject-model-candidate-10.md) so Anatoly can decide the proposed primary Subject structure and definitions. This is a proposal under [Epic P2673@2](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/03_plan/CA-P-2673-EPIC--subject-refinement-stage-3.md), not adopted methodology.

Reviewed: all 35 displayed primary entries, their defining Drafts, semantic anchors and relevant Current Subject grammar. Drafts describe the proposal; Current sources remain governing. Input readiness—42 Drafts and 27 unchanged Current originals—was verified by the manager before review.

Scope excludes instances, property inventories, Terms-Graph work, migration, source promotion, rendering, tools, code and runtime behavior. Existing Actor and Execution definitions were considered as concepts only. No project source was changed.

**Campaign:** `C10-36faec34`; first full challenge of A1218@2 and its linked Drafts, with no predecessor report. Checks: definition clarity, kind versus grouping, independent classification axes and latest-decision consistency. Findings I01/I02 remain OPEN; Anatoly's disposition is next. Repeat a full challenge only after a material meaning or scope change.

**Execution state:** COMPLETE. This final report consolidates the independently validated one-step challenge; no further analysis or source changes were made.

Saved report: `fpf-reports/20261027T134959Z-fpf-design-challenge-subject-model-candidate-10-review.md`.

### Composition receipt

Exact original invocation, retained with its amendments:

```text
okay, create candidate #10:
main entities only
update with new drafts what's changed.
get the definitions for other main entities

then do review with fpf with astra max for subagents

and create new Epic btw about this - Subject refinement stage 3(?)

main subject structure with atom ids with definition for each primary  entity

i think we can put all details into P atoms, and the candidate itself to - A
the type is Spec Candidate?

or Spec Proposal

no, use the standard FPF flow

the scope is:
new subject graph primary entities, with definitions for each primary entity

without any instances
```

Execution approval: `Do`. Profile: none. Approved sequence and executed prefix: `1. $fpf design challenge`. Unexecuted suffix: none. Incoming handoff: the immutable, independently validated Plan supplied the scope and authority; its Draft-readiness and Current-preservation prerequisites were satisfied by the manager. There is no analytical-to-analytical edge in this one-step run. Stop state: `COMPLETE`. Context ledger: 6 pages read, 4 used, 2 screened only, 0 deferred. Carried registers: `C10-I01–I02`, `C10-F01–F02`.

## Issues, weak points, and improvements

### Native result

**FPF result: concern.** The outline is usable as an organized Subject vocabulary. Two core definitions remain open to materially different readings; neither finding establishes that the whole structure is invalid.

**Source and decision boundary.** FPF revision `fb3b6a4ad1d51d732a365f75f7d68337c7a751e2`, generated 2026-10-25, supplies review criteria. CAPRMEDIO definitions and Anatoly retain project authority.

**Strengths — no concern found within inspected scope:**

- The definitions separate actual Event/Execution from their records, and Implementation from derived Projection. Direct editing of Implementation and source-only changes to Projection are stated consistently.
- Project and Documentation each have distinct thing and aspect meanings. Content Role remains an independent classification topic; it does not become another entity merely because it has a Subject.
- Namespace and grouping headings are expressly not automatic subtype assertions. Current R1931@11 also says `/` admits no native relation by itself. Therefore the outline alone does not establish an erroneous `NARROWER_THAN` edge. Any later claim of genuine specialization must follow the definitions, not indentation.
- Actor distinguishes the participant from its description and grants no authority merely by classification. No extra role-assignment machinery is needed for this bounded primary definition.

**FPF not decisive:** the exact aspect list, its intentional overlap, the chosen labels, and Carrier's display position are project choices. The inspected patterns do not require a disjoint or exhaustive taxonomy.

**Unchecked claims:** this is not proof of full grammar admission, complete legacy Term remapping, graph inheritance behavior, or an applied migration. No instances were needed to examine the declared definitions. Namespace spelling/collision behavior remains outside this abstract proposal review.

**Return to project authority:** decide the two clarifications below. No repair, adoption or release decision has been made.

### Issue registry

**C10-I01 — Clarify whether Node names a modeled target or its representation.**

- **Affected target / fingerprint:** Node and Project Model definitions; `Node–ProjectModel | primary Subject vocabulary | represented target versus model element`.
- **Evidence:** [R1994@11-draft:29](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1994@11-draft-CORE_META_MODEL--define-entity-node.md:29) calls Node a logical abstraction, admits Occurrents, then describes an Artifact as a Node instance delivered into Carriers. [R2209@1-draft:26](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2209@1-draft-CORE_META_MODEL-DEFINITION--define-project-model.md:26) names what exists in a project but also calls Project Model a logical model. R1968@8-draft defines an Event as the actual occurrence; R1958@9-draft permits carrying its record, not the occurrence. The Node/Carrier wording is inherited from Current R1994@10 and R1958@8, not introduced by Candidate #10.
- **Direct FPF basis:** A.7 §5.3–5.5 and §5.8 distinguish actual work/participants, descriptions and carriers; §5.6 separates organization in a representation from stronger claims about its subjects.
- **Reviewer inference / consequence:** the intended distinction is visible elsewhere, but these umbrella definitions leave two readings available. A reader could classify the thing itself, its logical representation, or its carried description under the same statement. Clarifying this once would stabilize every branch beneath Node.
- **Issue confidence:** 90%; the conflicting readings follow from the quoted definitions. **Limit:** this may be recoverable modeling shorthand, not an intended identity claim. No actual conflation or faulty graph behavior was observed.
- **State:** OPEN. **Mapped fix:** C10-F01. **Return condition:** a single accepted referent convention shared by Node, Project Model and Carrier.

**C10-I02 — Give Project one clear defining boundary.**

- **Affected target / fingerprint:** Project definition; `Project | primary Subject vocabulary | undertaking versus work-and-material aggregate`.
- **Evidence:** [R2220@1-draft:26](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2220@1-draft-CORE_META_MODEL-DEFINITION--define-project.md:26) defines Project as organized work “together with” governed material. Its next paragraph distinguishes Product, Implementation and repository Carrier, but does not say whether Project denotes the undertaking organizing them or their aggregate.
- **Direct FPF basis:** C.3 §5.1 and C.3.1 §5–6 recover a kind through its operative membership distinction and continuity; A.7 §5.6–5.7 warns against deriving a whole merely from grouping unlike things.
- **Reviewer inference / consequence:** the definition supports more than one boundary for the main Project concept. This can make Project, Execution and the material owned through Scope Units overlap for different reasons without saying which distinction the Project definition intends.
- **Issue confidence:** 85%; the missing discriminator is textual, but an intentionally broad domain definition may be adequate. **Limit:** FPF does not prohibit a composite Project concept or prescribe a particular project ontology.
- **State:** OPEN. **Mapped fix:** C10-F02. **Return condition:** Anatoly accepts one concise boundary that distinguishes Project from its work and material, or explicitly accepts the aggregate reading.

### Fix and improvement register

| ID | Exact proposed change and coverage | Basis, result and trade-off | Authority, order and verification |
|---|---|---|---|
| **C10-F01** | In R1994 and R2209, state one consistent convention: Node names an admitted thing or topic in the logical graph model; its graph representation and any carried description remain distinct. Define Project Model as the vocabulary grouping for project things, consistent with A1218. Qualify the Artifact sentence so carrying a record never means carrying the actual occurrence. Addresses C10-I01; relationship: **complementary** to F02. | **Fix confidence: 90%**, independently based on R1275's thing/topic target and A1218's explicit grouping decision. Expected result: the umbrella definitions preserve the existing target/record distinction. Trade-off: slightly more explicit prose; no new entity, property or renderer requirement. | Owner: Anatoly; requires acceptance of the wording and separate Draft-edit authority. Order 1; no prerequisite beyond disposition. Verify semantically that Node, Actor, Event, Project Model and Carrier consistently identify the thing, representation and record; retain the current absence of an intermediate Subject object. **Preferred; PROPOSED.** |
| **C10-F02** | In R2220, prefer: “A Project is a governed undertaking directed toward a result. Its work and governed material belong to that undertaking; they are not its definition by aggregation.” Keep its distinction from Product, Implementation, Carrier and root Scope Unit. Addresses C10-I02; relationship: **complementary** to F01. | **Fix confidence: 80%**, based on the existing root-Scope-Unit and result wording; the intended Project boundary is not yet confirmed. Expected result: one reusable definition of the undertaking. Trade-off: this chooses a narrower meaning than the current aggregate wording; Anatoly may retain the latter explicitly. | Owner: Anatoly; requires approval of the meaning and separate Draft-edit authority. Order 2; independent of F01, with a final joint consistency read. Verify semantically that Project is distinguishable from Execution, Implementation and Scope Unit, without adding lifecycle machinery or instances. **Acceptable; PROPOSED.** |

No fixes were applied or verified. After accepted Draft changes, check the changed definitions and affected neighbors. Broader correctness remains outside the reviewed scope; an unchanged frontier does not need another full challenge.

## Unresolved evidence gaps

- **C10-G01 — Intended Node convention** (I01/F01). Best current reading: the Subject names the modeled thing or topic, while representation and carrier remain separate. Missing evidence: an accepted sentence making that convention explicit in the Node and Project Model definitions. Consequence: I01 remains an interpretive concern. Next action: Anatoly dispositions F01; a targeted reread checks the resulting wording.
- **C10-G02 — Intended Project boundary** (I02/F02). Best current reading: an undertaking that organizes work and material. Missing evidence: acceptance of that boundary or an explicit decision to retain the composite meaning. Consequence: F02 remains a proposal with lower confidence. Next action: Anatoly dispositions F02.


The Plan's preparation gaps GAP-01/GAP-02 are closed. The remaining definition choices did not prevent the challenge.

## Skills used

1. `$fpf design challenge`

### FPF sources consulted (6 read; 4 used)

All paths below are relative to the verified FPF-Knowledge-Graph edition stated above. Only the named sections support this review.

| Page | Status and inspected contribution |
|---|---|
| `E_The FPF Constitution and Authoring Guides/10_11_First-Practical Entry and Pattern-Use Discoverability Discipline/01_E.11.PUA - Pattern Use in a Working Situation and First Useful Result.md` | **Used** as entrypoint: §§1–3, 4.0–4.1.1, 9, 12. Bounded use, useful result and stop; not a substantive ontology verdict. |
| `A_Kernel Architecture Cluster/07_Strict Distinction- Repair Conflations of FPF Objects (Clarity Lattice)/00_A.07 - Strict Distinction- Repair Conflations of FPF Objects (Clarity Lattice).md` | **Used:** §§0–4, 5.1–5.10, 10. Distinctions between thing, description, occurrence, grouping and carrier. |
| `A_Kernel Architecture Cluster/06_Signature Stack- Classify and Place Boundary Claims/16_A.06.05 - Relation-Declaration Slot Discipline - SlotKind, ValueKind, RefKind, and participant-designation discipline.md` | **Screened only:** §§1–3, 4.0–4.1, 4.4–4.5, 9. No reusable relation-participant declaration was required; no SlotSpec machinery proposed. |
| `A_Kernel Architecture Cluster/01_Recognize a Whole with Parts (U.Holon and Admitted Holon Kinds)/02_A.01.01 - Bounded Model-Use Structure- Applicability, Use and Expression Coherence (DDD Bounded Context).md` | **Screened only:** §§0–3, 4.1, 4.4–4.5, 4.7, 9. A namespace label does not establish a model-use structure; that stronger review was outside scope. |
| `C_Kernel Extension Specifications/01_03_Kinds, Intent and Extent, and Typed Reasoning/00_C.03 - Kinds, Intent and Extent, and Typed Reasoning.md` | **Used:** §§0–6 and 11; remaining sections screened. Distinguish kind, definition, classification and current members; route subkind reasoning to C.3.1. |
| `C_Kernel Extension Specifications/01_03_Kinds, Intent and Extent, and Typed Reasoning/01_C.03.01 - Kind Identity and Subkind Relations (U.Kind and U.SubkindOf).md` | **Used:** §§0–6 and 11. Definition-based membership boundaries and specialization; no subtype claim follows from layout alone. |
