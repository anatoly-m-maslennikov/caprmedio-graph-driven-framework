---
atom_id: CA-R-2275
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Term//ID
  passive:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Term
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Term Definition)'
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 1
role: Requirement
form: Term Definition
---
## Summary

Define ID

## Claim

### Prose Claim


The reusable lexical Term `ID` as used for identifiers of Continuant and Occurrent entity instances within a matching prefix namespace.


ID **means** a unique identifier used **to** find **`=1`** entity instance, whether Continuant **or** Occurrent, whose uniqueness is bounded **to** its matching prefix namespace. This Claim explicitly introduces the lexical Term instance named ID at `Entity/Object/Continuant/Term//ID`.

## Details

The Operator supplied this meaning and accepted `CA-P-123`, `CA-P-123@1-draft`, and `CA-P-123@3` as examples. The examples do not define lifecycle identity, version equivalence, Draft/Current/Archived transitions, or a rule for changing an existing identifier. Existing identifier and lifecycle authority retains those responsibilities. Matching local or numeric parts under different prefixes do not by themselves establish a collision; a collision within the matching prefix namespace does not satisfy the meaning.

`ID` is reusable in the accepted distinct complete qualified property names `atom.id` and `projection.id`. Their shared terminal label need not be globally unique. Dot remains qualification syntax rather than a Term. The accepted complete names are not changed to `atom.atom_id` or similar invented spellings, and existing code identifiers are not renamed.

This Term Definition is the dedicated authoritative meaning owner of the lexical Term ID under CA-R-1319 and CA-R-2468. M describes authoring and E evaluates well-formedness and conflicts. No dictionary Projection, extractor, or lookup service is required.

The lexical target is introduced by this defining Claim under CA-R-1194@29, CA-R-1931@15, and CA-R-2002@15, using the Current Term kind from CA-R-1318@28. It is not asserted to preexist this definition or inferred from the letters in property names. The definition introduces no property, domain instance, prefix namespace, Relation, or other entity merely by naming it. It neither waives CA-R-1279 nor implements the deferred Terms Graph; C605's separate Term-placement reconciliation remains applicable.
