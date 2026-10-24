# Candidate #7 — prepared Subject map

Date: 2026-10-23. Status: Step 1 preparation; not applied. This is a non-authoritative mapping report, not a graph Projection, source Atom, Journal event or executed migration.

## Result

All 9,301 reviewed occurrences have an explicit disposition: 7,692 supported mappings, 17 endpoint-only removals, 376 content holds, 1,215 unresolved mappings and 1 changed-source case. These counts include the one malformed legacy YAML Subject that can be represented as the intended quoted Method classifier.

[Complete prepared map](candidate-7.subject-map.prepared-2026-10-23.json). Exact source IDs, Versions, hashes, occurrence direction/index, targets, evidence and holds are retained. The map covers 1,973 distinct remaining-Subject owners from a bounded 2,146-source C/A/R/M/E/D/O inventory. Plan migration and missing-header/status legacy carriers remain outside that bounded map; their exclusions are visible in the JSON. The 348 canonical-looking occurrences were not newly semantically certified.

## Lane coverage

| Lane | Rows | Map | Remove endpoint | Content hold | Unresolved | Changed |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| history_actor | 1008 | 816 | 0 | 146 | 46 | 0 |
| content_roles_types | 1256 | 1229 | 17 | 10 | 0 | 0 |
| operations | 1650 | 1343 | 0 | 0 | 307 | 0 |
| relations_subjects | 377 | 212 | 0 | 0 | 165 | 0 |
| carrier_storage | 432 | 419 | 0 | 13 | 0 | 0 |
| methodology_configuration | 1401 | 1282 | 0 | 0 | 119 | 0 |
| other | 3176 | 2390 | 0 | 207 | 578 | 1 |
| legacy_shape | 1 | 1 | 0 | 0 | 0 | 0 |

The confidence threshold is at least 90% for each proposed mapping, not a required percentage of rows mapped. Unsupported cases remain explicit instead of being forced into the tree.

## First Operator question

Bare Tool appears in 210 unresolved occurrences across 207 Atoms. Proposed shared target: Subject/Engineering/Tool, covering both a Tool's contract and implementation. R/M/E/D would describe the role of each Atom; more-specific Subjects would remain specific. The question has been asked; no answer or source effect is assumed.

Do not turn descriptive Tool qualifiers into invented Tool instance names. Unknown domain/engineering topics are not automatically Term instances or new independent objects. Relation properties, classifiers and named kinds preserve their specificity rather than collapsing into the Relation root.

## Holds and source drift

- Revision is already obsolete as a separate entity. Held old Revision rules need source-specific preservation/retirement; this is not a question to restore Revision.
- Artifact is not a separate branch. Holds do not silently map Artifact to the Term class or archive its owning Atom.
- Cross-bearer Type/property meanings are not new universal entities or another authoritative definitions layer. The Terms Graph derives meanings from actual source cases.
- CA-C-576 changed while PROGRAMMATIC work continued. Its occurrence is marked changed_source; the report keeps captured and observed hashes. This affects that owner, not the entire map.
- No supported subset of a held or unresolved owner is ready for application. The JSON records whole-owner preparation status separately from supported individual mappings.

## Checks and limits

The seven lanes reconcile exactly to immutable input SHA-256 ce85508839243da0436574ba033805fdc7f368195645a01e60df3cf05f5a5313, with one additional explicit legacy-shape disposition. JSON/identity/source-field/target/confidence checks and independent semantic spot checks passed after precision corrections. The input frontier and observed source drift are preserved; no fixed global fingerprint gate or new approval mechanism was introduced.

No source Atoms or Plans were edited; no migration, code change, runtime tests, MCP operation, Journal append, commit or release occurred. General content migration remains separate. Resolve the grouped questions and content dispositions before claiming complete mapping or applying affected owners.
