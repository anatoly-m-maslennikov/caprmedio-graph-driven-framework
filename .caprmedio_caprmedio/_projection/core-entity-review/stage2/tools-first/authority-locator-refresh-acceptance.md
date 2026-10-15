# Complete-carrier validation: authority locator refresh

Derived verification record, 2026-10-12. This is not migration approval or a source Atom.

## Change

Corrected 20 `source_path` values across the validator's `registry.json`,
`graph_authority.json`, `structure_authority.json`, and `context_authority.json`.
The 18 distinct rule sources retain their exact IDs, versions and hashes.
No source Atom, obligation, validator behavior or other manifest value changed.

## Checks

- Producer: 80 UPDATE tests and the shared canonical graph-tuple test passed.
- Independent verifier: each changed file equals its prior bytes with only the
  approved path substitutions; all 18 pinned sources resolve unchanged.
- Real complete-carrier validation of canonical `CA-R-728` passed all 12 checks.
- Public preview still rejects a competing current `CA-R-728` copy with
  `subject-identity-duplicate`. No staging export or source write occurred.

## Evidence

Local scratch records under `.caprmedio_tmp/stage2-migration-20261012/validation-audit/`:

- `proposed-authority-locator-relocation.json`:
  `2d043b1cb634dbb8ccf8fbc102f9c0eb07b82819b5c118479b5da589920868f0`.
- `authority-locator-refresh-acceptance.json`:
  `4fe251e346a850b7713e1686afe39a206b89a5a8a26e209984142ea85aec9d08`.

This bounded refresh does not claim that broader graph-authority manifests or
all validation modes are current. Identity checks remain enabled.
