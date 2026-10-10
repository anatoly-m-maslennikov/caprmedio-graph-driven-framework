# Subject Tool RMEDO review — CA-P-1979

Reviewed 2026-10-10. This is derived review evidence, not Tool or Core authority.

## Decision and boundary

Keep two small reusable operations: structural Subject lookup and an exact Subject-only update preview for already-correct Atom files. Repairs, migration decisions, grammar cutover and batch application use bounded ad-hoc scripts. Do not build a reusable migration framework.

Only ATOM_SEARCH and ATOM_UPDATE Tool RMEDO need repair before their implementation. Their declared owner is `TOOLS`; their subfolders are artifact collections, not independently declared Scope Units. No Core entity-model Subject or body changes belong in this repair.

The current Project Structure pin is `0ceb85e781490b89fc539f27eb5bf3a5187d4c982a648f27b40b6057257df92c` for `.caprmedio_caprmedio/project_structure.toml`. Core authoring remains under `101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL`; delivered copies are not authority.

## Current Tool sources

All paths below are relative to `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/`. These are before-repair pins, not permanent latest-version references. Recheck bytes before changing any source.

| ID | Version | Source path | SHA-256 |
| --- | --- | --- | --- |
| CA-R-863 | 12 | ATOM_SEARCH/04_requirement/CA-R-863-ATOM_SEARCH-CORE-REQUIREMENT--search-caprmedio-markdown-atoms.md | b8498bb81cb94953f3d57a6e98e10ce5fda16fe53f54a223edd096c4feb6bd19 |
| CA-E-301 | 11 | ATOM_SEARCH/06_evaluation/CA-E-301-ATOM_SEARCH-QA_CASE--verify-search-caprmedio-atom-carriers.md | 2d15908b86a852b7b45e9b64fc7fa46ac24fe2364e51978c39ae9f6a452a550d |
| CA-D-038 | 9 | ATOM_SEARCH/07_delivery/CA-D-038-ATOM_SEARCH-DELIVERY--bind-atom-search-delivery-place.md | 1b704dfb8a0c343c3a4bebf3f9fab2f7480e7224d2d330a957ae45b64075e01e |
| CA-D-424 | 6 | ATOM_SEARCH/07_delivery/CA-D-424-ATOM_SEARCH-DELIVERY--deliver-atom-search-tool.md | b121c2e40e1847658bdd758c4cc102b5a978b9738dc9cf7adc4742e078dd0b8a |
| CA-O-046 | 2 | ATOM_SEARCH/09_operations/CA-O-046-ATOM_SEARCH-ACTION--search-caprmedio-atom-carriers.md | dc1604d8f5429d70cf908f6eaf063cc6716efdde2bb7c8b7ee47429f1fc73f63 |
| CA-R-866 | 12 | ATOM_UPDATE/04_requirement/CA-R-866-TOOLS-STANDARD-REQUIREMENT--update-caprmedio-markdown-atoms.md | 12cb9fccb479b0d6a9d7e6cc1db42d037b678a94b45e9f4dba5c4e3464f9a86d |
| CA-E-304 | 11 | ATOM_UPDATE/06_evaluation/CA-E-304-TOOLS-STANDARD-QA_CASE--verify-update-sealed-caprmedio-atom-carriers.md | 60be51d610c6e2d6ff94854c70a3db44b515ffe8309b3eb7399275c66e99fcbc |
| CA-D-041 | 9 | ATOM_UPDATE/07_delivery/CA-D-041-ATOM_UPDATE-DELIVERY--bind-atom-update-delivery-place.md | 336833d93374b4af85e466cc9efaf5bd397bf219949c204a1e84847359ed7900 |
| CA-D-425 | 6 | ATOM_UPDATE/07_delivery/CA-D-425-ATOM_UPDATE-DELIVERY--deliver-atom-update-tool.md | 2fcef924444003b0e52fee7c5bdcc0070d96ea7ad1ae7e712e6fbbc2ee56ad66 |
| CA-O-030 | 5 | ATOM_UPDATE/09_operations/CA-O-030-TOOLS-ACTION--update-sealed-caprmedio-atom-carriers.md | 99e18ebce351c72e7e6c684455057439209d107faa217a53782e58b8747c7edc |

Shared CA-R-1093 v9 (`04_requirement/CA-R-1093-TOOLS-CORE-REQUIREMENT--separate-generic-and-atom-specific-tool-authority.md`) has SHA-256 `7cde34e0fbb29499559dd522dce264839731266bf632239eeda1f6cdf06a7376`. It already separates Atom-specific semantics and read-only finders from doers; no change is required.

No active Method exists for either Tool. CA-M-183 and CA-M-186 are archived, not active authority. Add two focused Method Atoms; do not silently reactivate retired methods.

Search R/E/O and the Delivery carriers lack current identity/role/owner/status metadata. Their filenames and retained titles establish the legacy identities, but the current scanner cannot treat them as valid Active Atoms. Restore their current file structure as a bounded authoring repair, not through a reusable invalid-file updater. Use declared `TOOLS` ownership; preserve Summary and filename identity. Do not invent Tool Scope Units.

## Confirmed gaps and minimum contracts

| Role | Gap | Bounded repair and acceptance |
| --- | --- | --- |
| R | Search is whole-carrier substring matching; update accepts complete frontmatter/body only. | Define direct flat `subjects.governs` and `subjects.depends_on` lookup, exact/boundary-prefix matching and conjunctive source/role/owner/lifecycle filters. Define exact pinned Subjects-only preview on valid files. |
| M | No active method for either operation. | Use structured YAML fields, not text hits. Patch exact scalar spans, preserve unrelated bytes and line endings, reject invalid files instead of repairing them. Reuse existing update admission; no migration engine. |
| E | Existing tests do not cover the new field/pin/preservation contract. | Require independent fixture expectations, direction and prefix tests, stale/invalid/duplicate/path failures, no-write preview, unchanged unrelated bytes and unchanged standalone apply guard. |
| D | Generic wrappers deliver no field-aware request/result schema. | Specify small lookup and patch inputs/outputs, source pins and truthful CLI availability. Keep established wrapper locations; do not claim unsupported MCP delivery. |
| O | Search steps lack exact occurrences; update steps lack exact Subject-only proposal. | Validate request and source, find exact occurrences or preview explicit replacements, return pins and findings. Actual Subject changes use Version N+1 and actual updated_at; preview does not execute history or Journal effects. |

Lookup results identify Atom ID, Version, Status, owner, relative path, SHA-256, updated_at and exact field/index/value. `governs`, `depends_on` and both are selectable. Delimiters are lexical prefix boundaries only: the Tool does not infer ontology relations or adopt the pending new grammar.

Patch requests identify exact relative path, Atom ID, Version, SHA-256, field/index, old value and explicit new value. Reject malformed/nested legacy Subjects, ambiguous occurrences, duplicate dependency results, stale pins, path escapes and symlink targets. Validate the complete resulting carrier. Only Subjects and required Version/updated_at spans may change. No-op makes no revision. Do not mix this mode with complete frontmatter or body replacement.

Keep the existing generic update contract and its admission guard. The new Subject-only mode is preview-only locally. Its proposed actual change is a semantic revision with Version +1; this avoids silently changing the unrelated generic change-class policy during this Tool repair. Grammar adoption and migration-specific history/Journal effect planning remain later ad-hoc work.

## Implementation and capability evidence

`102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/atom_operations.py` has SHA-256 `06faa42ec6a4587123ac55a0a37b6795741492c32f5d3dfd30510dc12f8d782a`.

- `run_search` matches path/frontmatter/body text and returns no exact Subject occurrences or source digest. `scan_atoms` silently skips invalid carriers. The new valid-file mode must report rejected selected files separately.
- `run_update` accepts whole frontmatter or body. Reduced frontmatter can lose unrelated fields. It does not implement an exact Subjects-only pinned patch.
- The CLI rejects standalone ATOM_UPDATE apply. Keep that rejection. `lifecycle_intents.py` already supports the sealed generic update route; do not invoke raw internal apply as a substitute.
- Graph source readers and `migrations/subject_notation_migration.py` are derived or preview-only helpers, not live Subject writers. The migration-specific planner remains an ad-hoc path; it is not the new reusable Tool contract.
- Static `implementation_server.py` registration and `selected_routes.py` expose no field-aware Subject search or Subject-only patch MCP capability. Generic `update_atom` is not that capability. No live server advertisement was checked; no MCP call, adapter activation or capability support is claimed. Unsupported MCP is unused.

## Checks and lane closure

Read-only checks ran with uv: Atom operations 26 tests; source reader 12; mechanical graph 15; migration planner 7. All passed. These are existing-behavior checks, not acceptance of unimplemented features. Search/update describe returned only generic capability metadata.

| Lane | Owner | Edit scope | Acceptance | Status |
| --- | --- | --- | --- | --- |
| R/M inventory | subject_lookup_audit | None | Exact authority and minimum reusable contract | Done |
| E/D inventory | subject_tools_proof | None | Actual tests, schema and preservation gaps | Done |
| O/MCP inventory | subject_authority_audit | None | Static supported routes and guards identified | Done |
| Simple local split | consolidation_tooling | None | Reusable valid-file operations versus ad-hoc migration | Done |

Root rechecked all ten current Tool hashes and Project Structure before recording this receipt. No Tool RMEDO, Core Subject, code, runtime, history or Journal effects occurred. CA-P-1982 must assign disjoint R/M, E, D and O repair leaves; CA-P-1981 must independently verify the repaired packet before implementation starts.
