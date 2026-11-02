---
atom_id: CA-P-2683
content_role: Plan
type: Plan
label: Epic
current_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Entity
version: 14
updated_at: 2026-10-29 21:51:04 +0400
relations: {}
tier: 3
---
## Summary

Migrate Formal Model syntax and Claims

## Objective

Migrate Current Methodology and direct project-local RMED to the reviewed Model: mechanically migrate Subjects first, adopt the prepared Drafts with correct Subjects, complete entity Definitions and simple formal Claims, rebuild the actual Subject graph, then review and correct it.

## Details

### Scope

Use the existing Current Methodology and direct project-local R/M/E/D boundary. Declare exact Scope Units, statuses and IDs/Versions in P2684. Include only necessary governing-configuration alignment for that same source/subject boundary; do not add new Scope Units or expand configuration/tool features. Existing archived versions and unrelated Drafts are not migrated; selected Current updates create normal predecessors.

C/A/P/O content migration, Engine RMED, code, Tools/MCP/runtime, releases and Terms Graph implementation remain separate. [P2637 owns the later Engine RMED migration](CA-P-2637-EPIC--migrate-engine-rmed-atoms.md). Advanced formulas, functions and conditions in [] remain separate proposals and are excluded here.

### Order

**1. Mechanical Subject migration.** Prepare the exact frontier and thin mappings, then migrate subjects.governs before dependencies using the reviewed Model and new simple relation notation. Preserve content; do not gate this pass on a deep Claim review, adoption or complete missing Definitions. Hold only concrete unresolved mappings. This stage changes Subject-path notation only; it does not create native graph facts or apply newly introduced Relation Types to actual endpoints. Actual typed-relation changes wait until their relevant R Definitions are adopted in Stages 2–3. The later Definition-coverage pass therefore does not block this mechanical Subject pass.

- [CA-P-2684 — prepare the frontier and thin mappings](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/01-CA-P-2684-TASK--inventory-current-sources-and-reconcile-migration-drafts.md)
- [CA-P-2689 — apply the mechanical Subject migration](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/06-CA-P-2689-TASK--migrate-governing-paths-and-apply-the-new-relations.md)

**2. Adopt the reviewed Drafts with correct Subjects.** Reconcile each selected Draft with its actual Current predecessor, correct Governs/dependencies, then adopt it with the normal identity/version/archive treatment. Use the already reviewed packet; its existence is not adoption.

- [CA-P-2685 — reconcile the plain syntax/layout packet](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/02-CA-P-2685-TASK--complete-syntax-rmed-and-markdown-property-contracts.md)
- [CA-P-2688 — adopt the selected Drafts](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/05-CA-P-2688-TASK--adopt-the-formal-model-foundations.md)
- [CA-P-2690 — align necessary RMED body properties](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/07-CA-P-2690-TASK--migrate-rmed-body-sections-to-logical-properties.md)

**3. Complete Definitions and simple formal Claims.** Build coverage from both the Model and real governing Rs. Reuse existing Definitions before creating missing ones. Every declared in-scope entity must have adopted R/Entity Definition authority; define required properties, cardinalities, basic Formats and Relations. Add faithful R-only formal parts where possible and keep remaining conditions in prose. Preserve meanings and repair consumers before retiring superseded sources.

- [CA-P-2691 — own entity Definition coverage and bounded formalization](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/08-CA-P-2691-TASK--formalize-in-scope-claims-in-bounded-batches.md)
- [CA-P-2686 — complete used value Formats](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/03-CA-P-2686-TASK--complete-value-format-definitions-and-constraints.md)
- [CA-P-2687 — complete Relation Definitions](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/04-CA-P-2687-TASK--define-new-relations-and-their-derived-inverses.md)
- [CA-P-2692 — retire superseded sources after preservation](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/09-CA-P-2692-TASK--retire-superseded-contracts-after-preserving-their-meanings.md)

**4. Rebuild the Subject graph.** Generate the selected views from the adopted Current sources, including source IDs/Versions and defining R IDs. Do not substitute the proposal tree or hide unresolved source rows.

**5. Review the rebuilt graph and its Definitions.** Resolve findings, apply the corrections, rebuild and recheck the affected parts. A successful generation alone is not closure.

- [CA-P-2693 — own rebuild, actual-source review and closure](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/10-CA-P-2693-TASK--rebuild-the-actual-formal-model-views-and-close-the-migration.md)

### Model and authoring rules

The single root is Entity. Its four sibling branches are Object, Aspect, Graph Syntax and Carrier. Continuant and Occurrent specialize Object; Carrier stays separate from Object. Format and Relation are under Graph Syntax. Follow the latest Operator decisions and the repaired plain packet, not older candidate wording.

Use /, //, ., :, >, existing-kind @ references and ((RELATION_TYPE)); the new model needs no :: branch membership. Only specialization supplies inheritance. Containment has its declared immediate-whole rule; named-relation counts remain in prose. Direct facts are authored once and inverse views derived. A defining Atom can introduce its governed target; a string-format check does not demand prior existence.

Every complete RMED Atom requires direct prose Claim. R alone may add optional content.claim.formal_claim; it does not satisfy the prose count. Operative definitions belong in Claim; Semantics and Details explain/support. The top-level body properties are sibling ## Summary, optional ## Claim scope, ## Claim, optional ## Semantics and ## Details; ### Formal claim nests under Claim.

Use basic [format] and settled cardinalities {n}, {n+}, {n..m}. Counts apply independently to direct values, never nested keys; explicit {0} permits a grouping property with declared children, while omitted cardinality is undefined. list/map are carrier structures and identifying values use string, not ref. YAML null and empty strings are values; Formats and prose decide admissibility. Numeric conditions stay in prose for this scope.

### Tracking and execution

Keep the existing thin [Governs](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/governs.tsv) and [Depends On](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/depends_on.tsv) tables: Atom ID | old Subject | new Subject | status. Add a thin Definition-coverage list when Stage 3 starts: Subject | defining R IDs/Versions | status. Do not create copied-Claim inventories, per-Atom Analysis reports, confirmations or a new security/history framework.

Use bounded batches and leaf subtasks of at most 15 minutes. Use subagents for independent source/definition lanes with exclusive files. One owner handles shared Journal, adoption and integration. Use the supported operation path, or the already-authorized direct-file route when MCP cannot support it. Do not fix tools in this methodology Epic.

Preserve an existing Atom identity under the applicable rules; Summary or Content Role changes create successor identities. Check only the latest 48 hours of Operator input when confidence is below 90%; the latest words override older ones. If uncertainty remains, choose the best-supported option, create a C/Question, track it in A1305 with the latest candidate, and continue. No new kind, policy, scope boundary, field or function is invented merely to make a source pass.

### Preparation already completed

The [latest Entity-root candidate](../02_analysis/draft/CA-A-1302@1-draft-SPECIFICATION_PROPOSAL--entity-graph-candidate-with-four-root-branches.md) supersedes the root/Type naming of the [prior detailed inventory](../02_analysis/draft/CA-A-1239@1-draft-SPECIFICATION_PROPOSAL--formal-model-primary-kinds-and-properties.md). The prior inventory and selected Drafts were reviewed and repaired. [A1301](../02_analysis/CA-A-1301-ANALYSIS_REPORT--close-the-plain-model-review-repairs.md) closes the ten bounded plain-review findings. [A1297](../02_analysis/done/CA-A-1297-SPECIFICATION_PROPOSAL--separate-advanced-expressions-from-the-plain-model-review.md) defines the advanced-expression exclusion. These are preparation evidence, not Current migration results.

## Definition of Done

The selected Current frontier has migrated Subjects; the selected reviewed Drafts and missing R Definitions are adopted with correct Subjects; every declared in-scope entity has defining R authority; required simple property/Format/cardinality/Relation meaning is complete and advanced expressions stay separate. Superseded sources have a safe meaning/consumer disposition. The actual-source Subject graph has been rebuilt, reviewed, corrected and rechecked. No required unmapped row, missing Definition, broken consumer or omitted source is hidden by Done.

## Progress

Stages 1–3 are complete. The frozen authoring frontier has 1,108 Current Methodology and direct project-local RMED Atoms. Subjects are rooted at Entity; the formerly held Graph Rule paths have been mapped or retired. Forty-eight selected reviewed Drafts were adopted; additional missing Definitions, schemas and canonical legacy retentions were completed through the same staged predecessor-preserving route.

The actual-source coverage has 410 targets and 31 named Relation Types, with no required Definition/format/cardinality gaps. The direct source readback and native-reference checks pass. See [source review](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/source-review.md) and [thin Definition coverage](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/definition-coverage.tsv). A1305 tracks every chosen Question with the latest candidate.

Stages 4–5 are complete. CA-PROJ-014, CA-PROJ-015 and CA-PROJ-016 publish the primary-kind, property/inheritance and named Relation Type views from the frozen source vector. Actual source and artifact readback, renderer regression checks and bounded independent review pass. All ten child Tasks are Done. See the source-review report for exact evidence and limitations. No Engine, code, runtime, release or deferred Terms/advanced-expression work is included.

## Completion evidence

- [Subject Graph Primary Subjects](../_projection/CA-PROJ-014-CAPRMEDIO--Subject-Graph-Primary-Subjects--Current-Methodology-and-Project-RMED.md)
- [Subject Graph Properties](../_projection/CA-PROJ-015-CAPRMEDIO--Subject-Graph-Properties--Current-Methodology-and-Project-RMED.md)
- [Subject Graph Instances](../_projection/CA-PROJ-016-CAPRMEDIO--Subject-Graph-Instances--Current-Methodology-and-Project-RMED.md)

The model migration is complete for its declared authoring boundary. A1305 retains the chosen continuation Questions; C617 explicitly hands concrete Scope Unit ID carrier encoding to the separate Engine work. Runtime consumers have not been migrated or released by this Epic.
