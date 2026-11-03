---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Projection/(.Form: Implementation Overview)'
  passive:
  - CAPRMEDIO_MODEL <+ Projection
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Term//Artifact
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Traceability
  - CAPRMEDIO_MODEL <+ Journal
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Package/Project Implementation
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
version: 40
updated_at: 2026-11-02 18:35:20 +0400
relations: {}
atom_id: CA-R-1703
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Use Implementation Overview as a Projection

## Claim

### Prose Claim


Implementation Overview Projections.


an Implementation Overview is a non-authoritative Projection of what the current normative Atom frontier, native project targets, available provenance, **and** **any** registered implementation lineage sources show as implemented. its Implementation Bindings derive from the shared Project Journal under CA-R-1695; the current view does **not** replace the historical implementation event records retained **in** that Journal. the Atom Content Role axis does **not** apply **to** this Projection.

it **may** report realization coverage, source-to-target bindings, relevant commits, **and** unresolved implementation gaps. it is regenerated mechanically **or** rebuilt through governed reasoning from its declared source frontier. it is never an Atom **and** cannot replace the Journal, normative Atoms, native implementation, Operations evidence, **or** Verification.

the presence of this Projection does **not** require an internal Implementation Atom. storage, retention, **and** whether the Projection is committed **or** generated at runtime remain governed separately.

## Details

CAPRMEDIO represents the current view of project realization through an Implementation Overview Projection rather than an Implementation Atom.
