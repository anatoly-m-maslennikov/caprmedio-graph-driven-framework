---
atom_id: CA-P-1963
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Term, Property, Carrier, Revision, Scope Unit, Projection, Plan, Tool, Journal, Operator]
version: 1
updated_at: "2026-10-10 22:32:47 +0400"
relations: 
  is_decomposition_of: [CA-P-1959]
  blocks: [CA-P-1966, CA-P-1967, CA-P-1972]
---
# Summary

Verify Subject Tools on isolated fixtures

## Objective

Independently prove that lookup and preview work without losing Atom data or allowing unapproved writes.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Required prerequisites: CA-P-1961 and CA-P-1962.

Use isolated fixtures under .caprmedio_tmp. Verify exact governs versus depends_on hits, no body-text false positives, full source pins, deterministic previews and byte-identical Summary/Substance/Scope/Details. Check Version +1 and updated_at previews without persisting them.

Exercise stale hash/Version, invalid Subjects, missing occurrences, duplicate keys/values, collisions, overlapping patches, symlinks, escaped paths, CRLF preservation and failed preparation. Confirm live authoritative Atoms remain unchanged and the existing standalone apply guard remains intact.

Run the affected existing Atom/Subject/graph tests plus new focused tests using uv and declared dependencies. Record actual checks, implementation hashes and coverage limits. Fixture success is not a live mutation or runtime receipt. Hand defects back to the implementation owner.

Inherit CA-P-1959's source boundary, confidence threshold and preservation rules. Creating this Plan records work; it does not start or complete it.

### Definition of Done

The Plan is **not** Done if a required check fails or is unverified, unrelated data is lost, authoritative sources change, a write guard is weakened, or fixture evidence is claimed as live execution, any direct decomposing Plan is not Done, or own work exceeds 15 minutes without decomposition.
