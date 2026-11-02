---
subjects:
  governs: Scope Reference Validation
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Author
  - Atom Scope
  - Subject/Domain/Node/Continuant/Atom.Target Scope Unit
  - Subject/Domain/Node/Continuant/Atom.Substance
  - Subject/Domain/Node/Continuant/Atom.Subjects
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Project.Structure
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Hub Atom
version: 34
updated_at: 2026-10-22 16:12:51 +0000
relations:
  evaluation_for:
  - CA-R-1595
  - CA-R-1596
  - CA-R-922
  - CA-R-923
  - CA-R-1588
  - CA-R-1271
  - CA-R-947
  - CA-R-944
  - CA-R-2100
  - CA-R-1202
  - CA-D-482
  - CA-D-495
atom_id: CA-E-240@34
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
status: Archived
author: Anatoly Maslennikov
type: Eval Case
global_tier: 11
---
# Summary

Validate Atom Scope **and** Claim Scope

## Scope

independent resolution of Atom ownership, GOVERNS Subject, Claim Target Scope Unit, **and** textual applicability.

## Claim

### Claim checked

**every** Atom resolves its ownership, zero **or** one GOVERNS Relation, **and** **`=1`** Claim Target Scope Unit independently of **any** applicability restrictions **in** its Main Content.

## Details

### Test case

create a Current-scope Atom with its own Scope Unit carried as the target; repeat with zero **or** one GOVERNS target and with a narrower restriction **and** a composite restriction **in** its Scope section for RMED **or** the registered primary content for other roles. create a parent-owned Goal for a declared direct child, an external Project Goal with its Author's registered Operator name **and** an explicit Project target, **and** a permitted Demand. include a Plan **in** a nested Hub whose carried target is its owning Scope Unit.

**then** omit a required target, provide two target values, supply a Hub **or** another non-Scope-Unit target, leave a reference unresolved, infer a different target merely from textual restrictions, change ownership from the target, make the referenced Scope Unit bearer-dependent, reorder Subject declarations, **or** use a forbidden Goal **or** Demand target.

### Acceptance criteria

**every** valid fixture retains its ownership, resolves zero **or** one canonical GOVERNS target **and** **`=1`** Claim Target Scope Unit, **and** preserves its applicability restrictions **in** the body sections registered by CA-D-495-CORE_META_MODEL-CORE-DELIVERY--carry-applicability-in-the-registered-body-sections. a Current-scope target is selected from the owning Scope Unit during authoring **and** carried explicitly; an external Goal requires its explicit Project target. narrower **or** composite Claim Scope alone does **not** make an Atom Relational. a different permitted target does **not** transfer ownership **or** create Scope Unit ancestry. Subject ordering **and** Hub nesting do **not** change these facts. **every** invalid fixture fails with the exact affected fact identified.

### Failure disposition

report the invalid Atom **and** ownership, target, textual restriction, **or** Subject fact; do **not** repair unresolved references by guessing.
