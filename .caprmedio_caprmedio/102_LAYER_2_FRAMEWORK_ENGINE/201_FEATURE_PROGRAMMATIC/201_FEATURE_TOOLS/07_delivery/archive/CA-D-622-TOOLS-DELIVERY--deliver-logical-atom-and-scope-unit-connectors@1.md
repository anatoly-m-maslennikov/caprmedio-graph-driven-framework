---
atom_id: CA-D-622
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
  depends_on: ["Atom","Scope Unit","Workflow"]
version: 1
updated_at: "2026-10-12 23:13:13 +0400"
relations:
  delivery_for: ["CA-R-1093","CA-R-1067","CA-R-863","CA-R-864","CA-R-865","CA-R-866","CA-R-868","CA-R-1829"]
  relates_to: ["CA-M-372","CA-O-201","CA-O-202","CA-O-203"]
---
# Summary

Deliver logical Atom and Scope Unit connectors

## Scope

The required logical connector request/result contract under registered TOOLS, with the current file/TOML adapters as delivery bindings. It defines no new Scope Unit, executable path or admitted runtime/MCP route.

## Claim

Find, Read, Create and Modify are independent logical Atom/Scope Unit operations. Atom removal is Archive only. A replaceable backend must preserve the logical contract without exposing storage location as identity.

## Details

The operation-specific payload is carried inside the existing outer service/permission contract; it does not duplicate CA-D-527. Identify the requested logical kind and operation explicitly. Bind a Read Atom target to its full ID and explicit Version; bind a mutation to the exact logical identity, expected Version or applicable source revision/pin and complete proposed delta. Scope Unit requests use the admitted Scope Unit identity and backing source-state evidence; they do not invent an Atom Version for that kind.

Find serializes explicit scope/Property/Subject criteria and returns matching descriptors, not full Atom content. A Subject criterion carries field governs/depends_on/both, exact requested value and match exact/prefix/suffix/contains; prefix uses the selected grammar boundary, while suffix/contains compare literal text. Read returns the complete identified state. Neither operation invokes Modify, and Find does not invoke Read.

Create carries the complete proposed logical object and applicable identity/schema/ownership evidence. Modify carries only CA-D-623's explicit logical edits and rejects a Summary change under the same Atom ID. Archive returns the observed archived Atom state and retained history rather than deleting the Atom. Every actual changed same-ID update, including Status-only, carrier-only and refinement, advances Version exactly once and records actual time; exact prior history keeps its old Version. No-op preserves Version/time. Summary or Type changes use replacement. Unknown operations, denied scopes and missing/ambiguous/stale target evidence fail without silently widening the request.

Results preserve the exact requested identity/state evidence, admitted permission, validation diagnostics and actual known/unknown effects or no-op. Multiple Atom targets become independent actions under CA-M-372; one failed action retains earlier successes and leaves later targets unperformed. Current Markdown/TOML adapter locators, indexes or digests may support exact source binding internally, but a caller list index cannot select a logical list entry.

### Delivery status

This is a required contract awaiting implementation and functional verification. Legacy Core alignment is a separate content-Epic dependency before integrated runtime acceptance. Existing file adapters remain the current delivery mechanism; no DB implementation, installation, live route or stronger transaction/concurrency guarantee is claimed. New workflow resume/retry and the earlier concurrency/publication questions remain deferred.
