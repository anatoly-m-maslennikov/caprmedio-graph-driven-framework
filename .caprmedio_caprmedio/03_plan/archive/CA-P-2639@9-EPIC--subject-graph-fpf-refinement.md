---
atom_id: CA-P-2639@9
content_role: Plan
type: Plan
label: Epic
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject
version: 9
updated_at: 2026-10-26 05:17:30 +0400
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
| I02 | D651@5/D652@7 use Carrier/Filename/Atom.Tier; D525@11 places persistent-state Carrier under Runtime. Check kind, property and representation meanings. | Existing D-Subject/operator rules; P2649 created; not applied |
| I03 | R2001@9/R1269@23 exclude Claim for Graph Rules, while R2150@4/M232@24 describe additive inheritance without the applicability exception. | Decided by D03/D04; P2642 and P2643 created; not applied |
| I04 | R2003@7/R2149@7 operative Graph Rule YAML and R1997@10/D637@17 examples retain retired root paths. | Existing full-path/root decisions; P2650 created; not applied |
| I05 | D478@20/D480@15/D485@14 still govern Atom.Property; R1454@22 references Atom.Substance; O045@15 retains Atom.Atom/Tier. | Existing field-retirement decisions and D04; P2651 created; not applied |
| I06 | R1617@13 treats derivation-evidence classification as a Relation Type; R1653@24 admits imprecise related_to. | D06/D07 plus existing typed-only decision; P2645/P2646/P2648 created; not applied |
| I07 | R1989@9 and R868@25 disagree about archived Status, Version and Updated At. Distinguish an update predecessor from standalone archival. | Version decision accepted (D05); P2644 created; not applied |
| I08 | R1564@17/R1565@14 retain Actor as an Operations Type alongside Workflow, Step and Action. Preserve real participation policies when resolving it. | Actor definitions go to R (D08); P2647 created; not applied |

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
- Q06 / I06: resolved by D06/D07. Use explicit derivation between Relation
  Types and retire the old Relation Derivation Class definition. P2645/P2646
  track the accepted work. The prior typed-only decision already supplies the
  direction for related_to; do not ask for that policy again. P2648 tracks its
  bounded retirement and Current consumer correction.
- Q07 / I08: resolved by D08. Actor, Operator and AI Agent definitions belong
  in R, not O. P2647 tracks the source disposition and O catalogue correction.
- I02/I04/I05: the existing decisions already settle the direction: D governs
  the represented thing/property, paths use the accepted canonical root and
  operators, and retired generic fields are not revived. P2649–P2651 perform
  the source-specific mapping and ask only for concrete unsupported cases.
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

D07 — Retire Relation Derivation Class, accepted 2026-10-26:

Retire the old Relation Derivation Class definition rather than maintain a
parallel classification alongside explicit derivation relations and source
references. Preserve useful source references and the concrete containment
inverse meaning. Do not replace the retired classification with another
mandatory evidence taxonomy or silently remove unrelated obligations.
Coordinate the definition's affected consumers with P2645.

D08 — Actor definitions belong in R, accepted 2026-10-26:

Move the relevant Actor definitions to Requirements, including Operator and
AI Agent definitions. Actor is not an Operations Type. Preserve definitions
already in R; classify actual definitions as R/Type: Definition. A change of
Content Role creates a new Atom ID under the established identity rule;
archive predecessors and account for affected Current consumers. Preserve
participation/authorization constraints when retiring the O/Actor model;
place those normative rules in R rather than silently deleting them.
This is not permission to move every M/E/D that merely mentions an Actor.

Previously established decisions applied to the other findings:

- D Atoms govern the thing/property being represented; representation is in
  their Claim/Content Scope, not an invented Carrier subtype for each field.
- Use full canonical Subject paths and the accepted meanings of /, . and :.
  Repair retired root addresses without redesigning the operative condition.
- Atom.Property and generic Atom.Substance were retired. Do not revive them
  as nodes; use the actual governed thing/property and the accepted Claim
  model. Keep broad applicability in Content Scope where necessary.
- Relations must have precise typed meanings. Retire the imprecise related_to
  fallback; keep only evidenced typed replacements and drop redundant links,
  rather than inventing dependencies. The child_of/parent_of Epic stays separate.

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
  Active, not executed. Implements D06; coordinate with P2646's accepted
  retirement of the old classification.
- [CA-P-2646 — Retire the old Relation Derivation Class](CA-P-2639-EPIC--subject-graph-fpf-refinement/07-CA-P-2646-TASK--retire-the-old-relation-derivation-class.md):
  Active, not executed. Implements D07 with bounded consumer repair.

- [CA-P-2647 — Move Actor definitions to Requirements](CA-P-2639-EPIC--subject-graph-fpf-refinement/08-CA-P-2647-TASK--move-actor-definitions-to-requirements.md):
  Active, not executed.
- [CA-P-2648 — Retire the imprecise related_to fallback](CA-P-2639-EPIC--subject-graph-fpf-refinement/09-CA-P-2648-TASK--retire-the-imprecise-related-to-fallback.md):
  Active, not executed.
- [CA-P-2649 — Correct representation-policy Subjects](CA-P-2639-EPIC--subject-graph-fpf-refinement/10-CA-P-2649-TASK--correct-representation-policy-subjects.md):
  Active, not executed.
- [CA-P-2650 — Align formal Graph Rule addresses with canonical Subjects](CA-P-2639-EPIC--subject-graph-fpf-refinement/11-CA-P-2650-TASK--align-formal-graph-rule-addresses-with-canonical-subjects.md):
  Active, not executed.
- [CA-P-2651 — Remove retired generic property Subjects](CA-P-2639-EPIC--subject-graph-fpf-refinement/12-CA-P-2651-TASK--remove-retired-generic-property-subjects.md):
  Active, not executed.
- [CA-P-2652 — Verify refinement sources and rebuild Subject views](CA-P-2639-EPIC--subject-graph-fpf-refinement/13-CA-P-2652-TASK--verify-refinement-sources-and-rebuild-subject-views.md):
  Active, not executed.

### Execution ordering

- P2640/P2641 establish the accepted Subject meanings.
- P2643 follows P2642; P2646 follows the explicit derivation definition in P2645.
- P2648 coordinates with P2646; P2649 uses the accepted root paths.
- P2650 follows the Subject/Claim definitions; P2651 follows the Claim model.
- P2652 verifies completed source corrections and rebuilds derived views last.
- No Task has been executed by this planning update. The remaining evidence
  work is bounded consumer lookup, not another general design review.

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
