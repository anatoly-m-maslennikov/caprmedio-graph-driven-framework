# Current RMEDO placement review

This revision applies the latest Workflow responsibility rule. It supersedes the earlier blanket all-O-to-Project-Configuration proposal and its 418-candidate destination counts. No source has moved.

## Latest result

| Classification | Sources |
| --- | ---: |
| Methodology | 1344 |
| Engine | 971 |
| Project-local | 111 |
| Mixed | 18 |

All **2,444 Current RMEDO sources** are accounted for. This includes CA-R-2155, the Operator-owned Project Goal outside ordinary role folders, omitted from the initial 2,443-source census. It keeps its Actor owner; the separate Scope Definition trial has not changed it. C/A/P and legacy Implementation placement remains deferred.

- [Full thin table](current-rmedo-placement.tsv)
- [Uncertain cases](rmedo-placement-uncertainties.tsv)
- [Changed Workflow proposals](workflow-placement-corrections.tsv)
- [Verification summary](rmedo-placement-review-summary.json)

## Responsibility rule

- Core Meta-model owns reusable business workflow meaning: what happens to Atoms, Projections, Journal and other Objects, including general implementation work.
- Engine owns technical workflows and implementation: execution, scheduling, transport, adapters, storage mechanics and code.
- Project owns its Local/Public Release orchestration and other genuinely project-specific procedures.
- A Project Workflow can call Methodology or Engine Workflows as Steps. The callee keeps its definition and owner; calling does not copy it or force local definition.

The correction re-read 187 O definitions and 186 related R/M/E/D contracts. Concrete names alone do not make business meaning Project Configuration. The reviewed [ownership/composition Rule Draft](workflow-responsibility-drafts.md) records the decision without changing Current RMEDO.

## Proposed actions

| Action | Sources |
| --- | ---: |
| Keep | 1802 |
| MoveCandidate | 576 |
| NeedsDecision | 48 |
| SplitCandidate | 18 |

66 uncertain/split cases remain explicit. A candidate is not an approved move.

## Largest proposed destinations

| Destination | Move candidates |
| --- | ---: |
| CORE_META_MODEL | 216 |
| ATOM_ACTIONS | 50 |
| JOURNAL_ACTIONS | 41 |
| PROJECTION_ACTIONS | 35 |
| ADAPTERS | 33 |
| FRAMEWORK_METHODOLOGY | 32 |
| caprmedio | 30 |
| PROGRAMMATIC | 25 |
| PROJECT_ACTIONS | 20 |
| PROJECT_CONFIGURATION | 19 |
| MCP | 11 |
| FRAMEWORK_ENGINE | 9 |

## Limits

This is cheap placement triage with focused follow-up, not a full content migration, semantic certification, runtime audit or code change. Source hashes were rechecked. Engine destinations are registered Engine Scope Units. Native consumers, container placement, authority/ordering and identity/version/archive effects must be checked before actual moves. Existing metadata and unregistered legacy names remain explicit uncertainties.

The source-root Project Goal was checked directly rather than inferred from a role folder. Its legacy Subjects/body shape and proposed Scope Definition replacement are separate from placement. Forty-one execution-evidence documents were explicitly excluded as non-Atoms. Broader C/A/P work remains parked, including the deferred mixed-Plan question.
