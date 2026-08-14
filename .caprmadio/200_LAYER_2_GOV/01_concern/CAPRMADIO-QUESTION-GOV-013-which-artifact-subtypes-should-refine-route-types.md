---
artifact_type: concern
artifact_subtype: question
artifact_id: CAPRMADIO-QUESTION-GOV-013
scope_path: layer:gov
subject_scopes:
  - artifact-catalog
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-089
      - CAPRMADIO-REQUIREMENT-GOV-136
      - CAPRMADIO-REQUIREMENT-GOV-138
      - CAPRMADIO-REQUIREMENT-GOV-139
      - CAPRMADIO-REQUIREMENT-GOV-140
      - CAPRMADIO-REQUIREMENT-GOV-141
      - CAPRMADIO-REQUIREMENT-GOV-143
      - CAPRMADIO-REQUIREMENT-GOV-102
---

# Question — Which artifact subtypes should refine route types?

Which additional direct subtypes, if any, should express finer meanings beyond
the vocabularies currently registered by CAPRMADIO GOV?

The answer must:

- evaluate each proposed semantic name as a subtype candidate;
- assign each accepted subtype to exactly one canonical parent type;
- keep subtype depth at one;
- require every subtype to inherit its parent's complete route;
- avoid duplicate meanings across sibling or unrelated subtypes;
- preserve distinct identity and numbering only where the distinction is
  operationally useful.

This Question does not authorize subtype creation. Current registered subtypes
remain authoritative, and every addition requires a separate accepted GOV
Atom.
