---
atom_id: CA-O-draft
role: Operations
form: Action
status: Draft
version: 1
updated_at: '2026-11-03 18:54:48 +0400'
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Action
  passive:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
relations: {}
---
## Summary

Create one Atom Draft

## Claim scope

PROJECT_CONFIGURATION

## Claim

This reusable Action materializes one complete Draft carrier for one exact, admitted non-container Atom request. The caller supplies the complete proposed content/changes, Summary, Role, destination, applicable model, permission, and expected source; the Action validates and writes that proposal as `status: Draft`, without selecting a Workflow continuation, implementation/provider, or hidden edit.

### Source cases

- Missing or null source creates a new role-only Draft with initial proposed Version 1 and no allocated canonical identity.
- An explicit Current source resolves exactly once. When proposed Summary and Role are unchanged from Current version N, the Draft uses `canonical-ID@N+1-draft` and proposedVersion N+1. When either Summary or Role changes, the Draft uses a new role-only marker with initial proposed Version 1 and reports an explicit `replacementSummaryRole` old-to-new mapping; it never overwrites the Current.
- An explicit Draft source may be copied only to an explicitly distinct Draft destination. The source remains unchanged, and an existing-Atom marker's proposed Version stays fixed and synchronized with its filename.
- An explicit Archived source may seed a NEW role-only Draft with initial proposed Version 1. The Action never infers or restores the Archived Atom's canonical identity.

### Validation and outcomes

Resolve an existing source once: invalid source input returns attributable diagnostics, and an ambiguous source returns the available choices; neither writes. Validate the complete proposal's admitted fields, Draft status, placement, destination absence, and collision/overwrite conditions. Reject a container, including semantic containment without a folder, and never select descendants or cascade. There is no history gate: Journal lineage or an archive search is not required to create a valid Draft.

After a verified write, return the exact Draft path/carrier, marker, status, proposed Version, and any replacementSummaryRole mapping. Input or artifact failures return attributable diagnostics; if work is partial, preserve the actual completed results and identify the remainder. Do not automatically retry or roll back. Journal records actual business events only and does not prove permission, completeness, or success.

