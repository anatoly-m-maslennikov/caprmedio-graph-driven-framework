# Candidate #5 — Subjects migration outcome

Completed through the existing MCP batch workflow, Run `subjects-candidate5-20261015-001`.

- 750 Atoms migrated; 1,074 exact Subject patch operations.
- 750 predecessors archived byte-for-byte; 750 edit drafts promoted and consumed.
- Only Subjects, Version and Updated At changed. Summary, body, Status and all other metadata are unchanged.
- 228 Atoms required no supported change; five were held unchanged.
- 54 empty, unassigned R definition drafts remain in [empty-r-drafts](../empty-r-drafts/). They are review placeholders, not admitted definitions. Inherited properties and values reuse their parent definition; no duplicate descendant R drafts were created.

## Evidence

- Originals checkpoint: `9ef71f469b6d8b9d8dbc9a96661a9e11d7eb8152`.
- Edit-draft checkpoint: `82bcce370`.
- [Exact original packet](prepared-targets.json), [staging responses](staging/mcp-staging-responses.json), [successful preview](preview-response.json), [dispatch response](execute-response.json).
- [Independent final verification](verification-result.json): all 750 archive/current comparisons passed; all 233 untouched Atoms and 54 definition drafts preserved.
- Runtime progress: `.caprmedio_install/workflow_orchestrator/runs/subjects-candidate5-20261015-001/subject_batch_progress.json`: completed 750/750, remaining 0, no in-flight operation.

## Rebuilt graph

[Current Core Inherency graph](../../../core-subject-notation/after-current/inherency.md) rebuilt programmatically from current source files after promotion.

- 983 source Atoms, 4,865 Subject occurrences, 696 nodes, 277 edges.
- SHA-256: `209480b1bfbb63e5754707844b2ccc8d5a9ab3bfc1530afae650701d9950b523`.
- One existing diagnostic: CA-C-290 has no Subjects mapping.

## Still open

- R1563, R1570 and M305 have colliding Step aliases; D256 has colliding Carrier aliases. They were not silently deduplicated. C290 has no Subjects mapping. See [exclusions](exclusions.json).
- The 503 distinct unplaced Subject names remain unchanged, including where other Subjects in the same Atom migrated. The graph therefore still has names outside the Candidate #5 hierarchy.
- Missing R definitions and existing content conflicts remain for the separate content pass. Subject migration does not adopt or repair their meaning.
- The generic MCP status endpoint does not recognize this batch backend. The saved native progress and actual carrier readback establish completion; the execution was not resubmitted.

No code changes, runtime test suite, release or push were performed for this migration. Unrelated working-tree changes were preserved.
