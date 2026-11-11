# P2707 Current carrier-admission test receipt

Date: 2026-11-04

## Live authority receipt

The live selected Project context returned:

```text
base_authority=20/20/0 gaps=0
role_bindings=CA-R-2463,CA-R-2509,CA-R-2511,CA-R-2512,CA-R-2513,CA-R-2514,CA-R-2515,CA-R-2637
```

The D657 registry refresh matched the observed Current carrier exactly:

```text
registry=4:6604d4753f9373babb1e30ecf1ecf362890c312122015ccdb192717e16f7f26f
observed=4:6604d4753f9373babb1e30ecf1ecf362890c312122015ccdb192717e16f7f26f
match=True
```

The active D657 carrier produced zero findings and no Role-domain gap.  Its
only Current-encoding gaps are the two intentionally unresolved scope
compatibility fields.

## Commands and results

```text
PYTHONPATH=... .venv/bin/python -m unittest discover \
  -s LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/VALIDATE_ATOMS/tests -q

Ran 588 tests in 87.179s
OK
```

Focused checks passed before the complete run:

- 48 Current/admission tests;
- 23 proposed-carrier/alias tests;
- 65 authority/schema/current-rule tests.

Static verification passed:

```text
ruff check --select E4,E7,E9,F [changed production modules and Current-role test]
python -m py_compile [changed production modules]
git diff --check -- [VALIDATE_ATOMS]
```

No verifier was skipped.
