---
atom_id: CA-M-421@1
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Archived
subjects:
  governs: "Method/Established Solution Reuse"
  depends_on:
    - "Method/Necessity"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
author: Anatoly Maslennikov
---
# Summary

Reuse suitable established solutions

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and tests.

## Claim

**To** implement declared PROGRAMMATIC behavior, prefer well-adopted, well-suited existing libraries, approaches and tools over reimplementing their mechanics; use custom mechanics **when** existing solutions cannot meet a declared requirement **or** the custom choice provides a concrete benefit.

## Details

Candidate source: [CA-M-391@2](archive/CA-M-391-PROGRAMMATIC-CORE--reuse-suitable-established-solutions@2.md)

- Check existing Project capabilities and established solutions for actual fit, not popularity alone.
- Consider the complexity and dependency cost introduced by the choice.
- Keep custom work limited to the unmet requirement or demonstrated benefit. This Method selects no mandatory product or technology.

The Operator explicitly selected reuse of well-adopted and suitable libraries, approaches and tools instead of reinventing the wheel on 2026-10-15.
