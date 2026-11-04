---
atom_id: CA-A-1318
version: 1
status: Draft
role: Analysis
form: Specification Proposal
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
updated_at: 2026-11-05 00:12:31 +0400
carrier_destination:
  file:
    name: CA-A-1318@1-draft-CORE_META_MODEL-SPECIFICATION_PROPOSAL--consolidate-cfel-syntax-and-precise-relations.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/02_analysis/draft
---
## Summary

Consolidate CFEL syntax and precise Relations

## Proposal

1. Define every CFEL operator, Relation and expression construct.
2. Keep each Atom's normative Claim about its active Subject.
3. Use short statements and coherent names. Remove staging notes and repeated rules.
4. Preserve exact predecessors and frozen references.

## Syntax decisions

- `=` tests a condition. `==` assigns a value. `?==` assigns a value when the Property is missing.
- Default assignment preserves valid explicit values and rejects invalid supplied values.
- Numeric ranges are inclusive. Format constraints separated by commas all apply.
- Project Settings AI Agent Confidence Threshold defaults to integer 90 in 0..100. The Plan override uses the same numeric domain.
- A standalone typed instance binding lasts through its CFEL block.
- An IF binding lasts through its condition and matching THEN group. A new binding uses a different name from a bound outer variable.
- Mixed AND/OR expressions use parentheses.
- Text stays bare when unambiguous. Double quotes protect text containing syntax. Inside quotes, only escaped quote and escaped backslash are valid escapes.
- Model names and Property paths remain references.

## Precise Relations

- SPECIALIZES is Direct from a specific Atom to a general Atom. Its Claim is more specific or stricter in the same or narrower applicability, while preserving applicable parent constraints.
- IS_SPECIALIZED_BY is the Derived inverse.
- Classify each existing child_of link by its actual Claims. Evaluation, implementation and dependency use their own precise Relations.
- Endpoint domains and outgoing permissions are separate. Each direction has its own applicable permission.

## Focused source cleanup

- Keep Relation Name and Meaning Claims about those Properties.
- Put the existing edge-identity rule in Relation, preserving it during Name cleanup.
- Preserve endpoint restrictions across the combined Formal Claim and Prose Claim.

## Model scope

- Entity means anything represented in the Subject graph.
- Relation, Term and Node keep their separate branches.
- Relation and Term each declare Property-bearing permissions. Narrower entities inherit the applicable rules.

## Rationale

Consistent assignment symbols make conditions and defaults readable. Explicit scopes preserve variable identity. Parentheses and quoting resolve syntax without implicit precedence. Separate LOOKUP authority keeps default assignment focused. Precise Relations describe what each contribution does.

## Created Draft packet

These Drafts were created and reviewed before their accepted source promotions. The adoption plans retain their exact payloads.

- CA-R-2487@12-draft
- CA-R-2605@2-draft
- CA-R-2705@3-draft
- CA-R-2711@3-draft
- CA-R-2564@3-draft
- CA-A-1315@3-draft
- CA-R-2768@1-draft
- CA-R-2769@1-draft
- CA-R-2770@1-draft
- CA-R-2771@1-draft
- CA-R-2772@1-draft
- CA-R-2773@1-draft
- CA-R-2774@1-draft
- CA-R-2766@1-draft
- CA-R-2767@1-draft
- CA-R-2601@2-draft
- CA-R-2604@2-draft
- CA-R-2711@5-draft
- CA-R-1020@32-draft
- CA-R-1021@32-draft
- CA-R-2247@8-draft
- CA-R-2354@6-draft
- CA-R-2355@6-draft
- CA-M-451@6-draft
- CA-R-2247@10-draft
- CA-R-1318@36-draft
- CA-R-2170@11-draft
- CA-R-2485@6-draft
- CA-R-2765@4-draft

Updated and reviewed existing Drafts: CA-R-1318@34-draft and CA-M-453@4-draft. The Property Draft was rebased on Current before promotion.

## Remaining work

- Reconcile legacy Subject paths and ambiguous Relation domains.
- Split normative rules that govern unrelated Subjects.
- Classify the 343 legacy child_of links before migration.
- Complete source verification and rebuild the selected MODEL projections.
- Obtain parser, runtime and integration evidence from their owners.

Workbench and Workflow definitions remain owned by their other agents. This proposal does not supply their runtime verification.

## Successor design proposal

CA-A-1321@1-draft records the separate declarative notation proposal. Its new glyph meanings and named-instance grammar are not Current syntax yet.
