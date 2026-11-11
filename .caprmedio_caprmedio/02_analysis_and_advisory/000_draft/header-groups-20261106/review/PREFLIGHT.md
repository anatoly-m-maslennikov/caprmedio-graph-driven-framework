# Post-cutover readback preflight

`verify_application.py` is deliberately not runnable until the root-owned cutover has created `integration/adoption-plan.json` and `integration/adoption-receipt.json`. The existing `integration/rehearsal.json` is rehearsal evidence only and must not be substituted.

From the repository root, after the root owner has completed the authorized cutover, run:

```bash
./.venv/bin/python .caprmedio_caprmedio/02_analysis/draft/header-groups-20261106/review/verify_application.py
```

The script reads all planned postimages and writes only `review/application-verification.json`. It does not invoke the adopter, reserve identities, edit native sources, start runtime services, run test suites, or use Git.
