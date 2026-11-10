---
identity:
  id: CA-A-1334
  ref_id: CA-A-1334
context:
  container:
    scope_unit: CA-SU-00
  role: Analysis & Advisory
  form: Analysis Report
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Model
  tier: 3
state:
  status: Done
  version: 1
  updated_at: 2026-11-10 00:11:09 +0400
destination:
  file:
    name: CA-A-1334-ANALYSIS_REPORT--challenge-formal-model-specification-proposal.md
    path: .caprmedio_caprmedio/02_analysis
author: Anatoly Maslennikov
---

## Summary

Challenge formal Model specification proposal

## Details

## Task, scope, and boundaries

**Result: concern.** The proposal reflects the latest root, containment and Workflow–Run–Record decisions, but the prepared Definition packet is not yet internally consistent. Three repairs matter before adoption: put defining conditions inside Claims, distinguish Relation Types from named connection instances, and reconcile the linked Drafts with the latest model.

This review challenges [A1239](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/02_analysis/draft/CA-A-1239@1-draft-SPECIFICATION_PROPOSAL--formal-model-primary-kinds-and-properties.md:20>) and its relevant linked Drafts for Anatoly Maslennikov's decision. The inspected target is Version 1, updated **2026-10-28 21:39:16 +0400**. It is a proposal, not adopted Current authority. Inputs include A1251–A1260, the applicable A1242–A1244 Claim decisions, the prepared structure/notation/Claim/Type/Workflow/Run/record definitions, and bounded reads of cited Current rules. Latest Operator decisions take precedence over superseded preparation.

The review covers primary kinds, the six operators and reference marker, roots and containment counts, inherited properties, Types and Labels, Claim structure, and Workflow–Run–Record connections. It does not decide unplaced branches, complete the Type catalog, promote Drafts, migrate Current selectors, implement Terms Graph, or inspect engine code. Direct FPF sources are identified below; FPF supplies review criteria, not CAPRMEDIO decision authority.

**Campaign handoff.** Campaign `formal-model-review-3317a900`; phase: challenge complete, owner disposition pending. The semantic frontier is the proposal through A1260, including the A1258/A1259 root specializations. The carrier frontier is the exact A1239 version above and the linked Draft versions cited in the registry. The frozen evaluation profile is the bounded check list above. The approved Plan and its independently validated step are the execution basis; this final report preserves the passed step result. No prior analytical campaign or finding IDs were recovered or silently reused. FM-01–FM-03 are OPEN; their fingerprints are in the sole issue registry. One full challenge has now been performed for this frontier/profile. Next: owner disposition, then any separately authorized repair batch. Stop before repairs; do not repeat a full challenge on the unchanged proposal.

**Report outcome:** final consolidated plain Markdown review. Saved report: [fpf-reports/20261028T182222Z-fpf-design-challenge-review-formal-model-spec-proposal.md](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/fpf-reports/20261028T182222Z-fpf-design-challenge-review-formal-model-spec-proposal.md). This is non-normative result delivery; the reviewed proposal and governing project sources were not changed.

### Composition receipt

- Complete invocation:
  ```text
  [$fpf](/Users/am/.codex/skills/fpf/SKILL.md) let's review the current spec proposal with the new Formal Model graph
  challenge design + alignment check
  ```
- Approval steering: `do with astra max`; approved Plan `formal-model-review-3317a900`, blocking-decision threshold 95%. The execution agent was replaced at the user's requested model/effort before analytical work; the approved Plan was preserved.
- Selected profile: none. Requested intent: design challenge plus alignment check. Approved sequence and executed prefix: step 1, `$fpf design challenge`.
- Unexecuted suffix: none in the approved one-step Plan. A separate native `alignment audit` was deferred by that Plan; checking agreement with Operator decisions here does not claim that command executed.
- Typed edge: no inter-step edge executed. The contemplated design-challenge → alignment-audit edge lacks accepted findings mapped to applied repairs and changed-carrier evidence; its gate would return `STOP_NO_APPLIED_CHANGE`. It was not entered.
- Final stop state: COMPLETE. No blocking question was required. Context ledger: 5 direct FPF pages read, 5 used, 0 deferred bindings; no profile or conditional bindings. Routing/index material is separate.
- Validated handoff: step-001, attempt 1, warden PASS with no findings; its complete issue, fix, evidence and gap registries are preserved. All approved analytical steps are complete.
- Carried registry IDs: FM-01–FM-03, FX-01–FX-03 and G-01–G-04.

## Issues, weak points, and improvements

### Native result

**Proposal and decision boundary.** The intended result is a reusable Formal Model whose tree, property blocks and Definition Claims tell the same story. This review produces findings for the Operator; it grants no adoption or mutation authority.

**FPF Challenge Findings.** The three findings below are ordered by consequence. Each separates project evidence, the direct FPF basis and reviewer inference. The issue registry is the complete finding list for the inspected scope.

**Strengths within inspected scope — no concern found within inspected scope:**

- A1239 preserves the five base branches, groups Relation and Format under Graph Syntax, and distinguishes specialization, grouping and containment. References reuse declarations; they do not create runtime objects.
- Project is the parentless root Scope Unit; Project Implementation is the parentless root Package. Implementation remains a heading. The primary tree contains the latest Module, Prompt, Asset and Code Unit placements. The former wrapper decisions are superseded, not waiting for approval. [A1258](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/02_analysis/CA-A-1258-SPECIFICATION_PROPOSAL--specialize-project-as-the-root-scope-unit.md:20>); [A1259](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/02_analysis/CA-A-1259-SPECIFICATION_PROPOSAL--specialize-project-implementation-as-the-root-package.md:20>).
- Workflow contains at least one Step; a Step may contain zero or more Substeps. Containment supplies no Atom-property inheritance. Recursive Plan containment uses its corrected canonical reference.
- The shown R/A/C/E/M Type branches follow A1257. Label remains optional stored text with a derived Type fallback; there is no added `effective_label` field or Plan-label taxonomy.
- The complete RMED Claim contract is one Type-defined unit, with optional operative formal content only in R. This is a sound stated boundary; FM-01 concerns its application to prepared definitions.
- Workflow, Workflow Run and Event Record are explicitly distinct; the one-Workflow binding and direct-only storage are stated. RECORDS is not confined to Workflow Runs, and no universal record-count obligation is invented. [A1260](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/02_analysis/CA-A-1260-SPECIFICATION_PROPOSAL--connect-workflow-definitions-runs-and-event-records.md:20>). A.7's description/occurrence/carrier distinctions support this assessment; they do not establish that any run occurred.

**Unchecked claims and insufficient basis.** The source packet openly leaves several design and migration questions unfinished. G-01–G-04 retain them below. No missing parser, runtime activation, complete migration or full Type catalog is presented as a newly discovered failure.

**Return to project authority.** Anatoly owns disposition of FM-01–FM-03 and any repair authorization. The smallest next action is to settle the Relation-Type target in FM-02, then authorize the three bounded fixes together if accepted. The other two findings preserve already stated decisions. A closure audit becomes eligible only after accepted repairs are actually applied.

### Issue registry

#### FM-01 — Defining conditions remain outside the operative Claim

- **Result / priority / state:** concern / high / OPEN.
- **Affected claim and scope:** the prepared Definition packet claims that operative definitions live in `content.claim`, while Semantics and Details add no operative constraints. Fingerprint: `Definition packet | Claim-only authority | defining condition exists only outside Claim`.
- **Project evidence:** A1239 states that boundary at [lines 1937–1938](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/02_analysis/draft/CA-A-1239@1-draft-SPECIFICATION_PROPOSAL--formal-model-primary-kinds-and-properties.md:1937>), as do A1243 and R2110@7. Yet the [Asset Draft](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-implementation-asset.md:20>) has only `Package > Asset` inside Claim; “non-executable content” and the exclusion of arbitrary Atom/configuration/Journal files appear only in Semantics. The [Terms Projection Draft](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-terms-projection.md:20>) similarly puts its derivation from selected sources and absence of independent meaning authority only in Semantics.
- **Direct FPF basis:** A.6 §4.1 and §4.6 separate canonical declarations from explanations that must preserve their meaning; §4.6 is explicitly informative. C.3 §5.1 calls for the operative membership distinction. The exact Claim/Semantics authority rule here comes from CAPRMEDIO's Operator decisions, not from an imposed FPF layout.
- **Reviewer inference and consequence:** a reader using only the designated operative Claim cannot recover what separates an Asset from executable content, or a Terms Projection from an independently authored source. Promoting these Drafts unchanged would make the explanatory sections carry definition authority that the proposal denies them.
- **Issue confidence / basis:** 99%; directly visible section placement and the explicit local authority rule. **Coverage limit:** the two examples establish the defect; they are not an exhaustive count of every sentence needing relocation. No Current adoption or validator behavior was tested.
- **Mapped fix:** FX-01.

#### FM-02 — The new Relation-Type definitions target named Relation instances

- **Result / priority / state:** concern / high / OPEN.
- **Affected claim and scope:** the identity addressed by the two new Relation Definition Drafts. Fingerprint: `IS_EXECUTION_OF and RECORDS | declaration targets | reusable Type addressed as named connection instance`.
- **Project evidence:** their headers govern [`Relation//IS_EXECUTION_OF`](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-is-execution-of-relation.md:10>) and [`Relation//RECORDS`](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-records-relation.md:10>), while their Claims define reusable `relation_type` values and derived inverses. The cited [R1931@13](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1931@13-draft-CORE_META_MODEL-RULE--use-subject-path-separators-for-broader-to-narrower-and-bearer-to-dependent.md:30>) assigns `//` to an existing kind-to-named-instance connection. A1239 still cites [R1963](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1963-CORE_META_MODEL--define-entity-continuant-object-relation.md:29>), where Relation is a typed connection between identified endpoints, and displays its Type property at A1239:1784–1788.
- **Direct FPF basis:** A.6.5 §1 and §4.2–§4.3 distinguish a reusable relation declaration, the relation kind, an actual connection and the references identifying its participants. C.3 §4–§5 distinguishes a kind from its declaration and classified instances.
- **Reviewer inference and consequence:** under the cited meaning of Relation and `//`, the target looks like one particular connection named RECORDS, although the Claim defines the reusable Type. A consumer cannot consistently determine whether that governed target should have concrete source/target endpoints or define a family of such connections.
- **Issue confidence / basis:** 96%; the notation rule, target selectors and Claim bodies are explicit. **Coverage limit:** an intentional redefinition of the Relation branch as a Type registry could resolve this, but that redefinition was not found in the inspected packet. FPF does not decide which CAPRMEDIO representation to choose.
- **Mapped fix:** FX-02.

#### FM-03 — Linked preparation still contains superseded meanings and target paths

- **Result / priority / state:** concern / medium / OPEN.
- **Affected claim and scope:** consistency of the prepared source set with A1239 and A1251–A1260. Fingerprint: `prepared Definition and notation packet | latest model frontier | stale selector or superseded semantic clause remains`.
- **Project evidence:** [R1931@13:41](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1931@13-draft-CORE_META_MODEL-RULE--use-subject-path-separators-for-broader-to-narrower-and-bearer-to-dependent.md:41>) still places the root Package under Implementation; [its line 69](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1931@13-draft-CORE_META_MODEL-RULE--use-subject-path-separators-for-broader-to-narrower-and-bearer-to-dependent.md:69>) still says Module is independently declared. Those contradict A1259 and the same Draft's “Module belongs to Package” statement. The [Value Format Draft header](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-value-format.md:8>) still targets `Formal Model::CAPRMEDIO::Format`; [R1269@28](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1269@28-draft-CORE_META_MODEL-DEFINITION--define-claim.md:3>) and [R2110@7](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2110@7-draft-CORE_META_MODEL--define-atom-content-role-requirement-type-definition.md:9>) omit the new Governing Objects segment. These are prepared Draft headers, not a complaint that unchanged Current sources were not migrated.
- **Direct FPF basis:** A.6 §4.6's explanation/source consistency diagnostic and C.3 §5.1's exact declaration identity. The intended replacement meanings and paths are supplied by the latest Operator decisions and A1239.
- **Reviewer inference and consequence:** choosing a different linked preparation file changes the apparent answer about Module independence, the root Package's whole, or which target a Definition governs. The primary graph can be correct while its promotion packet remains contradictory.
- **Issue confidence / basis:** 99%; direct comparison of specific clauses and selectors. **Coverage limit:** A1239 already acknowledges that lexical preparation needs reconciliation and that Current paths remain old. This finding specifies remaining work, not an allegation of a claimed completed migration or an exhaustive stale-path inventory.
- **Mapped fix:** FX-03.

### Fix and improvement register

#### FX-01 — Make the existing Claim boundary effective

- **Exact change / addressed issues / relationship:** move each defining membership condition or operative constraint from Semantics/Details into complementary prose under the same Definition's Claim; retain explanations outside it. Start with Asset and Terms Projection, and check the other prepared Definition Claims against that same rule. Addresses FM-01; complementary.
- **Owner and authority / state:** Anatoly owns disposition; an authorized editor may change Drafts only after separate repair authorization. PROPOSED.
- **Fix confidence / basis:** 98%; A1243 explicitly allows formal structure and complementary prose in one Claim. No new Atom, field, section hierarchy or operative M/E/D formal child is needed.
- **Expected result / trade-offs:** the Claim alone contains the defining conditions; Semantics remains explanatory. Some prose moves, but the settled meaning and single-Claim design stay intact.
- **Dependencies and order:** first repair batch, independent of the Relation-Type representation choice. Do not promote as part of this review.
- **Verification:** for each touched Definition, temporarily ignore Semantics and Details and recover its membership/constraint answer from Claim alone; confirm the supporting sections introduce no additional operative rule. Preserve the R-only formal-child boundary.
- **Recommendation:** preferred.

#### FX-02 — Give Relation Types an unambiguous governed target

- **Exact change / addressed issues / relationship:** retain the cited meaning of Relation as a connection and target the reusable Type through its explicit Type qualification, then update the two Draft headers and their references consistently. A candidate spelling is `Formal Model::CAPRMEDIO::Graph Syntax::Relation.Type: RECORDS` (and the corresponding IS_EXECUTION_OF target); this is a proposed representation for Operator disposition, not an already admitted selector. Addresses FM-02; required prerequisite for source admission of these two definitions.
- **Owner and authority / state:** Anatoly chooses the identity/selector convention; an editor then applies only the accepted choice. PROPOSED.
- **Fix confidence / basis:** 91%; the existing Relation.Type property and allowed-value notation support this small correction, but exact target admission is not yet evidenced. If the intended model instead makes Relation a Type registry, its governing definition and instance meaning must be explicitly changed together.
- **Expected result / trade-offs:** reusable Types remain separate from particular connection facts; the direct/inverse meanings, broader RECORDS range and one-Workflow binding are preserved. The small cost is a precise selector decision and reference updates; no alias registry is needed.
- **Dependencies and order:** settle this before FX-03's final reference reconciliation. FX-01 can proceed independently after authorization.
- **Verification:** distinguish “RECORDS is a reusable Type” from “record r RECORDS run w”; only the latter has concrete endpoints. Confirm both inverse views derive from one authored fact and that no universal record count is added.
- **Recommendation:** preferred.

#### FX-03 — Reconcile the prepared packet once against the accepted frontier

- **Exact change / addressed issues / relationship:** remove superseded Module-independence and Implementation-wrapper clauses from R1931@13; bring its explanatory references into agreement with A1256/A1259. Replace the stale prepared Format, Claim and Definition-Type target selectors with the A1239 paths, and check references in the same bounded packet. Addresses FM-03; complementary.
- **Owner and authority / state:** authorized editor, under Anatoly's accepted Draft-repair scope. PROPOSED.
- **Fix confidence / basis:** 99% for the cited replacements; latest decisions and corresponding A1239 paths are explicit. This confidence does not cover uninspected Current-source migration.
- **Expected result / trade-offs:** all touched prepared sources identify the same kinds and preserve the same settled containment meanings. This is a bounded Draft cleanup, with no aliasing, archived-history rewrite or source promotion.
- **Dependencies and order:** final repair batch after FX-02's target decision; integrate FX-01's edits without changing their Claim meaning.
- **Verification:** inspect all touched selectors against the primary tree; search the prepared packet for the retired root-Implementation wrapper and independent-Module permission; check every remaining occurrence is explicitly historical. Confirm Project and Project Implementation remain parentless roots and all actually contained parts retain one immediate whole.
- **Recommendation:** preferred.

## Unresolved evidence gaps

- **G-01 — Relation-Type identity decision (FM-02 / FX-02).** Best current answer: preserve the existing connection meaning and use an explicit Type target. Missing: the Operator's accepted exact target convention. Consequence: the two new definitions should remain preparation material. Next action: decide this one representation with the two concrete examples in FX-02; the present read-only challenge does not need to pause.
- **G-02 — Formal notation admission.** Best current answer: the operators and chosen reference boundary are settled, while complete mixed-chain binding, primitive-format definitions and Atom-ID component/Selection bindings are unfinished. A1239 explicitly identifies these limits at 1923–1929 and 1947–1954. Missing: source definitions for those admitted uses. Consequence: no claim of a complete executable formal language or safe automated migration. Next action: finish those bounded definitions before relying on a parser or migration; no parser experiment was run here.
- **G-03 — Remaining model coverage.** Best current answer: Documentation/Resources await placement; Tool awaits disposition; the full Type catalog and Substep inheritance/nesting/Atom-Type admission remain open. The Step/Workflow Drafts also retain “Step Atom” wording whose exact representation needs to stay consistent with that pending Type work. Missing: the decisions and completed definitions. Consequence: this review cannot establish a complete primary-kind/Type inventory. Next action: resolve the existing tracked questions individually; preserve unplaced kinds and do not infer retirement or new inheritance.
- **G-04 — Complete constraint transfer and applied-state evidence.** Best current answer: Current legacy graph constraints remain authoritative in their existing scope; A1239 says useful constraints still require incorporation before retirement. Missing: a completed constraint-to-Definition map, accepted repair dispositions, changed-carrier evidence and relevant checks. Consequence: this proposal review cannot establish complete containment admission, Current migration, runtime enforcement or closure. Next action: after owner disposition, apply the authorized bounded repairs and perform targeted checks; enter native alignment audit only when its applied-change handoff exists.

## Skills used

1. `$fpf design challenge` — one approved analytical step. Native alignment audit did not execute.

### FPF sources consulted (5 read; 5 used)

Edition: installed knowledge graph, source revision `fb3b6a4ad1d51d732a365f75f7d68337c7a751e2`; every listed page's `fpf_id` was verified. Reads were bounded to the sections below, not whole-pattern or neighborhood coverage.

- **Used — E.11.PUA:** [Pattern Use in a Working Situation and First Useful Result](</Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph/E_The FPF Constitution and Authoring Guides/10_11_First-Practical Entry and Pattern-Use Discoverability Discipline/01_E.11.PUA - Pattern Use in a Working Situation and First Useful Result.md:60>). §§1–3, §4.0–4.1, §9; selected routing/closure passages. Used for the smallest useful result, honest boundaries and stopping discipline, not as the substantive governor of the Formal Model.
- **Used — C.3:** [Kinds, Intent and Extent, and Typed Reasoning](</Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph/C_Kernel Extension Specifications/01_03_Kinds, Intent and Extent, and Typed Reasoning/00_C.03 - Kinds, Intent and Extent, and Typed Reasoning.md:49>). §§0–5 and §11. Used to distinguish kinds, declarations, membership conditions and instances. No claim of full C.3.1/C.3.2 analysis.
- **Used — A.6:** [Signature Stack: Classify and Place Boundary Claims](</Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph/A_Kernel Architecture Cluster/06_Signature Stack- Classify and Place Boundary Claims/00_A.06 - Signature Stack- Classify and Place Boundary Claims.md:98>). §§1–3, §4.1, bounded §4.2, §4.5–4.6, §9. Used for declaration/explanation consistency. Its normative A.6.B classification was not imported or claimed executed.
- **Used — A.7:** [Strict Distinction](</Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph/A_Kernel Architecture Cluster/07_Strict Distinction- Repair Conflations of FPF Objects (Clarity Lattice)/00_A.07 - Strict Distinction- Repair Conflations of FPF Objects (Clarity Lattice).md:37>). §§0–4, §5.1, §5.3–5.8 and §10. Used for definition/occurrence/record/carrier separation; no Work occurrence or assurance was inferred.
- **Used — A.6.5:** [Relation-Declaration Slot Discipline](</Users/am/Documents/My_Repos/levenchuk-fpf-knowledge-graph-toolkit/FPF-Knowledge-Graph/A_Kernel Architecture Cluster/06_Signature Stack- Classify and Place Boundary Claims/16_A.06.05 - Relation-Declaration Slot Discipline - SlotKind, ValueKind, RefKind, and participant-designation discipline.md:62>). §§1–3, §4.0–4.6 and §9. Used for reusable relation declarations versus instances and references; no new SlotSpec machinery is prescribed.

Not checked: code, parser behavior, runtime, release, complete legacy-constraint transfer or Current-source migration. The remaining risk is treating this internally unfinished Draft packet as an adopted or executable specification.

<oai-mem-citation>
<citation_entries>
MEMORY.md:9-16|note=[prior context locator only live sources govern this review]
MEMORY.md:51-62|note=[notation review boundary rechecked against live proposal]
</citation_entries>
<rollout_ids>
</rollout_ids>
</oai-mem-citation>
