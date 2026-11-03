---
subjects:
  active: CAPRMEDIO_MODEL <+ Term
  passive:
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Authoring <+ Controlled English
  - CAPRMEDIO_MODEL <+ Scope Unit.Name
  - CAPRMEDIO_MODEL <+ Actor
  - CAPRMEDIO_MODEL <+ Carrier/File.Main Content.CCE Operator
version: 33
updated_at: 2026-11-02 18:35:20 +0400
relations: {}
atom_id: CA-M-229
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Method
form: Implementation Method
---
## Summary

Render Governed Terms and CCE Operators Distinctly

## Claim

### Prose Claim


CAPRMEDIO content lexical-case rendering.


**to** render CAPRMEDIO content, the Author **must** apply the following lexical-case rules:

- start **every** Governed Term with a capital letter.
- start **every** General Term with a lowercase letter.
- preserve the lowercase spelling of **every** ordinary English word at the start of a sentence **or** list item **unless** an active rule requires an exact-case token.
- preserve the required case of canonical Terms, Scope Unit Names, **and** exact registered references, including at sentence **and** list-item starts.
- preserve the canonical spelling of **every** registered CCE Operator. use CA-D-280 for its representation **in** Markdown Atom Carrier Main Content.
