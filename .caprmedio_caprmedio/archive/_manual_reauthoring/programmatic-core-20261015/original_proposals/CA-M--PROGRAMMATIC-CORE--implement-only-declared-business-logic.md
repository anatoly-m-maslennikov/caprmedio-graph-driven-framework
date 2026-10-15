---
content_role: Method
current_scope_unit: PROGRAMMATIC
local_tier: Core
global_tier: 6
status: Draft
author: Anatoly Maslennikov
subjects:
  governs: "programmatic software"
  depends_on: [Implementation]
version: 1
updated_at: "2026-10-15 22:01:28 +0400"
---
# Summary

Implement only declared business logic

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and tests.

## Claim

**To** implement PROGRAMMATIC behavior, realize **only** the business rules declared by applicable Active RMED, while choosing ordinary implementation details freely within those rules.

## Details

- Do not add implicit policies, restrictions, approval gates, lifecycle rules or Workflows, including through tests.
- Resolve a behavior-changing gap or conflict with the Operator and align affected RMED before implementing that decision.
- Algorithms, function layout and internal data structures need no separate policy when they preserve declared behavior and constraints.

Source basis: CA-M-384.
