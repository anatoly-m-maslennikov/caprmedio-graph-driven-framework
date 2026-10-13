# Proposed-carrier admission — bounded correction

Derived implementation receipt, 2026-10-13. This is not authority, a new FPF report, or full source/runtime acceptance.

## Decisions and scope

Keep PyYAML and targeted Markdown/frontmatter edits. No new Markdown/YAML dependency. The Operator approved fixing reference filtering and implicit Project context before TOMLKit implementation. No source Atom normalization, Core migration, installed activation, or dependency change was performed.

Reference lookup now filters by explicit carried ID before requiring the selected target's Status and Version. It does not infer identity from filenames. Requested targets, discovered Plan parents, malformed/unsafe inputs, duplicate identities, archive-only targets, read bounds and source currentness remain strict.

Complete-carrier validation now retains the actual selected Project Settings/Structure context. The implicit Project is not a synthetic Scope Unit row. Project-owned carriers must be in their own content-role subtree, outside declared Scope Unit authority paths. A Project name duplicated by a declared Scope Unit is refused. Settings/Structure changes and foreign ambient selections cannot silently change the captured context. Project-role subtrees also enter the finite reference inventory.

These repairs implement existing M316/D441/D482/D276 obligations; they do not add a new policy. Different-owner/target admission still requires its separate supported authority.

## Frozen implementation and tests

Paths below are relative to `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/`.

| File | SHA-256 |
| --- | --- |
| `VALIDATE_ATOMS/validate_atoms_workers/proposed_references.py` | `d93a81eb1aab826f8df5dd349043fafbfa024b0178b80a0120e726ffd49a748d` |
| `VALIDATE_ATOMS/validate_atoms_workers/proposed_carrier.py` | `00122dfc20f5e144407200aeb06ca37a20ff9e9e4f3ca5658c35bc0ed56ab573` |
| `VALIDATE_ATOMS/validate_atoms_workers/check_structure_extended.py` | `0bb4d7125fdbbcfc7619ce2174dac03a58998c8d0a75b1b74ca84da78178076a` |
| `VALIDATE_ATOMS/tests/test_proposed_carrier_admission_regressions.py` | `e1c2325f3d824d5edf1a5b245ed0653eede771a4b5f8d966f104dbd1fa54dc63` |
| `tests/test_selected_atom_lifecycle.py` | `2fbd35968ce0a21d3783704a08b16bc6b84c936fddff03a48184b110b84ca26d` |

## Checks

Independent final review: PASS for the three production-file pins and bounded P2311–P2313 closure only. The reviewer found the Project/Scope Unit name collision, verified its correction and regression, and retained all source-admission limits below.

- Independent regressions: 14 PASS. Actual old-module failures were reproduced before acceptance; the name-collision regression also fails against the authenticated pre-guard implementation. Literal file snapshots check that validation does not mutate fixtures.
- Existing reference-inventory controls: 9 PASS. Existing structure adapters: 31 PASS.
- Final complete validator suite: 272 run, 270 PASS, 2 pre-existing graph-authority refresh failures. Unchanged refresh roots still point to the old methodology location; CA-D-268 is already pinned in the new location. Confirmed against HEAD `f4f463ba50e3e50d185a67478f9f9011dce6790d`.
- Selected lifecycle: 30 PASS after adding complete explicit Settings to its fixture. No assertions were weakened.
- Combined lifecycle/preflight: 34 run, 32 PASS, 2 pre-existing snapshot failures from persistent selector lock creation before preflight. Both reproduce with the changed validator modules loaded from immutable HEAD. No fixture warming hides the side effect.
- Seven separate proposed-relation integration tests stop in unchanged fixture setup (`25 != 26` authority count). They do not provide acceptance evidence.
- The MCP selected-context caller test could not run offline because pinned `mcp==2.3.0` is not cached. No environment or dependency files were changed. Pinned Ruff is also unavailable offline.
- Diff whitespace check passed. No live publication was attempted.

Runner: offline `uv run --no-project --python 3.14 --with PyYAML==6.0.3 --with pydantic==2.13.5 python -m unittest`; cache, temporary files and bytecode are under `.caprmedio_tmp`. Validator discovery used `VALIDATE_ATOMS/tests/test_*.py`; lifecycle checks used `test_selected_atom_lifecycle` and `test_lifecycle_complete_carrier_preflight`.

## Actual source admission remains blocked

Complete new-carrier checks for M383, D632, E635, P2307 v2 and P2311–P2313 v1 all now reach the Project reference frontier, then refuse this existing non-Atom document:

These are pre-closure Plan snapshots; the later Done v2 Tasks and parent result/link edits are not claimed to have passed full admission. Checked Plan SHA-256 values: P2307 `086c411bc4c71fc4d11be05828a3488ddefcb3cdb7d41af0c25b8a77affd1176`; P2311 `4bd1babc108e1e193234dd7b869926aac85a3f30e5b1159faabddd8d2bdaf8a1`; P2312 `2955552918e4c1f2cc5604423826480fd4b94318fbd202b0e1769005174564a1`; P2313 `b006a543adb60e0fb3ccc2e090d5a9666918e1a07762180cf8ed142b421db69a`.

`.caprmedio_caprmedio/03_plan/12-CA-Epic-009-caprmedio-new-ops-migration/execution_evidence/CA-Epic-015-pre-execution-review.md`

It has no supported Atom frontmatter. The current inventory parses every discovered Markdown carrier in the admitted subtree. This receipt does not silently classify that document, exclude arbitrary directories, or relax malformed-Atom checks. An explicit distinction between non-Atom documents and malformed Atoms remains to be decided.

Separately, requested source Atoms M110, M281 and D250 lack explicit carried identity/Status metadata. They must not be made admissible through filename inference. No full reference-admission PASS is claimed, and further blockers can remain behind the first refusal.

P2307 and TOMLKit implementation remain open. The bounded validator work does not close G002 (complete source admission) or G003 (implementation evidence).
