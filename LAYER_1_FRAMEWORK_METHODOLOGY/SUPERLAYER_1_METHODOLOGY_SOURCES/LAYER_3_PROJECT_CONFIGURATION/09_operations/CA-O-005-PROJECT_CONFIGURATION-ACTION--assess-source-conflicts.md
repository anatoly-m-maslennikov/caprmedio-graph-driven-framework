---
subjects:
  governs: "Assess Source Conflicts"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Entity/Node/Continuant/Atom", "Entity/Node/Continuant/Atom.Substance", "Entity/Node/Continuant/Atom.Global Tier", "Entity/Node/Continuant/Atom.Updated At", "Entity/Node/Continuant/Atom.Local Tier: Principle", "Entity/Node/Continuant/Actor/Type: Operator"]
version: 12
updated_at: "2026-10-19 15:56:26 +0400"
relations: {}
atom_id: "CA-O-005"
content_role: "Operations"
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
---
# Summary

Assess source conflicts

## Operation

Assess Source Conflicts **means** the reusable Action that assesses one exact selected source frontier against its applicable authority **and** returns the conflict assessment **without** changing sources.

1. load the current accepted active authority **and** applicable Project Principles **before** relying on an earlier report **or** proposed fix.
2. identify the conflicting Claims **and** their applicability. for RMEDO Atoms, collect Global Tier, exact Revision, **and** Updated At. distinguish an actual conflict from different permitted cases.
3. for RMEDO conflicts, preserve higher-tier authority, whose Global Tier number is lower. within the applicable authority boundaries, prefer the freshest accepted active Claim over a conflicting older Claim; Updated At **must not** permit a lower-tier Claim **or** prohibited source override **to** defeat higher-tier authority.
4. check **every** proposed disposition against the active Principles **and** retain the evidence for its effect on alignment. a conflict between active Principles requires the Operator under CA-R-1551.
5. distinguish resolved, unresolved, **and** unevaluated conditions. report missing checks, uncertain applicability, equal **or** ambiguous timestamps, **and** unresolved authority **without** inventing precedence.
6. verify required resolution evidence against the exact proposal **and** current source frontier. missing, stale, partial, ambiguous, **or** mismatched approval **or** delegation does **not** resolve a conflict.

7. check affected authority coverage, including still-required Claims, active references **and** Relations, **and** required Evaluations. report an unresolved gap separately from a resolved conflict; absence of a conflict does **not** prove complete coverage.

this Action **must not** synthesize **or** merge Claims, treat an LLM judgment as Operator authorization, change source **or** projected content, **or** silently exclude a conflicting source from the assessment.

## Details
