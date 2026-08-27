---
atom_id: CA-E-378
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - installed-python-runtime
  depends_on:
    continuant:
      - PROGRAMMATIC
version: 1
updated_at: 2026-08-27 15:55:57 +0400
relations:
  evaluation_for:
    - CA-M-221
  derived_from:
    - CA-A-053
---
# Run an installed Tool without uv

## Claim checked

One installed CAPRMEDIO Tool executes from `.caprmedio_install` without uv, a
project virtual environment, or another dependency outside the installation.

## Test case

Invoke one installed Tool in a clean process where uv and the project virtual
environment are unavailable.

## Acceptance criteria

Pass only when the Tool reaches its declared entry boundary using solely its
installed carrier and admitted host prerequisites.

## Failure disposition

Reject the installed-runtime claim until the external workflow dependency is
removed.
