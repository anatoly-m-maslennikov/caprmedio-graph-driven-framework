---
atom_id: CA-C-548@1
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
priority: low
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-P-2401, CA-P-2478]
version: 1
updated_at: "2026-10-20T20:09:27.691Z"
---
# Summary

Reduce retained lifecycle typing debt

## Concern

An additional lifecycle-only strict Mypy diagnostic reports 28 retained errors. Do not describe the current lifecycle module as type-clean or weaken validation to silence typing. This is follow-up source-quality debt, not evidence of a production incident or a new regression from the P2478 extraction.

## Evidences

Root compared exact HEAD 0fbe62afe07fd1f6af62f891ea770c62bb619a3b lifecycle source in memory with frozen lifecycle SHA-256 568516545c8bbd870d9022d157bcdb6382a394da46420458251cd341a7aff4ea. Both report 28 strict errors, with identical message multiset after normalizing only changed source line references. No new diagnostic remains. The temporary helper-marker type and recovery-history inference regressions were corrected before this comparison.

The equivalent diagnostic options were strict, Python 3.14, follow-imports silent, no incremental cache, explicit lifecycle target, and its source directory as MYPYPATH. The checked-in default Mypy files target covers VALIDATE_ATOMS, not this broader module; this supplementary result does not assert that a configured release type gate failed. Examples include existing optional-value narrowing, duplicate local annotations and ExistingDraftPromotion represented as object.

## Blast radius

Retained static typing confidence in lifecycle_intents.py. No broad refactor or new type-gate policy is authorized here. Future work must preserve exact behavior/history/recovery and remain separately bounded with functional evidence. This Problem remains Active; P2478 may close its narrower new-complexity and no-new-diagnostic obligation without claiming all legacy debt resolved.
