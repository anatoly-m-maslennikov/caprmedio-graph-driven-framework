---
atom_id: CA-A-1298@1
content_role: Analysis
type: Analysis Report
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Model
version: 1
updated_at: 2026-10-29 03:57:45 +0400
relations: {}
tier: 3
---
# Summary

Review the plain Model proposal and related Drafts

## Question

Is the prepared plain Model packet internally consistent and aligned with the latest Operator decisions, with advanced formulas and bracketed conditions excluded?

## Scope

46 prepared files: the main Model proposal and 45 related Core RMED Drafts. The review covered primary kinds, simple relations and notation, roots/containment/inheritance, Claim placement, direct-value cardinality, basic Formats and carrier consistency. It did not review Engine/code/runtime or promote any source.

Advanced formulas, functions and conditions inside [] are preserved as separate proposals under A1297 and were excluded. The advanced Value Constraint Annotation Draft was not in the review packet. Simple [format], {cardinality} and ((RELATION_TYPE)) stayed in scope. Numeric and owner-specific requirements stayed in prose.

## Approach

Four independent read-only subagent lanes reviewed structure/relations; containment/inheritance; Claims/cardinalities/Formats/carriers; and alignment with latest Operator decisions. No FPF skill or command was run. The parent consolidated overlapping findings and performed mechanical file/link checks. All 46 reviewed carriers remained unchanged during review; all 69 local links checked resolved.

## Results

The prepared packet is not ready for adoption as-is. Ten concrete repair groups remain. Most follow already settled decisions. No reviewed defect repair was applied during this review; edits before it were limited to the requested separation of advanced material.

### PR-01 — P1 — Relation Types still carry properties of concrete edges

[Main Model, Relation properties](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/02_analysis/draft/CA-A-1239@1-draft-SPECIFICATION_PROPOSAL--formal-model-primary-kinds-and-properties.md:1763) lists Source Reference, Target Reference and Type on Relation, while the prepared named instances Relation//RECORDS and Relation//IS_EXECUTION_OF define reusable Types. A1261 already chose the Type-instance interpretation.

Consequence: A reusable Type can be mistaken for one particular edge with concrete endpoints.

Smallest correction: Reconcile the Relation Definition and property inventory: keep Type-level metadata separate from the actual edge tuple (source, Relation Type, target). Preserve the chosen // selectors. No new primary branch or new Operator decision is required.

### PR-02 — P1 — Notation Drafts restore rejected containment permissions

[R1931@13](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1931@13-draft-CORE_META_MODEL-RULE--use-subject-path-separators-for-broader-to-narrower-and-bearer-to-dependent.md:47) and [R1931@13](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1931@13-draft-CORE_META_MODEL-RULE--use-subject-path-separators-for-broader-to-narrower-and-bearer-to-dependent.md:75) retain the root-under-Implementation and independent-Module clauses. The obsolete root wrapper also remains in [R2150@11](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2150@11-draft-CORE_META_MODEL--define-subject-graph.md:76), [M232@27](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/05_method/draft/CA-M-232@27-draft-CORE_META_MODEL--derive-atom-subjects-graph-from-current-atom-subjects.md:49) and [E383@35](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/06_evaluation/draft/CA-E-383@35-draft-CORE_META_MODEL-POLICY--reject-invalid-subject-expressions.md:93). [E383@35](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/06_evaluation/draft/CA-E-383@35-draft-CORE_META_MODEL-POLICY--reject-invalid-subject-expressions.md:116) and [E383@35](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/06_evaluation/draft/CA-E-383@35-draft-CORE_META_MODEL-POLICY--reject-invalid-subject-expressions.md:128) would accept the superseded structures.

Consequence: The corrected primary definitions and their authoring/evaluation rules permit different structures.

Smallest correction: Use Project Implementation as the single parentless root Package; require each Module to have a Package. Replace the obsolete acceptance cases. The Operator decisions are already settled.

### PR-03 — P1 — Generic heading nesting contradicts the required content paths

[D479@23](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery/draft/CA-D-479@23-draft-CORE_META_MODEL-ENG_DECISION--use-stable-headings-for-atom-body-properties.md:61) and [D479@23](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery/draft/CA-D-479@23-draft-CORE_META_MODEL-ENG_DECISION--use-stable-headings-for-atom-body-properties.md:65) define section termination and nesting through heading levels. With # Summary followed by ## Claim, a literal outline puts Claim beneath Summary, although the required path is content.claim.

Consequence: The carrier rule does not unambiguously produce the Model properties it requires.

Smallest correction: Keep the chosen visible headings, but explicitly treat registered top-level RMED sections as logical sibling properties. Apply normal nesting within those sections. This follows the already chosen content paths; it does not require a new parser feature in this task.

### PR-04 — P1 — Operative conditions remain outside Claim

Examples: [R1269@28](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1269@28-draft-CORE_META_MODEL-DEFINITION--define-claim.md:38)–40 (heading/formal-expression/support counts), [R2160@4](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2160@4-draft-CORE_META_MODEL-DEFINITION--define-atom-content-scope.md:34) (scope omission/boundary), [R1510@17](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1510@17-draft-CORE_META_MODEL-DEFINITION--define-workflow-run.md:41) (Step Runs/outcomes/retry retention), [R1757@29](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1757@29-draft-CORE_META_MODEL--define-scope-unit.md:44) (no self-containment), [R2178@3](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2178@3-draft-CORE_META_MODEL-DEFINITION--define-package.md:40) (Package parent condition), and [define-value-format](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-value-format.md:37) (property meanings). Carrier rules repeat the issue at [D479@23](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery/draft/CA-D-479@23-draft-CORE_META_MODEL-ENG_DECISION--use-stable-headings-for-atom-body-properties.md:61)–67 and [D269@25](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery/draft/CA-D-269@25-draft-CORE_META_MODEL-ENG_DECISION--serialize-atom-subjects-in-frontmatter.md:59)–63.

Consequence: Reading only Claim omits rules that the packet says are operative; Semantics and Details acquire authority that the model denies them.

Smallest correction: Move those conditions into the existing prose Claims without adding requirements. Leave explanations, examples and provenance in supporting sections. The original Asset and Terms Projection omissions are already repaired; this is the remaining bounded set found by this review.

### PR-05 — P2 — Containment selector grammar conflicts with schema declarations

[R1931@13](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1931@13-draft-CORE_META_MODEL-RULE--use-subject-path-separators-for-broader-to-narrower-and-bearer-to-dependent.md:32) requires full canonical selectors on both sides of >, while its accepted examples and the main primary tree use declarations such as Workflow >{1+} Step and Scope Unit >@(Scope Unit).

Consequence: One rule would reject the schema notation used by the proposal itself.

Smallest correction: Distinguish schema declarations from ordinary full Subject selectors. Permit the already chosen whole/declared-part or existing-part-reference form in schema declarations, while retaining the full-path rule where required for ordinary Subject values.

### PR-06 — P2 — A Method still requires prior target existence for every Subject

[M228@29](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/05_method/draft/CA-M-228@29-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-subject-expressions-with-bearer-and-value-qualification.md:44) requires an already-existing target, contradicting its own [M228@29](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/05_method/draft/CA-M-228@29-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-subject-expressions-with-bearer-and-value-qualification.md:36) and A1285, which allow a defining Atom to introduce its governed target/path.

Consequence: The method could block authoring a new defined kind despite the accepted definition rule.

Smallest correction: State that a defining Atom can introduce its target. Preserve prior-existence requirements for actual existing-kind references and named-instance references rather than applying them to every defining GOVERNS path.

### PR-07 — P2 — Cardinality attached to named relations has no declared counting direction

[Named-relation examples](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/02_analysis/draft/CA-A-1239@1-draft-SPECIFICATION_PROPOSAL--formal-model-primary-kinds-and-properties.md:1995), [R1510@17](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1510@17-draft-CORE_META_MODEL-DEFINITION--define-workflow-run.md:36) and [R2177@3](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2177@3-draft-CORE_META_MODEL-DEFINITION--define-module.md:29) attach {1} to named relations. The current cardinality definition describes direct property values and > parts, not whether a named-relation suffix counts incoming or outgoing edges or which endpoint is the counting owner.

Consequence: Exactly-one is readable but its graph admission meaning is underspecified.

Smallest correction: Simplest recommendation: remove the suffix from these named-relation examples and keep the exact-one binding in prose. If the Operator wants to retain the notation, ask one question to define the counting endpoint/direction before using it. This is the only finding that needs a new choice if that notation is retained.

### PR-08 — P2 — Six prepared RMED scope headings retain the old name

[R1931@13](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1931@13-draft-CORE_META_MODEL-RULE--use-subject-path-separators-for-broader-to-narrower-and-bearer-to-dependent.md:24), [R2150@11](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2150@11-draft-CORE_META_MODEL--define-subject-graph.md:32), [M228@29](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/05_method/draft/CA-M-228@29-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-subject-expressions-with-bearer-and-value-qualification.md:26), [M232@27](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/05_method/draft/CA-M-232@27-draft-CORE_META_MODEL--derive-atom-subjects-graph-from-current-atom-subjects.md:27), [E383@35](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/06_evaluation/draft/CA-E-383@35-draft-CORE_META_MODEL-POLICY--reject-invalid-subject-expressions.md:40) and [D269@25](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery/draft/CA-D-269@25-draft-CORE_META_MODEL-ENG_DECISION--serialize-atom-subjects-in-frontmatter.md:26) still use ## Scope.

Consequence: The prepared packet does not consistently follow its chosen ## Claim scope layout.

Smallest correction: Rename these six headings to ## Claim scope, preserving their content.

### PR-09 — P2 — Ordinary prose falls within Formal claim sections

Ordinary Claim prose follows ### Formal claim in [define-cardinality-notation](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-cardinality-notation.md:52)–54 and [define-graph-syntax](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-graph-syntax.md:60)–66.

Consequence: Under the declared heading-to-property mapping, that prose becomes part of the formal child rather than direct Claim prose.

Smallest correction: Move those paragraphs above ### Formal claim. Keep the child as the declared fenced expression.

### PR-10 — P2 — Two preparation notes still call Resources classification unresolved

[define-project-implementation](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-draft-CORE_META_MODEL-DEFINITION--define-project-implementation.md:37) says Resources members remain unplaced, and [R2180@4](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2180@4-draft-CORE_META_MODEL-DEFINITION--define-documentation.md:40) refers to remaining Resources. The main Model and Asset Definition already record the accepted retirement/classification.

Consequence: The packet gives a stale account of what remains to decide.

Smallest correction: Update the readiness sentences to the Asset/Prompt/Documentation distinction while preserving the caveat that Current migration is not done.

### Confirmed alignment

The inspected primary definitions agree on the corrected Package/Module and Scope Unit/Project structures, Workflow–Step–Substep counts and leaf-call boundaries, permitted direct/indirect Workflow-call recursion, and no inheritance through containment. Counts apply independently to direct values; subjects{0} permits its declared children. Required Claim prose, an independently optional R Formal claim, string-valued Subjects, removal of list/map/ref Formats and YAML null/empty-value treatment agree in the inspected Claims. Remaining contradictions are in the supporting preparation packet described above.

### Remaining preparation and limits

The proposal explicitly retains incomplete primitive-Format definitions and final Type-catalog reconciliation. This bounded review does not certify a complete corpus migration, every old constraint transfer, parser behavior, source promotion or runtime enforcement. It does not assess the excluded advanced expression language. The historical FPF report was not altered or treated as a new run.

## TLDR

Repair the conflicting Draft clauses before promotion. Preserve the chosen primary model and the latest direct-value/Claim decisions. If named-relation cardinality is retained, settle its counting direction; otherwise keep those constraints in prose. Leave advanced expressions in their separate proposals.
