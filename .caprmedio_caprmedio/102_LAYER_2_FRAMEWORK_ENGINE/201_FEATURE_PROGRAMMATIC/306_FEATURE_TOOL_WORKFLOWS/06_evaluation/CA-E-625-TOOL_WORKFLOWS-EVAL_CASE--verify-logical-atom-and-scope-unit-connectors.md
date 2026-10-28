---
atom_id: CA-E-625
content_role: Evaluation
type: Eval Case
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Dynamic Testing
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
version: 12
updated_at: 2026-10-27 19:59:38 +0400
relations:
  evaluation_for:
  - CA-R-1093
  - CA-R-1067
  - CA-R-863
  - CA-R-864
  - CA-R-865
  - CA-R-866
  - CA-R-868
  - CA-R-1829
  - CA-R-1933
  - CA-R-1934
tier: 4
---
# Summary

Verify logical Atom and Scope Unit connectors

## Scope

Workflow admission owns identity, Version/time, lifecycle and complete schema decisions. Connector calls use CA-D-625 only to verify the supplied request, source preconditions and permission and to perform the explicit mechanical operation. A connector does not choose those decisions.

Required future tests for logical Atom and Scope Unit connectors under TOOL_WORKFLOWS, including independent Find, Read, Create, Modify and Archive workflows composed with simple connectors. No new Scope Unit, storage backend or runtime route is established.

Legacy Core identity/Version and content rules require separate alignment in the content Epic before integrated runtime acceptance. This Engine contract does not edit or adopt Core.

## Claim

Each workflow supplies explicit logical targets, current source-state evidence and admitted identity/lifecycle/schema decisions; connectors verify that bound evidence and perform only the supplied mechanical operation. Physical file/TOML locations remain adapter details.

## Details

- Find returns exactly the requested matches, without invoking Read or Modify. Independently test Atom and Scope Unit scopes, zero/one/several matches, invalid filters and deterministic attribution.
- For Atom Subjects, test governs, depends_on and both with exact, profile-boundary prefix, literal suffix and literal contains criteria, combined with Scope Unit filters. Body-only text is not a Subject occurrence.
- Read an Atom by explicit full ID without requiring a pre-known Version; verify the actual returned exact Version/state. When a Version or expected state is supplied for pinned or historical Read, require an exact match; compare its complete Properties/sections with independent expected data. Read a Scope Unit by its declared identity and applicable backing source-state evidence, without inventing an Atom Version field for it. Missing, conflicting or stale state fails explicitly.
- Create one fresh Atom and one valid Scope Unit. Check complete schema, identity admission, ownership and exact observed source-state evidence. Reject historical Atom ID reuse, occupied/conflicting identities, denied permission and stale inputs. No Atom deletion is accepted; Archive retains its historical identity/content.
- Test one section edit family for add, replace, remove, title and position; Property add/replace/remove; list entry add/remove, one-entry replacement by unique exact current value and complete-set replacement. Test malformed final state, unknown fields, duplicate/ambiguous values and caller indexes. Section position is an explicit section-order operation, not a list-entry selector.
- Workflow admission for ordinary same-ID Modify rejects every Summary change, including wording-only edits, and every Type change. Every other actual changed same-ID update, including Status-only, carrier-only and refinement, advances Version exactly once with actual Updated At; a no-op preserves Version/time. Preserve unrelated content, currentness checks and exact prior history.
- Use the current file/TOML adapters to establish only guarantees actually observed by future tests. The logical contract must not require a filename/path as identity or claim a working DB backend.

### Acceptance and failure disposition

Require independent expected results, exact before/after observations, schema/currentness/permission decisions and truthful failures/no-ops. Reject widened scope, implicit operations, hidden ambiguity, lost history, automatic reference rewriting or invented implementation guarantees. Resume/retry of the new workflow family and stronger concurrency/publication guarantees remain deferred. This Atom specifies tests; no execution or passing result is claimed.
