---
atom_id: CA-C-523
content_role: Concern
type: Problem
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: 2026-10-16 00:26:05 +0400
subjects:
  governs: Atom/Status
  depends_on:
  - Atom
  - Journal
  - Operator
relations:
  concern_about:
  - CA-P-2385
  - CA-P-2389
  - CA-C-520
---
# Summary

Host fixture directory operations refuse lifecycle tests

## Concern

Some fixture directory rename/removal operations fail with PermissionError before or during test cleanup, including when the functional assertions pass. This prevents counting those host module results as passed.

## Evidences

Observed during P2385 verification: a disposable _journal directory cannot rename to retained-journal; disposable TemporaryDirectory cleanup rmdir also returns Operation not permitted. The same errors persisted in /private/tmp, a fresh workspace TMPDIR, and a managed escalated test retry. Latest concrete workspace fixture root: .caprmedio_tmp/tests/ca-p-2385-wrappers.Vq2d6I; rename case tmpo_97l1li/.caprmedio_caprmedio/_journal; cleanup cases tmpiugp6zpe and tmptpnkd9sl. Observed directory modes drwx------, uid501/gid20, flags=- and no ACL entries; the underlying OS restriction is not established by this observation. New wrapper metadata/append assertions, selected_run_support7/7 and connector_plain_journal5/5 passed separately. Current C520 also records an earlier host atomic-directory rename restriction; that does not prove an identical root cause.

## Blast radius

Affected host permission/cleanup cases remain non-passing. Continue independent functional and connected checks; prefer existing isolated Linux test boundaries where available. Do not bypass required mutation atomicity, weaken assertions, force-delete fixtures, or infer success from an attempted call.

## Independent Linux verification

All 24 native Status-bundle publication/recovery tests passed in disposable Linux storage (37.333 seconds; image sha256:06f569d811bbf1b26e06766897d2588cb8e5a613fe99f9fe8f79cb7e05a0c0fc). The connected incomplete-Journal journey also passed (45.346 seconds). These observed results verify those paths independently; they do not resolve or explain the host restriction. No fixture was force-deleted and no atomicity assertion was weakened.
