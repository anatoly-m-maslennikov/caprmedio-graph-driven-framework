---
atom_id: CA-O-017@15
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Implementation Preparation
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Spec
  - Subject/Domain/Node/Continuant/Atom
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Method'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan/Type: Plan'
  - 'Entity/Node/Continuant/Atom/Content Role: Plan.Definition of Done'
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Dependency Order Derivation
  - Subject/Domain/Node/Continuant/Scope Unit
version: 15
updated_at: 2026-10-24 00:38:25 +0400
relations:
  relates_to:
  - CA-R-2117
  - CA-M-431
  - CA-E-653
  - CA-M-239
  - CA-M-266
  - CA-M-306
  - CA-R-1589
  - CA-R-1592
  - CA-R-1599
  - CA-R-1591
  - CA-D-481
  - CA-R-1525
tier: 3
---
# Summary

Prepare implementation work

## Operation

Implementation Preparation **means** the Agentic Action that resolves an implementation request into persistent Plan work **and** the next prerequisite-ready item.

### Inputs and authority preparation

- receive the bounded implementation request, an existing P/Plan Atom **when** supplied, admitted authority sources **and** their declared input universe, the selected implementation mode, complete execution inputs, retained work, candidate-specific evidence, **and** applicable permissions.
- gather the selected active Requirement **and** Delivery Atoms as what **to** implement: required behavior, constraints, Carriers, **and** delivery boundaries. gather applicable Evaluation Atoms separately as check authority; retain test-first work rather than dropping E from the Run.
- bind direct full-source rows in `requirements`, `methods`, `evaluations`, **and** `delivery`; each `methods` row uses the same shape and preserves full content, Atom ID, Version, source path, **and** digest. Do **not** replace Claims with summaries **or** silently omit selected sources.
- bind the complete explicit declared source universe and verify original current source content, identities, Revisions, paths, **and** digests. An authorized/frozen initial request may explicitly select roots; expand declared governing parents per root, retain other explicitly selected applicable policy branches, **and** evaluate Scope/capability conditions. Parent relations alone do not define applicability. Do **not** infer it from physical directory ancestors **or** irrelevant siblings. stale sources, conflicting identities, missing content, **or** unverifiable completeness return `blocked`.
- apply only the resulting applicable Methods to selected work. A supplied `method_projection` is an optional legacy derived convenience, not Method authority: it neither replaces direct rows **nor** blocks readiness when absent. Do **not** require or generate a compiled file **or** semantic paragraph. An authorized authority change requires refreshed direct source bindings.
- include applicable higher-tier authority, current Project Principles, concrete input/output boundaries, **and** test commands **or** enough admitted information **to** establish them. incomplete **or** conflicting authority returns `blocked`, **not** guessed scope.

- map every applicable selected R/M/D obligation to a substantive Evaluation predicate, selected check or semantic review, and required evidence, or an explicit justified inapplicability. A relation link or green linter alone does not establish coverage. Missing required Evaluation authority blocks readiness; resolve authorized E definitions before implementation. Optional source-bound review guidance/projections may be refreshed where useful; they are not authority or readiness prerequisites.

### Plan preparation and selection

- reuse the supplied Plan **and** existing suitable decomposition. **when** no Plan was supplied, create the admitted P/Plan for the bounded request **before** code work starts. Tasks **and** subtasks are P/Plan Atoms with their own Claims, Assignees, **and** Definitions of Done, **not** Workflow Steps **or** an ephemeral checklist.
- **when** practical, decompose work into independently verifiable P Atoms with an ETA **<15** minutes for one assigned AI Agent. record the estimate **and** its assumptions **in** Plan Details; it is an estimate, **not** an automatic time limit. **if** safe decomposition cannot meet the applicable leaf-work bound, return the specific blocker rather than inventing small estimates **or** weakening the Definition of Done.
- store `IS_DECOMPOSITION_OF` **only** on the child Plan **and** actual start prerequisites through `BLOCKS`, following CA-M-306 **and** CA-D-481. preserve an acyclic combined completion graph under CA-R-1592. navigation order is **not** a dependency.
- select **=1** ready bounded Plan item and the context explicitly bound by the invoking Step for test, implementation, diagnosis, and repair work. Integrated Steps retain the participating session; Isolated Steps require their admitted complete handoff. provide source-bound inputs, owned files/work boundary, expected outputs, verification, relevant prior results, **and** effective confidence/retry gates; preserve unrelated work.
- derive prerequisite-first work order under CA-M-239. prepare tests **before** the behavior they check wherever actual prerequisites permit; execute the prepared baseline tests **before** implementing that behavior **when** runnable. minimum execution prerequisites are explicit, **not** permission **to** implement the entire feature first. use Atom ID **only** **to** break remaining ties between ready work items.
- unchanged implementation mode, governing RMED, **and** complete execution inputs **must** yield the same applicable work **and** prerequisite-respecting order. retained results determine residual work, **not** a different normative interpretation.
- retain completed work **and** candidate-specific evidence. a new Method activation **or** other authorized authority change requires refreshed direct source bindings **and** renewed work/Evaluation resolution; it does **not** erase prior effects **or** reset retry accounting.

### Results and execution boundary

- return `evaluation_ready`, `requirement_ready`, `evaluation_runnable`, or `review_ready` with the selected Plan, exact work, prerequisites, assigned context, current baseline, gathered R/D targets, direct RMED source-row bindings, **and** separate Evaluation authority.
- select test preparation first, then its runnable baseline, then ready behavior implementation. After implementation or repair, select review_ready with explicit preliminary phase; after preliminary_clear, select evaluation_runnable for final checks; after current final checks pass, select review_ready with explicit final phase. Retain actual phase evidence, not a resettable completion flag; missing prerequisites block rather than skip a phase.
- return `complete` only with current final review and complete final checks bound to the same candidate, test definitions, source authority, selected portfolio, and relevant inputs, and **only** after **all** selected implementation Plan work, required child Plans, Definitions of Done, **and** applicable Evaluations are satisfied, with no failed, blocked, stale, **or** unevaluated implementation obligations. return retained issue/diagnosis/fix evidence for separate Method learning; creating **or** accepting a Method is **not** a completion condition **or** a next Step **in** this Run.
- return `blocked` for unmet authority, capability, confidence, permission, prerequisite, **or** Plan admission, including nonempty residual work with no ready next item.
- current execution uses the host's native subagent, file, **and** command capabilities. MCP **or** a running Workflow server is **not** required. missing capability blocks only work requiring it; never substitute another context silently. Step bindings own the Integrated/Isolated choice; do **not** introduce a Workflow-wide context Property.

## Details
