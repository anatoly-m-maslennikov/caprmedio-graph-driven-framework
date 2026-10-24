# Candidate #7 — remaining Subject worklist

Historical lexical input: superseded for continuation by the [2026-10-23 applied checkpoint](candidate-7.remaining-corrections-2026-10-23.md). Its broader frontier includes missing-Status legacy sources; use the new ledger for actual changes and the remaining literal inventory. Counts below describe this old snapshot only.

Status: derived, non-authoritative lexical inventory captured 2026-10-23; current Step 1 input refreshed for mapping-worker reconciliation.

The authoritative source Atom carriers remain the source of truth. This worklist routes literal non-canonical `subjects.governs` and `subjects.depends_on` strings for bounded research; it does not propose target Subjects, admit a Projection, or certify canonical-looking values semantically.

## Boundary

- Current means readable YAML frontmatter with a string own `status` other than `Draft` or `Archived`, case-insensitive; `Active` is not required.
- Included source Content Roles are Concern, Analysis, Requirement, Method, Evaluation, Delivery and Operations (C/A/R/M/E/D/O).
- Plan carriers are excluded from the remaining specification worklist. Their current metadata and Draft-ID work stays with CA-P-1968; this artifact does not claim full Candidate #7 all-role coverage.
- `_projection`, Applicable Methodology delivery mirrors, `archive`/`archived`, and `draft`/`drafts` paths are outside the source frontier.

## Source frontier

Discovery is read-only over the declared authority roots using `**/*.md` and regular non-symlink files. The frontier records each current readable carrier's file, SHA-256, Atom ID, Version and Status.

For project-root carriers, `PROJECT_CONTENT_ROOT` is only an inventory/root-routing label, not a declared Scope Unit ID. Consumers must use `declared_scope_units` and the source header before applying anything.

| Root | Authority path | Pattern |
| --- | --- | --- |
| METHODOLOGY_SOURCES | `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES` | `**/*.md` |
| FRAMEWORK_ENGINE | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE` | `**/*.md` |
| PROJECT_CONTENT_ROLE_ROOTS | `.caprmedio_caprmedio` | `{01_concern,02_analysis,03_plan,04_requirement,05_method,06_evaluation,07_delivery,08_implementation,09_operations,09_ops}/**/*.md` |

## Counts

| Measure | Count |
| --- | ---: |
| Markdown files discovered | 29151 |
| Current readable source records | 3584 |
| Included C/A/R/M/E/D/O sources | 2146 |
| Excluded current Plan sources | 1438 |
| Excluded other/missing-role current sources | 0 |
| Canonical-looking occurrences (excluded from remaining) | 348 |
| Remaining string occurrences | 9300 |
| Legacy non-string occurrences | 1 |
| Malformed subject diagnostics | 0 |
| Missing-header diagnostics | 29 |
| Missing-status diagnostics | 1082 |

### Research lanes

Each remaining occurrence has exactly one lexical routing lane. These are research queues, not target mappings.

| Lane | Sources | Occurrences | Heuristic |
| --- | ---: | ---: | --- |
| `history_actor` | 690 | 1008 | history, journal, actor, author, or revision marker |
| `content_roles_types` | 596 | 1256 | explicit Content Role or Type path marker; checked before carrier markers |
| `operations` | 793 | 1650 | operation, workflow, action, execution, run, or tool-flow marker |
| `relations_subjects` | 231 | 377 | relation, Subject, target, or Graph relation/rule marker |
| `carrier_storage` | 374 | 432 | carrier, storage, file/directory/database, filename, format, or path marker |
| `methodology_configuration` | 841 | 1401 | methodology, configuration, Project, Extension, settings, or source marker |
| `other` | 1494 | 3176 | no earlier lexical routing marker matched |

## Visible exclusions and diagnostics

- Plan occurrences excluded from this worklist: 8052 string and 0 non-string.
- Other/missing-role occurrences excluded from this worklist: 0 string and 0 non-string.
- One or more legacy non-string/malformed values remain visible in `legacy_nonstring_subjects` and `malformed_subjects`; no value was guessed.
- Path exclusions are counted by component: `{"applicable_methodology": 13, "archive": 23708, "archived": 690, "draft": 27, "drafts": 20}`.

## Snapshot checks

- Source frontier SHA-256: `901e2f541694dfcd4bcf6d258c1e8910746f6b29cabb743e60e354a12b166a44`.
- Path-level delta from the 2026-10-22 presentation: 19 paths added, 9 paths removed, and 10 retained records updated; this is source drift evidence only, not semantic coverage.
- Hashes recorded for all current frontier records: `True`.
- Remaining occurrence ownership is unique and lane totals reconcile: `True` / `True`.
- Two-pass source rehash stable during generation: `True`.

The JSON artifact contains the complete bounded record lists and diagnostics for independent checks. Refresh changed source records before using any lane.
