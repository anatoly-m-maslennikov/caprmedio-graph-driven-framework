# Preview and graph verification

2026-10-12. Non-authoritative implementation evidence for CA-P-2175 and CA-P-2176.

## Subject preview

Independent code review: `tools_first_verifier` (GPT-6.1 Sol, xhigh), PASS after the duplicate-original and same-path currentness gaps were fixed. Production `atom_subject_patch.py` SHA-256: `cc67263b7e91650c42e95a7bd933b8af45b03f072176bdfd0e81e7f8391c01e4`. Independent fixture `test_nonarchived_subject_preview.py` SHA-256: `089c2015dc678f14b036f0eb8cd4a94c749c497604ba2c248f72e30617306a0e`.

Root reran the complete ATOM_UPDATE directory: **49 tests passed**. The 14 new real-validator tests cover valid non-Active originals, unchanged Status/unrelated bytes, no-op, archived/Draft rejection, invalid role/status placement, stale pins, duplicate originals outside the request, archived predecessors, malformed competing claims, directory symlinks, candidate insertion and same-path identity changes during the final inventory. The existing lookup default remains Active. The fixture source-path correction reads the current original Core location without changing disposable validation destinations or bypassing validation; its author also ran 30 selected-lifecycle and four carrier-preflight tests successfully.

These exact code/test changes were included by the concurrently running release task in commit `9a40b76e3`; this review neither evaluates nor takes ownership of its unrelated changes.

## Public graph profile

Commit `a8da9b50b`. Independent code review: `tools_first_verifier`, PASS. Root ran **245 graph tests and four MCP descriptor tests**, all passing. Approved-profile forwarding and grammar evidence are explicit; legacy/default semantic output remains compatible. Native admission is separate. Stale or aliased grammar evidence is refused before publication, including no-op publication.

## Boundary

These results close the bounded preview/graph implementation checks. They do not close the guarded Subject application implementation or the complete tools-first gate. No original Core Subject was migrated, and no live MCP runtime was activated by these checks. Later intent/materialization edits require their own verification; this document preserves the tested snapshot rather than claiming future code is accepted.
