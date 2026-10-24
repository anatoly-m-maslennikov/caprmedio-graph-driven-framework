---
subjects:
  governs: Atom Tier Validation.Concrete Cases
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Tier
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Atom.Target Scope Unit
  - Subtree-targeting Atoms
  - Subject/Domain/Node/Continuant/Atom/Content Role
  - Subject/Domain/Node/Continuant/Atom.Status
  - Evaluation For Relation
  - Methodology Source.Expansion Boundary
  - Subject/Domain/Node/Continuant/Project.Framework Settings
version: 25
updated_at: 2026-10-24 00:38:25 +0400
relations:
  evaluation_for:
  - CA-R-1402
  - CA-R-1430
  - CA-R-2124
  - CA-R-2125
  - CA-R-2126
  - CA-R-2127
  - CA-R-2128
  - CA-R-2129
  - CA-R-2130
  - CA-R-2131
  - CA-R-2132
  - CA-R-1449
  - CA-M-288
  - CA-R-1018
  - CA-R-1429
  - CA-R-1375
  - CA-R-796
  - CA-R-829
  - CA-M-235
  - CA-M-265
  - CA-M-437
  - CA-M-273
  - CA-D-280
  - CA-D-651
  - CA-D-368
  - CA-R-2149
atom_id: CA-E-447@25
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Eval Case
tier: 3
---
# Summary

Validate three-tier boundaries with concrete cases

## Scope

three-tier classification, structural, scope, and representation fixtures.

## Claim

This Evaluation **must** reject a tier fixture that derives authority from a legacy label, role/type shortcut, filename, or structural depth instead of the complete Claim, owner Scope Unit, and applicable numeric definition.

### Numeric fixtures

- classify Project ordinary Atoms at Tier `0` or higher, non-Project Atoms at Tier `1` or higher, and a Project-owned Goal at exactly `-1`; use the initial display names Principle, Core, General, and Standard only as labels for `0`, `1`, `2`, and `3`.
- preserve each Atom's numeric Tier through Projection, filename, and other delivery representations; omission of the Standard display token does not erase the internal Tier and no representation token is a Tier source.
- admit a governing stored relation only when its source is a Current RMED Atom and its registered target is Current: a same-Scope target must have a strictly lower Tier; a strict-ancestor target is accepted without Tier comparison; descendant and sibling targets fail; derived inverses do not qualify.
- accept qualifying Evaluation and Operations targets under the registered Evaluation relation without inventing a role/type-to-Tier restriction; unresolved endpoint, membership, owner, or ancestry evidence remains unresolved rather than passing.
- preserve Project ownership and Scope ancestry independently from numeric Tier, keep siblings distinct, and reject cycles, stale legacy tier fields, or a Project Goal with any value other than `-1`.
- source replacement and concrete serialization changes do not authorize a new tier, while active source-authorized additions retain their exact variation point and carrier identity.

### Failure disposition

identify the exact source Revision, fixture, expected result, and observed counterexample; restore the invalid fixture's governed source, owner, binding, classification evidence, relation, or representation and rerun that fixture. A repair must not rewrite frozen historical evidence, invent authority, transfer source ownership, or report an unexecuted operational case as passed.
