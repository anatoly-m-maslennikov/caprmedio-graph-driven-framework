---
atom_id: CA-P-2568@3
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 20
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph/Relation
  depends_on: []
version: 3
updated_at: 2026-10-24 11:18:21 +0400
relations: {}
tier: 3
---
# Summary

Replace overly broad child_of and parent_of relations

## Objective

Replace generic Atom parentage with precise relations. Preserve the meaning of each supported link, distinguish refinement from a separate constraint, and retire child_of / parent_of after their Current uses and consumers are resolved.

## Details

This is a separate Epic, not a change to [CA-P-1959](18-CA-P-1959-EPIC--improve-entity-model-stage-2.md). The Operator requested its creation instead of starting the migration. No relation definition, link, runtime behavior or projection changes as part of creating this Plan.

### Accepted direction

- Reuse existing precise relations: IS_CONTAINED_BY for containment; derived_from for provenance; method_for, evaluation_for, delivery_for and rationale_for for their distinct purposes; depends_on for a real prerequisite.
- Add refines for a more specific statement of the same rule or Claim: same-role RMED, compatible applicability and no contradiction on shared scope.
- Add is_constrained_by when an RMED Atom must obey a separate explicit normative RMED constraint. This is not the same fact as serving or evaluating a Requirement.
- Neither new relation grants automatic inheritance or permission to override its target. Do not recreate generic tier-parent traversal under another name.
- Store only the direct relation. Derive inverse views; do not author duplicate inverse lists. IS_CONTAINED_BY remains child to container, with CONTAINS derived.
- Do not replace links by Content Role alone. For example, an M Atom can both serve an R Atom and be constrained by it; method_for does not automatically replace its old authority link.

### Work sequence

This grouping Plan has no own implementation work. Before execution, create bounded child Tasks with at most 15 minutes of own work each.

1. [ ] Inventory Current source definitions, child_of / parent_of uses, and affected registry, validation, query and projection consumers. Follow configured authority paths, not delivery mirrors. Record supported mappings and unresolved cases with source IDs, Versions and reasons; do not infer meaning from relation names or role letters alone.
2. [ ] Update RMEDO first. Define the two new relation meanings and descriptive metadata; put endpoint permissions and other constraints in the separate rule contracts. Align conflicting parentage Requirements and Evaluations. Reuse generic direct-relation Delivery policies where they already fit. Starting points include R879, R796, R833, R806, M120, D268 and their actual current dependants.
3. [ ] Align the existing runtime registry, validator and affected callers with the accepted contracts. Add focused positive and negative tests for the new kinds, retained precise links, direct/inverse storage and the absence of automatic authority inheritance. Do not add a new rule engine or a parallel migration framework.
4. [ ] Migrate supported links in bounded batches. Preserve exact predecessors; increment Version once per real same-ID update and use the actual update time. Leave unrelated content unchanged. Keep ambiguous links explicitly queued instead of forcing a mapping, deleting their meaning or declaring their migration complete. Current means non-archived, not only Status Active.
5. [ ] Rebuild the affected derived views and verify the actual source links. Finish retirement of child_of / parent_of only after their Current uses and required consumers are resolved. Keep archived history readable and unchanged.

### Known review cases

- M297 currently carries both child_of and method_for to R1487: distinguish the two facts before replacing either.
- R951 to R933 is a candidate for same-rule refinement, subject to current source review.
- R796 to R1174 needs its exact constraint or Goal-contribution meaning established; a specification link is not proof that a Goal was achieved.
- E207 to R815, D250 to M261 and M160 to M110 need their current endpoints or governing propositions resolved before mapping.

These are review leads, not a complete migration map or permission to reuse old Version/hash pins. Reopen the current sources before execution. General unrelated content migration remains [CA-P-1970](19-CA-P-1970-EPIC--align-atom-content-after-subject-migration.md).

### Definition of Done

The two precise kinds and their required source/runtime contracts agree. Every old Current parentage link has a supported disposition and verified effect; unresolved cases keep this Epic incomplete. Required consumers no longer depend on the retired pair. Focused tests and rebuilt views reflect the actual result, direct relations have no authored inverse duplicates, and exact predecessor history is preserved. No hidden inheritance, guessed mapping, unrelated content migration or deployment is included.
