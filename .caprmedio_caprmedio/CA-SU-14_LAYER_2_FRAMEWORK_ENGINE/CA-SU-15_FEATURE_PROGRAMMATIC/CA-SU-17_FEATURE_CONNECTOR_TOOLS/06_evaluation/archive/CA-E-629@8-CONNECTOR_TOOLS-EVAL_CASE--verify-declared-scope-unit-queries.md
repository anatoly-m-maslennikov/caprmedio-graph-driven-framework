---
atom_id: CA-E-629@8
content_role: Evaluation
type: Eval Case
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
status: Archived
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-24 12:35:51 +0400
subjects:
  governs: Subject/Domain/Node/Continuant/Scope Unit
  depends_on:
  - Subject/Domain/Node/Continuant/Project
  - Subject/Engineering/Project Structure Declaration
  - Subject/Engineering/Project Settings Snapshot
relations:
  relates_to:
  - CA-R-1937
  - CA-M-377
  - CA-D-626
  - CA-O-211
  - CA-R-1936
  - CA-M-376
  - CA-E-628
  - CA-D-625
  - CA-R-1484
  - CA-D-442
tier: 3
---
# Summary

Verify declared Scope Unit queries

## Scope

Future conformance evaluation of CA-R-1937-CONNECTOR_TOOLS-RULE--query-declared-scope-units, CA-D-626-CONNECTOR_TOOLS-ENG_DECISION--deliver-declared-scope-unit-query-data and CA-O-211-CONNECTOR_TOOLS-ACTION--query-declared-scope-units.

## Claim

a Scope Unit Query implementation passes this Evaluation **only** **when** independently authored inputs, reopened declared-source evidence **and** actual results show exact matching, complete truthful coverage **and** no mutation. missing implementation **or** observations is unavailable evidence, **not** a pass.

## Details

Use a bound Project Settings root and a valid Project Structure fixture with two sibling units, an Ordered child with Local Order, an Unordered unit, and an unmaterialized unit without a Goal. Fix their exact source-state evidence independently of the connector.

1. Query an explicit root frontier including descendants. Check complete empty, singular and several-match outcomes using name, Type, Label and direct-parent predicates. Check conjunctive composition, case-sensitive exact/prefix/suffix/contains where admitted, canonical-name ordering and requested fact projection. The unmaterialized or Goal-gap unit remains discoverable.
2. Query an explicit non-root frontier with each admitted self/descendant selection. Verify no sibling, hidden default, alias expansion, implicit Read, full declaration, inferred Subject relation or subsequent mutation is introduced. Explicit full-Project inclusion differs from an omitted frontier.
3. Check the root identity from Project Settings and non-Project identities from declarations. Reject duplicate names or a root/child name collision as ambiguous; reject missing parents, cycles, malformed schema and a Projection/folder substituted for authority. No Atom Version is fabricated.
4. Verify current source-state evidence and an exact pinned/historical view. Change a required pin before completion, remove requested history or deny read permission; require the precise non-success error and truthful incomplete coverage, not refreshed approval or a false empty match set.
5. Reject unknown request/filter/result fields, unsupported modes, wrong value types, empty/unresolved context and target/query conflict under CA-D-625-CONNECTOR_TOOLS-ENG_DECISION--deliver-coherent-connector-interface. Backend failure is not successful empty coverage. No matching row after a valid complete query is not an error.
6. Compare authoritative source, Carrier/history, metadata and lifecycle state before and after every valid and invalid request. Required mutation effects are none. Unexpected observed effects fail acceptance and remain truthfully reported; unknown effect evidence includes `effect_uncertain`. Nonempty errors cannot pass, and empty errors require independently verified declared coverage.

Independent review of this source packet is separate from these unexecuted implementation tests. Record absent evidence explicitly; historical Atom-only fixtures do not establish Scope Unit acceptance.
