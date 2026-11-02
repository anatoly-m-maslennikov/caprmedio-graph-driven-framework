---
atom_id: CA-E-635@8
content_role: Evaluation
type: Eval Case
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Engineering/Pure TOML Materialization Conformance Evaluation
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Governing Configuration
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - Subject/Graph Node/Engineering/TOML Configuration Value
version: 8
updated_at: 2026-10-25 17:32:27 +0400
relations:
  evaluation_for:
  - CA-R-1936
  - CA-M-383
  - CA-D-632
  - CA-O-204
  depends_on:
  - CA-E-254
tier: 6
---
# Summary

verify lossless pure TOML materialization

## Scope

independent acceptance of the private pure TOML materializer selected by CA-M-383 **and** delivered under CA-D-632. these are required checks, **not** executed results **or** receiving Workflow acceptance.

## Claim

the pure materializer passes **only** **when** independently authored source/proposed byte ledgers **and** complete native type/value observations prove the exact explicit delta, unchanged unrelated content, exact no-op **and** truthful refusal under accepted CA-R-1936 **and** CA-O-204 authority.

## Details

### Required cases

1. supply literal LF **and** CRLF documents with unrelated comments, whitespace, quoted/dotted keys, tables **and** native typed values. compare complete proposed bytes **and** complete parsed values/types against independent expected ledgers for supported add, replace **and** remove edits. no production planner, serializer **or** returned digest supplies the expected result.
2. exercise item/value edits selected by a unique exact current value, **not** a caller index. compare the selected change **and** remaining collection content/trivia. a missing, duplicate **or** ambiguous selected value refuses; an item edit **must not** replace the complete collection. exercise explicit full-set add, replace **and** remove separately, preserving bytes outside that supplied collection effect.
3. prove exact byte-identical no-op **when** the requested state is already satisfied, including equivalent source spellings. retain native type distinctions; Boolean, integer **and** floating-point values **must not** be silently conflated. no-op returns no effective diff, write, revision **or** timestamp.
4. reject malformed/duplicate TOML, malformed delta/key bindings, unsupported values, incomplete results **and** a baseline parse/serialization round trip that changes bytes. refuse normalization **or** a lossy representation rather than widen the delta. reparse the complete proposed document; valid syntax alone does **not** prove the expected values/types **or** preservation.
5. deliberately introduce wrong proposed bytes, an extra unrelated edit, a missing/extra effective diff **and** a wrong value type; each independent oracle **must** detect the wrong output. compare supplied mutable inputs **before** **and** **after** supported, no-op **and** refused calls.
6. deny filesystem effect APIs during pure calls **and** verify no source/history/runtime mutation. require a truthful unsupported/refusal outcome **when** a safe representation cannot be established. check the current selecting Method, exact canonical dependency/lock pins **and** complete CA-E-254 exception evidence; source approval **or** an upstream library description is **not** actual execution evidence.

### Evidence and disposition

record exact accepted contract, configuration, lock, code **and** test pins with actual command/interpreter/dependency version, positive/negative outcomes **and** observed limits. implementation **and** execution results are PENDING at source authoring; missing **or** unavailable evidence does **not** pass. reject byte/type drift, whole-document normalization, widened effects, producer-derived expected output **or** incomplete dependency admission; retain the concrete failed observations for correction.

this check does **not** accept public TOML value encoding, configuration-specific schema/permission bindings, storage writes, history, selected-service recording, installed runtime, live routing **or** Core migration. those remain separately governed integration **and** verification work.
