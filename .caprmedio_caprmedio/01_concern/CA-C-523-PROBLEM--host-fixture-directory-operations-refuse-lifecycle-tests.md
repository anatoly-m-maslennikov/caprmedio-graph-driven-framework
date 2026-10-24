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
version: 5
updated_at: 2026-10-23 03:14:50 +0400
subjects:
  governs: Atom/Status
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Engineering/Test Isolation/Fixture Directory
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
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

Host concurrency verification also failed closed while opening the runtime identity lock: FileNotFoundError/ENOENT from os.open with O_CREAT|O_RDWR|O_NOFOLLOW and a valid parent dir_fd. Native-independent raw OS probes reproduced it: 7/12 fresh directory chains using only the safe-parent helper; direct mkdir/openat/close probes failed 5/8 fresh-parent and 5/8 precreated-parent workspace roots, and 3/8 fresh-parent and 5/8 precreated-parent /private/tmp roots. In failed probes the parent FD was valid, st_nlink was 3, its inode matched the existing physical parent, and identity.lock existed. This does not establish the underlying OS/interposition cause. No Atom, schema, history or flock operation was needed for that reproduction; no retry or host-specific workaround was added.

The final native lock code separately passed all four concurrency/interruption tests in disposable Linux (4.268 seconds; image sha256:0fac136ec9661a8884cbdcf53e0b7da34f5bc24506b71b6d452bc934c8df80a3). The incomplete-Journal connected journey passed on that image in 46.038 seconds. These do not turn the failed host runs into passes.

All 24 native Status-bundle publication/recovery tests passed in disposable Linux storage (37.333 seconds; image sha256:06f569d811bbf1b26e06766897d2588cb8e5a613fe99f9fe8f79cb7e05a0c0fc). The connected incomplete-Journal journey also passed (45.346 seconds). These observed results verify those paths independently; they do not resolve or explain the host restriction. No fixture was force-deleted and no atomicity assertion was weakened.
