---
atom_id: CA-P-2665
content_role: Plan
type: Plan
label: Epic
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Subject/Graph Node/Engineering
version: 11
updated_at: 2026-10-27 06:35:03 +0400
relations: {}
tier: 3
---
# Summary

Refine Engineering Subject branch

## Objective

Apply the latest approved Subject model, preserving source meaning and normal version history, then rebuild the Current Subject views.

## Details

### Decision authority

[Task P2667](CA-P-2665-EPIC--refine-engineering-subject-branch/done/02-CA-P-2667-TASK--settle-engineering-subject-structure.md) contains Candidate #9. Its latest Operator decisions supersede incompatible earlier candidates and placements. Keep the candidate in that Task rather than maintaining a second decision document.

Engineering becomes aspects-only. Implementation, Runtime and Carrier are direct Graph Node branches. Release belongs to Domain/Continuant/History. Git Commit, Git Branch, Pull Request, Git Index and the remote Git repository are Carriers. The full meaning and boundaries are recorded in P2667.

### Work order

1. Review Governs before Depends On, using Current sources and the supported corrections already prepared in Drafts.
2. Maintain one thin table: [Candidate #9 Subject changes](../../_projection/core-entity-review/presentation/candidate-9.subjects.md). Columns: Atom ID | old Subject | new Subject | status. Do not copy bodies, hashes or analysis reports into it.
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

### Applied result

Candidate #9 is applied: 1,350 existing Atoms updated and 35 new Definition Atoms. Two of those existing Atoms received final Definition-text corrections during completion audit, for 1,352 update events and 1,352 predecessor archives in total. The batch includes 20 ownership/carrier relocations. All 873 unselected Current source files remain byte-identical. All 1,387 actual source changes were appended to the Journal without invented Workflow Runs or earlier history.

The four regenerated views use 2,258 Current RMEDO sources: Core 819, Project Methodology 413 and Engine 1,026. Each view has primary Subjects, properties with inheritance, instances and exact dependency-only Subjects. No unmapped occurrences remain in these selected views. The broad inventory's 15 non-rooted occurrences are outside the selected RMEDO view and were not silently remapped.

Git Repository > Git Branch means containment. Both remain Carrier kinds. Engineering is aspects-only; Implementation, Runtime and Carrier are direct Graph Node branches. Release belongs to Domain/Continuant/History, and Version is Release.ID.

The thin table records Applied source changes. R1754's Extension-promotion feature remains deferred; this batch only normalizes its Subject classification. No production Tool, runtime or release execution is claimed. General content migration and wider Engine restructuring remain outside this completed batch.

Final completion audit corrected CA-R-2150@7 to describe the approved branches and removed the duplicate Semantics block in CA-R-1971@9. The final four views include those versions. Source identity/version/hash checks, predecessor reconstruction, release Workflow ownership and closure, thin-table application, exact dependency-only sets, and projection layout all passed. The thin table has 2,408 Applied rows and no pending Drafted rows. Generic Engineering-topic glossary Definitions were not added: the approved namespace Rule and existing source Semantics remain sufficient. No unresolved decision remains within this Epic's scope.

P2639 remains Done for its earlier bounded FPF work. P2637 consumes this accepted model in the wider Engine work.

## Definition of Done

- Candidate #9 and its missing definitions are represented by accepted source Atoms.
- Affected Subjects are migrated or have explicit unresolved Operator decisions; no unsupported mapping is silently applied.
- Current successors and predecessor archives match the reviewed batch; unrelated work is preserved.
- Four rebuilt views cite actual Current sources and versions and retain the dependency-only section.
- No code, runtime or broader migration completion is inferred from these methodology changes.
