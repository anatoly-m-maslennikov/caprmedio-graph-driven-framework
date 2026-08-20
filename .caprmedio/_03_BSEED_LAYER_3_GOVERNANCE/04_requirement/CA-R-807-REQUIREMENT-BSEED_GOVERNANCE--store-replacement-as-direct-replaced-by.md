---
subject_scopes:
  - relation-model
version: 2
updated_at: 2026-08-20 19:59:00
relations:
  child_of:
    - CA-R-806-REQUIREMENT-BSEED_GOVERNANCE--register-complete-relation-kind-metadata
    - CAPRMEDIO-GOV-REQU-767--keep-active-rmed-relations-out-of-archives
---
# Store replacement as direct replaced_by

Replacement lineage must be authored only as direct `replaced_by` relations from each predecessor Atom to one or more successor Atoms that are already active when the relation is created. The predecessor is archived in the same governed carrier change that adds `replaced_by`. A successor may later become an archived predecessor in another replacement, while the original direct edge remains part of the replacement chain and the current active successor is derived transitively. `replacement_of` is the derived inverse view from a successor to its predecessor and must never be authored in an Atom carrier. Multiple predecessors may name one successor and one predecessor may name multiple successors without changing this storage direction.
