---
atom_id: CA-E-648@7
content_role: Evaluation
type: Policy
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Archived
author: Anatoly Maslennikov
version: 7
updated_at: 2026-10-24 02:14:24 +0400
subjects:
  governs: Subject/Engineering/Pure Computation and Recording Boundary
  depends_on:
  - Subject/Engineering/Business Workflow Lifecycle Recording
relations:
  evaluation_for:
  - CA-M-426
  - CA-M-399
tier: 5
---
# Summary

Evaluate pure effects and business recording

## Scope

PROGRAMMATIC functions, methods, Tools, workflows and lifecycle paths that compute decisions, apply effects or record technical and business history.

## Claim

Accept the boundary only when pure computations have no hidden I/O or event emission. Explicit external effects belong to effect owners and cannot become pure merely through a name or wrapper. Technical diagnostics stay on stdout/stderr, business lifecycle records are written to the Journal, preflight does not invent a business Run, and failure to record a business event is reported independently without invalidating an already applied effect.

## Details

- Invoke pure transformations with controlled inputs and observe no file, network, time, process, database, Journal or log effects.
- Verify any operation that needs such an effect is owned by an explicit effect boundary rather than labeled as pure.
- Observe effect owners separately and verify each effect has a target, precondition and completion fact.
- Trigger technical warnings and runtime failures and verify they are not fabricated business records.
- Trigger workflow lifecycle events and verify Journal records contain only business events with the correct initiative and run identity.
- Simulate a Journal or diagnostic sink failure after a valid effect and verify the effect result remains truthful while record failure uses its own channel.
