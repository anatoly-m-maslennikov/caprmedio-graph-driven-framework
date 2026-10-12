# Subject file operations — grammar-aware compiled contract

Derived from the current twelve-source `tool-grammar.packet.json` and independent `tool-grammar.acceptance.md`. Recorded 2026-10-11 04:42:11 +0400. Source Atoms remain authority; this is a compilation, not another authority.

## Latest Operator decision

"We don't need @ - it's just D atoms."

Compact Entity notation has only `/`, `.` and `:`. There is no fourth carrier/display operator. D atoms define carrier and storage rules. The existing negative rejection of `@` in a Subject does not give it a notation role. Do not remove `@<version>` from historical filenames: that is a separate D-governed carrier convention, not an Entity operator. Frozen candidates, receipts and archived versions remain historical evidence.

## Same-profile ordinary operations

- Profiles are `legacy` and `approved`. Omission means legacy; approved is explicit. Unknown or malformed supplied profiles fail.
- Legacy uses `/` for bearer qualification, `:` for allowed values, and literal dots. Approved uses `/` broader-to-narrower, `.` bearer-to-dependent and `:` Property-to-allowed-value.
- Both reject `@` in Subject syntax. Do not introduce escaping, selectors, conjunctions or inferred profile detection.
- Search has an optional `subject_profile` input (`--subject-profile` at the CLI). Prefix matching uses the selected profile's boundaries; exact stays literal. Results are lexical matches, not semantic-conformance attestations.
- Subject-only preview has the closed root envelope `{atoms, subject_profile?}`. Each item remains `{selector, expected, subject_patches}`; other root/item keys fail. Select one profile for source and result syntax checks. Full-carrier validation, pins, no-follow protection, byte preservation and no-op/apply guards remain required.
- Both results add `subject_profile` (the selected name) and `subject_profile_evidence` with exactly `grammar_pins` and `native_admission: "not_performed"`. Each grammar pin contains `atom_id`, `version`, `path` and `sha256`. Preview seals these fields in its digest. They are reviewed grammar evidence, not a native endpoint registry or an attestation about source semantic conformance.
- Legacy evidence cites the five exact historical definitions adopted before CA-P-2059; approved evidence cites the five current definitions. Generic Atom operations do not hardcode a target Project's Core root.
- The shared syntax module proves syntax/direction only. Approved graph slash produces neither a native IS_BORNE_BY nor NARROWER_THAN edge. Dot gives Dependent IS_BORNE_BY Bearer; colon gives AllowedValue IS_ALLOWED_VALUE_OF Property.
- Graph selection is internal, keyword-only, legacy by default. Existing public generator entry points are unchanged. A current approved Core provider checks current source pins; do not silently switch native admission consumers or frozen Step 1 consumers.
- Repairs, cross-profile conversion and live source migration are separate approved ad-hoc work. No reusable migration framework, unguarded writer or new apply path.

## Ownership and gates

CA-P-2063 owns R863/R866/M370/M371; CA-P-2064 owns E301/E304/D424/D425; CA-P-2065 owns O046/O030. Each author owns only those current Engine Tool sources and exact old-version archives. Preserve identity, Summary, Scope, Subjects and unrelated metadata; change Claim/Details, Version +1 and the actual configured Updated At only. CA-D-038/041 remain unchanged.

Root owns Plans, Journal and Git. Independent CA-P-2066 checks all ten effects and shared contract agreement, then creates fresh grammar-aware packet, acceptance and compiled contract. The frozen twelve-source packet and acceptance remain unchanged. Code implementation starts only after that gate.

## Accepted source pins

- `CA-D-038@11` — `300175a169b9cb70689477e4bff3eb09b370c98bd8d12dc21fc2d45b6ca19be6`; `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_SEARCH/07_delivery/CA-D-038-ATOM_SEARCH-DELIVERY--bind-atom-search-delivery-place.md`.
- `CA-D-041@11` — `b0b0731d7d2ee5f05a179ee29c9e9d4a3d6f50268508ea57e59a74809b36bd52`; `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_UPDATE/07_delivery/CA-D-041-ATOM_UPDATE-DELIVERY--bind-atom-update-delivery-place.md`.
- `CA-D-424@9` — `c370269e36f7c057ac2eec0fa920e76f797c574cde6bc29734fb2cfce1294686`; `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_SEARCH/07_delivery/CA-D-424-ATOM_SEARCH-DELIVERY--deliver-atom-search-tool.md`.
- `CA-D-425@9` — `f562f1e827e03ab42941cd0ece3d24894f73c7b32ebe29fd689f9a8e4bfe445d`; `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_UPDATE/07_delivery/CA-D-425-ATOM_UPDATE-DELIVERY--deliver-atom-update-tool.md`.
- `CA-E-301@14` — `416be34f445b8515bb6fa5be9a8894f306a0c5ee48b88452b017e254ec3ae97e`; `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_SEARCH/06_evaluation/CA-E-301-ATOM_SEARCH-QA_CASE--verify-search-caprmedio-atom-carriers.md`.
- `CA-E-304@13` — `f696e778937f7f1c312e78533657ee436c56208ea4d85282bc3f1c63f8dd653e`; `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_UPDATE/06_evaluation/CA-E-304-TOOLS-STANDARD-QA_CASE--verify-update-sealed-caprmedio-atom-carriers.md`.
- `CA-M-370@2` — `7588b5e5d774733d8fe9027d24309b62e7c0af72bbd47acadb28eb856af1a6d9`; `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_SEARCH/05_method/CA-M-370-ATOM_SEARCH-METHOD--match-direct-subject-fields.md`.
- `CA-M-371@2` — `3c3a5e4d9781f3901f397b2ef87c10f94ad3431fad56beea1bd633c36530e605`; `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_UPDATE/05_method/CA-M-371-ATOM_UPDATE-METHOD--preview-exact-subject-patches.md`.
- `CA-O-030@7` — `c2d70fa275a075d2fbc978cab246158cfd8413cec88716521336736d0bf060cc`; `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_UPDATE/09_operations/CA-O-030-TOOLS-ACTION--update-sealed-caprmedio-atom-carriers.md`.
- `CA-O-046@5` — `6198c977e456a9c2c8457dd288a2a188231a37fe5420882d3f1378f57e009271`; `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_SEARCH/09_operations/CA-O-046-ATOM_SEARCH-ACTION--search-caprmedio-atom-carriers.md`.
- `CA-R-863@15` — `18ea1e4593ffb9741f83c1e736aba6ef6c955022fbc85b07549757c6c7215c0c`; `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_SEARCH/04_requirement/CA-R-863-ATOM_SEARCH-CORE-REQUIREMENT--search-caprmedio-markdown-atoms.md`.
- `CA-R-866@14` — `6971d51a68934c6c8e2a3889d54542b375445e663e8d2e201f8ec94847231c0d`; `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_UPDATE/04_requirement/CA-R-866-TOOLS-STANDARD-REQUIREMENT--update-caprmedio-markdown-atoms.md`.

Legacy and approved grammar evidence pins are sealed in `tool-grammar.packet.json`. This contract permits ordinary selected-profile syntax/lexical work only; it does not supply arbitrary endpoint admission or approve the later live migration. CA-P-1965 implements it and CA-P-1975 independently verifies the final changed code.
