---
content_role: Method
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Draft
subjects:
  governs: PROGRAMMATIC
  depends_on: []
version: 1
updated_at: "2026-10-20 02:50:15 +0400"
relations: {}
---
# Summary

Resolve one provenance-bearing effective model

## Scope

Assembly or load/refresh of the model used by one selected Project.

## Claim

Resolve the Project and applicable source frontier; obtain the protected base, currently activated Extension identities/revisions and Project Configuration. Validate carrier/schema versions, source freshness, references and the selected compatibility/override contract. Bind the candidate to exact observed base, activated Extension and Project Configuration inputs, each identified by revision and byte digest (or an equally exact immutable source reference). Verify that the Project Configuration carrier is admitted for the retained Project identity and override surface. Compose one complete candidate effective model, preserving source meanings and distinguishing additions from explicit overrides. Apply the declared precedence; unresolved precedence or an unauthorized override shall not be resolved by discovery order, filename order or guesswork.

## Details

Record which source supplied every effective value and which declaration permits each override. A cyclic reference is accepted or rejected according to its declared semantics, not a blanket cycle ban. Produce one versioned effective-model generation and its diagnostics, whether it is materialized for consumers or composed by the runtime. Recheck the exact observed input set immediately before selecting the generation; changed inputs return a stale-candidate condition for a new resolution, rather than publishing mixed observations. Publish/select it only after complete validation; an invalid candidate shall never become a partially selected model. For refresh, retain the prior complete generation without silently presenting it as the new one, and report the rejection; whether new operations may continue using that prior generation or must pause is an explicit policy choice. An operation shall retain one model generation through its dependent validation/effects rather than mixing generations mid-operation, while preserving existing freshness/revalidation rules at effects. When no complete usable generation exists, model-dependent operations return an attributable unavailable condition under the existing admission rules. Triggering refresh and changing unsupported engine semantics are separate procedures. This Method creates no new source authority and does not modify the graph-view quartet.
