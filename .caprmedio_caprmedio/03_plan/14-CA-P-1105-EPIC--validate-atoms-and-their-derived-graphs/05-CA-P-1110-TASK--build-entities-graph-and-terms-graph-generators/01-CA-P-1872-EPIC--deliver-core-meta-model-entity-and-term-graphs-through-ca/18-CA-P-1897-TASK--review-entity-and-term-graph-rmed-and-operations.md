---
atom_id: CA-P-1897
content_role: Plan
type: Plan
label: Task
work_sequence_number: 18
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Projection
  depends_on:
    - Requirement
    - Method
    - Evaluation
    - Delivery
    - Workflow
    - Action
    - Entity
    - Term
    - Plan
version: 2
updated_at: "2026-10-09 19:23:34 +0400"
relations:
  is_decomposition_of:
    - CA-P-1872
  blocks:
    - CA-P-1898
---
# Summary

Review entity and term graph RMED and Operations

## Objective

Independently review the current entity and term graph RMED and Operations packet before implementation.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent.

Inputs: CA-R-1835–1838, CA-E-555–558, CA-D-538–540, CA-M-259 and applicable Core graph Methods; CA-O-133–138 and their current referenced authority. Bind exact source paths, versions and SHA-256 digests.

Output: an independent review with accepted, rejected or unresolved findings and an obligation-to-code/test map. Check native Entity/Property ownership, governed Term definitions, graph-qualified Relation metadata, source and display selection, request/result grammar, destination safety, currentness, actual recording and recovery.

Exclusive scope: read-only graph RMED+O and related implementation evidence. Write review evidence in this Task's Details only. Do not repair source authority, release bindings or runtime in this Task.

Acceptance: every required graph contribution has clear governing authority and a bounded implementation/test responsibility. Missing source-fact syntax, unresolved definition qualification or incomplete relation metadata remains a finding; do not invent a contract or accept a partial prototype as the complete graph. If the review exceeds 15 minutes, decompose it before continuing.

### Independent review record — 2026-10-09

Independent semantic reviewer: `property_ownership`. Independent execution/binding reviewer: `graph_bindings`. Both reviewed source bytes and the held implementation without mutating authority. Their combined packet disposition is **rejected pending repair**, not a delivery or Run receipt.

| Obligation | Finding and disposition | Repair owner / implementation check |
|---|---|---|
| Native Entity Property facts | No admitted fact-context grammar; generic source metadata is incorrectly copied to governed Entities | CA-P-1900 / CA-P-1902; owner/value/source positive, metadata-leak negatives |
| Native graph Relations | Subject incidence and legacy body-text hierarchy are promoted to native edges | CA-P-1900 / CA-P-1902; graph-qualified registry and exact declaration/admission checks |
| Terms and hierarchy | Defining Claims and qualified Entity occurrences must remain distinct; NARROWER_THAN requires definition implication | CA-P-1900; current Claim fixtures, reusable Term labels, unresolved-admission negatives |
| Source/display selection | Evidenced empty source selection is rejected; display selection is echoed but not applied | CA-P-1902; empty/absent/unreadable and exact subset cases |
| Publication | Implicit filenames do not establish a registered destination; actual created/replaced effects are misclassified | CA-P-1901; no-destination, prior-file, drift and write-failure cases |
| Recording | Pure-builder Journal nonmutation conflicts with required executor events; start context is conflated with terminal completion | CA-P-1901; append-only actual recording, pending completion and recording-only recovery |
| Tool/runtime binding | Source declaration is not proof of an exposed MCP capability or current Docker realization | CA-P-1901; keep local, fixture and actual live receipts separate |
| Applicable Methods | Full-content Method inventory must identify modern Active authority and legacy candidates without inventing status | CA-P-1904; explicit universe, complete source contents, hashes and coverage diagnostics |
| Methodology edit ownership | Private strict-authority sources are canonical; public staged delivery and materialized Applicable Methodology members are derived | CA-P-1903; source-only revisions, no manual copy or manifest rehash |

The Operator approved design of a derived, source-pinned fact context built from authoritative Atoms. This approval permits the contract design, not invented facts, a new source grammar, source admission, runtime activation or fabricated recording.

The following baseline pins bind the reviewed pre-repair bytes at Git commit `136cbb132`. New revisions need a new independent review under CA-P-1899; these baseline pins do not accept later changes.

- `CA-D-538@1` — `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/07_delivery/CA-D-538-GRAPH_PROJECTIONS--bind-graph-projection-tool-carriers.md` — SHA-256 `d5cafb65efc13a6524f9fc987e2e7260e30f221acf4d0a15f7d5f8ac84a91d20`.
- `CA-D-539@1` — `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/07_delivery/CA-D-539-GRAPH_PROJECTIONS--bind-strict-graph-request-and-result-contract.md` — SHA-256 `97b2a02883f0364e0544cd26c00a5a4b6174a43f9643db2a2436799eacb62ab6`.
- `CA-D-540@1` — `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/07_delivery/CA-D-540-GRAPH_PROJECTIONS--bind-implementation-and-review-boundaries.md` — SHA-256 `a533b8bf4b3232729f8ee1dd6659c2cf23dbc0b0bffd4e38807cbc5597674247`.
- `CA-E-382@21` — `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-382-CORE_META_MODEL-GENERAL-EVALUATION_APPROACH--validate-terms-graph.md` — SHA-256 `605b14d1ec40fb708c294bdd01fca7c0b46c56cc8ec5cf3ef463a8575487d840`.
- `CA-E-449@12` — `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-449-CORE_META_MODEL-GENERAL-EVALUATION_APPROACH--validate-entities-graph.md` — SHA-256 `29db3bbff5744963c4fc7960042e6267a826b2fe16198e954039f5b223f3b00a`.
- `CA-E-555@1` — `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/06_evaluation/CA-E-555-GRAPH_PROJECTIONS--verify-complete-entities-graph-golden-output.md` — SHA-256 `872ead227a470cbfaa9e666fecb8e1d51ef0085d30c2e5d74b5c81248d02f4de`.
- `CA-E-556@1` — `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/06_evaluation/CA-E-556-GRAPH_PROJECTIONS--verify-complete-terms-graph-golden-output.md` — SHA-256 `239d33cf16ea0a3b0593bbea95d3897bf948f925c4958239ea54ec715833aeb1`.
- `CA-E-557@1` — `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/06_evaluation/CA-E-557-GRAPH_PROJECTIONS--verify-incomplete-conflicting-and-invalid-graph-truth.md` — SHA-256 `eb3d465d73c6ac5c89e46f20fb13d5474b83933588d5728277552c33668fee99`.
- `CA-E-558@1` — `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/06_evaluation/CA-E-558-GRAPH_PROJECTIONS--verify-determinism-persistence-and-nonmutation.md` — SHA-256 `3cfcfd15cd9e238cfc5d957c15277fe757d7768b3cee5c8c660907a42583b9cf`.
- `CA-M-114@20` — `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-114-CORE_META_MODEL--derive-terminology-projection-from-definition-atoms.md` — SHA-256 `16513dca0a7370d9a98999f537da293fd8d14ae4d9a47fee7f70fb1f8a9b1dd6`.
- `CA-M-120@14` — `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-120-CORE_META_MODEL-CORE--compile-the-direct-relation-registry.md` — SHA-256 `4f1a2004c885b1134ef57e309c37e1ab14c86bf008a3374fc93bbc20a2c104db`.
- `CA-M-259@7` — `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/GENERATE_ENTITY_GRAPH/05_method/CA-M-259-GENERATE_ENTITY_GRAPH-CORE-METHOD--derive-one-entity-and-term-graph-projection.md` — SHA-256 `86cc628f83be9151a1b3b40ddd028e2149908cbbb08b5e3032c5ac9d9609b3d7`.
- `CA-M-266@5` — `.caprmedio_caprmedio/05_method/CA-M-266-CORE-METHOD--follow-the-operator-selected-implementation-mode.md` — SHA-256 `f40c7467ac8641663fc20e26ce293d5495da516a80adbfce0637056222c4759f`.
- `CA-O-016@11` — `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-016-CORE_META_MODEL-WORKFLOW--implement-evaluations-before-required-behavior.md` — SHA-256 `b9a90e2133152c136353baae7db9d98c163cb595897b5fe2e870e4ffb394e13a`.
- `CA-O-017@6` — `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-017-CORE_META_MODEL-ACTION--prepare-implementation-work.md` — SHA-256 `02bdc37b110592f3171840bf995c4598af793d6679cc4261a075440aa9be943a`.
- `CA-O-018@6` — `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-018-CORE_META_MODEL-ACTION--implement-evaluations.md` — SHA-256 `ee6a141167ae2a8d9b387f3a92633a02d64b91c7539b901b876a8391e2555f6c`.
- `CA-O-019@4` — `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-019-CORE_META_MODEL-ACTION--implement-requirements.md` — SHA-256 `618eeb966ee41889d487d9ff1e48d4825aaa372bb2180e55688d446bdbc5065b`.
- `CA-O-020@5` — `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-020-CORE_META_MODEL-ACTION--run-implementation-evaluations.md` — SHA-256 `13aea0488ac7b230becf1739bd7ad6f29e5f964f0db1e4e1b680aac3b5f59051`.
- `CA-O-021@9` — `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-021-CORE_META_MODEL-ACTION--repair-nonconforming-implementation.md` — SHA-256 `841858a2234e54f51952a94724756e1af967249f7baa37623ce27eb4834f2121`.
- `CA-O-133@2` — `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-133-CORE_META_MODEL-WORKFLOW--build-entities-graph.md` — SHA-256 `17a2d268d16603d53bc963fdbfdac860eaa978bb78ea0d1096a4b29ebf12f780`.
- `CA-O-134@2` — `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-134-CORE_META_MODEL-ACTION--construct-entities-graph-projection.md` — SHA-256 `b94eebdd85eab9f7080680e85999c68022e82cdfa7945bf0d840b429ebad037a`.
- `CA-O-135@1` — `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-135-CORE_META_MODEL-STEP--construct-the-requested-entities-graph.md` — SHA-256 `f4040e234326114694b42dc4a96d494b12a024912342658a87d3ff28fae13805`.
- `CA-O-136@2` — `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-136-CORE_META_MODEL-WORKFLOW--build-terms-graph.md` — SHA-256 `60a2d8abbed65e00b376608c39ed01ae8d1960566f49a60ef498c694f508d3ff`.
- `CA-O-137@2` — `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-137-CORE_META_MODEL-ACTION--construct-terms-graph-projection.md` — SHA-256 `6c154852b99df16961fe63c8fd869dbf86f8d75ecc950b25b189e41c3c1c5dad`.
- `CA-O-138@1` — `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-138-CORE_META_MODEL-STEP--construct-the-requested-terms-graph.md` — SHA-256 `7fbffaea2fced0f5120805623cd6fcebc9bfaa34534cd23db7c71b54025e8005`.
- `CA-R-1279@12` — `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1279-CORE_META_MODEL-CORE-REQUIREMENT--govern-every-defined-term.md` — SHA-256 `80e2ba7b9461cf5909891d3c7c2c2bcd12baccc161b7a86f7b977552a61666d5`.
- `CA-R-1319@10` — `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1319-CORE_META_MODEL-CORE--define-governed-term.md` — SHA-256 `9c7f8ebf078c05a7d5ebef82ddec4e0903d269a387341a5c7fb6731b8ffbea58`.
- `CA-R-1435@7` — `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1435-CORE_META_MODEL-CORE--define-narrower-than.md` — SHA-256 `3146341d2251f2d539cdbf7dd63313bf5b0c7c1b09656b3b38070b037cbecf72`.
- `CA-R-1437@6` — `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1437-CORE_META_MODEL-CORE--keep-one-source-for-each-relation-fact.md` — SHA-256 `31392aee334fa3ca828d8459d585ca6655f99506ee7a98d59d2ff381bfa0ddbf`.
- `CA-R-1454@7` — `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1454-CORE_META_MODEL-GENERAL--derive-governed-terms-views-from-selected-authority.md` — SHA-256 `bab78ca52edb070123af5d40dd61fe4f44cf70941253aeb6aaf9deab0a5283f5`.
- `CA-R-1456@8` — `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1456-CORE_META_MODEL-GENERAL--derive-entities-views-from-selected-authority.md` — SHA-256 `3e389c9c223a5200e8fd7a1f3929dfa800f107e2b4e9a606a4eaf70247094fc8`.
- `CA-R-1835@1` — `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/04_requirement/CA-R-1835-GRAPH_PROJECTIONS--build-faithful-entities-graph-projections.md` — SHA-256 `3d54055b0861ce4cf6734705067f24516ff2adb2259d481e66290618daab9778`.
- `CA-R-1836@1` — `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/04_requirement/CA-R-1836-GRAPH_PROJECTIONS--build-faithful-terms-graph-projections.md` — SHA-256 `0acb0b60fb4312f712a85e968f35803c71260d39574041c2951da555e81d33b0`.
- `CA-R-1837@1` — `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/04_requirement/CA-R-1837-GRAPH_PROJECTIONS--enforce-projection-quality-and-truthful-outcomes.md` — SHA-256 `eca0abd92eacea169782d061bb697acd4cff81e59bd61cdc8604debf4ce4b969`.
- `CA-R-1838@1` — `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/04_requirement/CA-R-1838-GRAPH_PROJECTIONS--retain-source-and-shared-run-boundaries.md` — SHA-256 `2c01f157d5927197e9dc39148b84790cee2195f26a2e0a7b2bdb6e169267abf6`.
- `CA-R-806@21` — `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-806-CORE_META_MODEL-GENERAL--register-complete-relation-kind-metadata.md` — SHA-256 `933901316d347a2e09222d19d3a985c2feb93c7efc86e0a8332ab292cd169dd0`.

### Definition of Done

the Plan is **not** Done **if** ((the independent source-pinned RMED+O review or its required obligation map is missing or incomplete) **or** (a finding lacks a source-backed disposition **or** bounded repair responsibility) **or** (a required check has not been performed) **or** (any direct decomposing Plan is **not** Done)).
