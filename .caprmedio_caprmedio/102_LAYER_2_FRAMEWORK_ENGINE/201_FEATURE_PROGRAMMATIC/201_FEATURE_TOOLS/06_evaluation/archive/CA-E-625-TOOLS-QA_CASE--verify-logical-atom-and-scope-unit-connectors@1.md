---
atom_id: CA-E-625
content_role: Evaluation
type: QA Case
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
  evaluation_for: ["CA-R-1093","CA-R-1067","CA-R-863","CA-R-864","CA-R-865","CA-R-866","CA-R-868","CA-R-1829","CA-R-1933","CA-R-1934"]
  relates_to: ["CA-M-373","CA-M-374","CA-O-201","CA-O-047","CA-O-203"]
---
# Summary

Verify logical Atom and Scope Unit connectors

## Scope

Required future tests for logical Atom and Scope Unit connectors under TOOLS, including independent Find, Read, Create and Modify and Atom Archive. No new Scope Unit, storage backend or runtime route is established.

Legacy Core identity/Version and content rules require separate alignment in the content Epic before integrated runtime acceptance. This Engine contract does not edit or adopt Core.

## Claim

Each connector uses logical identity and current source-state evidence, preserves validation/permission boundaries and exposes only its requested operation. Physical file/TOML locations remain adapter details.

## Details

- Find returns exactly the requested matches, without invoking Read or Modify. Independently test Atom and Scope Unit scopes, zero/one/several matches, invalid filters and deterministic attribution.
- For Atom Subjects, test governs, depends_on and both with exact, profile-boundary prefix, literal suffix and literal contains criteria, combined with Scope Unit filters. Body-only text is not a Subject occurrence.
- Read an Atom by full ID and explicit Version; compare its complete Properties/sections with independent expected data. Read a Scope Unit by its declared identity and applicable backing source-state evidence, without inventing an Atom Version field for it. Missing, conflicting or stale state fails explicitly.
- Create one fresh Atom and one valid Scope Unit. Check complete schema, identity admission, ownership and exact observed source-state evidence. Reject historical Atom ID reuse, occupied/conflicting identities, denied permission and stale inputs. No Atom deletion is accepted; Archive retains its historical identity/content.
- Test one section edit family for add, replace, remove, title and position; Property add/replace/remove; list entry add/remove, one-entry replacement by unique exact current value and complete-set replacement. Test malformed final state, unknown fields, duplicate/ambiguous values and caller indexes. Section position is an explicit section-order operation, not a list-entry selector.
- Ordinary same-ID Modify rejects every Summary change, including wording-only edits, and every Type change. Every other actual changed same-ID update, including Status-only, carrier-only and refinement, advances Version exactly once with actual Updated At; a no-op preserves Version/time. Preserve unrelated content, currentness checks and exact prior history.
- Use the current file/TOML adapters to establish only guarantees actually observed by future tests. The logical contract must not require a filename/path as identity or claim a working DB backend.

### Acceptance and failure disposition

Require independent expected results, exact before/after observations, schema/currentness/permission decisions and truthful failures/no-ops. Reject widened scope, implicit operations, hidden ambiguity, lost history, automatic reference rewriting or invented implementation guarantees. Resume/retry of the new workflow family and stronger concurrency/publication guarantees remain deferred. This Atom specifies tests; no execution or passing result is claimed.
