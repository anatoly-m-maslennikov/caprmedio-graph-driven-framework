---
atom_id: CA-O-032@9
content_role: Operations
type: Action
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Create Sealed Atom Carriers
  depends_on:
  - Action
  - Tool/ATOM_CREATE
  - Subject/Domain/Node/Continuant/Atom
  - Atom/Identifier
  - Atom/Revision
  - Atom/Summary
  - Artifact/Carrier
  - Journal/Record
version: 9
updated_at: 2026-10-23 03:06:32 +0400
relations: {}
---
# Summary

Create sealed CAPRMEDIO Atom carriers

## Operation

Create Sealed Atom Carriers **means** the reusable Action that creates one explicitly requested logical Atom under CA-R-865 with its admitted new ID, owning Scope Unit, required Type, complete Properties and Sections. Storage realization is private; no additional Atom is created as a hidden batch effect. Identity admission, complete content, initial Version/lifecycle and permission are workflow-owned decisions. A future connector delegation uses D625's explicit `create` request and supplied evidence, not hidden connector decisions; no runnable binding is selected here.

### Action

1. bind the explicit new Atom request and declared owning Scope Unit. Validate its complete content, Summary, Content Role/Type, intended lifecycle and applicable schema before any effect.
2. establish the requested unused Project ID from current authority and preserved assignment/history evidence under CA-D-508/CA-D-378. Archived, replaced or absorbed Atoms do not release IDs for reuse. Missing, conflicting or changed evidence blocks creation; do not silently allocate a different ID.
3. resolve the private governed destination and prove it absent, safe and collision-free. Return the exact mutation-free proposal and identity-admission evidence.
4. execute only with current exact permission under the admitted Project-local route. Recheck this one target's absence, content and identity pins immediately before its safe effect.
5. independently verify the new Atom and actual first Revision and retain its source/effect evidence. Independently attempt Journal recording; its failure is diagnostic only and neither invalidates a verified creation nor authorizes replay. A failure invokes only this Action's admitted safe recovery and retains truthful partial or unknown effects; it does not erase earlier successful Atom creations.
6. return the actual created new Atom ID and Version. In replacement of Atom 100 by Atom 200, creation targets and reports 200; archival of 100 is a separate explicit effect with its own evidence. Creation neither edits 100 nor retargets its references.

### Batch and stop boundary

A requested batch is an ordered list of independently authorized Atom Actions. Invoke one Action at a time; advance to the next distinct explicit Atom only after confirmed success. On the first failure, stop, retain all earlier successful effects and their evidence, and leave the remaining targets untouched. Never roll back earlier successful Atoms to simulate a cross-Atom transaction. Validation, stale-source checks, permissions, safe effects and recovery within the failing Atom Action remain required. Automatic retry or resume of this new batch policy is deferred; existing recording-only recovery must not replay a performed Action.

Preview is prepared, not created. Existing Draft admission and private Carrier rules remain applicable where explicitly selected; this Action does not invent identity for an unassigned Draft or advertise new runnable capability.

## Details

Bind each actual standalone **or** nested Action Run **to** the shared every-Run contract in CA-P-1117 v3, Done CA-P-1443 J01–J08, independently reviewed by CA-P-1451: exact admitted definition Revision, actual Run identity/lineage, safe input/result/effect references, start and truthful terminal **or** still-pending interruption. Workflow-contained bindings also follow CA-R-1525; standalone coverage is the selected Epic obligation, **not** a broadened applicability claim for that Requirement. Reuse the shared recording capability **without** owning another Journal implementation. Preserve actual in-memory Run evidence and any pending observation; a supported recording retry uses the same Event identity/payload, never the performed Action. A receipt, intake acknowledgment, or Git Commit alone proves neither successful effects nor complete Run recording.
