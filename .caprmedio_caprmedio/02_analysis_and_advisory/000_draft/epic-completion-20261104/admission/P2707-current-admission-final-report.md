# P2707 Current carrier-admission final report

Date: 2026-11-04

## Result

`VALIDATE_ATOMS` now selects Current D657 independently of retired D274/D482,
normalizes only equal legacy aliases for reading, rejects alias conflicts, and
keeps Current-only semantics fail-closed.  The live Current context resolves
20 of 20 obligations with no authority gaps.

The Current registry entry is bound to:

- Atom: `CA-D-657`
- Version: `4`
- SHA-256: `6604d4753f9373babb1e30ecf1ecf362890c312122015ccdb192717e16f7f26f`

The Current Role domain is derived from, and carries exact bindings for, the
eight active Current `R/Declaration` carriers:

- `CA-R-2463`, `CA-R-2509`, `CA-R-2511`, `CA-R-2512`, `CA-R-2513`,
  `CA-R-2514`, `CA-R-2515`, and `CA-R-2637`.

The validator does not duplicate those Role values in production code.  It
requires eight distinct exact declarations, rejects a changed, missing,
duplicate, projected, Draft, wrong-role/form, forms-only, or non-Atom-Role
candidate, and fails closed when that set is incomplete.

## Remaining explicit scope gap

`current_scope_unit` and `claim_target_scope_unit` remain compatibility data
under D657.  Their retention/removal/consistency contract has not been
selected, so a Current carrier carrying either field records an unresolved
migration-disposition gap.  This lane did not infer Scope from a directory,
or use either value as a fallback.

## Owned staged-file inventory

All pre-existing files below were clean at this lane's baseline (`HEAD`);
there were no pre-existing dirty files in this owned validator/test surface.
The sole new file is identified explicitly.  Unrelated Workbench/MCP changes
are outside this inventory and must remain unstaged by this lane.

| Path | Baseline state | Purpose |
| --- | --- | --- |
| `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/VALIDATE_ATOMS/validate_atoms_workers/authority.py` | clean `HEAD` | D657 conditional closure and exact derived Current Role-domain obligation |
| `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/VALIDATE_ATOMS/validate_atoms_workers/check_context_extended.py` | clean `HEAD` | Current Plan confidence-field selection |
| `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/VALIDATE_ATOMS/validate_atoms_workers/check_domains.py` | clean `HEAD` | Current Plan confidence override field |
| `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/VALIDATE_ATOMS/validate_atoms_workers/check_fields.py` | clean `HEAD` | D657 profile, role/form, author prohibition, scope compatibility, Subjects |
| `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/VALIDATE_ATOMS/validate_atoms_workers/check_schema_extended.py` | clean `HEAD` | Current property admission, Role domain use, canonical AI confidence field |
| `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/VALIDATE_ATOMS/validate_atoms_workers/checks.py` | clean `HEAD` | alias-read view and conflict diagnostic boundary |
| `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/VALIDATE_ATOMS/validate_atoms_workers/proposed_carrier.py` | clean `HEAD` | D657 source closure and exact Role-declaration discovery |
| `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/VALIDATE_ATOMS/validate_atoms_workers/registry.json` | clean `HEAD` | D657 v4 pin and retired D274 disposition |
| `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/VALIDATE_ATOMS/validate_atoms_workers/registry_refresh.py` | clean `HEAD` | reviewed D657 refresh allowlist |
| `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/VALIDATE_ATOMS/tests/test_current_frontmatter_encoding.py` | clean `HEAD` | D657 role/form, no-author, scope, and closure tests |
| `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/VALIDATE_ATOMS/tests/test_current_type_admission.py` | clean `HEAD` | exact Current Role-declaration and fail-closed tests |
| `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/VALIDATE_ATOMS/tests/test_proposed_carrier_admission_regressions.py` | clean `HEAD` | shared legacy fixture binds explicit D276/D274/D482 historical closure |
| `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/VALIDATE_ATOMS/tests/fixtures/current_encoding_d657_proposed.md` | new | reviewed D657 fixture for focused Current admission tests |

No Current methodology carrier and no Git state was modified by this lane.
