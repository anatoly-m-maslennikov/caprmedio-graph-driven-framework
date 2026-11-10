---
atom_id: CA-D-510
ref_id: CA-D-510
container:
  scope_unit: CA-SU-24
role: Delivery
form: Decision
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality
    <+ Traceability
  dependencies:
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Role := Evaluation)
  - MODEL//CAPRMEDIO <+ Atom
  - MODEL//CAPRMEDIO <+ Atom.Header.ID
  - MODEL//CAPRMEDIO <+ Atom.Header.Version
  - MODEL//CAPRMEDIO <+ Execution/Workflow Run
  - MODEL//CAPRMEDIO <+ Term//Property
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling
    <+ Serialization
tier: 3
status: Active
version: 18
updated_at: 2026-11-10 20:47:54 +0400
carrier_destination:
  file:
    name: CA-D-510-PROMPTS-DECISION--serialize-review-coverage-and-correction-outcomes-separately.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-24_FEATURE_PROMPTS/07_delivery
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
author: Anatoly Maslennikov
---

## Summary

Serialize review coverage and correction outcomes separately

## Claim

### Prose Claim

the Implementation **must** serialize initial check evidence, applied corrections, **and** derived completion **in** separate fields within the report layout governed by CA-D-496-CORE_META_MODEL--store-one-review-report-per-source-atom.

## Details

### Scope

temporary JSON reports **and** progress records emitted by the RMED review prompt Implementation.

| Record | Field | Encoding |
|---|---|---|
| report | `source` | object containing the checked path, Version, **and** SHA-256 digest |
| report | `atom_id` | checked Atom ID |
| report | `workflow_run_id` | the caller's Run ID, retained through checking, correction, **and** handoff |
| report | `criteria_sha256` | the supplied shared checking-packet digest, linked **to** its exact rule bindings; retain that digest rather than hashing a different subset |
| report | `checks` | object keyed by `properties`, `cce`, `scope`, `claim`, `details`, **and** `summary`; **every** entry carries `status` **and** evidence **or** a reason |
| report | `findings`, `blockers` | separate arrays of confirmed findings **and** incomplete check coverage |
| report | `corrections`, `rejected_findings`, `unresolved_findings` | separate arrays retaining the disposition of findings; a completed fix carries an explicit empty `unresolved_findings` array |
| report | `fix_blockers` | correction blockers, distinct from incomplete initial check coverage |
| report | `result` | recorded check **or** fix result |
| progress item | `reported_result` | retained report result |
| progress item | `check_complete` | Boolean for completion of **all** required initial checks |
| progress item | `complete` | Boolean for completion of this Atom's admitted work |
| progress item | `state` | derived state that retains `blocked` for unresolved coverage **or** findings |
| progress total | `total`, `reported`, `checked`, `completed`, `complete`, `states` | selection size, report count, complete-check count, completed-Atom count, aggregate Boolean, **and** state counts |

initial check outcomes remain preserved **after** correction. `fixed_not_rechecked` **or** an approved `replaced_not_rechecked` result does **not** overwrite blocked check evidence **or** independently set `complete` **to** true.

**every** finding has a stable per-report identifier **or** fixed array index. corrections, rejections, **and** unresolved dispositions reference those findings explicitly; a correction **may** address multiple identified findings. a finding omitted from **all** dispositions remains unresolved. retain correction blockers separately so that a fully performed check remains distinguishable from an unauthorized **or** unfinished fix.
