---
atom_id: CA-E-460
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Selection
  passive:
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom.Header.Subjects.Active
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
  - CAPRMEDIO_MODEL <+ Atom.Header.Status
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Selection
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Header.Tier
version: 34
updated_at: 2026-11-02 00:18:22 +0400
relations:
  evaluation_for:
  - CA-R-2102
  - CA-D-495
  - CA-M-273
  - CA-M-288
  - CA-R-1271
  - CA-R-1447
  - CA-R-1448
  - CA-R-1449
  - CA-R-1595@21
  - CA-R-1596
  - CA-R-942
tier: 4
role: Evaluation
form: Eval Case
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-460-CORE_META_MODEL-EVAL_CASE--validate-atom-set-selection-and-the-spec-alias.md
  source_atom_id: CA-E-460
  source_atom_revision: 34
  source_sha256: 8cbc1b2d9266b0d6039a8c68d0e3840703daa9f1c0c085c8f4558d36ecbbfc60
  original_relations_sha256: baa052213884859710efa6fdbde2944dae90c241dec1db15d7502bc3cc23369d
---
## Summary

Validate Atom-set Selection **and** the spec Alias

## Claim

### Prose Claim

the four ownership **and** targeting selections for a Scope Unit, including the `spec` alias.


**Claim checked.**

ownership **and** Claim targeting produce their respective direct **and** recursive Atom sets, **and** the alias `spec` selects **only** Active RMED Subtree-targeting Atoms.

## Details

### Test case

construct Scope Unit `A`, its child Scope Unit `A_CHILD`, a sibling Scope Unit `B`, **and** nested Atom Collections inside `A`. the fixture Scope Units are Unordered. use the following distinct source Atoms; resolve each target Scope Unit from the Atom’s one active Subject under CA-R-2102; derive its current Scope Unit from containment. `d`, `e`, **and** `f` have Role Requirement **and** Form Demand under CA-R-932@37, with applicable Demand conditions satisfied. The remaining rows are valid Current-scope Atoms with admitted non-relational Forms; a target equal to the current Scope Unit does **not** make them Relational.

| Atom | Current Scope Unit | Placement | Claim Target Scope Unit | Role | Status |
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

derive **all** four sets for `A` **and** the alias `spec`. repeat **after** moving `a` into a nested Atom Collection under `A` **and** changing **only** numeric Tiers; repeat with narrower **and** explicitly grouped composite applicability restrictions **in** Claim.Prose Claim while retaining the active Subjects; repeat with `b` assigned **every** RMED Role while retaining its other properties. **then** omit `B` from the claimed-complete source frontier, treat a Hub Plan as a Scope Unit, replace targeting with ownership, copy a selected Atom as new authority, omit an active Subject, infer a different target from Claim text, use an unresolved structural target **or** cyclic ancestry, **or** register `spec` as a separate Entity.

### Acceptance criteria

the results **must** be:

| Selection | Members |
|---|---|
| Owned Atoms | `a, b, f, g, h, i` |
| Targeting Atoms | `a, b, d, g, h, i` |
| Subtree-owned Atoms | `a, b, c, f, g, h, i` |
| Subtree-targeting Atoms | `a, b, c, d, e, g, h, i` |
| `spec` alias | `a, b, c, d, e` |

collection nesting, textual applicability restrictions, **and** numeric-Tier-only changes **must not** alter those results. `spec` **must not** create a separate Entity, independently maintained Atom set, **or** source of authority. incoming `d` **and** `e` retain ownership under `B`; outgoing `f` remains owned by `A` **without** entering its Targeting Atoms **or** `spec`. incomplete source coverage, missing, multiple **or** unresolved active Subjects, targets inferred from Claim text, cyclic ancestry, ownership/target substitution, **and** duplicate authority fail explicitly.

### Failure disposition

report the source Revision, selected Scope Unit, expected set, **and** exact missing, extra, duplicated, **or** unresolved member; do **not** silently return a complete result **or** rewrite source ownership.
