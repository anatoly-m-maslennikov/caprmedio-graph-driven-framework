---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    occurrent:
      - subject-authority-establishment
version: 4
updated_at: 2026-08-23 16:26:00
autonomous_confidence_threshold: 98
---
# Establish two-axis Subject authority

THE Assignee MUST establish the two-axis Subject authority for every Atom in Task Scope.

## Scope

`(Atom ID IN (CA-R-1012, CA-R-1013, CA-R-1014, CA-R-1015, CA-R-1084, CA-R-1085, CA-R-1086, CA-R-1087, CA-R-1088, CA-R-1089, CA-R-1090, CA-R-1091, CA-R-1092, CA-M-125, CA-M-126, CA-E-246))`

## Definition of Done

THE Task is NOT DONE IF (the Task Scope Resolution does not record the exact Task Scope and Project revision OR ANY Atom in Task Scope is absent OR ANY Subject lacks exactly one Claim Role and one Claim Participant Temporal Form OR the Claim Role values are not exactly DECLARED and PREREQUISITE OR the Claim Participant Temporal Form values are not exactly CONTINUANT and OCCURRENT OR an active or draft Atom may have zero DECLARED Subjects OR an Atom may have more than one DECLARED CONTINUANT Subject OR an Atom may have more than one DECLARED OCCURRENT Subject OR independently replaceable DECLARED Subjects of the same Temporal Form are not split across Atoms OR the governed Subject frontmatter encoding and validation case are incomplete).

## Details

The established authority permits one DECLARED CONTINUANT Subject and one DECLARED OCCURRENT Subject in the same Atom. It permits any number of PREREQUISITE Subjects in either Temporal Form. A Task dependency may therefore be a PREREQUISITE CONTINUANT Subject.

## Task Scope Resolution

- Resolved at: `2026-08-23 16:26:00 +0400`.
- Project revision: Git revision `33dced3e164dfe2625c724e03b5624cbd8c30d1c` plus the governed working-tree carrier revisions bound by this manifest.
- Manifest row: `<ATOM_ID><TAB><CARRIER_SHA256><TAB><PROJECT_RELATIVE_PATH>`.
- Manifest order: ascending by Atom ID and then project-relative path.
- Manifest digest: `ad896a3f4f7efa8a68f4b19b4d1cf32c6a9efbd79da719910e69476032cf3505`.
- Resolved Atom count: `16`.

```text
CA-E-246	68707c6ba3c8fd044f36f7d105ed759ca36d34766f36486d7c2caf3c75fe3515	.caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY/-103_BSEED_LAYER_3_GOVERNANCE/06_evaluation/CA-E-246-GOVERN-QA_CASE--validate-atom-subjects.md
CA-M-125	dc8095469ac7dd685ea5dfc3367fde4fec1f32a33b2277c142e787700a8663e5	.caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY/-102_BSEED_LAYER_2_SEMANTICS/05_method/CA-M-125-SEMNTC-CORE-METHOD--assign-subjects-from-the-claim.md
CA-M-126	d582862b6a2baf73801309c9b508d2f46e0e0f649da9f3eba9597363e87a8d23	.caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY/-102_BSEED_LAYER_2_SEMANTICS/05_method/CA-M-126-SEMNTC-CORE-METHOD--derive-the-subject-projection.md
CA-R-1012	71a2c1718a6cc608f929fc20ab5c3e6c7fa4b9c84a3458947f3c434bed9b1be5	.caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY/-101_BSEED_LAYER_1_METAMODEL/04_requirement/CA-R-1012-MMODEL-CORE-REQUIREMENT--define-subject.md
CA-R-1013	79f870a2ccb7e1fe9138abc1f1a1437e62987e5360cb6b6639a0e877a5fc1111	.caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY/-101_BSEED_LAYER_1_METAMODEL/04_requirement/CA-R-1013-MMODEL-CORE-REQUIREMENT--require-subjects-on-active-and-draft-atoms.md
CA-R-1014	58da72e746d26de7d245e6c5a48422e63561e9b9feb62b19aef2939acb912d59	.caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY/-101_BSEED_LAYER_1_METAMODEL/04_requirement/CA-R-1014-MMODEL-CORE-REQUIREMENT--separate-subjects-from-scope-coordinates.md
CA-R-1015	23454e9b0cdcfcdc788ecf874d34456688b5c045337b62eeb5613b523264ac5d	.caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY/-103_BSEED_LAYER_3_GOVERNANCE/04_requirement/CA-R-1015-GOVERN-CORE-REQUIREMENT--encode-subjects-in-frontmatter.md
CA-R-1084	233e90c22d612e7886533c8e1bbca400fc97720ac20c34aa5d70c4be1d70ef38	.caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY/-101_BSEED_LAYER_1_METAMODEL/04_requirement/CA-R-1084-MMODEL-CORE-REQUIREMENT--define-claim-role.md
CA-R-1085	ddaf514cba5c9d87c43a146a8de7262f37f8f5812e3ffac5588c0d7aa99a427c	.caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY/-101_BSEED_LAYER_1_METAMODEL/04_requirement/CA-R-1085-MMODEL-CORE-REQUIREMENT--define-declared-claim-role.md
CA-R-1086	4ac2e0c2fee721ab4057e5316411f83a983fb49dc837bffa55f3af1b62f88001	.caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY/-101_BSEED_LAYER_1_METAMODEL/04_requirement/CA-R-1086-MMODEL-CORE-REQUIREMENT--define-prerequisite-claim-role.md
CA-R-1087	a1eaa5ce739b7a1fb0f34cd7fcaab309899007fccaeb1c7b0e75bf9814abd201	.caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY/-101_BSEED_LAYER_1_METAMODEL/04_requirement/CA-R-1087-MMODEL-CORE-REQUIREMENT--define-claim-participant-temporal-form.md
CA-R-1088	973210dd3c7a239a0330dbf3fe72fb6e245a53e615981fb1c2a4614a7e04f62a	.caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY/-101_BSEED_LAYER_1_METAMODEL/04_requirement/CA-R-1088-MMODEL-CORE-REQUIREMENT--define-continuant-temporal-form.md
CA-R-1089	2319ea16975489a134abd25846403b7f5f794ec8978b848c97d003b84f8e930f	.caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY/-101_BSEED_LAYER_1_METAMODEL/04_requirement/CA-R-1089-MMODEL-CORE-REQUIREMENT--define-occurrent-temporal-form.md
CA-R-1090	73bb13ee0cdfdba54f7078b60c386e215c35cbe7bf02d45ba299c43b89397104	.caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY/-101_BSEED_LAYER_1_METAMODEL/04_requirement/CA-R-1090-MMODEL-CORE-REQUIREMENT--classify-every-subject-by-both-axes.md
CA-R-1091	b6a87d580daf8592989cb7bc23aa3d8e45b45588d40b2aa88e05ea4d6c92c74f	.caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY/-101_BSEED_LAYER_1_METAMODEL/04_requirement/CA-R-1091-MMODEL-CORE-REQUIREMENT--limit-declared-subjects-by-temporal-form.md
CA-R-1092	7d806742672ca1b358cda5d8f62a2eaccc77e14a8b31cfe8b0d1ec5d641b4afa	.caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY/-101_BSEED_LAYER_1_METAMODEL/04_requirement/CA-R-1092-MMODEL-CORE-REQUIREMENT--split-at-same-form-declared-subject-boundaries.md
```

## Execution Result

PASS. All 16 resolved Atoms already establish the required Subject definitions, Claim Roles, Claim Participant Temporal Forms, declared-Subject cardinality, same-form split rule, frontmatter encoding, assignment Method, projection Method, and Evaluation case. This execution required no changes to the resolved authority Atoms.
