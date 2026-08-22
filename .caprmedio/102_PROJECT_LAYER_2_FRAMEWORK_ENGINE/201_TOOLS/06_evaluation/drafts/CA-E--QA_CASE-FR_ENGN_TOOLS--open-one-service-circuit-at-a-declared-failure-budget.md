---
subject_scopes:
  - background-services
  - failure-recovery
version: 1
updated_at: 2026-08-22 02:30:28
relations: {}
---
# Open one service circuit at a declared failure budget

Given a configured consecutive-failure budget and queued work, return the same classified worker failure until the budget is exhausted. Verify each budget check records `satisfied`, `violated`, `unknown`, or `error`; the final violation opens the circuit, pauses new autonomous dispatch, preserves queued work, exposes the cause and recovery action through status, and does not enter an automatic restart or resume loop.

The case fails if a missing or erroneous check is treated as success, work is discarded, dispatch continues beyond the budget, or recovery occurs without the declared cooldown, health, and failure-classification conditions.

Candidate alignment: CA-E-001, CA-E-002, CA-R-004, CA-R-815, CA-R-846, CA-R-861.

## Sources

- [Python documentation: exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Python documentation: asyncio synchronization primitives](https://docs.python.org/3/library/asyncio-sync.html)
