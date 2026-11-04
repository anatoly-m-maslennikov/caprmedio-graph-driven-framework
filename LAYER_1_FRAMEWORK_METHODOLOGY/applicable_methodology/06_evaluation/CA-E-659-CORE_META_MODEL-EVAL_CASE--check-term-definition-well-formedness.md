---
atom_id: CA-E-659
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role: Method)/(.Header.Form: Term Definition)'
  passive:
  - CAPRMEDIO_MODEL <+ Term//ID
  - CAPRMEDIO_MODEL <+ Term
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom.Header.Subjects
version: 3
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 4
role: Evaluation
form: Eval Case
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-659-CORE_META_MODEL-EVAL_CASE--check-term-definition-well-formedness.md
  source_atom_id: CA-E-659
  source_atom_revision: 3
  source_sha256: fe1f7e9d82f5585c59a1eaeafe3f88db1120ba0f23db79ea1a3870d175a24374
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Check Term Definition well-formedness

## Claim

### Prose Claim


One selected Method Atom of Type Term Definition reviewed against its exact carried text **and** applicable Atom-shape rules. Cross-source authority uniqueness **and** authored occurrence consistency are checked separately under CA-E-444.


a Term Definition passes well-formedness **only** **when** it is explicitly classified as a Method Atom of Type Term Definition, identifies **`=1`** reusable word **or** phrase as its Term, carries **`=1`** independently replaceable Claim that establishes that Term's meaning within its stated Scope, **and** satisfies the applicable metadata, Subject-binding **and** body-layout rules. An Entity Definition, recurring descriptive wording **or** agreement among Semantics sections **must not** substitute for this dedicated Method Type. Missing **or** unresolved required evidence **must** remain visible **and** **must not** pass; local well-formedness alone **does not** establish unique defining authority **or** consistency of other authored sources.

## Details

### Test cases

1. Provide a Term Definition with admitted metadata **and** Subject binding, one explicit Term **and** meaning, one coherent Scope, one Claim **and** applicable supporting sections. Include a word Term **and** a phrase Term; no special dictionary schema **or** generated view is required.
2. Provide an ordinary Entity Definition with similar wording; two Terms with independently replaceable meanings **in** one candidate; a missing meaning Claim; contradictory Scope **and** Details; wrong Content Role or Method Type; a Requirement Atom classified as Term Definition; absent required metadata; **and** unresolved lexical Subject binding. A saved incomplete Draft is **not** automatically well-formed **or** ready for promotion.
3. Provide two locally well-formed active Term Definitions for the same Term, first with agreeing Claims **and** **then** with conflicting Claims. Local shape is assessed independently; CA-E-444 records duplicate defining authority **and** any source inconsistency. Ordinary vocabulary **without** established Project-specific Term use needs no dedicated Term Definition merely to satisfy this Evaluation.
4. Use an explicit `ID` Term Definition governing `Term//ID`, whose Claim introduces that lexical Term instance under the admitted defining-Atom target rules: a unique identifier used to find an entity instance, including Continuant **and** Occurrent instances, with uniqueness limited to matching prefixes. Test a conflicting definition **and** a Claim that extends uniqueness across unmatched prefixes. The examples `CA-P-123`, `CA-P-123@1-draft` **and** `CA-P-123@3` **must not** be used to invent version identity, prefix equivalence **or** case-folding rules.

### Acceptance criteria

The complete valid fixture passes its local shape **and** meaning-Claim checks. Each malformed fixture fails its evidenced local rule; an undeclared **or** unresolved lexical Subject binding remains a reported gap, **not** a fabricated selector **or** exemption. A different Content Role **or** Method Type **must not** pass as Term Definition merely because its prose describes a word. A well-formed Term Definition's meaning Claim is the source for the subsequent review of entity names, Claim, Claim Scope, Semantics, Details **and** other authored fields **in** that order under CA-E-444.

Every finding identifies the exact source Atom, Revision, logical field **and** occurrence **or** exact passage, plus the governing rule. Distinguish local well-formedness, cross-source defining-authority uniqueness, authored-use consistency **and** checked coverage. Agreement on meaning does **not** excuse duplicate active authority. Insufficient source selection **or** unresolved meaning remains unresolved; a complete combined result **must not** pass **when** a required check fails **or** remains unresolved. No dictionary, lookup service, synthetic Term node **or** Projection is created **or** required.

### Failure disposition

Preserve the malformed **or** unresolved source evidence **and** identify the precise correction **or** missing decision. Do **not** change the source Type, create a definition, infer a lexical Subject target, repair another source, **or** promote a Draft as a side effect of this Evaluation.

### Governing Type and lexical binding

Term Definition requires an admitted Type declaration in the Method Type domain. CA-R-2468's Requirement Type declaration does not establish that Method Type. Under the applicable target-admission rules, an explicit defining Claim **may** introduce its governed lexical Term instance; the `ID` fixture uses `Term//ID`. This lexical Term target is distinct from the Property entities referred to by the contextual topic/code spellings `atom.id` **and** `projection.id`. Parsing **or** spelling alone **does not** admit the target. Missing **or** uncertain binding remains a negative fixture requiring evidence, **not** an exemption. The Evaluation itself creates no targets **or** definitions.

