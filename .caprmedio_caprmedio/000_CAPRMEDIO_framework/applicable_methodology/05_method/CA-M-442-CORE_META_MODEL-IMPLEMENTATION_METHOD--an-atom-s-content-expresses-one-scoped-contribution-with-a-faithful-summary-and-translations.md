---
atom_id: CA-M-442
ref_id: CA-M-442
container:
  scope_unit: CA-SU-11
role: Method
form: Implementation Method
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Authoring
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Authoring <+ Controlled English
  - CAPRMEDIO_MODEL <+ Atom.Content.Summary
tier: 3
relations:
  depends_on:
  - CA-R-2503
  - CA-R-2499
status: Active
version: 5
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-M-442-CORE_META_MODEL-IMPLEMENTATION_METHOD--an-atom-s-content-expresses-one-scoped-contribution-with-a-faithful-summary-and-translations.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-442-CORE_META_MODEL-IMPLEMENTATION_METHOD--an-atom-s-content-expresses-one-scoped-contribution-with-a-faithful-summary-and-translations.md
  source_atom_id: CA-M-442
  source_atom_revision: 5
  source_sha256: 387ecbd0ff775b926865cc09ede7df8a25cb38a578b380f19f4b9c83c4c746ea
  original_relations_sha256: f8518842cf0b787cef6f48ca5728c442c11d261fb493f3cfdd569ac28b834129
---
## Summary

An Atom's content expresses one scoped contribution with a faithful Summary and Translations.

## Claim

### Prose Claim


authoring an Atom's prose CCE primary contribution, its applicability, **and** its derived Summary. The same Claim may contain readable prose and an optional R-only nested Formal claim under the Claim definition.


**to** author one CCE Claim **and** its derived Summary, an Author **must** use these authoring constraints:

- express **`=1`** coherent contribution whose full meaning is covered by one precise Summary using the applicable CCE Content Role profile. carry it under the primary contribution heading registered for the Content Role rather than imposing the literal heading Claim on **every** role.
- resolve **`=1`** Claim Target Scope Unit independently of ownership. select the current Scope Unit as the authoring default **or** an explicitly permitted different target; carry the resolved value under the target Scope Unit carrier definition. express applicability under the applicability carrier definition. for RMED, describe what the Claim applies **to**, including applicable conditions **and** exclusions, **in** Scope; do **not** merely repeat the carried current **or** target Scope Unit; those restrictions alone do **not** make the Atom Relational.
- keep Details within the primary contribution. for RMED, read the Claim within its Scope; Details **must not** change either. **if** supporting content reveals an incomplete **or** inaccurate contribution **or** applicability, revise the affected Scope **or** primary contribution explicitly **and** recheck agreement; do **not** hide the change **in** Details.
- write Summary **only after** the other body sections **and** the contribution review are complete. shorten the finalized primary contribution. use plain wording that expresses the Claim’s meaning. preserve established principle names such as DRY **and** MECE instead of paraphrasing them. a familiar name **or** short instruction **may** be the Summary; do **not** force it into a declarative sentence. for RMED, summarize the Claim within its finalized Scope, **not** the Scope alone; do **not** substitute supporting Results **or** TLDR as the source.
- for an existing Atom, retain the established Summary **and** check its faithfulness; **if** the Summary needs changing, use a new Atom identity under the Atom identity rule.
- derive **every** Translation from the full corresponding source content, **not** the Summary.
