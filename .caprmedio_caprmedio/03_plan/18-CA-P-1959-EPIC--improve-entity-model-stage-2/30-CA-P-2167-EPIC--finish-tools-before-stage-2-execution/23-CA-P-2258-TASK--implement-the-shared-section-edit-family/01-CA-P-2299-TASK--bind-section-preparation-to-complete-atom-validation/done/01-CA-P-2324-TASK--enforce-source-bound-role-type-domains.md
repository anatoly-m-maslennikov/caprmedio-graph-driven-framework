---
atom_id: CA-P-2324
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Tool
  depends_on: [Atom, Property, Plan]
version: 2
updated_at: "2026-10-13 19:25:32 +0400"
relations:
  is_decomposition_of: [CA-P-2299]
---
# Summary

Enforce source-bound role Type domains

## Objective

The proposed-carrier boundary uses the existing generic role/Type domain check and refuses invalid or unbound Type combinations.

## Details

Estimated own work: up to 15 minutes; split further work before exceeding the bound. Bind the existing model.domains check to its finite current source closure. Compare prior/current domain contributions before refreshing exact source pins and fixtures; no domain policy changes, legacy fallback or blanket repinning. Missing or semantically conflicting current authority requires a separate disposition.

Verify all supported role/Type combinations and invalid combinations, including Plan/Action, and missing/stale Type authority refusal. Preserve valid separately admitted extensions and existing non-Type checks. Remove the section regression's expected-failure marker only after the real shared check rejects it. Independently review the implementation and exact unchanged domain evidence. Root owns Git and Plans; serialize shared manifest edits.

No source Atom migration, new Type values, write route, installed activation or claim of full-project source validity.

### Acceptance

Independent acceptance passes: all 19 exact source bindings and 20 mirrors checked, Type tests 4/4, validator 316/316, relation tests 7/7, and the section portfolio 34/34 without expected failures. See .caprmedio_caprmedio/_projection/core-entity-review/stage2/tools-first/section-preparation-and-type-admission-acceptance.md. This closes only generic role/Type admission; no receiver, publication or full-checkout validity is inferred.

### Definition of Done

The Plan is **not** Done if any supported role's declared Type domain is omitted to pass a narrower fixture; exact source admission or independent checks are missing; the invalid Plan/Action still passes; existing valid Types fail; or stale/missing authority is silently accepted.
