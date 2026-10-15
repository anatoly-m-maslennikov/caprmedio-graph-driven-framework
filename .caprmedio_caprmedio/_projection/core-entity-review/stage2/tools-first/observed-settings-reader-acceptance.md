# Observed Settings reader acceptance — 2026-10-13

Derived acceptance receipt for P2350/P2351, after P2348/P2349 source acceptance. No live Journal registration.

The existing graph reader now validates registered schema-3 completed changes and observed recovered-state records. It requires selected Project name, exact Carrier filename/path, current digest, positive Revision and the admitted observation fields. Missing, malformed, stale, mismatched or duplicate evidence cannot resolve a current binding. The independent suite found a direct-call stale-digest bug; the final reader compares the supplied digest with the actual current Carrier and refuses unavailable Carriers.

All 46 graph-generator tests passed. Independent verification includes nine test methods and 195 subtests using actual canonical records appended by the existing Journal writer in isolated test trees, not validation bypasses. Tests cover both Settings identities, completed/recovered forms, exact receipt references, tampering, malformed types, wrong Project/path/digest, invalid Revisions, ambiguity, drift, absent files and unchanged reader inputs.

| File | SHA-256 |
|---|---|
| GENERATE_PROJECT_GRAPH_STATE/generate_project_graph_state.py | `3641ce9ae898fb5d9878e2a54908ce40af3a6f6832a684db811e05e8aca72c44` |
| tests/test_settings_binding_identity_independent.py | `e795095ea88f92eb2f6f20573fd3e93b853c15bf8c4896e2021a657c35383857` |
| tests/test_generate_project_graph_state.py | `0b730617a7ee93069198c8e0e92783c18b7f9899c28da7d4a84222baa77ea3e7` |
| tests/test_observed_settings_binding_independent.py | `21fd44e8af72632d1c5e735d9c803abd97a8914c91c5c7e4d7c9d8e57234c807` |

Paths are relative to the existing GENERATE_PROJECT_GRAPH_STATE Tool except where its directory is shown. Tests use offline Python 3.14 with pinned project test dependencies and scratch under .caprmedio_tmp. Settings and live Journal were not edited. This does not provide an advertised live registration route, whole Settings schema validation, runtime activation or Epic completion.
