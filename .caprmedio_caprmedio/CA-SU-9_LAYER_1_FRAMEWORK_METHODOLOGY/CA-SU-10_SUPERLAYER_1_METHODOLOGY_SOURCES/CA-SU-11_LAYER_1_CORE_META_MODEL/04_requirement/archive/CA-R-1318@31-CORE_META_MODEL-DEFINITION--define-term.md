---
subjects:
  active: Term
  passive:
  - Project
  - Entity
  - Term.Name
  - Term//Term
  - Term//Empty
  - Term//ID
  - Term//Entity
  - Entity/Property
  - Term//Property
version: 31
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1318@31
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 1
role: Requirement
form: Entity Definition
---
## Summary

Define Term

## Claim scope

Project-specific vocabulary used as reusable lexical components of complete or qualified entity names and authored content, including the word `Term` itself.

## Claim

A Term is a direct specialization of Entity at `Term`. A Term has one Name, the word or phrase used for its meaning. Its named instances initially form a flat set, using `Term//<Name>` without additional Term groups. This declares the vocabulary kind and its existing Name property; it does not implement the deferred Terms Graph.

**every** instance of `Term` **must** represent a reusable word **or** phrase component of complete **or** qualified entity expressions **and** authored content whose approved Project-specific meaning remains consistent across **all** its uses.

### Formal claim

```text
Term
Term.Name[string]{1}
```

## Details

This Requirement Atom of Type Entity Definition defines the kind at `Term` and its Name property. Its Claim states membership and structural constraints; the separate proposed Method Term Definition owns the word Term's lexical meaning at `Term//Term`. That Method Draft explicitly introduces the lexical instance. This structural Requirement does not supply its dedicated Method ownership or prove its admission under CA-R-1319. Using the word Term in its own definition does not require another lexical instance or an infinite chain of definition layers.

The lexical forms `Package`, `Eval Package` and `Runtime Package` illustrate reuse of the Term `Package`; `Scope Unit` and `Code Unit` illustrate reuse of the Term `Unit`. These lexical forms are not asserted to be complete canonical entity names outside the Term branch. An Entity outside the Term branch uses its complete source-admitted expression as its canonical name. Its complete name cannot be just one registered Term; the sole exception is `Entity`, because it is the Subject root. Reusable Terms occur as components within qualified expressions. Reusing `Package` inside `Eval Package` does not itself reference the separately named `Package` entity or establish a Relation. Lexical composition does not introduce another entity or require a separate `Unit` instance.

The earlier schematic example `Package > Module > Code Unit` connects three entities; its short displayed labels do not by themselves establish their full canonical names. Authored references use the complete source-admitted expressions for those entities. The contextual topic/code spellings `atom.id` and `projection.id` distinguish their respective ID Properties; they are not alternative complete canonical Subject names or case-folded aliases. Authored Subjects use their full admitted expressions. These spellings reuse the Term `ID`; their shared terminal label is not a collision. The dot remains an operator. Neither spelling is replaced with `atom.atom_id` or another invented spelling. Arbitrary composite expressions are not one Term under CA-R-1325 or automatically one entity name. Literal source quotations and code identifiers are distinguished from authored entity mentions and are not automatically renamed.

A Governed Term has exactly one dedicated active Method Atom of Type Term Definition as its authoritative meaning owner under the proposed successor of CA-R-1319 and the new Method-qualified Type declaration. The lexical Term target is distinct from an entity whose complete name uses it. A defining Atom may explicitly introduce its lexical target under CA-R-1194 and CA-R-1931; a parser or word occurrence does not introduce it. The confirmed placement supplies direct lexical targets such as `Term//Empty` and `Term//ID`; these examples do not generate their lexical definitions or establish those instances without the respective defining Claims. No dictionary Projection, extractor, lookup, Term groups, or Terms Graph implementation is required.

The only Entity outside the Term branch whose complete canonical name is also a registered Term is `Entity`, because it is the Subject root. The R / Entity Definition governs `Entity`; the M / Term Definition governs `Term//Entity`. Their matching word does not merge the two targets. Root status in another hierarchy does not extend this sole Subject-root exception.

Use the full expression when identifying or comparing entities. `Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: X)/(.Type: X)` is a possible qualified expression: the repeated X components retain the same Term meaning while their complete qualifications differ. Each value still requires admission in its own context; the example does not introduce X or new value admissions. Likewise, `Entity/Property` is a qualified entity expression, while Property is the lexical Term at `Term//Property`. This distinction does not withdraw either pending definition or require a new Term Definition for every complete entity expression.

### Draft source pin

The Operator explicitly confirmed direct `Term` placement, an initially flat set, and Content Role Method for Term Definitions; this latest decision supersedes the earlier Requirement-role lexical ownership and Object/Continuant placement. This is a proposed semantic revision of Current CA-R-1318@29. Its Requirement Content Role, Summary and Entity Definition Type are retained; the Name cardinality remains exactly one at the new root.

Source path: `/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1318-CORE_META_MODEL-DEFINITION--define-term.md`. Source SHA-256: `02063cdcc24fa8ccc40ad6008958c821ccbf3608229a80f454a5d81a441e928d`. Source-fingerprint snapshot: `/tmp/cce-term-root-migration-20261029/current-before.json`; snapshot SHA-256: `23c1414c96d6e57cdc9f1bf50569de396ef130a7231b765cd8b4511bcb573ad5`. This Draft changes no Current source, allocates no identity and performs no promotion.
