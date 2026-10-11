# CA-P-2061 — grammar-aware Subject Tool contract review

Recorded 2026-10-11 04:12:12 +0400. Derived review only; no authority, code, source migration or native admission is created by this report.

## Current boundary

The five Core grammar definitions were actually adopted by CA-P-2059, commit `5fa5fbfd8`. Grammar effect receipt SHA-256: `29c9122a27c470127e33acea75a8e56433c78f924fa1126b0349bd27fe542155`. All twelve previously accepted Engine Tool source pins remain current. The four independent read-only audits covered authority/API contracts (subject_review_006), graph parser/provider (subject_review_001), lookup (subject_review_004), and preview/validation (subject_review_008).

Current lookup recognizes only lexical `/` and `:` boundaries. The graph parser treats `/` as IS_BORNE_BY and dot as literal. Subject-only preview validates flat scalar shape and complete-carrier structure but not expression grammar. The finite proposed-carrier `_CODES` does not include subjects.resolution/migration; those exact-target checks do not parse operators either. These are concrete implementation gaps, not completed grammar support.

## Minimal decision

- Use two named profiles: `legacy` and `approved`. Omission preserves existing legacy behavior; approved interpretation is explicitly selected. Never detect a profile from string spelling or silently change old sources.
- Legacy preserves existing `/` bearer qualification, `:` allowed-value qualification and literal dots. Approved uses `/` broader-to-narrower syntax with no native Entity/Subject edge, `.` dependent IS_BORNE_BY bearer, and `:` allowed value IS_ALLOWED_VALUE_OF property. `@` is outside Subject syntax and is rejected under both profiles; it remains display/carrier-only. Legacy compatibility does not admit an invalid `@` Subject token.
- Ordinary lookup/patch operations use one selected profile. They do not implement a source-to-target grammar transition. Cross-profile conversion, mapping and actual migration remain separately approved ad-hoc work. This follows the Operator's latest instruction that reusable Tools operate correct files only.
- Search adds a profile option and echoes the selected profile and reviewed grammar evidence. Approved prefix boundaries add dot; exact matching remains literal. This is lexical matching, not proof that returned sources were authored in that semantic profile. Profiles do not infer source eligibility, ontology relationships or target admission.
- Subject-only preview uses a closed root envelope with `atoms` and optional `subject_profile` only; per-item selector/expected/subject_patches remain closed. Omission selects legacy, while unknown keys and malformed/unknown supplied profiles reject rather than being ignored. Validate all selected source and resulting scalar Subjects under that same profile around the existing complete-carrier boundary. Seal the selected profile/evidence in the preview hash. Do not add profile metadata to authoritative Subjects or add an apply path.
- Add one small shared immutable syntax/profile module. It verifies syntax and operator direction, not arbitrary canonical-target or endpoint admission. Keep finite complete-carrier validation required. Missing semantic endpoint proof cannot be described as a pass.
- Keep graph profile selection internal and keyword-only. A new public generator CLI/MCP selector is unnecessary here and would require a separately revised generator authority set. CA-M-259 already requires a pinned provider profile. Default legacy calls retain old behavior; approved slash produces neither IS_BORNE_BY nor NARROWER_THAN.
- Historical legacy interpretation cites the exact archived five definitions, not their new active replacements. Approved interpretation cites the five current definitions. Immutable code/profile evidence is not a claim of live native admission; a current Core provider must check its actual approved authority pins before using that profile. Do not hardcode the target Project's Core root into generic Atom search.
- No selector/conjunction or escape grammar is added. Reserved characters remain operators; backslash or quoting must not invent a way to hide them inside a Term. Existing YAML quoting remains carrier encoding, not Subject escaping.

## Required source alignment

Revise only these ten existing Engine Tool R/M/E/D/O contracts before implementation: Search CA-R-863, CA-M-370, CA-E-301, CA-D-424, CA-O-046; Update CA-R-866, CA-M-371, CA-E-304, CA-D-425, CA-O-030. Preserve their Summaries, IDs, Subject fields, scopes, owner TOOLS and wrapper locations; increments are exactly +1. Their current clauses fix old delimiters or omit explicit profile inputs/output evidence. CA-D-038 and CA-D-041 only bind locations and need no revision. Tool authoring is separate from CA-P-1965's code-only children, within the already approved Engine Tool-RMEDO scope; no additional ordinary Core body changes belong here.

The ten-source alignment must have bounded authoring leaves, independent acceptance and a fresh derived contract. Do not overwrite the frozen twelve-source packet or its acceptance receipt.

## Disjoint implementation lanes

| Lane | Exclusive scope | Dependency | Acceptance |
| --- | --- | --- | --- |
| Shared profile | New 201_TOOLS/subject_notation.py and its dedicated tests | Accepted aligned Tool contracts | Legacy/proposed syntax, immutable pin evidence, empty/malformed/@/escape cases |
| Lookup | atom_subject_lookup.py and lookup tests | Shared profile contract | Explicit selection, exact/delimiter prefixes, truthful source diagnostics and evidence |
| Preview | atom_subject_patch.py and dedicated preview tests | Shared profile contract | Same-profile before/after syntax, full validator retained, sealed evidence and all pin/byte/no-write guards |
| Graph | generate_entity_graph.py, subject_model_sources.py and graph/profile tests | Shared profile contract | Approved mixed operators, no native slash edge, namespace/prefix preservation, current authority checks |
| Integration | atom_operations.py describe/request wiring and independent acceptance tests; Root owns shared file | Implemented modules | Public search/profile and root-envelope preview dispatch, generic/apply guards unchanged |

Frozen Step1 outputs, subject_notation_snapshot.py, mechanical_subject_graph.py and subject_tree.py stay legacy and are not rewritten. Native admission consumers are not silently switched. Changing a producer code fingerprint may change newly generated metadata hashes; it does not change captured Step1 artifacts.

## Acceptance and remaining boundaries

Test legacy dot literals and byte/result compatibility; approved mixed `/ . :`, leading/trailing/doubled separators, `@` rejection and unadmitted escaping; exact/prefix lookup boundaries; profile echo and digest sealing; malformed source/result diagnostics; stale IDs/versions/hashes/old values; duplicate targets/dependencies; no-follow paths and CRLF/Unicode/unknown fields/body preservation; no-op metadata; and unchanged standalone apply rejection. Independent expected values must not be generated by the producer. Recheck frozen mechanical suites. CA-P-1975 must accept the final changed implementation; old CA-P-1963 does not prove it.

A separate concrete endpoint registry is not supplied by these grammar changes. Syntax/direction support is not native target admission. There is no public validator profile API in this work. Full original Subjects migration, accepted graph, exact live preview approval, history effects, runtime activation and later content updates remain open.

## Current authority pins

- `CA-D-038@11` — `300175a169b9cb70689477e4bff3eb09b370c98bd8d12dc21fc2d45b6ca19be6`; `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_SEARCH/07_delivery/CA-D-038-ATOM_SEARCH-DELIVERY--bind-atom-search-delivery-place.md`.
- `CA-D-041@11` — `b0b0731d7d2ee5f05a179ee29c9e9d4a3d6f50268508ea57e59a74809b36bd52`; `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_UPDATE/07_delivery/CA-D-041-ATOM_UPDATE-DELIVERY--bind-atom-update-delivery-place.md`.
- `CA-D-424@8` — `0c75b89f884a9da6de735f79642bcce9b6025f6dc5b436012cdde9aab698662d`; `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_SEARCH/07_delivery/CA-D-424-ATOM_SEARCH-DELIVERY--deliver-atom-search-tool.md`.
- `CA-D-425@8` — `7652c6b65166f8d6a1c616cbda1ee753a2372e7e373189f552f3917039b0f87f`; `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_UPDATE/07_delivery/CA-D-425-ATOM_UPDATE-DELIVERY--deliver-atom-update-tool.md`.
- `CA-E-301@13` — `ca1538da46464a45076dd755a6647240976cf52d40ea61d99c4e003786f45e46`; `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_SEARCH/06_evaluation/CA-E-301-ATOM_SEARCH-QA_CASE--verify-search-caprmedio-atom-carriers.md`.
- `CA-E-304@12` — `595c4ea753df4f4cee070ae53e73b1fc3d9c7df66aa385f6ca8f1f6e2f705df9`; `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_UPDATE/06_evaluation/CA-E-304-TOOLS-STANDARD-QA_CASE--verify-update-sealed-caprmedio-atom-carriers.md`.
- `CA-M-370@1` — `91ba4ccd580bf24434700ca9150930b182b61dad287d2ec15ef439eae178f238`; `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_SEARCH/05_method/CA-M-370-ATOM_SEARCH-METHOD--match-direct-subject-fields.md`.
- `CA-M-371@1` — `7a97d7278c4e2002b8d48720957106b21312a157c8c129a4c283d3bd86b3e321`; `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_UPDATE/05_method/CA-M-371-ATOM_UPDATE-METHOD--preview-exact-subject-patches.md`.
- `CA-O-030@6` — `19097af83287005dae4d55e4b4da2234acce9e9f92b0f70671afb831bd8b256b`; `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_UPDATE/09_operations/CA-O-030-TOOLS-ACTION--update-sealed-caprmedio-atom-carriers.md`.
- `CA-O-046@4` — `6e8194cc18c0377344b785d8bf89897c8c785aa83cd1eb51e32cf1d479a6bfe5`; `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_SEARCH/09_operations/CA-O-046-ATOM_SEARCH-ACTION--search-caprmedio-atom-carriers.md`.
- `CA-R-863@14` — `0b984b73158b066dbe1434ffa2050f42b78d6e620cfd4ad2a5b39cebbc4dbdf0`; `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_SEARCH/04_requirement/CA-R-863-ATOM_SEARCH-CORE-REQUIREMENT--search-caprmedio-markdown-atoms.md`.
- `CA-R-866@13` — `baeca5734a850332d7c77529cb1a7e10639bd9f4dbbc733849fa5ae8d0a9747d`; `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_UPDATE/04_requirement/CA-R-866-TOOLS-STANDARD-REQUIREMENT--update-caprmedio-markdown-atoms.md`.

## Current implementation pins

- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/atom_subject_lookup.py` — `eed6074a7a93b5fdbe8987160fe73968882635ea62357bf5edcaa9f8d66cbaa6`.
- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/atom_subject_patch.py` — `783d838fdb035921ae7219e8a7a8dcd31e27efc34b988e64b6d0989d7091cc04`.
- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/atom_operations.py` — `cb5cdaa90188d6bcb96ed590cd8a0369f515f2d2715e2411a4f851d07ac12647`.
- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_ENTITY_GRAPH/generate_entity_graph.py` — `55428c5d202910aaa3a0a2c4f1f3c1a6dd8e5f50673b7bc34e957beb9efb048a`.
- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_ENTITY_GRAPH/subject_model_sources.py` — `138a4a6b065c70cf21d3d27e7633865113ebc59bdaecc0acc8016c5e6ec00916`.
- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS/validate_atoms_workers/proposed_carrier.py` — `fe16bee6291ec871a975ed53b63694539f73cec3bc776cdb2bb6afbb4fd4f834`.
- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS/validate_atoms_workers/check_graph_extended.py` — `644c341b9d45fb9aac08516a1790f51cea33c1bfdc5e3f2dca5325cca29bf92b`.

No source or implementation file was edited by this review. The independent audits are read-only evidence; their suggestions do not themselves authorize extra grammar, native relations or migration.
