---
atom_id: CA-P-2639@7
content_role: Plan
type: Plan
label: Epic
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject
version: 7
updated_at: 2026-10-26 05:11:58 +0400
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
| I01 | R1994@8 limits Graph Nodes to Continuant/Occurrent, while R2006@7 admits abstract topics. R1275@24 defines Subject as the link rather than its target. | Decided; P2640 and P2641 created; not applied |
| I02 | D651@5/D652@7 use Carrier/Filename/Atom.Tier; D525@11 places persistent-state Carrier under Runtime. Check kind, property and representation meanings. | Awaiting Operator |
| I03 | R2001@9/R1269@23 exclude Claim for Graph Rules, while R2150@4/M232@24 describe additive inheritance without the applicability exception. | Decided by D03/D04; P2642 and P2643 created; not applied |
| I04 | R2003@7/R2149@7 operative Graph Rule YAML and R1997@10/D637@17 examples retain retired root paths. | Awaiting Operator |
| I05 | D478@20/D480@15/D485@14 still govern Atom.Property; R1454@22 references Atom.Substance; O045@15 retains Atom.Atom/Tier. | Awaiting Operator |
| I06 | R1617@13 treats derivation-evidence classification as a Relation Type; R1653@24 admits imprecise related_to. | Relation-type derivation decided (D06); P2645 created; R1617 disposition and related_to still open |
| I07 | R1989@9 and R868@25 disagree about archived Status, Version and Updated At. Distinguish an update predecessor from standalone archival. | Version decision accepted (D05); P2644 created; not applied |
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
- Q02 / I01: decided by D02. Continuant, Occurrent and Aspect are permitted,
  and the category list is open. P2641 tracks source alignment, not yet applied.
- Q03 / I03 and Q04: resolved for this refinement by D04. Every RMED Atom has
  a logical Claim; its representation is not fixed universally. Formal Claims
  may be carried by an Atom or Governing Configuration. No forced conversion
  or test based on the presence of a Semantics section is authorized.
- Q05 / G02: resolved by D05. Standalone archival preserves the existing
  Version; do not create a new Version merely to archive it. P2644 tracks
  alignment with the already-agreed update-predecessor behavior.
- Q06 / I06: D06 records derivation as a relation between Relation Type
  instances. P2645 tracks it. Ask whether to retire R1617's old classification
  after preserving any still-needed meaning; do not assume the answer for
  inference/observation categories. The imprecise related_to kind remains a
  separate part of I06.
- G03: perform bounded consumer lookup for the approved fixes, especially old
  Depends On references, relation metadata and participation policies. The
  audit did not establish complete affected-source coverage.

### Accepted decisions

D01 — Subject definition, accepted and clarified 2026-10-26:

Subject names the thing or topic an Atom governs or depends on.

That sentence is the definition. GOVERNS / DEPENDS_ON are connected relations,
not part of the Subject definition. Define those relations in separate Atoms
that depend_on the Subject-definition Atom. The whole set of Subjects forms
another graph; those special relations connect Atoms to its nodes.

D02 — Open Graph Node categories, accepted 2026-10-26:

A Graph Node can be Continuant, Occurrent or Aspect. This list is open under
the framework's expandability principle; it is not an exhaustive three-value
enumeration. Do not force every Subject into Continuant or Occurrent, invent
new categories for existing topics, or remap all topics under a new Aspect
path merely from this decision.

D03 — Graph Rule Claim, accepted 2026-10-26:

Graph Rules have a Claim, carried in the YAML part. Absence of a Markdown
Claim section does not mean the logical Claim is absent. This supersedes the
review's proposed no-Claim inheritance exception. D04 below supplies the accepted representation choices; no migration of
existing formal rules into configuration is authorized. Do not silently
duplicate the same operative rule in both forms.

D04 — Claim meaning and representation, accepted 2026-10-26:

- Each RMED Atom has a Claim. State this without defining a universal storage
  location for Claim. This decision does not require a Claim on C, A, P or O.
- A natural-language Claim carries non-formal meaning and uses
  `atom.content.claim`.
- A fully formal Claim (statement) may use structured `atom.claim.*` fields
  or Governing Configuration. Project Structure is an existing precedent for
  the configuration form; do not prescribe it universally for formal Claims.
- YAML that merely contains natural-language prose is not made formal by its
  carrier. Formality is about the statement, not the file extension or an
  optional Semantics section.
- Correct the old no-Claim Graph Rule definitions rather than adding an
  inheritance exclusion. Do not duplicate a formal Claim into Markdown just
  to satisfy an old required-heading rule.

D05 — Standalone archival preserves Version, accepted 2026-10-26:

Archive the existing version without creating another version merely to
archive it. For example, Current CA-R-123 at Version 3 becomes the Archived
representation CA-R-123@3, not a newly invented Version 4. This also agrees
with preserving an update predecessor's historical Version. It does not
prevent a real content update from creating its normal successor Version.
The representation still receives its agreed Archived Status, qualified
identity/filename and archive location. This answer settles the Version
question; do not invent a new timestamp policy from it.

D06 — Derivation between Relation Types, accepted 2026-10-26:

Use the relation "is derived relation of" between Relation Type instances:

CONTAINS — is derived relation of → IS_CONTAINED_BY.

For this known pair, derivation is the inverse with reversed endpoints; the
current R1368 already describes that meaning. This is distinct from an actual
Task/Epic containment link. Preserve direct-only storage of actual links and
inverse derivation. Do not add mandatory derivation-evidence classifications,
new inference behavior or a general transformation engine from this decision.
The precise serialized spelling is not newly chosen here; reuse an admitted
kind if present, otherwise define it under the accepted relation model.

The Operator authorized direct Plan edits. Create tasks from these decisions;
source-model corrections and projection rebuilds are not yet performed.

### Child Tasks

- [CA-P-2640 — Align Subject and Subject-link definitions](CA-P-2639-EPIC--subject-graph-fpf-refinement/01-CA-P-2640-TASK--align-subject-and-subject-link-definitions.md):
  Active, not executed. Implements D01, including the separately defined
  relations and their dependency on the Subject definition.
- [CA-P-2641 — Align open Graph Node categories](CA-P-2639-EPIC--subject-graph-fpf-refinement/02-CA-P-2641-TASK--align-open-graph-node-categories.md):
  Active, not executed. Implements D02 without inventing additional categories.
- [CA-P-2642 — Define carrier-independent RMED Claims](CA-P-2639-EPIC--subject-graph-fpf-refinement/03-CA-P-2642-TASK--define-carrier-independent-rmed-claims.md):
  Active, not executed. Aligns the logical definitions with D03/D04.
- [CA-P-2643 — Align formal and natural-language Claim representation](CA-P-2639-EPIC--subject-graph-fpf-refinement/04-CA-P-2643-TASK--align-formal-and-natural-language-claim-representation.md):
  Active, not executed. Follows P2642; aligns representation contracts only.
- [CA-P-2644 — Align archival with preservation of the existing Version](CA-P-2639-EPIC--subject-graph-fpf-refinement/05-CA-P-2644-TASK--align-archival-with-preservation-of-the-existing-version.md):
  Active, not executed. Implements D05 in the conflicting source contracts.
- [CA-P-2645 — Define derivation between Relation Types](CA-P-2639-EPIC--subject-graph-fpf-refinement/06-CA-P-2645-TASK--define-derivation-between-relation-types.md):
  Active, not executed. Implements D06; old provenance-class disposition remains
  explicit rather than silently assumed.

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
