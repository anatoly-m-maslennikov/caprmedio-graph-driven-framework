---
atom_id: CA-P-2685@10
content_role: Plan
type: Plan
label: Task
current_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Formal Model
version: 10
updated_at: 2026-10-28 23:40:14 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2683
tier: 4
---
# Summary

Complete syntax RMED and Markdown property contracts

## Objective

Complete syntax RMED and Markdown property contracts.

## Details

After CA-P-2684.

Reconcile the syntax/layout successor Drafts with A1240–A1243. Define the Formal Model root, Graph Syntax and the exact meanings of /, //, ., :, ::, >, @(...), ((RELATION_TYPE)), cardinality and format annotations. Distinguish a governing node selector from the formal Claim that constrains it. Preserve the declared direct direction and derive inverse views; no separate backwards syntax or duplicate inverse fact is created.

Complete R definitions, M authoring instructions, E acceptance cases and D representation contracts needed for these constructs. The source of authority is methodology, not what the old code currently accepts. Require one Role/Type-defined Claim, prose directly in ## Claim and optional ### Formal claim at content.claim.formal_claim. Preserve the exact Summary/Claim scope/Claim/Semantics/Details order and conditional scope rule. Semantics explains meaning outside the Claim.

Register Markdown-to-property naming and nesting: lowercase, spaces to underscores, strip characters except letters/numbers/_/-. Review collision, empty-key, duplicate-sibling, fenced-heading and skipped-level cases. Canonical paths follow actual parents; flat shortcuts must not silently choose ambiguous targets. Record any unresolved identifier/escaping case instead of inventing a parser policy. Keep getter APIs as the separate proposal A1237.

## Definition of Done

The required syntax/property RMED is complete and agrees with the latest decisions; unresolved cases are explicit; no source promotion or tool/runtime work is claimed.

## Progress

Not started. Prior analysis and Drafts are inputs, not completion evidence.

## R-only scope

Only R enters operative formal Claim conversion. M/E/D may describe syntax, Formats and Relations in prose and undergo the shared body/path migration, but have no operative content.claim.formal_claim field in this iteration. A1244 records the latest scope.

## Latest prepared decisions

CA-A-1251 places value Format under Graph Syntax. CA-A-1252 places Code Units inside Modules. CA-A-1253 makes each contained part belong to exactly one immediate whole. CA-A-1254 removes the Code wrapper: Implementation contains the root Package; Packages contain nested Packages, Modules and Assets. CA-A-1255 adds Prompt under Package and distinguishes LLM-agent execution from language-engine execution. Definition and notation Drafts reflect these changes. The consolidated model Draft was rebuilt; no Current source promotion is claimed.

CA-A-1256 removes the independent Operations /@(Step) classification and the duplicate Continuant references. Prepared R1508/R1509/Substep Definitions use Workflow >{1..} Step >{0..} Substep. The model Draft was rebuilt without transferring Atom properties through containment.

CA-A-1257 fills the requested R/A/C/E/M Type branches and prepares the affected Definition/Type-catalog Drafts. Label remains a property; Epic, Task, Subtask and Version are Plan Label examples, not new Types or a closed whitelist. Source catalog reconciliation remains open and no Current Type/Label migration is claimed.

CA-A-1258 corrects Project to Scope Unit/Project with no parent Scope Unit. CA-A-1259 removes Implementation as a kind: it is only a section heading; Package/Project Implementation is the root Package. Corresponding Definition/Delivery Draft selectors and the primary/properties model are refreshed. Former R2173 wrapper Draft is superseded. Documentation and Resources are retained separately awaiting placement. Current Atoms remain unchanged.

A1262–A1264 resolve Substep nesting and call targets: Substeps are Action-only leaves; leaf Steps call one Action or Workflow with parameters; containing Steps make no own call. Prepared R1508/R1509/Substep/R1511 definitions and the Formal Model proposal are updated. The Update Atom example is preserved in A1263 without creating Workflow instances. Current sources and Engine implementation remain unchanged.

CA-A-1265 settles colon with a formula on its right-hand side: still an allowed-value declaration, not assignment or a literal formula string. The ID expression uses Atom.id: ...; no equals operator is introduced and > remains structural containment. Formula grammar, property bindings and evaluator implementation are not claimed complete.

CA-A-1266 distinguishes runtime-required non-executable Assets from non-runtime Documentation. Both are Package parts; Documentation is not an Asset subtype. Prepared Asset/Documentation/Package definitions and the model tree are updated. Resources remains unplaced; the build/test runtime boundary awaits the Operator. Current sources and files are unchanged.

CA-A-1267 resolves the runtime/test boundary: both Modules and Assets can serve runtime or tests. This is usage, not a new primary kind or mandatory property. Prepared Module/Asset/Package/Documentation definitions and the proposal are aligned. Resources member mapping remains separate; no Current source or implementation migration occurred.
