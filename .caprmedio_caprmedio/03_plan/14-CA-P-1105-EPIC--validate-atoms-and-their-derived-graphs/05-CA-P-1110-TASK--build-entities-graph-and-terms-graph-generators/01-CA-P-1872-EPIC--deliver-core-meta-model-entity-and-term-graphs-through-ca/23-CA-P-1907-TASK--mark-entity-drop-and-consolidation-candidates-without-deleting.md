---
atom_id: CA-P-1907
content_role: Plan
type: Plan
label: Task
work_sequence_number: 23
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Projection
  depends_on: [Entity, Term, Atom, Property, Carrier, Plan]
version: 6
updated_at: "2026-10-10 04:24:00 +0400"
relations:
  is_decomposition_of: [CA-P-1872]
  blocks: [CA-P-1908]
---
# Summary

Mark Entity drop and consolidation candidates without deleting

## Objective

Review every Entity in the proposed graph for dropping, consolidation or generalization. Mark the candidates without deleting them, preserving every reviewed source identity and its evidence.

## Details

Review context: the Operator chose **Finish against the captured snapshot only**. Use the original CA-P-1905 source pins and immutable Git commit `a971d0e00c33c779f485fc8cad63194894d440fb`; read `nodes/snapshot.context.md` and `nodes/support/snapshot_sources.py`. CA-D-494 revision 2 remains the review input; live revision 3 is outside this snapshot. Preserve originals and label receipts as captured-snapshot checks, not current-Core checks. Any currentness or source-pin requirement below means exact validity against this selected captured snapshot. Do not silently rebind or overwrite live Core.

Child work only; no separately executable own work. Nine source-pinned review batches and three bounded meaning repairs precede integration and independent verification. Original completed review receipts remain historical; the repairs explicitly BLOCK integration.

Required start prerequisite: CA-P-1906. Inputs: CA-P-1905's pinned inventory and CA-P-1906's proposed structure, inheritance map and complete relation-occurrence ledger.

Review the whole Entity inventory, not only Revision or already suspected nodes. Look for duplicates, redundant concepts, empty definitions, entities with no distinct meaning and entities that can share a more general concept. Record the check for every baseline identity. A repeated name is not proof of duplication; a leaf with no children is not proof of emptiness. An unresolved definition is a question, not automatic permission to drop it.

Review repeated fields, Carrier bindings, serialization details, helper labels and operation-definition/run distinctions. Distinguish an unnecessary independent Entity from a useful Property, inherited constraint, relation, allowed value or detail that should only be hidden in a particular view.

Record a disposition for every baseline identity: retain, move, inherit, consolidate, generalize, drop candidate, or question. Every drop, consolidation or generalization mark needs its source references, reason, proposed replacement and impact on Relations, constraints, historical references and queries. State which distinctions survive and which could be lost. Mark affected nodes visibly; do not delete them or their governing Atoms. A generalization is not an accepted new subtype relation.

Keep every original row in CA-P-1906's relation-occurrence ledger. Add the effects of each proposed drop, consolidation or generalization on its qualified endpoints and candidate relation, with source evidence or an explicit unresolved/not-native disposition, reason, checks performed and any required Operator question. Preserve the original missing-evidence or inapplicability reasons; do not invent proposals to fill unresolved rows. Cover affected and unaffected occurrences; do not replace the ledger with a deduplicated edge list. Additional proposed relations need separate evidence and must not be presented as original Subject occurrences.

Explicit example: mark Revision as a drop/consolidation candidate because Version Number and Updated At can describe an Atom's selected state. Propose Atom.Version Number and Atom.Updated At as replacements where appropriate, while preserving distinct historical states and exact reference information. Do not remove revision history or rename serialization keys in this Task.

Explicit generalization example: check Applicable Methodology as a case of a general Projection concept. Compiling all applicable Method Atoms for a Scope Unit into one document used as a prompt follows the same pattern. Evaluate a compiled Applicable Methodology document with the single-document form, not a set of source Atoms. Show the source set separately from the derived document; the document does not gain source-of-truth authority just by compiling it. Check which applicability, authority, ordering and provenance constraints must remain, and whether they fit the general Projection model. Mark the proposed generalization and ask about any unresolved loss of meaning before adopting it.

Output: a complete node-disposition ledger, updated complete relation-occurrence ledger and marked candidate graph covering all five checks: duplicates, redundancy, emptiness, lack of meaning and generalization. Include Revision and Applicable Methodology as explicit examples, with source-backed reasons and proposed replacements. Keep marked identities visible and traceable; count retained independent roots separately from marked drop candidates.

Exclusive scope: candidate annotations and review evidence only. No source, Subject, schema, implementation or historical-artifact deletions or migrations.

Inherit CA-P-1872's explicit 90% confidence threshold and local-without-MCP authorization. Ask the Operator before deciding below that threshold; do not disguise uncertainty as an accepted fact. If the ready workload exceeds 15 minutes, split it into bounded direct child Plans before execution. These Tasks are created now; their work has not started.

### Bounded direct Tasks

The 62 explicit Substance/Revision/Projection identities are reviewed separately; the other 644 identities form eight disjoint sorted partitions. Each original identity appears exactly once. All nine reviews start only after CA-P-1906 is Done. They explicitly BLOCK CA-P-1937; integration BLOCKS independent verification CA-P-1938. This parent remains Active until every child is Done and its own Definition of Done is satisfied.

- [CA-P-1928](23-CA-P-1907-TASK--mark-entity-drop-and-consolidation-candidates-without-deleting/done/01-CA-P-1928-TASK--review-substance-revision-and-compiled-projection-candidates.md): Review Substance Revision and compiled Projection candidates (62 nodes); 15 minutes.
- [CA-P-1929](23-CA-P-1907-TASK--mark-entity-drop-and-consolidation-candidates-without-deleting/done/02-CA-P-1929-TASK--review-first-core-node-disposition-batch.md): Review first Core node disposition batch (80 nodes); 15 minutes.
- [CA-P-1930](23-CA-P-1907-TASK--mark-entity-drop-and-consolidation-candidates-without-deleting/done/03-CA-P-1930-TASK--review-second-core-node-disposition-batch.md): Review second Core node disposition batch (81 nodes); 15 minutes.
- [CA-P-1931](23-CA-P-1907-TASK--mark-entity-drop-and-consolidation-candidates-without-deleting/done/04-CA-P-1931-TASK--review-third-core-node-disposition-batch.md): Review third Core node disposition batch (80 nodes); 15 minutes.
- [CA-P-1932](23-CA-P-1907-TASK--mark-entity-drop-and-consolidation-candidates-without-deleting/done/05-CA-P-1932-TASK--review-fourth-core-node-disposition-batch.md): Review fourth Core node disposition batch (81 nodes); 15 minutes.
- [CA-P-1933](23-CA-P-1907-TASK--mark-entity-drop-and-consolidation-candidates-without-deleting/done/06-CA-P-1933-TASK--review-fifth-core-node-disposition-batch.md): Review fifth Core node disposition batch (80 nodes); 15 minutes.
- [CA-P-1934](23-CA-P-1907-TASK--mark-entity-drop-and-consolidation-candidates-without-deleting/done/07-CA-P-1934-TASK--review-sixth-core-node-disposition-batch.md): Review sixth Core node disposition batch (81 nodes); 15 minutes.
- [CA-P-1935](23-CA-P-1907-TASK--mark-entity-drop-and-consolidation-candidates-without-deleting/done/08-CA-P-1935-TASK--review-seventh-core-node-disposition-batch.md): Review seventh Core node disposition batch (80 nodes); 15 minutes.
- [CA-P-1936](23-CA-P-1907-TASK--mark-entity-drop-and-consolidation-candidates-without-deleting/done/09-CA-P-1936-TASK--review-eighth-core-node-disposition-batch.md): Review eighth Core node disposition batch (81 nodes); 15 minutes.
- [CA-P-1937](23-CA-P-1907-TASK--mark-entity-drop-and-consolidation-candidates-without-deleting/10-CA-P-1937-TASK--integrate-the-complete-core-node-disposition-review.md): Integrate the complete Core node disposition review; 15 minutes.
- [CA-P-1938](23-CA-P-1907-TASK--mark-entity-drop-and-consolidation-candidates-without-deleting/11-CA-P-1938-TASK--verify-the-complete-core-node-disposition-review.md): Verify the complete Core node disposition review; 15 minutes.

Latest content direction: use Substance as the shared primary-content name, with Substance Scope describing applicability and optional general Details. Explicit Substance Scope may be omitted only for the whole governed Subject AND the whole owning Scope Unit; omission resolves that default. Preserve ownership metadata, role-specific labels and type-required content. Review this in the candidate only; do not rewrite Core or treat the new direction as old source evidence.

### Meaning-repair prerequisites

Independent preparation found false missing-meaning questions in captured batches 1, 4 and 8. These bounded repairs must be Done before CA-P-1937 starts. Prior Done receipts are not retroactively rewritten.

- [CA-P-1952](23-CA-P-1907-TASK--mark-entity-drop-and-consolidation-candidates-without-deleting/12-CA-P-1952-TASK--repair-qualified-atom-and-artifact-node-review.md): Repair qualified Atom and Artifact node review; 15 minutes. Explicitly BLOCKS CA-P-1937.
- [CA-P-1953](23-CA-P-1907-TASK--mark-entity-drop-and-consolidation-candidates-without-deleting/13-CA-P-1953-TASK--repair-qualified-carrier-and-settings-node-review.md): Repair qualified Carrier and settings node review; 15 minutes. Explicitly BLOCKS CA-P-1937.
- [CA-P-1954](23-CA-P-1907-TASK--mark-entity-drop-and-consolidation-candidates-without-deleting/14-CA-P-1954-TASK--repair-qualified-subject-and-workflow-node-review.md): Repair qualified Subject and Workflow node review; 15 minutes. Explicitly BLOCKS CA-P-1937.

### Definition of Done

the Plan is **not** Done **if** ((the stated output, complete source traceability **or** required handoff is missing) **or** (an original relation occurrence is omitted from the ledger) **or** (an affected relation has **none** evidenced proposal **and** has **none** explicit unresolved/not-native disposition with its preserved reason and checks performed) **or** (a required start prerequisite is **not** Done) **or** (the stated acceptance conditions are failed, stale **or** unverified) **or** (uncertainty below the inherited confidence threshold is silently resolved **or** not put to the Operator) **or** (work exceeds the admitted boundary **or** any source, Subject, history **or** marked Entity was changed **or** deleted without separate authorization) **or** (any direct decomposing Plan is **not** Done)).
