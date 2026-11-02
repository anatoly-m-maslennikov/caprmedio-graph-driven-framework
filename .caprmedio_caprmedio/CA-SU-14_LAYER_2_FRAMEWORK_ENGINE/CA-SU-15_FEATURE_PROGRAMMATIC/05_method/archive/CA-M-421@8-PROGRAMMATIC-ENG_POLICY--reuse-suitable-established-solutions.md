---
atom_id: CA-M-421@8
content_role: Method
type: Eng Policy
current_scope_unit: PROGRAMMATIC
status: Archived
subjects:
  governs: Subject/Graph Node/Engineering/Authoring/Code Authoring
  depends_on:
  - Subject/Graph Node/Engineering/Authoring/Code Authoring
version: 8
updated_at: 2026-10-27 06:04:45 +0400
author: Anatoly Maslennikov
tier: 3
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
