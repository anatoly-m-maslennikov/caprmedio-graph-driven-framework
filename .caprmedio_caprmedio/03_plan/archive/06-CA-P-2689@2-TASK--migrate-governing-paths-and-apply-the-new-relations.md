---
atom_id: CA-P-2689@2
content_role: Plan
type: Plan
label: Task
current_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Model
version: 2
updated_at: 2026-10-29 04:56:21 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2683
tier: 4
---
# Summary

Migrate governing paths and apply the new Relations

## Objective

Mechanically migrate the selected Current Atoms’ Subjects to the new Model and relation notation, before adopting replacement content.

## Details

Stage 1, after P2684. Migrate subjects.governs first, then the dependency Subjects. Use the approved paths/operators and the thin tracking rows; update statuses from planned/drafted to applied only after readback of actual Current files.

This pass changes Subjects and the normal identity/version/timestamp/carrier lifecycle metadata required by an update. It does not rewrite Summaries, Claims, Semantics or Details, adopt replacement content, or add a new domain kind. Preserve each predecessor through the established archive process. Keep direct facts singular and inverse views derived; migrating notation is not permission to infer new relations.

Do not depend on P2688 adoption or completion of all entity Definitions. A defining Atom may introduce its governed entity/path; prior existence is not a basic string-format requirement. Hold only genuinely unmapped cases and continue independent supported rows. Record any old literal Model path inside content for the later replacement/Definition pass rather than expanding this mechanical pass.

## Definition of Done

Every selected Governs and dependency row has an applied or explicit held disposition; applied rows match the reviewed Model/notation on readback. Content is preserved apart from normal lifecycle metadata. Held cases remain visible and must be resolved before final closure.

## Progress

Not executed. No Current Subject migration is inferred from prepared Drafts or review results.
