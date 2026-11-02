---
atom_id: CA-P-2685@25
content_role: Plan
type: Plan
label: Task
current_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Formal Model
version: 25
updated_at: 2026-10-29 02:57:48 +0400
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

CA-A-1268 names the root Model. Active prepared Draft selectors and proposed tracking targets use Model::...; historical/superseded preparation and Current sources remain unchanged. CA-A-1269 adds Runtime Package and Test Package specializations. CA-A-1270 names the kind Asset File, with a new unnumbered replacement Definition Draft; the old Asset Draft is marked superseded. Model/Runtime Package/Test Package Definitions are prepared. No parser, runtime, governing-config or Current methodology migration is claimed.

CA-A-1271 overrides Asset File naming: Asset is the logical kind; files remain Carriers. Active prepared references and the model use Package > Asset. The original unnumbered Asset Definition is restored as the promotion candidate; the Asset File naming Draft is explicitly superseded. Runtime/test Package specializations and the Model root remain unchanged. Current methodology and runtime are untouched.

CA-A-1272 renames Test Package to Eval Package, supporting both Modules and Prompts for evaluations. The new Eval Package Definition replaces the old naming Draft; prepared references and the Model proposal are aligned. Evaluations include executable tests and Prompt-based checks. No Current sources or runner code changed.

CA-A-1273 removes Tool as a primary kind; Tool instances remain Scope Units with Package implementations. CA-A-1274 uses API as the umbrella for CLI, Web/REST, RPC and other forms. CA-A-1275 places API Self Documentation in Engineering. Two abstract Definition Drafts are prepared. R2197 retirement and R2205 replacement are tracked; R2204 Effect Result remains unresolved. No mandatory API field, universal exposure rule, specific Scope Unit, code or runtime is created.

CA-A-1276 resolves old Effect Result mapping: Execution.Result is actual execution data/effects; Engineering/API Result Contract describes expected structure and meaning. Event Records can preserve actual results without a universal recording requirement. Two Definitions are drafted; the unspecified Outcome placeholder is replaced in the proposal. R2204 replacement is tracked; no Current source, result envelope or runtime change occurred.

CA-A-1277 permits direct and indirect recursive Workflow calls through leaf Steps. Workflow/Step Definition Drafts and the Model proposal reflect this; no acyclic-call constraint or mandatory recursion limit is introduced. Substeps remain Action-only leaves. Current source adoption and Engine behavior are unchanged.

CA-A-1278 removes Resources as too broad. R2189 retirement is tracked; R2190–R2193 next-version Drafts place non-executable Configuration, Schema, Template and Test Fixture under Asset. Prompt, Documentation and Governing Configuration boundaries are preserved. The proposal and Asset Draft reflect this; Current source promotion/retirement and implementation remain pending.

CA-A-1279 reconfirms Workflow >{>=1} Step >{>=0} Substep as the settled container hierarchy. Definition Drafts and the Model proposal use that notation. No new Type decision or implementation work is inferred.

CA-A-1280 adds exact `{n}`, unbounded `{n+}` and inclusive bounded `{n..m}` cardinalities, including `{0}`, `{1}`, `{0+}`, `{1+}` and `{0..1}`. A new Definition Draft and the R/M/E/D notation Drafts cover meanings, bounds, count direction, invalid cases and carrier preservation. Container Drafts use Workflow >{1+} Step >{0+} Substep. Current methodology and runtime remain unchanged.

CA-A-1281 groups the complete composed Atom ID allowed value after the colon and applies `{1}` after the closing parenthesis. Component int/uniqueness annotations remain local. The proposal and relevant R/M/E/D Drafts are aligned; no property Subject rename, new stored component or parser change is introduced.

CA-A-1282 defers general formula expressions, not just ID composition. The main Model and relevant syntax R/M/E/D Drafts omit operative composition, value interpolation, formula grouping and function-style uniqueness requirements. The formula examples remain in the separate Spec Proposal. Retained syntax includes relationships, existing-kind references, cardinalities, formats and general named relations. Existing ID rules and Current sources are unchanged.

CA-A-1283 makes cardinality independent at each property path and counts only direct values. Explicit subjects{0} allows governs{1} and dependencies{0+}; nested keys do not contribute to parent counts. YAML keys are unique, multi-values use sequences, and list is removed as a Format. RMED requires direct prose Claim; R optionally adds an independently counted formal child. Related R/M/E/D Drafts and formal-only prepared Definitions are aligned from their existing meanings. Current sources and runtime remain unchanged.

CA-A-1284 confirms that omitted cardinality is undefined, never an implicit {0}. Explicit subjects{0} and independent child counts remain unchanged. The Cardinality Notation and Model Drafts state the distinction; no Current or runtime change occurred.

CA-A-1285 uses string for Subject paths. Basic format checks cover string values and admitted Model notation without requiring prior existence; a defining Atom may introduce its target and path together. Subject cardinalities and the existing YAML dependency key stay unchanged. Related Drafts and Model examples are aligned; Current sources and runtime remain untouched.

CA-A-1286 removes map from value Formats. Nested property paths describe structure; YAML mappings carry it. The Model and Value Format Drafts reflect this without changing child counts or YAML field names. Current sources and runtime remain unchanged.
