---
subject_scopes:
  - relation-model
version: 1
updated_at: 2026-08-20 19:57:00
relations:
  child_of:
    - CA-R-806-REQUIREMENT-BSEED_GOVERNANCE--register-complete-relation-kind-metadata
    - CAPRMEDIO-GOV-REQU-767--keep-active-rmed-relations-out-of-archives
---
# Limit active direct relations to upstream or same tier

For every active Atom with derived global tier `N`, each authored direct relation target must be active and have derived global tier less than or equal to `N`. A relation type may narrow this universal boundary to a lower tier, the same tier, or more specific endpoint classes, but must never permit a direct edge from an active source to a target with a greater global tier number. Derived inverse views do not create another authored edge and are not evaluated as direct relations from their displayed source.
