---
atom_id: CA-P-2498
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2494]
version: 2
updated_at: "2026-10-20T21:45:26.971Z"
---
# Summary

Freeze current container lifecycle fixture

## Objective

Prepare current-source synthetic selected-execution data without live source fixtures.

## Details

At most 15 minutes own work; split before extending. Own only a new container lifecycle fixture helper and its frozen test-data directory under APP tests. Reuse existing containment/lifecycle fixtures and source-pinned selected graph build helpers. Existing selected-lifecycle corpus has older O127/O128/O029 paths and Versions; do not rewrite that legacy corpus or read mutable live Atoms during tests. Freeze exact current originals and required directly bound graph/model closure, verify declared hashes at materialization, and return the ready public-fixture interface. Actual caller assertions wait for reviewed implementation interface.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.

### Reviewed correction before acceptance

Initial fixture self-check passed, but P2498 is NOT Done: code review found live authority/projection reads in fixture preparation. C553 requires frozen source bytes plus closed route-shape JSON in the dedicated checked-in corpus; test execution may read only that corpus and disposable Project data. Current original O127@15/O128@15/O129@12/O029@10 bytes may be harvested once during authoring, not dynamically located or refreshed in runtime tests. Existing validator golden closure may be reused without mutation. Re-run self-check and an isolation regression before P2495 uses the fixture.
