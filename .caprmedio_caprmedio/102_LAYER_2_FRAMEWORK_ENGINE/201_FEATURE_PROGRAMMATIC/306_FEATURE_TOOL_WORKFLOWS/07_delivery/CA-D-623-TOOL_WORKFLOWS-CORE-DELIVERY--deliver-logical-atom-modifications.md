---
atom_id: CA-D-623
content_role: Delivery
type: Eng Decision
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/Engineering/Atom Editing/Logical Modification Interface
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
version: 6
updated_at: 2026-10-24 02:14:24 +0400
relations:
  delivery_for:
  - CA-R-1933
  - CA-R-1934
  - CA-R-866
  relates_to:
  - CA-M-373
  - CA-M-374
  - CA-O-202
tier: 4
---
# Summary

Deliver logical Atom modifications

## Scope

Workflow admission owns identity, Version/time, lifecycle and complete schema decisions. Connector calls use CA-D-625 only to verify the supplied request, source preconditions and permission and to perform the explicit mechanical operation. A connector does not choose those decisions.

Required serialization for explicit section, Property and list edits on one logical Atom, inside the existing service and currentness/permission envelope.

## Claim

The workflow supplies an explicit edit operation, exact logical target/value and admitted metadata delta to CA-D-625's modify connector. Atom ID, Version and source-state evidence bind the surrounding Atom; they are not a list-position selector. Workflow admission completely validates every proposed final Atom before an authorized connector effect.

## Details

One section-edit family carries the section identity and operation add, replace, remove, title or position. Add/replace supplies explicit content; title supplies the requested title; position supplies the explicit requested section ordering. Remove names the exact section. Missing or ambiguous sections, conflicting titles/positions and schema-invalid resulting content fail. Section position does not permit positional list replacement.

Property add carries the exact field and value; replace carries field plus exact current old value and explicit new value; remove names the exact field with its expected current state. Required Properties cannot be removed if the resulting Atom is invalid.

For a list Property, one-entry replacement is exactly field, old and new; old is the unique exact current value. Entry addition/removal carries field, operation add/remove and explicit value. Complete-set replacement carries field, operation replace_set, the exact current collection as old and complete proposed collection as new. The workflow's supplied governing field schema decides allowed values and ordering; no implicit entry merge or duplicate acceptance is introduced. Missing, duplicate/ambiguous current values, wrong full-set precondition and caller indexes fail. An implementation may compute an occurrence position after matching the bound current value.

Preserve all unrelated content and exact prior history. The workflow supplies Version/time metadata for every actual changed same-ID edit, including carrier-only, refinement and Status-only, advances Version once and records actual time; no-op retains Version/time. Any Summary change, including wording-only edits, requires separately authorized fresh-ID replacement and predecessor archival; ordinary same-ID Modify rejects it. Type changes also require replacement. Subject-only preview/staging uses these operations only on governs/depends_on, remains separate from generic section/content edits and retains its complete-carrier/pin/permission protections.

### Delivery status

These are required input shapes, not a new CLI binding, admitted MCP route or current implementation claim. Historical indexed fixtures/staging receipts do not prove this revised contract. New workflow resume/retry and stronger concurrency/publication guarantees remain deferred.
