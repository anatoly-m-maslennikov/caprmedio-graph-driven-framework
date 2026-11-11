---
atom_id: CA-M-450
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Term//ID
  passive:
  - CAPRMEDIO <+ MODEL <+ Term
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Method)/(.Type: Term Definition)'
version: 4
updated_at: 2026-11-02 19:46:47 +0400
relations: {}
tier: 1
role: Method
form: Term Definition
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-450-CORE_META_MODEL-TERM_DEFINITION--define-id.md
  source_atom_id: CA-M-450
  source_atom_revision: 4
  source_sha256: 7a4d720c61fb905a7503424b471ddeb68ceec39fd47865a7d10a9bb9da3878a4
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define ID

## Claim scope

The reusable lexical Term `ID` as used for identifiers of Continuant and Occurrent entity instances within a matching prefix namespace.

## Claim

ID **means** a unique identifier used **to** find **`=1`** entity instance, whether Continuant **or** Occurrent, whose uniqueness is bounded **to** its matching prefix namespace. This Claim explicitly introduces the lexical Term instance named ID at `Term//ID`.

## Details

The Operator supplied this meaning and accepted `CA-P-123`, `CA-P-123@1-draft`, and `CA-P-123@3` as examples. The examples do not define lifecycle identity, version equivalence, Draft/Current/Archived transitions, or a rule for changing an existing identifier. Existing identifier and lifecycle authority retains those responsibilities. Matching local or numeric parts under different prefixes do not by themselves establish a collision; a collision within the matching prefix namespace does not satisfy the meaning.

`ID` retains its approved meaning across its uses. The contextual topic/code spellings `atom.id` and `projection.id` distinguish their respective ID Properties; they are not alternative complete canonical Subject names or case-folded aliases. Authored Subjects use their full admitted expressions. Their shared terminal label need not be globally unique. Dot remains qualification syntax rather than a Term. These literal spellings are not changed to `atom.atom_id` or similar invented spellings, and existing code identifiers are not renamed.

This Draft proposes a Method Term Definition as the dedicated authoritative meaning owner of the lexical Term ID, preserving the approved meaning from the exact Current source `.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2275-CORE_META_MODEL-TERM_DEFINITION--define-id.md`, Requirement CA-R-2275 Version 1, SHA-256 `e07b52086e0205f0400c6f01db7a8d2bff52b0dbc94fbf68d785283400ae6402`. E evaluates well-formedness and conflicts. No dictionary Projection, extractor, or lookup service is required.

The proposed lexical target follows the Operator-confirmed initially flat placement at `Term//ID`; the separate Term branch and Method Type Term Definition declaration remain Draft dependencies. The target is explicitly introduced by the defining Claim rather than inferred from the letters in property names. The definition introduces no property, domain instance, prefix namespace, Relation, or other entity merely by naming it. It does not implement the deferred Terms Graph or waive the applicable defining-target binding rules; C605's separate Term-placement reconciliation remains applicable.

Adoption requires a new canonical Method identity because the Content Role changes from Requirement to Method; the role-only `CA-M-draft` marker allocates no number and does not transfer CA-R-2275's identity. The replacement plan retires only the exact pinned Core Requirement source after this Method replacement and its governing declarations have been validated and adopted. Until that replacement is completed, this Draft does not retire, archive, overwrite, or supersede any Current source by itself. No ID-only lookup is sufficient to select the predecessor.

### Pending governing declarations

- [Entity root with the Term branch](../../04_requirement/draft/CA-R-1248@24-draft-CORE_META_MODEL-DEFINITION--define-entity.md).
- [Term kind and inherited structure](../../04_requirement/draft/CA-R-1318@30-draft-CORE_META_MODEL-DEFINITION--define-term.md).
- [Method Type Term Definition](../../04_requirement/draft/CA-R-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-method-type-term-definition.md).
- [Dedicated Method meaning owner](../../04_requirement/draft/CA-R-1319@26-draft-CORE_META_MODEL--define-governed-term.md).

These links identify pending Draft dependencies, not Current admission.

The former Current collision was explicitly repaired under CA-M-276: the original ID Term Definition retains `CA-R-2275` and its exact pinned bytes; the later Settings definition now carries `CA-R-2423@1`. Journal event `0e1853d5-f441-4bc7-9460-bd4db67a0c3c` preserves the correction mapping and preimage. The original number remains reserved. Generated views containing the old Settings provenance still require regeneration; that remaining derived-output work does not change this exact predecessor pin.
