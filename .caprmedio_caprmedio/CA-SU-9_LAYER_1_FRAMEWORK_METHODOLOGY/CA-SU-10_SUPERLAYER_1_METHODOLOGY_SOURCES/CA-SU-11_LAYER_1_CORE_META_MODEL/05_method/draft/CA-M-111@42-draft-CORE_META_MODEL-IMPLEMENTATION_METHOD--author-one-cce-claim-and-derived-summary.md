---
subjects:
  governs: Model::CAPRMEDIO::Continuant/Governing Objects/Atom.content
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Controlled English
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Summary
version: 42
updated_at: 2026-10-29 00:04:17 +0400
relations:
  depends_on:
  - CA-R-1624
  - CA-R-1465
atom_id: CA-M-111@42-draft
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
tier: 3
type: Implementation Method
---
# Summary

Author one CCE Claim and derived Summary

## Claim scope

Authoring a primary contribution, its applicability and derived Summary; RMED uses the unified body layout.

## Claim

**to** author one CCE Claim **and** its derived Summary, an Author **must** use these authoring constraints:

- express **`=1`** independently replaceable contribution using the applicable CCE Content Role profile. carry it under the primary contribution heading registered **in** CA-D-479 rather than imposing the literal heading Claim on **every** role.
- resolve **`=1`** Claim Target Scope Unit independently of ownership. select the current Scope Unit as the authoring default **or** an explicitly permitted different target; carry the resolved value under CA-D-482. express applicability under CA-D-495. for RMED, describe what the Claim applies **to**, including applicable conditions **and** exclusions, **in** Claim scope when required; do **not** merely repeat the carried current **or** target Scope Unit; those restrictions alone do **not** make the Atom Relational.
- keep Details within the primary contribution under CA-R-1624. for RMED, read the Claim within its Claim scope; Details **must not** change either. **if** supporting content reveals an incomplete **or** inaccurate contribution **or** applicability, revise the affected Claim scope **or** primary contribution explicitly **and** recheck agreement; do **not** hide the change **in** Details.
- write Summary **only after** the other body sections **and** the contribution review are complete. shorten the finalized primary contribution under CA-R-1465 **and** CA-R-1273. for RMED, summarize the Claim within its finalized Claim scope, **not** the Scope alone; do **not** substitute supporting Results **or** TLDR as the source.
- for an existing Atom, retain the established Summary **and** check its faithfulness; **if** the Summary needs changing, use a new Atom identity under CA-R-1464.
- derive **every** Translation from the full corresponding source content, **not** the Summary.

For RMED, use the single content.claim and exact headings in CA-D-479. A natural-language Claim remains prose; the optional formal child occupies one complete fenced block under ### Formal claim; prose may coexist in the same Claim. Never create an additional atom.claim or atom.formal_claim. Optional sections may be absent. For a formal child use the applicable model Definition and declared Graph Syntax; the superseded special Graph Rule authoring packet is not another Claim layout.

## Details

R-only scope refinement (CA-A-1244): the optional ### Formal claim / content.claim.formal_claim is admitted only for Requirement Atoms for now. Method, Evaluation and Delivery have prose Claims with no operative formal child; code examples remain examples. Any earlier generic optional-formal wording in this Draft is limited by that Role condition. The complete one-Claim contract and optional supporting sections remain unchanged.
