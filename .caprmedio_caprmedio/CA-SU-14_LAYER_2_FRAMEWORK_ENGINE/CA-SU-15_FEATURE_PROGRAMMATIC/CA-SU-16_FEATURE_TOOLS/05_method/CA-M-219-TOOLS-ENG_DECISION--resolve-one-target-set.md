---
atom_id: CA-M-219
ref_id: CA-M-219
container:
  scope_unit: CA-SU-16
role: Method
form: Eng Decision
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Source Selection"
tier: 2
relations:
  method_for:
  - CA-R-1153
  derived_from:
  - CA-A-058
status: Active
version: 24
updated_at: 2026-11-02 19:46:47 +0400
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Resolve one target set

## Applicable when

use this Method **when** `TARGET_SET` **must** resolve identities **or** governed selectors **before** another Tool checks **or** changes the targets.

## Procedure

1. confirm that `TARGET_SET` is registered as one `unordered_unit` Finder owned immediately by `TOOLS` at Structural level `4`, with prefix `TARGET_SET`, address `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/TARGET_SET`, **and** realization path `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/TARGET_SET/`.
2. resolve the supplied explicit identities **and** composable governed selectors against the current project frontier.
3. deduplicate the resolved members **and** order them by the registered stable ordering rule.
4. seal membership, source frontier, **and** content digest together as one target-set identity.
5. return the sealed set read-only **to** a named downstream Tool **without** evaluating **or** changing **any** target; reject an invalid unit boundary, unresolved selector, ambiguous identity, missing member, **or** changed frontier.

## Outcome

one `TARGET_SET` result **contains** exactly its stable ordered membership, source frontier, **and** content digest for downstream checking **or** change.

## Failure or stop

do **not** mutate targets, execute Evaluations, create change plans, **or** rebuild Projections; return an explicit unresolved **or** stale result instead.
