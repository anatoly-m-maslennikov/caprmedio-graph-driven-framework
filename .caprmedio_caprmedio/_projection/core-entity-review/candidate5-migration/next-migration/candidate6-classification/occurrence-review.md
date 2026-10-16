# Candidate #6 — Source-occurrence mapping

Date: 2026-10-16. Candidate review only; no source migration or content rewrite.

## Result

All **48** source-specific Subject families were inspected: **546 Subject/source pairs** across **441 current source Atoms**, comprising **548 governs/depends_on uses**. Two sources use the same reviewed Subject in both roles.

| Disposition | Uses | Meaning |
| --- | ---: | --- |
| Map | 314 | Source-specific candidate target, with instance/domain qualifications retained |
| Remove reference | 94 | Redundant or unsupported dependency link; not deletion of the Atom |
| Content deferred | 82 | Mapping alone would narrow or contradict the rule, or its target is not yet defined |
| C/A deferred | 58 | Leave historical Concern/Analysis material unchanged |
| Total | 548 | All cited source IDs and observed roles covered |

No new Operator decision is required by this pass. This does **not** make the migration executable: named-instance qualifications still need faithful encoding, missing R definitions remain required, and content conflicts remain held. A map/remove disposition for one Subject does not permit editing an Atom held by another Subject or review. Thirteen sources have both mapped/removable and held uses within this pass.

Hold these whole Atoms despite their other mapped/removable references: `CA-D-407`, `CA-E-246`, `CA-E-249`, `CA-E-379`, `CA-M-295`, `CA-M-298`, `CA-O-054`, `CA-R-1268`, `CA-R-1375`, `CA-R-1409`, `CA-R-1580`, `CA-R-1682`, `CA-R-1683`. This includes twelve Atoms with mapped uses and R1409 with a removable reference. Resolve their content conflicts before any Subject-only write.

The 19 previously identified content-deferred Subject families remain separate. Their number is not comparable to the 82 occurrence-level content holds here.

## Per-Subject result

Each linked JSON record includes the exact source path, role, target, reason and source evidence. Candidate targets are not a new selector grammar. The earlier 511-Subject classification remains a snapshot; these records supersede its pending per-occurrence assignment for the 48 entries below.

| Index | Subject | Map | Remove link | Content hold | C/A hold |
| ---: | --- | ---: | ---: | ---: | ---: |
| 8 | [Agentic Step Execution Context](occurrence-map-execution.json) | 35 | 0 | 0 | 0 |
| 30 | [Artifact](occurrence-map-artifact.json) | 12 | 36 | 20 | 0 |
| 53 | [Artifact/Revision](occurrence-map-revision.json) | 8 | 5 | 5 | 56 |
| 72 | [Atom Change Classification](occurrence-map-execution.json) | 3 | 1 | 0 | 0 |
| 86 | [Atom Scope](occurrence-map-scope-relations.json) | 28 | 0 | 3 | 0 |
| 89 | [Atom Tier Validation.Concrete Cases](occurrence-map-scope-relations.json) | 1 | 0 | 0 | 0 |
| 138 | [CAPRMEDIO Framework Identity](occurrence-map-config.json) | 0 | 0 | 1 | 0 |
| 139 | [CAPRMEDIO Framework Instance](occurrence-map-execution.json) | 2 | 8 | 0 | 0 |
| 141 | [CAPRMEDIO Graph](occurrence-map-scope-relations.json) | 7 | 8 | 1 | 0 |
| 142 | [CAPRMEDIO Graph.Connectivity](occurrence-map-scope-relations.json) | 1 | 0 | 1 | 0 |
| 149 | [CCE Method](occurrence-map-topics.json) | 2 | 0 | 0 | 0 |
| 195 | [DEPENDS_ON](occurrence-map-scope-relations.json) | 16 | 0 | 0 | 0 |
| 197 | [Default Settings](occurrence-map-config.json) | 15 | 0 | 3 | 0 |
| 229 | [Extension](occurrence-map-config.json) | 19 | 2 | 8 | 0 |
| 253 | [Hub Atom](occurrence-map-topics.json) | 3 | 10 | 8 | 0 |
| 254 | [Hub Carrier.Navigation Entry](occurrence-map-topics.json) | 1 | 0 | 0 | 0 |
| 275 | [Implementation Workflow](occurrence-map-execution.json) | 6 | 1 | 0 | 0 |
| 291 | [Markdown Atom Carrier.Main Content](occurrence-map-topics.json) | 6 | 2 | 0 | 0 |
| 294 | [Markdown Atom Carrier.YAML Frontmatter](occurrence-map-topics.json) | 3 | 3 | 0 | 0 |
| 303 | [Methodology Source](occurrence-map-config.json) | 16 | 1 | 2 | 0 |
| 305 | [Methodology Source.Expansion Boundary](occurrence-map-config.json) | 8 | 0 | 2 | 0 |
| 306 | [Methodology Source.Expansion Mapping](occurrence-map-config.json) | 0 | 0 | 3 | 0 |
| 342 | [Project Configuration](occurrence-map-config.json) | 17 | 2 | 6 | 0 |
| 343 | [Project Lexicographic Selection](occurrence-map-execution.json) | 3 | 0 | 0 | 0 |
| 347 | [Project Priority Model Application](occurrence-map-execution.json) | 5 | 0 | 0 | 0 |
| 390 | [Relation Kind Metadata](occurrence-map-scope-relations.json) | 5 | 0 | 0 | 0 |
| 405 | [Runtime State](occurrence-map-execution.json) | 1 | 1 | 0 | 0 |
| 438 | [Spec Content Roles](occurrence-map-scope-relations.json) | 10 | 0 | 0 | 0 |
| 443 | [Step/Agentic Execution Context](occurrence-map-execution.json) | 3 | 0 | 0 | 1 |
| 448 | [Structural Entity Recursive Containment](occurrence-map-scope-relations.json) | 1 | 0 | 0 | 0 |
| 459 | [Subject Relation Kind: DEPENDS_ON](occurrence-map-scope-relations.json) | 1 | 0 | 0 | 0 |
| 471 | [Translation](occurrence-map-topics.json) | 2 | 0 | 1 | 0 |
| 477 | [Verification](occurrence-map-execution.json) | 3 | 0 | 3 | 0 |
| 482 | [Workflow/Step binding ownership](occurrence-map-execution.json) | 0 | 0 | 0 | 1 |
| 486 | [artifact-model](occurrence-map-topics.json) | 7 | 3 | 2 | 0 |
| 488 | [authority](occurrence-map-topics.json) | 5 | 5 | 2 | 0 |
| 490 | [continuous-improvement](occurrence-map-topics.json) | 3 | 1 | 1 | 0 |
| 491 | [development-flow](occurrence-map-topics.json) | 3 | 0 | 2 | 0 |
| 492 | [evaluation](occurrence-map-topics.json) | 6 | 0 | 0 | 0 |
| 493 | [extension-model](occurrence-map-config.json) | 3 | 0 | 2 | 0 |
| 494 | [external-boundary](occurrence-map-topics.json) | 2 | 0 | 0 | 0 |
| 495 | [framework-boundary](occurrence-map-config.json) | 1 | 0 | 0 | 0 |
| 497 | [language](occurrence-map-topics.json) | 5 | 0 | 1 | 0 |
| 499 | [lifecycle-traceability](occurrence-map-topics.json) | 10 | 0 | 0 | 0 |
| 500 | [principles](occurrence-map-config.json) | 1 | 0 | 0 | 0 |
| 507 | [scope-topology](occurrence-map-scope-relations.json) | 19 | 0 | 4 | 0 |
| 508 | [semantics](occurrence-map-topics.json) | 5 | 5 | 1 | 0 |
| 509 | [settings specification](occurrence-map-config.json) | 1 | 0 | 0 | 0 |

## What remains held

- Old Artifact taxonomy and broad non-Atom rules: preserve valid meaning; do not narrow them to Atom by renaming the Subject.
- Historical Revision versus current source identity: current versioned Atoms/configuration/Projections are not automatically History/Revision. Obsolete receipt gates and lifecycle exceptions need content work.
- Old Hub, activation/binding, Definition-Atom, backlog and Implementation assumptions: apply the approved content decisions separately.
- The CAPRMEDIO framework-name rule and Expansion Mapping: no invented result Object or evidence carrier to force a target.
- C/A records remain outside the current migration scope.

## Checks

- Six disjoint lanes cover all 48 inventory indices and every cited source ID.
- Exact governs/depends_on presence and full role coverage were checked against current canonical source headers.
- JSON structure, canonical Project paths and source-file existence checked.
- Independent semantic review sampled risky mappings. It corrected two overly narrow scope mappings and one copied YAML applicability qualifier; it was not a second full content audit.
- Source-tree checksum is unchanged: `3f3bf6d739f95863c5575638c23de92560939c932e7eb9ec92fe860f5cd64adf` (sorted Markdown file checksums under canonical METHODOLOGY_SOURCES).
- No live Atom changes, graph rebuild, content migration or runtime tests performed.

