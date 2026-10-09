# CA-P-1920 — derived RMED views

Non-authoritative pointer views from the pinned Core baseline. They neither migrate sources nor admit semantics, relations, applicability, locus, or inheritance.

Baseline inventory: `23394abaf6e9c18a585cf3146aedd0a80df166c9dd82be6e86ed7c3c56780bdc`. All 908 selected source-carrier byte hashes match their baseline pins.

## Role-centered overview

| Role | View purpose | GOVERNS pointers | Governed identities | DEPENDS_ON pointers | Dependency identities |
| --- | --- | ---: | ---: | ---: | ---: |
| R | model skeleton and required results | 524 | 283 | 1535 | 226 |
| M | construction and authoring conventions; excludes Operations-specific actions and workflows | 59 | 55 | 292 | 132 |
| E | checks and acceptance evidence | 77 | 67 | 588 | 181 |
| D | Carrier model, formats, and placement or storage; a direct Delivery definition can also be a model-skeleton input | 145 | 122 | 429 | 155 |

`GOVERNS` and `DEPENDS_ON` are separate pointer channels. A dependency is never rendered as a governing Claim. `Operations` (102 governing / 782 dependency pointers) and `Concern` (1 / 0) remain outside RMED; M does not stand for Operations.

## Entity-centered view

The JSON contains 580 literal target identities. Each has separately keyed governing pointers and dependency pointers, plus nonempty optional M/E/D governing links. Membership is pointer-derived only; shared source pins live once in `source_catalog`.

Detailed presentation trees: `rmed.roles.indented.txt` and `rmed.entities.indented.txt`. Their slash-prefix indentation is display only; it does not assign slash semantics or create Entity hierarchy.

## Source-backed examples

- `R` `CA-R-655@23:28258bfdc5515abe6efa40fe8ab1951cc70a226f58daaa6ced7466036bbca29d` → `Atom`: .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-655-CORE_META_MODEL-CORE--define-atom-artifact-form.md:26 — an Atom **means** the smallest independently governed Artifact.
- `M` `CA-M-111@25:c762357b6e9c9478e559d2abeaa5dc86ccd316e66957123b50d5391e0ba703c5` → `Atom Claim Authoring`: .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-111-CORE_META_MODEL--author-one-cce-claim-and-derived-summary.md:30 — **to** author one CCE Claim **and** its derived Summary, an Author **must** use these authoring constraints:
- `E` `CA-E-520@5:9e3cdee5027c3e24cb91e1ce9fe009dc281b499a49a45aaacea38f3ff59fcada` → `Atom`: .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-520-CORE_META_MODEL-EVALUATION_APPROACH--check-rmed-atom-coherence.md:41 — an RMED Atom passes this local Evaluation **only** **when** **all** of these checks pass with source evidence:
- `D` `CA-D-414@14:f0d1d76efc3191ec5dd067f692f8fdaed1f66e242951ee4f6f1c15be80346015` → `Carrier`: .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-414-CORE_META_MODEL-CORE--classify-carrier-as-a-primary-entity.md:28 — the Term Carrier **must** be **NARROWER_THAN** Primary Entity.
- `D` `CA-D-478@5:a40ad3683ecddd536e5b7eb6c044e8da15806ab44946fa1354c408ce5e966464` → `Atom/Property/Carrier`: .caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-478-CORE_META_MODEL-CORE-DELIVERY--store-every-atom-property-in-one-internal-location.md:33 — **every** applicable Atom Property **must** have **`=1`** canonical internal location assigned by its Delivery authority:

CA-D-414 is deliberately visible as a Delivery-source skeleton input example: that does not promote Delivery generally or create a new fact. CA-D-478 illustrates the distinct Carrier/format/storage/placement channel.

## Full baseline accounting

The RMED view has 805 GOVERNS and 2,844 DEPENDS_ON pointers. Excluded Operations contributes 102 GOVERNS and 782 DEPENDS_ON pointers; excluded Concern contributes 1 GOVERNS and 0 DEPENDS_ON pointers. Together these are the pinned baseline's 4,534 occurrences.

## Open semantic work

- Establishing actual applicability of any per-Entity M/E/D pointer requires later Main Content semantic review.
- Identifying further Delivery definitions that inform the skeleton requires the same review.
- Internal, External, and Relational remain orthogonal and unclassified here.
