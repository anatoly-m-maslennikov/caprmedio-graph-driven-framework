---
atom_id: CA-E-659
ref_id: CA-E-659
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method)/(.Header.Form := Term Definition)
  dependencies:
  - CAPRMEDIO_MODEL <+ Term//ID
  - CAPRMEDIO_MODEL <+ Term
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom.Header.Topics
tier: 4
status: Active
version: 6
updated_at: 2026-11-04 18:28:33 +0400
carrier_destination:
  file:
    name: CA-E-659-EVAL_CASE--check-term-definition-well-formedness.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
---
## Summary

Check Term Definition well-formedness

## Claim

### Prose Claim


One selected Method Atom with Form Term Definition reviewed against its exact carried text **and** applicable Atom-shape rules. Cross-source authority uniqueness **and** authored occurrence consistency are checked separately under CA-E-444.


a Term Definition passes well-formedness **only** **when** it is explicitly classified as a Method Atom with Form Term Definition, identifies **`=1`** reusable word **or** phrase as its Term, carries **`=1`** independently replaceable Claim that establishes that Term's meaning within its stated Scope, **and** satisfies the applicable metadata, Subject-binding **and** body-layout rules. An Entity Definition, recurring descriptive wording **or** agreement among Semantics sections **must not** substitute for this dedicated Method Form. Missing **or** unresolved required evidence **must** remain visible **and** **must not** pass; local well-formedness alone **does not** establish unique defining authority **or** consistency of other authored sources.

## Details

### Test cases

1. Provide a Term Definition with admitted metadata **and** Subject binding, one explicit Term **and** meaning, one coherent Scope, one Claim **and** applicable supporting sections. Include a word Term **and** a phrase Term; no special dictionary schema **or** generated view is required.
2. Provide an ordinary Entity Definition with similar wording; two Terms with independently replaceable meanings **in** one candidate; a missing meaning Claim; contradictory Scope **and** Details; wrong Content Role or Method Form; a Requirement Atom classified as Term Definition; absent required metadata; **and** unresolved lexical Subject binding. A saved incomplete Draft is **not** automatically well-formed **or** ready for promotion.
3. Provide two locally well-formed active Term Definitions for the same Term, first with agreeing Claims **and** **then** with conflicting Claims. Local shape is assessed independently; CA-E-444 records duplicate defining authority **and** any source inconsistency. Ordinary vocabulary **without** established Project-specific Term use needs no dedicated Term Definition merely to satisfy this Evaluation.
4. Use an explicit `ID` Term Definition governing `Term//ID`, whose Claim introduces that lexical Term instance under the admitted defining-Atom target rules: a unique identifier used to find an entity instance, including Continuant **and** Occurrent instances, with uniqueness limited to matching prefixes. Test a conflicting definition **and** a Claim that extends uniqueness across unmatched prefixes. The examples `CA-P-123`, `CA-P-123@1-draft` **and** `CA-P-123@3` **must not** be used to invent version identity, prefix equivalence **or** case-folding rules.

### Acceptance criteria

The complete valid fixture passes its local shape **and** meaning-Claim checks. Each malformed fixture fails its evidenced local rule; an undeclared **or** unresolved lexical Subject binding remains a reported gap, **not** a fabricated selector **or** exemption. A different Content Role **or** Method Form **must not** pass as Term Definition merely because its prose describes a word. A well-formed Term Definition's meaning Claim is the source for the subsequent review of entity names, Claim, Claim Scope, Semantics, Details **and** other authored fields **in** that order under CA-E-444.

Every finding identifies the exact source Atom, Revision, logical field **and** occurrence **or** exact passage, plus the governing rule. Distinguish local well-formedness, cross-source defining-authority uniqueness, authored-use consistency **and** checked coverage. Agreement on meaning does **not** excuse duplicate active authority. Insufficient source selection **or** unresolved meaning remains unresolved; a complete combined result **must not** pass **when** a required check fails **or** remains unresolved. No dictionary, lookup service, synthetic Term node **or** Projection is created **or** required.

### Failure disposition

Preserve the malformed **or** unresolved source evidence **and** identify the precise correction **or** missing decision. Do **not** change the source Atom role or form, create a definition, infer a lexical Subject target, repair another source, **or** promote a Draft as a side effect of this Evaluation.

### Governing Form and lexical binding

Term Definition requires the Method Form admitted by declaration CA-R-2765, which specializes the existing Method declaration CA-R-2513. CA-R-2468 registers Declaration as a Requirement Form and does not admit Term Definition as a Method Form. CA-R-1318 defines the Term kind. CA-R-1319 keeps the flat target family `Term//<Name>` and includes `Term//ID` among approved target names. Under current target-admission Rules CA-R-1194 and CA-R-1931, an explicit defining Claim **may** introduce that governed target; the `ID` fixture does so at exactly `Term//ID`. This lexical Term target is distinct from the Property entities referred to by the contextual topic/code spellings `atom.id` **and** `projection.id`. Parsing **or** spelling alone **does not** admit the target. Missing **or** uncertain binding remains a negative fixture requiring evidence, **not** an exemption. The Evaluation itself creates no targets **or** definitions.

