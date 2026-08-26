---
artifact_subtype: question
subjects:
  - artifact-catalog
priority: high
version: 4
updated_at: 2026-08-23 01:44:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  concern_about:
    - CAPRMEDIO-META-REQU-113--coordinate-artifacts-without-an-81-type-bijection
    - CAPRMEDIO-GOV-REQU-317--register-evaluation-atom-subtypes
    - CAPRMEDIO-GOV-REQU-318--register-concern-atom-subtypes
    - CAPRMEDIO-GOV-REQU-321--register-caprmedio-atom-type-surface
    - CAPRMEDIO-GOV-REQU-332--register-ops-subtypes
    - CAPRMEDIO-GOV-REQU-343--register-plan-subtypes
    - CAPRMEDIO-GOV-REQU-357--register-implementation-decision-method-subtype
    - CAPRMEDIO-GOV-REQU-385--resolve-artifact-routes-from-governed-authority-and-project-settings
---

# Question — Which artifact subtypes should refine route types?

Which additional direct subtypes, if any, should express finer meanings beyond
the vocabularies currently registered by CAPRMEDIO GOVERNANCE?

The answer must:

- evaluate each proposed semantic name as a subtype candidate;
- assign each accepted subtype to exactly one canonical parent type;
- keep subtype depth at one;
- require every subtype to inherit its parent's complete route;
- avoid duplicate meanings across sibling or unrelated subtypes;
- preserve distinct identity and numbering only where the distinction is
  operationally useful.

This Question does not authorize subtype creation. Current registered subtypes
remain authoritative, and every addition requires a separate accepted GOVERNANCE
Atom.
