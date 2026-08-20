---
subject_scopes:
  - relation-model
version: 1
updated_at: 2026-08-20 19:56:00
relations:
  child_of:
    - CA-R-806-REQUIREMENT-BSEED_GOVERNANCE--register-complete-relation-kind-metadata
    - CAPRMEDIO-GOV-REQU-767--keep-active-rmed-relations-out-of-archives
---
# Store replacement as direct replaced_by

Replacement lineage must be authored only as direct `replaced_by` relations from each predecessor Atom to one or more already active successor Atoms. The predecessor is archived in the same governed carrier change that adds `replaced_by`, so the resulting direct edge runs from archived history to active authority. `replacement_of` is the derived inverse view from a successor to its predecessor and must never be authored in an Atom carrier. Multiple predecessors may name one successor and one predecessor may name multiple successors without changing this storage direction.
