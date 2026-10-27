---
atom_id: CA-E-460
content_role: Evaluation
type: Eval Case
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Selection
  depends_on:
  - Subject/Graph Node/Carrier
  - Subject/Graph Node/Domain/Continuant/Atom.Content
  - Subject/Graph Node/Domain/Continuant/Atom.Target Scope Unit
  - Subject/Graph Node/Domain/Continuant/Atom/Content Role
  - Subject/Graph Node/Domain/Continuant/Atom.Status
  - Subject/Graph Node/Domain/Continuant/Selection
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Atom.Tier
version: 30
updated_at: 2026-10-27 06:04:45 +0400
relations:
  evaluation_for:
  - CA-D-482
  - CA-D-495
  - CA-M-273
  - CA-M-288
  - CA-R-1271
  - CA-R-1447
  - CA-R-1448
  - CA-R-1449
  - CA-R-1595
  - CA-R-1596
  - CA-R-942
tier: 4
---
# Summary

Validate Atom-set Selection **and** the spec Alias

## Scope

the four ownership **and** targeting selections for a Scope Unit, including the `spec` alias.

## Claim

### Claim checked

ownership **and** Claim targeting produce their respective direct **and** recursive Atom sets, **and** the alias `spec` selects **only** Active RMED Subtree-targeting Atoms.

## Details

### Test case

construct Scope Unit `A`, its child Scope Unit `A_CHILD`, a sibling Scope Unit `B`, **and** nested Atom Collections inside `A`. the fixture Scope Units are Unordered. use the following distinct source Atoms; a Current-scope Atom explicitly carries its current Scope Unit as target. `d`, `e`, **and** `f` have Content Role Requirement **and** Type Demand under CA-R-932-CORE_META_MODEL-DEFINITION--define-demand-atom, with their applicable Demand conditions satisfied. the remaining rows are valid Current-scope Atoms with admitted non-relational Types; their resolved targets are carried internally under CA-D-482-CORE_META_MODEL-DELIVERY--carry-the-resolved-claim-target-scope-unit; equality **to** ownership does **not** make them Relational.

| Atom | Current Scope Unit | Placement | Claim Target Scope Unit | Content Role | Status |
|---|---|---|---|---|---|
| `a` | `A` | directly under `A` | `A` | Requirement | Active |
| `b` | `A` | nested Atom Collection | `A` | Method | Active |
| `c` | `A_CHILD` | directly under `A_CHILD` | `A_CHILD` | Evaluation | Active |
| `d` | `B` | directly under `B` | `A` | Requirement | Active |
| `e` | `B` | directly under `B` | `A_CHILD` | Requirement | Active |
| `f` | `A` | directly under `A` | `B` | Requirement | Active |
| `g` | `A` | Draft placement | `A` | Requirement | Draft |
| `h` | `A` | directly under `A` | `A` | Plan | Active |
| `i` | `A` | Archived placement | `A` | Delivery | Archived |

derive **all** four sets for `A` **and** the alias `spec`. repeat **after** moving `a` into a nested Atom Collection under `A` **and** changing **only** numeric Tiers; repeat with narrower **and** explicitly grouped composite Claim Scope restrictions **in** the Scope section for RMED, **or** the registered primary content for other roles, while retaining the carried targets; repeat with `b` assigned **every** RMED Content Role while retaining its other properties. **then** omit `B` from the claimed-complete source frontier, treat a Hub Plan as a Scope Unit, replace targeting with ownership, copy a selected Atom as new authority, omit a carried target, infer a different target from Claim text, use an unresolved structural target **or** cyclic ancestry, **or** register `spec` as a separate Entity.

### Acceptance criteria

the results **must** be:

| Selection | Members |
|---|---|
| Owned Atoms | `a, b, f, g, h, i` |
| Targeting Atoms | `a, b, d, g, h, i` |
| Subtree-owned Atoms | `a, b, c, f, g, h, i` |
| Subtree-targeting Atoms | `a, b, c, d, e, g, h, i` |
| `spec` alias | `a, b, c, d, e` |

collection nesting, textual applicability restrictions, **and** numeric-Tier-only changes **must not** alter those results. `spec` **must not** create a separate Entity, independently maintained Atom set, **or** source of authority. incoming `d` **and** `e` retain ownership under `B`; outgoing `f` remains owned by `A` **without** entering its Targeting Atoms **or** `spec`. incomplete source coverage, missing **or** unresolved carried targets, targets inferred from Claim text, cyclic ancestry, ownership/target substitution, **and** duplicate authority fail explicitly.

### Failure disposition

report the source Revision, selected Scope Unit, expected set, **and** exact missing, extra, duplicated, **or** unresolved member; do **not** silently return a complete result **or** rewrite source ownership.
