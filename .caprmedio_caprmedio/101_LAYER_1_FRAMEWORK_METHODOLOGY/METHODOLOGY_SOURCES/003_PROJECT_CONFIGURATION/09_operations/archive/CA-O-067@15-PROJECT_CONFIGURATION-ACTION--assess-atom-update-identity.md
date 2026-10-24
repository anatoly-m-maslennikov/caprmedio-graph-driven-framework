---
subjects:
  governs: Assess Atom Update Identity
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Continuant/Atom
  - Entity/Node/Continuant/Atom.Summary
  - Subject/Domain/Node/Continuant/Atom.Substance
  - Atom Change Classification
  - 'Entity/Node/Continuant/History/Revision/Type: Atom'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 15
updated_at: 2026-10-24 00:38:25 +0400
relations:
  relates_to:
  - CA-R-1432
  - CA-R-1464
  - CA-M-303
  - CA-R-1520
atom_id: CA-O-067@15
content_role: Operations
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
type: Action
tier: 3
---
# Summary

Assess Atom update identity

## Operation

Assess Atom Update Identity **means** the reusable read-only Action that compares an existing Atom with its proposed result **and** returns whether the requested update preserves its identity under CA-R-1432 **and** CA-R-1464.

### Inputs

- the exact existing Atom Revision **and** the proposed Claim, properties, **and** Summary.
- applicable change authority **and** relevant evidence for this assessment.

### Outcomes

| Condition | Returned result |
|---|---|
| the applicable change class preserves identity | the admitted change class, proposed result, **and** assessment evidence; **every** actual same-ID update requires the target Version incremented by exactly **`1`** **and** an actual Project-time Updated At; an exact no-op retains Version **and** Updated At; required predecessor history retains its exact prior bytes; no presumed authorization **or** persistence |
| replacement is required, including **any** change of Summary value | replacement required, with the target Revision, proposed result, classification reason, **and** assessment evidence |
| evidence **or** classification is uncertain | unresolved, with the missing evidence **or** required Operator decision; no presumed update **or** replacement approval |

the result describes **only** the supplied proposal against the identified target Revision. it does **not** remain sufficient **when** that proposal, Revision, **or** relevant evidence changes.

this Action **must not** select a continuation Workflow, end its caller's Run, schedule another Run, authorize a mutation, **or** persist **any** change. the calling Workflow declares its routing under CA-M-303 **and** supplies its own performed-effect account **when** preparing a handoff under CA-R-1520.

## Details
