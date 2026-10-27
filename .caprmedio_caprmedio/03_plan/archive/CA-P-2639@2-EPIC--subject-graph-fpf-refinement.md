---
atom_id: CA-P-2639@2
content_role: Plan
type: Plan
label: Epic
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject
version: 2
updated_at: 2026-10-26 04:51:47 +0400
relations: {}
tier: 3
---
# Summary

Subject graph FPF refinement

## Objective

Resolve the Subject Graph content review with the Operator, one question at a
time. Turn accepted decisions into bounded child Tasks, then correct the source
Atoms and rebuild the affected Subject views.

## Details

### Starting point

The FPF alignment audit of 2026-10-26 found eight open issues in the Current
RMEDO Subject Graph and its governing sources. The reviewed projection is
[CA-PROJ-009](../_projection/CA-PROJ-009-CAPRMEDIO--Subject-Graph--Current-RMEDO.md),
recorded rebuild 2026-10-26 02:53:08 +0400, with 2,238 sources.

The audit inspected selected source bodies, not every source body. Its findings
and suggested repairs are not approved model changes. Current sources must be
read again before a Task changes them. Latest explicit Operator decisions win.

### Findings to resolve

| ID | Issue and source leads | State |
|---|---|---|
| I01 | R1994@8 limits Graph Nodes to Continuant/Occurrent, while R2006@7 admits abstract topics. R1275@24 defines Subject as the link rather than its target. | Subject/link distinction decided; P2640 created; temporal classification open |
| I02 | D651@5/D652@7 use Carrier/Filename/Atom.Tier; D525@11 places persistent-state Carrier under Runtime. Check kind, property and representation meanings. | Awaiting Operator |
| I03 | R2001@9/R1269@23 exclude Claim for Graph Rules, while R2150@4/M232@24 describe additive inheritance without the applicability exception. | Awaiting Operator |
| I04 | R2003@7/R2149@7 operative Graph Rule YAML and R1997@10/D637@17 examples retain retired root paths. | Awaiting Operator |
| I05 | D478@20/D480@15/D485@14 still govern Atom.Property; R1454@22 references Atom.Substance; O045@15 retains Atom.Atom/Tier. | Awaiting Operator |
| I06 | R1617@13 treats derivation-evidence classification as a Relation Type; R1653@24 admits imprecise related_to. | Awaiting Operator |
| I07 | R1989@9 and R868@25 disagree about archived Status, Version and Updated At. Distinguish an update predecessor from standalone archival. | Awaiting Operator |
| I08 | R1564@17/R1565@14 retain Actor as an Operations Type alongside Workflow, Step and Action. Preserve real participation policies when resolving it. | Awaiting Operator |

The corresponding FPF proposals F01–F08 remain proposals. Do not infer approval
from this queue or turn a classification repair into deletion of useful rules.

### Decision process

1. Ask one question with the conflicting source meanings, a proposed resolution,
   and its blast radius. Start with I01, because it affects every later mapping.
2. Record the Operator's answer here. Do not ask again where the latest answer
   already resolves a later issue.
3. Create child Task Atoms from accepted decisions. Each has a bounded source
   set, preserved obligations, dependencies and a checkable completion condition.
   Split own work into at most 15-minute Tasks where practical.
4. Track each issue as decided, tasked, applied and verified. A decision or
   Draft alone is not an applied correction.
5. After the accepted source corrections, rebuild affected views and check the
   specific findings and affected neighbors. Do not restart a general audit.

### Open questions and evidence gaps

- Q01 / G01: Subject/link distinction decided below; implementation tracked by
  P2640, not yet applied to governing definitions.
- Q02 / I01: the remaining Graph Node question is whether abstract topics need
  any Continuant/Occurrent classification. Ask next; the Operator's Q01 answer
  did not explicitly settle that part.
- G02: clarify standalone retirement versus preserving an update predecessor
  before changing the archive contracts.
- G03: perform bounded consumer lookup for the approved fixes, especially old
  Depends On references, relation metadata and participation policies. The
  audit did not establish complete affected-source coverage.

### Accepted decisions

D01 — Subject and its links, accepted 2026-10-26:

- Subject names the thing or topic an Atom governs or depends on.
- GOVERNS / DEPENDS_ON are the links, not the Subjects themselves.
- The whole set of Subjects forms a graph. The Atom's GOVERNS / DEPENDS_ON
  entries are special relations from that Atom to nodes in the Subject graph.
- This distinction does not create another intermediate Subject object, grant
  those links authority precedence, or decide temporal classification.

The Operator authorized direct Plan edits. Create tasks from these decisions;
source-model corrections and projection rebuilds are not yet performed.

### Child Tasks

- [CA-P-2640 — Align Subject and Subject-link definitions](CA-P-2639-EPIC--subject-graph-fpf-refinement/01-CA-P-2640-TASK--align-subject-and-subject-link-definitions.md):
  Active, not executed. Implements D01 only. The remaining temporal distinction
  and all other findings await their own decisions.

### Boundaries

- This is source-model refinement, not renderer, tool, code, runtime, test-suite,
  MCP, deployment or release implementation.
- Core, Project Configuration and affected Engine RMEDO source contracts are
  candidates only where the accepted findings require them. Do not expand into
  unrelated migration or introduce new Domain entities without the Operator.
- Terms Graph implementation stays deferred. The separate child_of/parent_of
  replacement Epic remains separate; coordinate overlapping sources, do not
  absorb its whole migration.
- Preserve existing Drafts, Archives and unrelated changes. Later approved
  Current updates create normal predecessor archives under the agreed lifecycle.
- No source correction, projection rebuild, commit or push has occurred merely
  by creating this Epic.

## Definition of Done

- Every I01–I08 finding has an explicit Operator disposition and a recorded
  outcome; deferred work is not reported fixed.
- Accepted repairs have child Tasks with bounded scope and completion evidence.
- The accepted source definitions, Subjects, operative YAML and affected
  consumers agree; useful obligations remain intact.
- Rebuilt derived views reflect the corrected Current sources. Targeted checks
  close the accepted findings without claiming a review of all source bodies.
- No unapproved taxonomy, Terms Graph work or runtime implementation is added.
