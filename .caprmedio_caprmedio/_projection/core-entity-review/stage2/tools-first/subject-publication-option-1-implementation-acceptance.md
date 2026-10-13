# Subject publication: Option 1 implementation acceptance

Derived local verification evidence, not authority or installed-runtime acceptance. Date: 2026-10-13.

## Scope and source acceptance

The Operator approved caught-error restoration, an exclusive window with a shared Engine lock, and internal confirmation behind the existing authorization reference. The public request remains unchanged.

Source contract: [independent source acceptance](subject-publication-option-1-source-acceptance.md), committed in `0be79f865`. The five accepted source pins remain unchanged. The implementation and tests below are reviewed against that packet.

The private trusted host records actual Operator confirmation for the exact reviewed change, staged candidate, source and affected files. A serializable request cannot issue this capability. Revalidation and actual admission precede publication; the lock spans final checks, effects, readback and caught restoration. Confirmation is single-use. The ordinary installed path has no confirmation provider and still refuses changed publication.

Cooperating writers covered: Atom Operations apply and raw writes; lifecycle Actions; Project Structure apply/rollback; metadata application; global-tier and required-property backfills; retired-property removal. Existing release lock ownership is reused. Preview behavior remains unchanged. Manual edits, Git, sync and nonparticipating scripts remain outside this cooperative guarantee and must be paused.

## Final verification

All counts below are distinct; repeated reviewer runs are not added.

| Suite | Passed |
| --- | ---: |
| Subject preparation portfolio | 7 |
| Raw revision | 8 |
| Selected Subject publication | 25 |
| Engine lock and writer exclusion | 20 |
| Native selected Atom lifecycle | 30 |
| Atom Operations | 26 |
| Project Structure | 23 |
| Artifact metadata | 8 |
| Global-tier backfill | 12 |
| Required-property backfill | 13 |
| Retired-property removal | 20 |
| Total scoped checks | 192 |

The final selected suite ran against all four frozen production pins after the last authorization correction (199.317 seconds). It uses real admission, assessment, Session and Run recording with isolated current-source fixtures. It covers missing/forged/mutated/stale/reused confirmation, omitted legacy profile, LF/CRLF preservation, source identity and mode changes, caught restoration, uncertain outcomes, and recording failure. Actual subprocess exits after history/current publication retain unfinished evidence and do not replay effects.

Independent process contention checks cover shared exclusion, valid reentry, expired copied context, and representative real metadata/lifecycle writers. Four final error-boundary cases distinguish pre-acquisition refusal from real writes followed by failed lock-exit verification. The latter retains observed evidence and reports partial/unknown effects without automatic retry.

Independent reviewers `connector_binding_review` and `epic_atom_read` checked the bounded production and exclusion/error paths. `epic_publication_blocker` reran all 102 existing writer cases against unchanged final wrapper/test hashes. `epic_sections` ran all 40 Subject cases against the final production pins. Main independently reran the 30 native lifecycle cases (7.696 seconds). Whitespace validation passed.

Runner: offline `uv run --no-project --python 3.14 --with PyYAML==6.0.3 --with pydantic==2.13.5 python`, using unittest discovery or the suite entry point. Regression runner verified Python 3.14.7. Temporary fixtures and bytecode are under `.caprmedio_tmp`; the regression worker used existing `/tmp/codex-uv-cache`, and main used `.caprmedio_tmp/cache/uv`.

## Additional failed check and limits

A broader orchestrator `test_selected_lifecycle*.py` discovery ran 22 tests: 16 passed; 6 composition cases failed during fixture preparation at the unavailable/stale old `CA-O-128-CORE_META_MODEL-ACTION--apply-authorized-atom-lifecycle-changes.md` source pin. No Action execution was reached in those six cases. This is not counted in the 192 passing scoped checks. The old reviewed manifest was not silently rebound.

No full repository suite, installed provider, installed-runtime end-to-end acceptance, manifest activation, release or live Core migration occurred. The installed manifest still contains old workflow pins. Plans remain Active until their broader route/runtime gates are met. No claim of completion of the tools Epic.

Caught errors attempt restoration only within owned effects. Abrupt process termination may leave partial state and requires inspection before separately admitted continuation. Outside writers ignoring the exclusive window are not prevented; crash atomicity and automatic replay are not provided.

## Frozen implementation and changed-test pins

Paths are relative to the repository root.

```text
8e5c6769ace0db1d782ae8c9547d1b02bcd56ccf7722ed6ed6e62bef419af319  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_UPDATE/tests/test_subject_apply_portfolio.py
3a4298470474f6ca3537e0ce2335a1238674be6ed7d5c48b7c75da853b8b9908  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/WORKFLOW_OPERATIONS/PROJECT_STRUCTURE/project_structure.py
2da4325618aaccf0b70a25a012d6ba559d377a7d9e626fd1aba5ff6960f22c48  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/artifact_metadata.py
25f827b3a99fef761add069acf5a59b9221746e8c4e355f49f43002db3d8278a  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/atom_operations.py
aec65a589ec38a05555036970fe7c6a66d6d3d52ee1d175d603b87a6b6d4c4a3  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/atom_subject_apply.py
12351c2d9bc0fa69e01b3fa4d6f65947827ff9901a3e3f03fdc0a08e953315df  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/lifecycle_intents.py
a3da7122477a869f781a5ccb95dd96265b975c122f13d3b9b21509ede6d404e6  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/migrations/backfill_global_tier.py
532617ff4628b26b48f88b9fae6fc05f315af6e32486aaccb79ffa2c4a14efb2  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/migrations/backfill_required_atom_properties.py
3e01eda1c1424437d624701fbf6c918b65fe28889297511fb31bd3e160c14385  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/migrations/remove_retired_atom_properties.py
4b9c336964b64d61ead759ddfce7b3aaff1166f3bd54d8b31bede7cadb71edbb  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests/test_raw_atom_revision.py
2456867692c24549e97a91b4639c624ce33fe8e6dc4dafae7015fe04c8a09fe7  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/selected_execution.py
3f006e5819879ef41d903503b7688f1ea5482fe927d86a8adb3e0af939b07e2f  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_subject_apply.py
3b7f7e9bb7d3d1276881658e53b7bf65b309d7ecb8c4f37e76a204ff41fc0080  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/engine_publication_lock.py
29ceec6f53bb22470fe6614f234d075e38f56f12c14b1c32ebfe03093f8d4120  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/subject_publication_authorization.py
a723b61a79ef7f86d6bd4f6c9f0678dcd183bc5022c969d26829a9405870472c  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests/test_engine_publication_lock.py
b4ae520a82b78bf7b4270c2e81d91749a799d890cd4afe7de20710e213e40817  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests/test_engine_writer_exclusion.py
```
