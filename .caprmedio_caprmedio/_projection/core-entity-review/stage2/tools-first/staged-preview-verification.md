# Checked Subject staging: implementation verification

2026-10-12. Non-authoritative evidence for CA-P-2183–2186. This receipt accepts the local staging capability, not Core migration, source publication or installed MCP support.

## Contract and scope

The Operator chose: stage the migration; update Tool RMEDO and Plans normally. The five updated authoritative contracts passed [independent actual-source acceptance](staged-preview-contract-acceptance.md), committed as `15d2373db`. The Epic's bounded staging branch is recorded in `0e60307ea`.

`ATOM_UPDATE run --stage-preview` consumes the existing closed Subjects-only payload. It preserves the default mutation-free preview and the pure planner. It creates a fresh generated `.caprmedio_tmp/subject-preview/<id>/` batch with numbered directories and unchanged source filenames. It reads back full candidate bytes, checks their hashes, validates at the original logical source path, and rechecks the same pinned preview using its original illustrative timestamp.

The separate closed manifest binds source pins, intent hashes, candidate paths/hashes and validation. The enclosing result retains the complete original preview and marks staging-only, illustrative, sources-unchanged evidence. These are point-in-time observations, not approval or a lock. Later use must recheck hashes. Partial failures report retained owned artifacts or explicitly unverified attempted paths; they do not overwrite or clean up uncertain files.

No original, predecessor-history, Journal or MCP effects are performed by staging. The native changed-Subject route still refuses publication. Ordinary Tool-rule and Plan revisions above are separate explicitly authorized changes, not a migration through this capability.

## Independent review and fixes

`tools_first_verifier` reviewed the implementation against the actual contracts and accepted the final code. Two findings were fixed and independently rechecked: use the existing complete-validation exception wrapper for structured post-export authority failures; retain truthful directory references when post-creation verification fails. No live-publication or general recovery design was introduced.

`preview_currentness_tests` independently authored 14 cases with literal before/after byte ledgers. `tools_first_verifier` separately accepted their independence and boundary coverage: real complete validation, real CLI subprocesses, failure-only injection, externally changed bytes preserved, and exactly 14 discovered methods rather than duplicate imported test classes.

## Execution evidence

- Root reran the full ATOM_UPDATE suite: **80 passed**, 39.286 seconds. This includes the 14 staging cases and seven native portfolio cases; do not add them again. It supersedes the earlier in-progress 78-test result.
- The independent staging author separately ran its 14 cases: all passed, 12.997 seconds.
- ATOM_SEARCH: **49 passed**, 2.058 seconds, against the same shared integration code.
- Root reran the generic selected-Atom lifecycle suite: **30 passed**, 3.418 seconds.
- The current-O030 fixture alignment passed seven native portfolio tests and eight real selected-Subject tests (12.712 and 49.219 seconds). Seven overlap the full UPDATE suite. Historical Golden O030 v7 pins remain unchanged; the current Subject fixture binds v11.
- Root checked the actual local wrapper's description: staging is explicit, standalone apply is unsupported, and no MCP binding is advertised.

Checks used `uv`, the locked isolated environment under `.caprmedio_tmp/tools-first-validation.kO9IcX/venv`, offline/no-sync/frozen dependencies, Python 3.14, project-local temporary/cache paths, and disabled bytecode writes. No installation, service activation or release was performed.

Coverage includes legacy/approved profiles, LF/CRLF, Active/Done/Backlog, mixed change/no-op batches, exact manifest and full-preview hashes, unchanged body/source modes/history/Journal, stale sources/grammar/identity/validation authority, symlink/occupied/substituted destinations, partial writes/readback/tampering, validator exceptions and known/unverified directory leftovers. The tool preserves externally injected edits rather than rolling them back. Default preview and generic/invalid/apply input boundaries remain checked.

## Final implementation pins

Paths are repository-relative; SHA-256 values were reopened by Root after the final suite.

| File | SHA-256 |
| --- | --- |
| `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/atom_subject_stage.py` | `9e5c60078054d8a738c3b8fbba0681f7d699620184378172d8c1363f076100ef` |
| `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/atom_operations.py` | `a78f3dea98b5b183fe406192197f399602c12be9919c9abe5a777c02730ffb64` |
| `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/atom_subject_patch.py` (unchanged) | `0c2c7058470309820002ce9f97db8a2c30be17fe7726675658d4414c3633f218` |
| `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_UPDATE/tests/test_subject_stage_preview.py` | `c3655910ef12527653aa338976e35f357d3348270f9c3257d72b2cee4c1c5826` |
| `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_UPDATE/tests/test_subject_apply_portfolio.py` | `123ded747abf7c68d4cd4b310acc619e7ee7200157d02dacaade69c9ee4ec900` |

## Readiness boundary

This completes the bounded staging capability. With CA-P-1963, it permits read-only current-source adaptation/re-pinning/mapping for staged candidates. Candidate #3 remains non-authoritative; old mapping pins are not refreshed or adopted by this receipt. No Core Subject, Summary, Substance, scope or detail was migrated by this work. CA-P-2167's full publication gate, CA-P-1909–1912's shared final gates and Step 2 after CA-P-1969 remain open. Concurrent safe publication is still deferred, not solved by staging.
