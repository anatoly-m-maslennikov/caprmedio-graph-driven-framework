# Candidate #6 — Subjects-only migration result

Date: 2026-10-16. Status: supported batch completed; full Candidate #6 remains incomplete.

## Applied

- Existing MCP batch workflow: `subjects-candidate6-20261016-001`.
- Source checkpoint: `38328edef2a937498ead4996e6be112b5326f4ac`.
- Draft checkpoint: `d1a6b7b5f` (198 exact edit drafts).
- 198 source Atoms updated through 260 Subject patches, including 33 redundant dependency removals.
- 198 exact predecessors archived; 198 edit drafts consumed; Version incremented once per Atom.
- Independent readback passed: bodies and unrelated metadata unchanged; 796 other pre-existing Core Markdown files unchanged.
- Native completion reports 198/198, zero remaining, and no recording errors.
- Rebuilt [current source-derived graph](../../../../core-subject-notation/after-current/inherency.md); all 198 new source versions are present among its 990 sources. Unmapped names remain visible.

## Not applied

Of 990 current source Atoms, 708 were explicitly held and 84 needed no change. [Exclusions](exclusions.json) retain the per-Atom reasons: deferred C/A or content, Terms handling, named-instance qualifiers that the existing Subject field cannot preserve, uncompiled removal dispositions and unresolved mappings. These are not silently treated as migrated.

No content rewrite, Core/Project Configuration relocation, new R definition, source retirement, runtime implementation change, release or push. Missing R definitions did not block this approved Subjects-first batch; coverage remains later work.

## Execution note

The final Git commit was not created: an existing `.git/index.lock` blocked staging. The lock was left untouched. The source and draft checkpoints remain committed; the completed migration and evidence are currently local working-tree changes. No push was attempted.

MCP initially queued the batch without a live project worker. The existing worker was started inside the same live MCP container. The queue contained only this run. It consumed the already-queued request; the migration was not resubmitted. The separate test containers were left untouched.

Evidence: [prepared targets](prepared-targets.json), [preview response](preview-response.json), [readback](readback.json), and native progress at `.caprmedio_install/workflow_orchestrator/runs/subjects-candidate6-20261016-001/subject_batch_progress.json`.
