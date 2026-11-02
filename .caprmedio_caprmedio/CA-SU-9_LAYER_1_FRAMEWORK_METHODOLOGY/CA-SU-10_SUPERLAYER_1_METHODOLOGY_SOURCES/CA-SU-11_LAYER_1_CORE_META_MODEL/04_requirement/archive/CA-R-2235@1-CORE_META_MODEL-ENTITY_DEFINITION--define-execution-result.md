---
atom_id: CA-R-2235@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Object/Occurrent/Execution.Result
  depends_on:
  - Entity/Object/Occurrent/Execution
  - Entity/Aspect/Engineering/Architecture/Communication/API/Result Contract
version: 1
updated_at: 2026-10-29 07:32:39 +0400
relations: {}
tier: 1
---
## Summary

Define Execution Result

## Claim

Execution.Result is data actually produced by that execution, including returned values and observed-effect information when provided. It belongs to the execution rather than to an API contract. A Journal Event Record can preserve the result or describe it without becoming the execution itself.

### Formal claim

```text
Execution.Result
```

## Semantics

For an Update Atom execution, the result can state which Atom version was created or archived. The API contract can specify the shape and meaning of that data; it does not prove that the change happened. An actual failure result is not evidence of successful completion.

## Details

CA-A-1276 records the Operator decision. Numeric identity, property formats/counts and Current adoption remain pending; this does not implement a result envelope or Journal writer.
