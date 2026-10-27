---
subjects:
  governs: Subject/Graph Node/Engineering/Authoring
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom.Content
  - Subject/Graph Rule/CCE
  - Subject/Graph Node/Domain/Continuant/Atom.Summary
version: 40
updated_at: 2026-10-27 06:04:45 +0400
relations:
  depends_on:
  - CA-R-1624
  - CA-R-1465
atom_id: CA-M-111
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Implementation Method
---
# Summary

Author one CCE Claim and derived Summary

## Scope

authoring an Atom's prose CCE primary contribution, its applicability, **and** its derived Summary. Formal Graph Rule Atoms use CA-M-394 instead, retaining one structured contribution and a source-faithful Summary. This exception does not apply automatically to every R/Type: Rule Atom.

## Claim

**to** author one CCE Claim **and** its derived Summary, an Author **must** use these authoring constraints:

- express **`=1`** independently replaceable contribution using the applicable CCE Content Role profile. carry it under the primary contribution heading registered **in** CA-D-479 rather than imposing the literal heading Claim on **every** role.
- resolve **`=1`** Claim Target Scope Unit independently of ownership. select the current Scope Unit as the authoring default **or** an explicitly permitted different target; carry the resolved value under CA-D-482. express applicability under CA-D-495. for RMED, describe what the Claim applies **to**, including applicable conditions **and** exclusions, **in** Scope; do **not** merely repeat the carried current **or** target Scope Unit; those restrictions alone do **not** make the Atom Relational.
- keep Details within the primary contribution under CA-R-1624. for RMED, read the Claim within its Scope; Details **must not** change either. **if** supporting content reveals an incomplete **or** inaccurate contribution **or** applicability, revise the affected Scope **or** primary contribution explicitly **and** recheck agreement; do **not** hide the change **in** Details.
- write Summary **only after** the other body sections **and** the contribution review are complete. shorten the finalized primary contribution under CA-R-1465 **and** CA-R-1273. for RMED, summarize the Claim within its finalized Scope, **not** the Scope alone; do **not** substitute supporting Results **or** TLDR as the source.
- for an existing Atom, retain the established Summary **and** check its faithfulness; **if** the Summary needs changing, use a new Atom identity under CA-R-1464.
- derive **every** Translation from the full corresponding source content, **not** the Summary.

## Details
