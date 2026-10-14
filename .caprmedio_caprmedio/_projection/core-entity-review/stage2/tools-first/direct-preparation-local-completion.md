# Direct Subject preparation — local completion

2026-10-14. Derived acceptance evidence, not an Atom, source of authority or publication approval.

## Delivered

- Rules: ef3bde3c6; native reviewed-seal guard: bb04069b6; compatibility pins: 7d015c24e; provider and final guards/protocol: 15f9ce76e.
- Six independently reviewed rules: R866 v23, R1093 v12, M371 v11, E304 v22, D425 v16, O030 v16. Exact predecessors retained; Summary and Subjects unchanged. R1093's explicit identity header is the only added metadata beyond Version/time.
- Existing ATOM_UPDATE provider exposes atom_update with preview_subjects and stage_subjects. Closed logical inputs resolve privately within the bound Project. No direct publication operation is added.
- Preview writes nothing. Stage compares its own preview seal and exact illustrative time before any scratch creation, exports only a fresh .caprmedio_tmp batch, and preserves the original preview seal. Sources/history/Journal remain unchanged.
- Currentness and identity safeguards remain. Selected-ID checks retain collisions while unrelated malformed excluded content is not a global schema gate. Live/dangling role-directory links cannot hide competing identities.
- Partial write and final provider-boundary failures retain actual scratch evidence; they are not reported as successful or zero-effect publication.

## Checks

- Independent rule review: six source/current archive pairs, all twelve hashes, exact predecessor bytes, Version+1 and unchanged Summary/Subjects.
- Independent provider/native review: passed after fixing no-op timestamp mismatch and hidden role-directory symlinks. Ordinary Plan container folders also verified.
- Final native guard/stage/identity suites: 48 passed.
- Provider: seven passed; existing patch preview: sixteen passed. Root's final combined rerun: 23 passed.
- Protocol: eight passed in 25.700 seconds; seven real production-server MCP transport cases and one native CLI compatibility regression. Actual source/binding/complete validation is used, with injected write/readback/currentness faults.
- Publication compatibility: 43 distinct methods passed, including the re-run interrupted-publication method with history/current subtests after its expected O030 version changed to 16.
- Discovery prerequisite: 68 affected checks passed; Root independently reran 63. Test-only fixture repair is dea79c410.

These counts describe separate suites, not an assertion that the whole repository test suite passed.

## Exact implementation evidence

- ATOM_UPDATE/atom_update.py: 0cd13d45df7ecf8e77f1fa6571bc63b84c9e1679b7c4c8fb77b73bf7e18f132c.
- atom_subject_stage.py: 114720e53f24774911321cd692a03488f426c44361de116dc3120fd487056627.
- atom_subject_patch.py: efc673aef0bc843150c30f19a0448cb1de41304ad4f14956184404e9116fc36b.
- MCP test_direct_subject_preparation_protocol.py: 532c3ac05111847e7b85679745f60783fa82fd4b5cc51be1e4c22ce19857d1a6.

## Still open

The actual connected MCP recognizes D425 v16 but reports ATOM_UPDATE unresolved; local source changes did not update its immutable image. Activation/reconnection from reviewed commit 15f9ce76e requires the separately requested exact Project endpoint replacement. Do not bundle unrelated dirty changes or run the broader Local release.

No actual Core preview/staging, live migration, source publication, Session/Journal operation, image build/restart, push or installed-package update occurred in this increment. Ordinary content migration remains separate. The parent Epics remain Active.
