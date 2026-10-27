---
atom_id: CA-D-533@8
content_role: Delivery
type: Eng Decision
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-24 09:42:52 +0400
subjects:
  governs: Subject/Engineering/Project Structure/Request and Result Interface
  depends_on:
  - Subject/Engineering/Project Structure
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Project.Structure
relations:
  relates_to:
  - CA-R-1829
  - CA-R-1832
tier: 3
---
# Summary

Bind PROJECT_STRUCTURE Tool request and result

## Scope

The route-specific `parameters` and `structural_result` boundary for one structural request inside CA-D-527's implementation-facing service interface; it does not designate an undeclared folder as a Scope Unit.

## Claim

Delivery **must** bind typed PROJECT_STRUCTURE `parameters` to CA-D-527's one outer request and bind a structural domain result inside its result, without duplicating CA-D-527 service fields or creating a second Run/Journal contract.

## Details

- D527 supplies the outer mode, route identity, pinned definition bindings, sealed Initiative/authorization, idempotency, preview receipt, service disposition, Run/Event identities, currentness, and retry representation. PROJECT_STRUCTURE supplies only `parameters`: `operation`, target identity, expected TOML revision, exact declaration delta, current reference frontier, and authorized preservation/recovery and Goal-coverage dispositions.
- The authoritative input carrier is `.caprmedio_caprmedio/project_structure.toml`; `authority_path`, `delivery_path`, effective authority mode, and observed implementation/Carrier paths are distinct route result fields.
- `structural_result` contains `state` (`completed`, `no_op`, `stale`, `conflict`, `permission_denied`, `partial`, or `rolled_back`), exact pre/post source revisions, affected/repaired/broken/preserved sets, actual effects, and route evidence references. It is not D527's service disposition or a Workflow Run outcome.
- Preview or unstarted D527 results contain no structural effect and no fabricated Run/Event identity. The implementation path is bound only after independent RMED review; this Delivery Atom grants no write permission or code completion claim.
- The implementation path is to be bound by the implementation task only after independent RMED review; this Delivery Atom grants no write permission or code completion claim.
