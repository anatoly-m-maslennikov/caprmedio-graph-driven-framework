# Nested Header validation implementation evidence

Implementation and local functional evidence only. Live Atom carriers, model sources, prepared source packet originals, runtime activation and deployment were not changed by this validation lane.

## Boundaries implemented

- `ParsedCarrier.metadata` remains the actual raw YAML mapping. Selection, reports, source bindings and reference records use a separate read compatibility view.
- The nested schema validates declared base groups, immediate child paths, nonempty mappings, integer versus boolean values, Role-specific Context paths, Priority, Plan confidence and work sequence values, Topics, destination shape and canonical group order. Unknown nested fields and Role/Form groups are not admitted by their presence.
- Timestamp quote validation inspects the original `state.updated_at` YAML scalar node. Safe YAML protections and historical flat readers remain intact.
- Container resolution accepts `context.container`, resolves the same bounded Scope Unit/Plan chain, and rejects disagreement with a retained containment alias. Reviewed Header.Context selector spellings are checked against extracted source constraints.
- Current Role/Form Declaration coordinates can be resolved from complete selectors. Historical Entity Definition coordinates remain supported.
- The approved nested D657 contract is bound to an exact full-body digest copied from the prepared packet. Other arbitrary evolved D657 contracts are not admitted. Reviewed D378 and containment source bodies have explicit finite seals in addition to retained historical byte pins. Independently copied new fixtures do not modify the retained frozen oracle.

## Existing-write preservation API

`CarrierPredecessor(path, sha256, identity_transition=None)` is an internal operation-established predecessor pin. `validate_proposed_carrier(..., predecessor=...)` and `CarrierValidationScope.validate(..., predecessor=...)` re-read its actual bytes using the bound reader, verify its digest, enforce the selected control-root boundary and reject frozen archive paths or generated projections.

Only exact type/value-preserving root residue may pass under this capability. Changed, deleted or newly introduced residue is refused. The optional identity transition is an exact before/after pair supplied by the owning verified lifecycle operation; it is rechecked against the actual predecessor and proposed identities and Role. This preserves accepted legacy Plan Priority values without admitting new Plan Priority fields. Retained scope fields never supply Container ownership.

## Focused local evidence

- New nested schema/admission/public-command/predecessor tests: **15 passed**. The source closure is regrouped as nested Headers while its bodies remain independently retained. Public-command checks assert an independently specified report identity spine, its expected incomplete coverage outcome, exit code and unchanged whole-fixture fingerprint.
- Existing Current frontmatter tests: **8 passed**.
- Existing schema tests: **41 passed**.
- Existing public-command golden tests: **28 passed**, with retained expected reports and frozen authority bytes unchanged.
- New schema module and focused tests pass Ruff; the modified validation tree passes non-complexity Ruff checks. Remaining complexity findings are inherited functions, with historical dispatch split where needed to avoid adding new complexity findings.
- The new nested schema module passes direct Mypy. The documented whole-tree Mypy command stops at existing duplicate imports of the same modules under `validate_atoms_workers` and `VALIDATE_ATOMS.validate_atoms_workers`.
- Exact copied D657, D378, R2508 and R2511 reviewed bodies were rechecked against the current prepared packet after implementation; they still match.

## Original baseline failures

A read-only `git archive HEAD` snapshot reproduced both original failing groups independently of these changes:

- `test_draft_marker_formats_golden.py`: 11 tests, 12 existing complete-carrier admission errors from the D276/D378 fixture mismatch.
- `test_current_type_admission.py`: 9 tests, 1 failure and 1 error from legacy-project fixtures switching to Current encoding without the already-required containment authority closure.

The original oracle was not changed to hide those failures. The completed baseline snapshot is retained under `.caprmedio_tmp/header-groups-20261106/head-baseline/`; no baseline process remains running.

No full repository suite, live source cutover, runtime loading, image build, release or deployment was claimed by this lane.
