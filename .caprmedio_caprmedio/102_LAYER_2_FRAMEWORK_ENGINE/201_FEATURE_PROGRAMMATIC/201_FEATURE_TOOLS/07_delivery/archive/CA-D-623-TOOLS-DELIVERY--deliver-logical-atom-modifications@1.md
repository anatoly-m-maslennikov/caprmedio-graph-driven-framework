---
atom_id: CA-D-623
content_role: Delivery
type: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool"
  depends_on: ["Atom","Workflow"]
version: 1
updated_at: "2026-10-12 23:13:13 +0400"
relations:
  delivery_for: ["CA-R-1933","CA-R-1934","CA-R-866"]
  relates_to: ["CA-M-373","CA-M-374","CA-O-202"]
---
# Summary

Deliver logical Atom modifications

## Scope

Required serialization for explicit section, Property and list edits on one logical Atom, inside the existing service and currentness/permission envelope.

## Claim

The caller chooses an edit operation and its exact logical target/value. Atom ID, Version and source-state evidence bind the surrounding Atom; they are not a list-position selector. Every proposed final Atom is completely validated before an authorized effect.

## Details

One section-edit family carries the section identity and operation add, replace, remove, title or position. Add/replace supplies explicit content; title supplies the requested title; position supplies the explicit requested section ordering. Remove names the exact section. Missing or ambiguous sections, conflicting titles/positions and schema-invalid resulting content fail. Section position does not permit positional list replacement.

Property add carries the exact field and value; replace carries field plus exact current old value and explicit new value; remove names the exact field with its expected current state. Required Properties cannot be removed if the resulting Atom is invalid.

For a list Property, one-entry replacement is exactly field, old and new; old is the unique exact current value. Entry addition/removal carries field, operation add/remove and explicit value. Complete-set replacement carries field, operation replace_set, the exact current collection as old and complete proposed collection as new. The governing field schema decides allowed values and ordering; no implicit entry merge or duplicate acceptance is introduced. Missing, duplicate/ambiguous current values, wrong full-set precondition and caller indexes fail. An implementation may compute an occurrence position after matching the bound current value.

Preserve all unrelated content and exact prior history. Every actual changed same-ID edit, including carrier-only, refinement and Status-only, advances Version once and records actual time; no-op retains Version/time. Any Summary change, including wording-only edits, requires separately authorized fresh-ID replacement and predecessor archival; ordinary same-ID Modify rejects it. Type changes also require replacement. Subject-only preview/staging uses these operations only on governs/depends_on, remains separate from generic section/content edits and retains its complete-carrier/pin/permission protections.

### Delivery status

These are required input shapes, not a new CLI binding, admitted MCP route or current implementation claim. Historical indexed fixtures/staging receipts do not prove this revised contract. New workflow resume/retry and stronger concurrency/publication guarantees remain deferred.
