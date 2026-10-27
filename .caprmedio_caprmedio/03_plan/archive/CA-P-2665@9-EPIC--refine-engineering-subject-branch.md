---
atom_id: CA-P-2665@9
content_role: Plan
type: Plan
label: Epic
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Engineering
version: 9
updated_at: 2026-10-27 04:47:08 +0400
relations: {}
tier: 3
---
# Summary

Refine Engineering Subject branch

## Objective

Apply the latest approved Subject model, preserving source meaning and normal version history, then rebuild the Current Subject views.

## Details

### Decision authority

[Task P2667](CA-P-2665-EPIC--refine-engineering-subject-branch/02-CA-P-2667-TASK--settle-engineering-subject-structure.md) contains Candidate #9. Its latest Operator decisions supersede incompatible earlier candidates and placements. Keep the candidate in that Task rather than maintaining a second decision document.

Engineering becomes aspects-only. Implementation, Runtime and Carrier are direct Graph Node branches. Release belongs to Domain/Continuant/History. Git Commit, Git Branch, Pull Request, Git Index and the remote Git repository are Carriers. The full meaning and boundaries are recorded in P2667.

### Work order

1. Review Governs before Depends On, using Current sources and the supported corrections already prepared in Drafts.
2. Maintain one thin table: [Candidate #9 Subject changes](../_projection/core-entity-review/presentation/candidate-9.subjects.md). Columns: Atom ID | old Subject | new Subject | status. Do not copy bodies, hashes or analysis reports into it.
3. Create or refine actual correction Drafts. Reuse existing R/Definition meanings and create missing Definition Drafts. Keep generic Core definitions in Core and technology-specific definitions in PROJECT_CONFIGURATION.
4. Review and apply the supported batch. Archive each Current predecessor and promote its accepted successor. Keep identity unless Summary or Content Role changes. Stop on failure and record actual progress.
5. Rebuild Core, Project Methodology, Engine and Full Current Subject views from the resulting source heads.

Ask one context-rich question when confidence is below 90%. Do not invent a new Domain kind to force a mapping. Preserve unrelated work and existing historical Drafts/Archives.

### Retained scope decisions

- Subject, Content Role and Local Scope Unit are independent. Topics do not copy Scope Unit or Tool identities.
- Workflow-specific Local Release/Public Release definitions and RMED belong in PROJECT_CONFIGURATION.
- R1752, R1753 and M260 govern Applicable Methodology Compilation; their Drafts belong in PROJECT_CONFIGURATION. R1754 Extension promotion remains deferred.
- Current source application, Draft preparation and projection generation are distinct states.
- No code, Tools, runtime, release execution, general Scope Unit reorganization or Terms Graph implementation is included. Broader content migration remains separate except for definitions required by Candidate #9.

### Projection

Keep the four sections: primary Subjects; properties with inheritance; instances; dependency-only Subjects. Dependency-only means exact values in Depends On absent from Governs within that view's own Current source set. List referring Atom IDs. Rooting alone does not prove semantic correctness.

### Progress

The preceding review prepared 675 selected Drafts and verified 2,223 Current source hashes without changing those heads. Candidate #9 now supersedes their earlier branch placements. Use actual Draft files and the new thin table to record the next batch; do not treat the earlier count as Candidate #9 completion.

P2639 remains Done for its earlier bounded FPF work. P2637 consumes this accepted model in the wider Engine work.

## Definition of Done

- Candidate #9 and its missing definitions are represented by accepted source Atoms.
- Affected Subjects are migrated or have explicit unresolved Operator decisions; no unsupported mapping is silently applied.
- Current successors and predecessor archives match the reviewed batch; unrelated work is preserved.
- Four rebuilt views cite actual Current sources and versions and retain the dependency-only section.
- No code, runtime or broader migration completion is inferred from these methodology changes.
