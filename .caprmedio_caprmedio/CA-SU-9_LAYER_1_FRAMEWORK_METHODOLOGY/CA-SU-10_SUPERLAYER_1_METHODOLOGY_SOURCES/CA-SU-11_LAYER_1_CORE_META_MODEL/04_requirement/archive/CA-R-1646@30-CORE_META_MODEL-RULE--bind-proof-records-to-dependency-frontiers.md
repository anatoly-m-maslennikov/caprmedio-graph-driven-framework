---
subjects:
  governs: Subject/Graph Node/Engineering/Outcome Evidence
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Term//Artifact
  - Subject/Graph Node/Engineering/Execution Identity/Source Binding
  - Subject/Graph Node/Domain/Continuant/Projection
  - Subject/Graph Node/Engineering/Continuant/Carrier
version: 30
updated_at: 2026-10-25 17:32:27 +0400
relations:
  resolution_of:
  - CAPRMEDIO-GOV-CONC-054--how-should-proof-currentness-be-represented
  relates_to:
  - CA-D-329
atom_id: CA-R-1646@30
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Rule
---
# Summary

Bind proof records to dependency frontiers

## Scope

governed proof records, their applicable inputs, and all selected Workflows, release policies, and version-control mechanisms.

## Claim

**every** governed proof record **must** bind its observation **to** the exact applicable inputs under which it was produced.

- the binding includes the relevant Artifact **and** Implementation Revisions, configuration, evaluators, environments, **and** material inputs; CA-D-329 governs its representation.
- reliance on that observation for a current candidate requires a matching input binding **and** satisfaction of its additional governing invalidation conditions.
- a changed material input makes the affected proof stale for that candidate **until** the required checks run against the changed inputs. a missing **or** unresolved binding is unknown, **not** current.
- an unrelated change does **not** invalidate proof **unless** it changes the evaluated dependencies **or** satisfies an additional governing invalidation condition.
- retain the historical record unchanged. **not** (a recent timestamp **or** a refreshed Projection) alone proves currentness.

## Details
