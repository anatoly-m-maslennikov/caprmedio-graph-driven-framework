---
atom_id: CA-D-535@13
content_role: Delivery
type: Eng Decision
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 13
updated_at: 2026-10-26 05:59:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Verification/Test Data
  depends_on:
  - Subject/Graph Node/Engineering/Project Structure
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Continuant/Project.Structure
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Evaluation'
relations: {}
tier: 3
---
# Summary

Bind PROJECT_STRUCTURE functional fixture boundary

## Scope

The disposable-project input/output boundary for the four golden functional cases, including the one shared CA-D-527 request/result interface.

## Claim

Delivery **must** provide an isolated project fixture whose authoritative TOML, reference/Carrier observations, one CA-D-527 request/result, route `structural_result`, and preservation/breakage assertions are inspectable independently.

## Details

- Fixture input includes declared Ordered and Unordered siblings, nonempty labels, structural levels, navigational numbers, explicit and inherited authority modes, known incoming references, parent-owned attachments, observed Carrier content, captured TOML revision, and an explicit direct-parent Goal-coverage disposition for Create/Move.
- Fixture output preserves pre/post TOML text or revision, the exact D527 service result and separate `structural_result`, actual effect set, unchanged unrelated content check, and available Workflow/Action/Journal evidence references. It includes the default-preview/no-effect, unstarted-denial/no-effect, successful explicit-execute, and partial/authorized-rollback cases from CA-E-549/551/552 without a duplicate route envelope.
- This is a future implementation/test delivery boundary; saved RMED does not claim a runtime fixture or a passing functional run.
