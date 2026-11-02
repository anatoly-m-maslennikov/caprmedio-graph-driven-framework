---
atom_id: "CA-D-613"
content_role: "Delivery"
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release Workflow bindings"
  depends_on: [Workflow, Step, Action, Tool]
version: 5
updated_at: "2026-10-10 18:14:20 +0400"
relations:
  delivery_for: [CA-R-1922]
---
# Summary

Serialize public-release Workflow bindings

## Scope

the definition identities of one public-release execution.

## Claim

the canonical selected-workflow manifest **must** admit `public.release` only through one closed `public_release_source_admissions` record. Its exact fields are `route`, `workflow`, `ordered_steps`, `ordered_actions`, `rmed_frontier`, `mutation_capable`, and `native_action_calls`; `route` is exactly `public.release`, `mutation_capable` is exactly `true`, and `native_action_calls` is exactly `[]`. The record binds CA-O-188 and the ordered CA-O-189/CA-O-190 through CA-O-197/CA-O-198 Step/Action occurrences before native dispatch.

## Details

`public_release_source_admissions` is a JSON-compatible array of exactly one
closed object. Its fields are exactly the seven Claim fields, with no unknown
field. Every table row below is one canonical Pin with exactly `atom_id`,
positive integer `version`, safe Project-relative `source_path`, and lowercase
64-hexadecimal `sha256`; parsers must reject any non-row, reordered, duplicate,
missing, or digest-mismatched member. `rmed_frontier` is itself a closed object
whose keys are exactly `requirements`, `methods`, `evaluations`, and
`deliveries`, each an ordered array of the matching table rows. The
No Task, Task Done status, separate acceptance, or worker-review condition is
an execution prerequisite. The pinned RMED and Operation rows are current-source
evidence only; one Operator command authorizes the covered workflow and Actions.

#### `workflow`

| atom_id | version | source_path | sha256 |
| --- | ---: | --- | --- |
| CA-O-188 | 2 | `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-188-PROJECT_CONFIGURATION-WORKFLOW--release-a-selected-public-version.md` | `d6121d7cc83bcb13f36416f512e37cd7dfb835755818d33939cbb29f94f3ceba` |

#### `ordered_steps` and `ordered_actions`

The arrays have exactly the following paired positions. A parser constructs
`ordered_steps` from the Step columns and `ordered_actions` from the Action
columns; each position must have both current Pins.

| position | step_atom_id | step_version | step_source_path | step_sha256 | action_atom_id | action_version | action_source_path | action_sha256 |
| ---: | --- | ---: | --- | --- | ---: | --- | --- |
| 1 | CA-O-189 | 1 | `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-189-PROJECT_CONFIGURATION-STEP--discover-a-matching-public-main-pr.md` | `04c8c6ec95bdbb4cc74ce8bf53dd3488f50f302795ececb743d70bcf136ba9f8` | CA-O-190 | 1 | `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-190-PROJECT_CONFIGURATION-ACTION--discover-a-matching-public-main-pr.md` | `b218c432c0c7ffe6b191773b77baa09e03ca46f218e2b406ea775d8358ad069e` |
| 2 | CA-O-191 | 1 | `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-191-PROJECT_CONFIGURATION-STEP--prepare-bound-public-release-materials.md` | `023dcb13f1eed05d10f7ce80de761681dbd51483aa52e144006062ada83f81b8` | CA-O-192 | 1 | `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-192-PROJECT_CONFIGURATION-ACTION--prepare-bound-public-release-materials.md` | `c5b4c0a14b34c29a4b714516e0ebaf9587d450f5cc6c3e0d7dd915f8147feb23` |
| 3 | CA-O-193 | 1 | `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-193-PROJECT_CONFIGURATION-STEP--freeze-and-prove-the-public-source-closure.md` | `dcc02fc411bd989a4dad9b1b5c7530ebffe288c5809b09a3b82a883cd8a55bc4` | CA-O-194 | 1 | `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-194-PROJECT_CONFIGURATION-ACTION--freeze-and-prove-the-public-source-closure.md` | `6c36e9a5e8fe880efe1f4e6bf1a97f9e19a1b2b156acc50b2db909536a8c0f80` |
| 4 | CA-O-195 | 1 | `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-195-PROJECT_CONFIGURATION-STEP--push-the-gated-public-closure-and-upsert-main-pr.md` | `fd5bf777d82dad1f3be07ae67c765b2f250082834d8eca3e7ac749935c690312` | CA-O-196 | 1 | `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-196-PROJECT_CONFIGURATION-ACTION--push-the-gated-public-closure-and-upsert-main-pr.md` | `09ce6a856fe4c220babc6e8861808258e496847d6cecd946b004a309479c63a4` |
| 5 | CA-O-197 | 1 | `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-197-PROJECT_CONFIGURATION-STEP--finalize-the-actual-public-history-link.md` | `ac033acf2be2e14c57a8550f3c451100c468a18ef9bdde5518edb0bb8e3015f6` | CA-O-198 | 1 | `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-198-PROJECT_CONFIGURATION-ACTION--finalize-the-actual-public-history-link.md` | `664bab53813481d3785e0129969f95208f509273f6e75cbfa85d6b22e6cd763c` |

#### `rmed_frontier`

| collection | position | atom_id | version | source_path | sha256 |
| --- | ---: | --- | ---: | --- | --- |
| requirements | 1 | CA-R-1920 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1920-TOOLS-REQUIREMENT--require-explicit-operator-invocation-for-public-release.md` | `03b2e63a511e9619f91371b4a9e3c82b89b375281ed62712c62d18c824e7c213` |
| requirements | 2 | CA-R-1921 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1921-TOOLS-REQUIREMENT--bound-public-release-to-one-personal-remote.md` | `90e60e551bf27bb1a14d3ce8ec643179ee3103c74ae4a1b9398df021d3499009` |
| requirements | 3 | CA-R-1922 | 2 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1922-TOOLS-REQUIREMENT--bind-public-materials-to-the-selected-source-snapshot.md` | `9109b7d0eeec39aa7dd3f4c1a381e992b3d887ae31844233f80d5a67fea9e1fd` |
| requirements | 4 | CA-R-1923 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1923-TOOLS-REQUIREMENT--require-an-actual-pr-link-in-version-history.md` | `92b7357aa2f7eddba738a6e4c986494c0372162a01bbb7bc8b63ef3886249fb6` |
| requirements | 5 | CA-R-1924 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1924-TOOLS-REQUIREMENT--require-current-typed-full-gate-before-public-push.md` | `92670cb2a7fc7a0b06853e4a6b097ac02c1255d1a4ee1edf6314b40edb181426` |
| requirements | 6 | CA-R-1925 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1925-TOOLS-REQUIREMENT--require-immutable-proof-for-public-push.md` | `e162be60bd128d368a16d7329f3c5a041da5181aadf36efe25478210e716e2b8` |
| requirements | 7 | CA-R-1926 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1926-TOOLS-REQUIREMENT--maintain-one-matching-open-main-pr.md` | `86ec92c37bcdd2cd2edc665fef18ebabb83d0660df100442da5cb9f00ec83f98` |
| requirements | 8 | CA-R-1927 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1927-TOOLS-REQUIREMENT--exclude-merge-from-public-release-workflow.md` | `cb954a11bc588176dff667dcb3582fea02284fe49996a23479887d0234412b83` |
| requirements | 9 | CA-R-1928 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1928-TOOLS-REQUIREMENT--record-public-release-lineage-with-schema-v5-runs.md` | `c7ce8fbc83a4b3c38ec595a9ccb4d592fe4975c07ce4e052d1a071c36acdb9b0` |
| requirements | 10 | CA-R-1929 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1929-TOOLS-REQUIREMENT--bound-public-release-recovery-without-remote-replay.md` | `f0f53ad7d50602da323f61823a33dbdd0451814c965915c0e42dbc83112f10f6` |
| methods | 1 | CA-M-365 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-365-TOOLS-METHOD--admit-a-bound-public-release-request.md` | `8975d119ba5f2e24616ef1279476780e6d96a5e3aafa1b4fce93c1a02bcb1aac` |
| methods | 2 | CA-M-366 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-366-TOOLS-METHOD--prepare-public-materials-with-an-actual-pr-link.md` | `6ec86e2a18367f8cb74d2fc15562a6a4223789cd72a402839042d8037784f865` |
| methods | 3 | CA-M-367 | 4 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-367-TOOLS-METHOD--reopen-the-current-full-gate-for-each-public-source-closure.md` | `e45500bb6a73f4973b3aca49da4ca814eb539fcc896cdb85cf88c15bdd7dc607` |
| methods | 4 | CA-M-368 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-368-TOOLS-METHOD--bind-public-remote-effects-to-one-pr-identity.md` | `e5c9897216d0692b6c7b4114f8fc291812db6c24a8a956c94a1742dd68ac74d6` |
| methods | 5 | CA-M-369 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-369-TOOLS-METHOD--recover-public-release-by-discovering-uncertain-effects.md` | `9f02b2933fd4007794863c179bfcca3b5bcb8ce59711b27027440410d0b0c936` |
| evaluations | 1 | CA-E-610 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-610-TOOLS-QA_CASE--validate-public-release-request-admission.md` | `b9e33e2dcbbe373904f52154f7eacafc64187e8100d8313e1ce61999bfbc2e34` |
| evaluations | 2 | CA-E-611 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-611-TOOLS-QA_CASE--validate-personal-remote-and-branch-boundary.md` | `7f89a4e67a517d312e6c7e935e002e6e05aee59f774e9d57cd759ea827203b54` |
| evaluations | 3 | CA-E-612 | 2 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-612-TOOLS-QA_CASE--validate-public-material-source-binding.md` | `3099a1f09a20b044e31342a605972cb7c17ba6d5a48abc2338540de0cb6af73a` |
| evaluations | 4 | CA-E-613 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-613-TOOLS-QA_CASE--validate-actual-version-history-pr-link.md` | `c0d6b18676dc4212401c2e7d2339226a169f725a8b9bcea3525508beee8d678d` |
| evaluations | 5 | CA-E-614 | 2 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-614-TOOLS-QA_CASE--validate-current-typed-public-full-gate.md` | `7890ae2fd59876148fe0cef5067fd43821d399c383857d32f5ae1edfc31fc241` |
| evaluations | 6 | CA-E-615 | 2 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-615-TOOLS-QA_CASE--exercise-successful-public-release-with-mocked-remote-effects.md` | `c6ecfc9be8cf73e85b4beb00c8377e8a61bf7239edd0e29fee177b537168f212` |
| evaluations | 7 | CA-E-616 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-616-TOOLS-QA_CASE--validate-unique-matching-main-pr.md` | `6611e02ea86d039fdf1878cbededa10c5ffdb858c8714dcf3f177f24a40c8abd` |
| evaluations | 8 | CA-E-617 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-617-TOOLS-QA_CASE--validate-public-release-does-not-merge.md` | `dea7122b0d47107eb78f79f458923b655a09aee93ff850fe1d655b9a979aa5b4` |
| evaluations | 9 | CA-E-618 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-618-TOOLS-QA_CASE--validate-public-release-schema-v5-run-and-tool-call-lineage.md` | `9267d550a2d15433aca855d27b90a137a8bb49da0fe9803d528018a153f88fd6` |
| evaluations | 10 | CA-E-619 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-619-TOOLS-QA_CASE--validate-public-release-interruption-and-recovery-boundary.md` | `3f66ed982c53c9745ee180a1ac2d0cbaae5778a48888243d9ab606a36ce5f3ca` |
| deliveries | 1 | CA-D-610 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-610-TOOLS-DELIVERY--place-the-public-release-native-tool-source.md` | `01a9270f571f1c07c93e487bc57b01b7288cb53eed8c8168f4e9d069beee5a5f` |
| deliveries | 2 | CA-D-611 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-611-TOOLS-DELIVERY--bind-public-release-to-its-own-package-root.md` | `121d857c6fe9926415bc19195cf5adb4c8ee3bc711ea9c282468e1d7544b4367` |
| deliveries | 3 | CA-D-612 | 2 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-612-TOOLS-DELIVERY--serialize-public-release-native-entrypoint-discovery.md` | `ad5c745a82f1b376fa847d963a0858db5fc791cfd5753afa04a4478545a942f3` |
| deliveries | 4 | CA-D-614 | 3 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-614-TOOLS-DELIVERY--serialize-public-material-source-proof.md` | `793c9b6183491f89d16e6c33e8cd8c0377097692a83aa3c24a564785f850921b` |
| deliveries | 5 | CA-D-615 | 3 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-615-TOOLS-DELIVERY--retain-public-full-gate-receipt-references.md` | `3eb17f5f881387146e881451a66d2e8050e4c1244dbe46d7967abea3a86129fe` |
| deliveries | 6 | CA-D-616 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-616-TOOLS-DELIVERY--serialize-public-remote-effect-proofs-without-secrets.md` | `7fdd8122d3e74c32986eb49479eb1e133b5174513c0107a7fd6ce09f0446276a` |
| deliveries | 7 | CA-D-617 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-617-TOOLS-DELIVERY--serialize-one-actual-public-pr-identity.md` | `38b7a113537926fff46ef7830e27a12a1508891e0c3619cf0855f27505058027` |
| deliveries | 8 | CA-D-618 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-618-TOOLS-DELIVERY--serialize-parented-public-tool-call-evidence.md` | `b11fab960f9da8b26817fea252cfd5f19e15fd7b52e3be9eb80b45f8858fd5eb` |
| deliveries | 9 | CA-D-619 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-619-TOOLS-DELIVERY--retain-public-release-recovery-references.md` | `ceff499eb32786dfafb52530f714d056939e228b5abc880bc2ba9dff4e0c1855` |

CA-D-613 itself is deliberately absent from `rmed_frontier`: a record must not
pin its own carrier. The ordered O188–O198 Pins and the RMED Pins are source
evidence only; they contain no canonical-
manifest digest, caller authorization, Run result, output digest, or cross-hash
cycle.

The record is an additive seventeenth selected-route admission. It does not
alter the existing D572 `release_source_admissions` record or its
`release_version` route. The selected request retains CA-D-527's existing
two-field `definition_manifest`; it never carries this admission record or a
second manifest binding. The sequence remains source-controlled Operations
authority; executable code neither replaces nor derives definition revisions.
