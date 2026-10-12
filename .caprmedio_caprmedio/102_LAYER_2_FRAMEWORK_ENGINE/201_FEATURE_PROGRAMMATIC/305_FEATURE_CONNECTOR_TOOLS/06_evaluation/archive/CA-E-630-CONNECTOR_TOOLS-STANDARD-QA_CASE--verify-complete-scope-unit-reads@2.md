---
atom_id: CA-E-630
content_role: Evaluation
type: QA Case
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-13 01:54:26 +0400"
subjects:
  governs: "Tool"
  depends_on: ["Scope Unit", "Project", "Project Structure", "Project Settings"]
relations:
  relates_to: [CA-R-1938, CA-M-378, CA-D-627, CA-O-212, CA-R-1936, CA-M-376, CA-E-628, CA-D-625, CA-R-1484, CA-D-442]
---
# Summary

Verify complete Scope Unit reads

## Scope

Future conformance evaluation of CA-R-1938-CONNECTOR_TOOLS-STANDARD-REQUIREMENT--read-one-complete-scope-unit-declaration, CA-D-627-CONNECTOR_TOOLS-STANDARD-DELIVERY--deliver-complete-scope-unit-read-data and CA-O-212-CONNECTOR_TOOLS-STANDARD-ACTION--read-one-complete-scope-unit-declaration.

## Claim

A Scope Unit Read implementation passes **only** **when** independent complete-source observations **and** exact result/error/effect evidence establish full faithful Read of its explicit target **and** no mutation. Missing implementation **or** observations is unavailable evidence, **not** a pass.

## Details

Use independently pinned current and retained historical Project Settings/Project Structure fixtures. Include a root Project, a declared non-Project unit with every admitted field, an Unordered unit without Local Order, and an unmaterialized declaration. Record independent expected values and source evidence before calling the connector.

1. Read the explicit root and each non-Project name without a pre-known state token. Require the complete applicable declaration, exact carried values and presence/absence, and actual source-state evidence. Root has no fabricated child row, Scope Unit ID or Atom Version; an unmaterialized unit remains readable.
2. Read a supplied exact pin and historical view. Verify the exact selected declaration, not latest data. Inject stale evidence, unavailable history, ambiguous view and a changed required source during the check; require the applicable declared error, not a refreshed pin or silent fallback.
3. Verify that Query/Find, owned Atom reads, descendant traversal, directory enumeration, normalization, lifecycle choice and Modify are not invoked implicitly. Declared path/binding values may appear as data but cannot select the target or become a backend API.
4. Reject a missing target, duplicate/colliding name, malformed declaration/schema, unbound Project/context, invalid kind, unknown fields, non-null query/delta, denied read permission and backend failure. A missing target uses `target_not_found`; competing targets use `target_ambiguous`; neither yields successful empty data.
5. Compare source declarations, Carrier/history, metadata and lifecycle state before and after success and failure. Required effects are none. Unexpected observed effects fail acceptance and remain truthfully reported; every unknown effect includes `effect_uncertain`. Nonempty errors never pass, and empty errors require independent verification of the complete declared Read result.

Use CA-D-625-CONNECTOR_TOOLS-CORE-DELIVERY--deliver-coherent-connector-interface's exact common roles and codes. These cases are unexecuted test specifications. A different reviewer must separately accept the pinned authoring packet; historical Atom Read tests do not establish Scope Unit implementation.
