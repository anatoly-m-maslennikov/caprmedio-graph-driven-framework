---
atom_id: CA-O-029
content_role: Operations
type: Action
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Archive Selected Active Atoms"
  depends_on:
    - "Action"
    - "Tool/ATOM_ARCHIVE"
    - "Atom"
    - "Atom/Revision"
    - "Artifact/Carrier"
    - "Journal/Record"
version: 8
updated_at: "2026-10-13 18:55:32 +0400"
relations: {}
---
# Summary

Archive selected active Atoms

## Operation

Archive Selected Active Atoms **means** the reusable Action that archives one explicit current logical Atom under its applicable lifecycle model, preserving its identity, Summary, content and recoverable history. This Atom lifecycle Action offers no Atom deletion; file cleanup is separately scoped.

### Action

1. bind the exact Atom ID and Version, owning Scope Unit, current Status and private source evidence. Resolve its applicable Content Role/Type archival transition and current permission under CA-R-1521/CA-R-1308. Do not assume a universal Archived value or reinterpret resolved/canceled Concern states as archival meaning.
2. require one eligible current non-archived Atom and an explicitly allowed archival transition. Reject Draft, already archived, missing, ambiguous or stale targets, unavailable archival models and unsafe or occupied destinations before effects.
3. derive its private governed history destination under CA-D-565/CA-D-466/CA-D-289, preserving ID, Summary, body and unrelated metadata. Preserve exact prior Version N bytes as history, and bind the archival effect's allowed lifecycle Status, Version N+1 and actual Project-time updated_at with its corresponding governed basename and historical-resolution checks. Never rewrite the preserved N predecessor.
4. execute only through the current admitted Project-local route with exact sealed permission and rechecked source/destination evidence. Safely perform and verify this one Atom's archival effect, retaining its actual result and required recording.
5. on failure recover only this Action's verified mutable frontier while preserving earlier successful Atoms, pre-existing history and accepted Journal evidence. Retain truthful failed/partial/unknown effects if recovery or recording is incomplete.
6. return the actual archived Atom ID and Version. In replacement 100 -> 200, archival targets and reports 100; it neither reports 200 as the archived target nor automatically changes references from 100 to 200.

For a folder-backed Plan, Workflow or Step, include its matching Directory Carrier in this one Atom's admitted placement map and retain the recursively contained tree under the parent's governed archived placement and matching basename. Preserve exact older Revision bytes and do not migrate noncanonical legacy archive trees. Relocation does not infer or rewrite descendants' Status or Revision metadata. The calling Workflow composes the required R1521 cascade as separate individually admitted Actions for the parent and each selected descendant's latest Revision; this Action neither selects those descendants nor reports their changes complete. Referenced Atoms outside the Carrier tree remain untouched.

### Batch and stop boundary

A requested batch is an ordered list of independently authorized Atom Actions. Invoke one Action at a time; advance to the next distinct explicit Atom only after confirmed success. On the first failure, stop, retain all earlier successful effects and their evidence, and leave the remaining targets untouched. Never roll back earlier successful Atoms to simulate a cross-Atom transaction. Validation, stale-source checks, permissions, safe effects and recovery within the failing Atom Action remain required. Automatic retry or resume of this new batch policy is deferred; existing recording-only recovery must not replay a performed Action.

An archive preview or no-op is not an invented effect. Historical references remain resolvable without an automatic reference rewrite.

## Details

Bind each actual standalone **or** nested Action Run **to** the shared every-Run contract in CA-P-1117 v3, Done CA-P-1443 J01–J08, independently reviewed by CA-P-1451: exact admitted definition Revision, actual Run identity/lineage, safe input/result/effect references, start, truthful terminal **or** still-pending interruption, **and** durable canonical Journal receipts under CA-R-1720. Workflow-contained bindings also follow CA-R-1525; standalone coverage is the selected Epic obligation, **not** a broadened applicability claim for that Requirement. Reuse the shared recording capability **without** owning another Journal implementation. Preserve accepted events **and** pending evidence; retry failed recording with the same Event identity/payload, **not** the performed Action. No receipt, intake acknowledgment, **or** Git Commit alone proves successful effects **or** complete Run recording.
