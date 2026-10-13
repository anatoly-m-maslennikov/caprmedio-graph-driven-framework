# Admitted-container reference lookup

Derived implementation receipt, 2026-10-13. Not source authority, an FPF report, or installed-runtime acceptance.

## Scope and result

CA-P-2314 is complete for the bounded lookup correction. Source rules and Plans were independently accepted and committed in `c9c22b34d`; implementation, exact consumed source bindings and fixtures were independently accepted and committed in `5a1d3171d`.

Lookup follows declared Scope Unit and selected Project roots, exact Content Role/Status directories, and authenticated same-stem Plan/Workflow/Step containers. Unknown directories cannot supply targets or parents. Independently declared nested Scope Units use their own authority; row order cannot transfer ownership. Requested targets require their own carried identity, role, owner, Status, Version and valid placement. Archived history never satisfies current references, including exact old bytes carrying Active. Existing malformed admitted carriers still refuse lookup. No identity is inferred from filenames.

Reads remain bounded and no-follow. Rechecking covers source bytes, admitted membership and newly appearing admitted directories. Unknown-directory changes do not become authority or affect the result. Shared ReadContext and mutation APIs were not changed.

## Frozen implementation

Paths are relative to `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS/`.

| File | SHA-256 |
| --- | --- |
| `validate_atoms_workers/proposed_references.py` | `13c6dfd42a3c420383c8a0dec3f0d9ae292d3bf6948b3b9a560e68161cced304` |
| `validate_atoms_workers/proposed_carrier.py` | `26f41eb482bbcf2bdcf3060da047ab74de41846b6312e9f43c8644bf047d6f14` |
| `tests/test_proposed_references.py` | `dccb813fb010b1afa5c74a9119cb0af404cbe482e2ecad1970b91d45dc455918` |
| `tests/test_proposed_carrier_admission_regressions.py` | `33b26b270eb252e719201236527ef5dd8e53cc039c01856c6607cb6351eb6812` |

Only the consumed whitelist source closure was refreshed. Nine source fixtures match their exact source bytes; the four refreshed role-domain clauses retain the same admitted values. Unrelated source-path migration was not performed.

## Verification

- Focused final inventory and admission suite: 55/55 PASS, including a real relation-bearing caller success and missing-target refusal.
- Source-binding suite: 4/4 PASS; real selected-context source reads and missing/changed authority refusal.
- Independent fixture checks: 75/75 PASS; 113 combined support-source fixtures match their manifest hashes.
- Independent implementation review: PASS. Its concrete row-order ownership defect was fixed and rechecked. Ten additional actual-file ownership/currentness/status-authority checks passed.
- Final complete validator suite: 308 run, 306 PASS. The same two pre-existing graph-authority refresh tests fail because refresh roots still point to the old methodology location (`CA-D-268` absent). This is not a full-suite PASS.
- Selected lifecycle suite: 30/30 PASS. These regressions do not establish cascade execution.
- Diff whitespace checks passed. Ruff and mypy were unavailable in the offline environment; no dependencies or shared environment were changed.

Tests used offline standalone uv with Python 3.14, PyYAML 6.0.3 and pydantic 2.13.5; caches, temporary files and bytecode were routed to `.caprmedio_tmp`. The isolated caller fixture uses exact manifest-hashed graph source bytes at declared fixture paths, not proof that the live checkout's legacy graph paths are ready.

## Remaining boundaries

Read-only complete-carrier rechecks of current M383, D632, E635 and P2307 v4 now pass the former unknown evidence directory. All still refuse this admitted Concern carrier because it lacks supported YAML frontmatter:

`.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/205_FEATURE_SKILLS/01_concern/CAPRMEDIO-FRAMEWORK-ENGINE-CONC-076-SKILLS-PROBLEM--problem-core-skill-runtime-is-incomplete.md`

That source was not normalized or excluded. Previously identified requested legacy metadata and graph-path gaps may remain behind this first refusal. Parent P2307, TOMLKit implementation and full source admission remain open.

All-status containment cascades are now specified, but runtime cascade composition remains separate under CA-P-2264. O127/O129 still expose single-target execution. Nested Operations reference discovery is supported; new nested Operations carrier authoring remains unsupported by the separate proposed-carrier placement check. No live Status changes, installed activation, projection rebuild, broad content/Subject migration or legacy `archive/` migration occurred.
