---
subjects:
  governs: Entity/Aspect/Engineering/Authoring
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom.Content
  - Entity/Aspect/Engineering/Authoring/Controlled English
  - Entity/Object/Continuant/Governing Objects/Atom.Content.Summary
version: 2
updated_at: 2026-10-30 01:32:01 +0400
relations:
  depends_on:
  - CA-R-1624
  - CA-R-1465
atom_id: CA-M-442@2
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Implementation Method
---
## Summary

An Atom's content expresses one scoped contribution with a faithful Summary and Translations.

## Claim scope

authoring an Atom's prose CCE primary contribution, its applicability, **and** its derived Summary. The same Claim may contain readable prose and an optional R-only nested Formal claim under the Claim definition.

## Claim

**to** author one CCE Claim **and** its derived Summary, an Author **must** use these authoring constraints:

- express **`=1`** coherent contribution whose full meaning is covered by one precise Summary using the applicable CCE Content Role profile. carry it under the primary contribution heading registered for the Content Role rather than imposing the literal heading Claim on **every** role.
- resolve **`=1`** Claim Target Scope Unit independently of ownership. select the current Scope Unit as the authoring default **or** an explicitly permitted different target; carry the resolved value under the target Scope Unit carrier definition. express applicability under the applicability carrier definition. for RMED, describe what the Claim applies **to**, including applicable conditions **and** exclusions, **in** Scope; do **not** merely repeat the carried current **or** target Scope Unit; those restrictions alone do **not** make the Atom Relational.
- keep Details within the primary contribution. for RMED, read the Claim within its Scope; Details **must not** change either. **if** supporting content reveals an incomplete **or** inaccurate contribution **or** applicability, revise the affected Scope **or** primary contribution explicitly **and** recheck agreement; do **not** hide the change **in** Details.
- write Summary **only after** the other body sections **and** the contribution review are complete. shorten the finalized primary contribution. use plain wording that expresses the Claim’s meaning. preserve established principle names such as DRY **and** MECE instead of paraphrasing them. a familiar name **or** short instruction **may** be the Summary; do **not** force it into a declarative sentence. for RMED, summarize the Claim within its finalized Scope, **not** the Scope alone; do **not** substitute supporting Results **or** TLDR as the source.
- for an existing Atom, retain the established Summary **and** check its faithfulness; **if** the Summary needs changing, use a new Atom identity under the Atom identity rule.
- derive **every** Translation from the full corresponding source content, **not** the Summary.
