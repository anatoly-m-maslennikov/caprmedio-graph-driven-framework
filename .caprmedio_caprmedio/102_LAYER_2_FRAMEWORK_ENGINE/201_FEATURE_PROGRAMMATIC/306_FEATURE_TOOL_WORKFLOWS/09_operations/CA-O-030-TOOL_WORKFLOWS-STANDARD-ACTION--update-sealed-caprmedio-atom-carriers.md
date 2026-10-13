---
atom_id: CA-O-030
content_role: Operations
type: Action
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Update Sealed Atom Carriers"
  depends_on:
    - "Action"
    - "Tool/ATOM_UPDATE"
    - "Atom"
    - "Atom/Revision"
    - "Atom/Summary"
    - "Atom/Revision/Updated At"
    - "Artifact/Carrier"
    - "Journal/Record"
version: 14
updated_at: "2026-10-13 05:22:20 +0400"
relations: {}
---
# Summary

Update sealed CAPRMEDIO Atom carriers

## Operation

Update Sealed Atom Carriers **means** the reusable Action that performs one explicit admitted same-identity edit to one logical Atom under CA-R-866. Each Action preserves ID, Summary, Type and unrelated values; its private Carrier and history effects remain safely validated. A batch does not become one cross-Atom transaction.

## Details

This workflow-facing Action addresses logical Atoms by Atom ID and Version and Scope Units by their declared identity. Carrier paths, filenames and serialization are private implementation details, not public selectors. Resolve current authoritative sources and retain exact private source evidence without inferring a missing or ambiguous identity. No implicit search, successor allocation or reference retargeting is part of an explicitly targeted Action.

### Explicit Property and Section edits

- use exactly one edit family for the Action. A Property edit under CA-R-1934/CA-M-374 adds, replaces or removes one named Property; a list edit adds or removes individual explicit values, replaces one uniquely identified current value, or replaces the complete set. Caller-supplied list indexes are rejected. Missing or ambiguous current values, duplicate results and unsupported cardinality or value types stop before effects.
- a Section edit under CA-R-1933/CA-M-373 addresses exactly one explicit Section and adds, replaces, removes, renames its title or reorders it. The explicit position for reordering is a Section position, not a Property-list index. Preserve every unrelated Section and Property and all required content/structure rules.
- validate the whole proposed Atom under its current Content Role/Type and owning authority before writing. Do not accept mixed families, hidden search or unrelated changes. Any Summary-value change, including wording-only, or Type change returns replacement-required and leaves the target unchanged; this same-ID Action neither allocates a new ID nor archives the predecessor implicitly.
- reference modification is an explicit Property use with exact target ID/Version, current reference value and requested new value. No implicit Find, retargeting to a replacement successor or mutation of other referencing Atoms is admitted.

### Workflow-owned policy and connector boundary

Identity, Summary/Type replacement classification, Version/time, Status, history, semantic validation, authorization and independent-target progression are owned by this workflow feature, not inferred by a mechanical connector. Any selected connector delegation uses D625's explicit logical `modify` request with supplied target, complete delta/content, expected_state and authorization/context; D527's outer transport is unchanged. This definition does not add a runnable binding.

### Per-Atom effect and batch boundary

A requested batch is an ordered list of independently authorized Atom Actions. Invoke one Action at a time; advance to the next distinct explicit Atom only after confirmed success. On the first failure, stop, retain all earlier successful effects and their evidence, and leave the remaining targets untouched. Never roll back earlier successful Atoms to simulate a cross-Atom transaction. Validation, stale-source checks, permissions, safe effects and recovery within the failing Atom Action remain required. Automatic retry or resume of this new batch policy is deferred; existing recording-only recovery must not replay a performed Action.

Resolve the current original and exact proposal, recheck admitted identity classification and actual authority, and retain the mutation-free preview before execution. Apply only through the existing admitted Project-local route with its exact sealed permission, selected Session, completed required assessment and recorded Action start. A direct call, caller Boolean, candidate acceptance or local preview grants no effect permission. Bind and recheck the source, proposal, validation, definition, destination and history evidence before the one-Atom effect.

Every actual same-ID Atom change, including Status-only, carrier-only and equivalent refinement, advances exactly from Version N to N+1 and records actual Project-time updated_at. Preserve the exact prior N bytes as history without rewriting their metadata. A no-op retains Version/time and creates no history or change event. Identity classification remains required, but it cannot exempt an actual change from this Version rule. Preserve Summary, identity, intended Status, unrelated bytes and prior semantic history. Recover only the verified mutable frontier and attempt-owned history of this Action on its failure; preserve pre-existing history, earlier successful Atoms and accepted Journal evidence. Missing or unverifiable recovery or recording is not success.

### Subject-only preview and staged candidates

The closed Subject preview root remains `{atoms, subject_profile?}`; each selected logical Atom has pinned identity/Version/source evidence and explicit `subject_patches`. A patch names governs or depends_on, exact old/current value and explicit new value. Resolve a dependency replacement by its unique current value and reject a caller index, missing/ambiguous old value, resulting duplicate or mixed body/complete-frontmatter request. Syntax checking neither establishes meaning nor chooses a mapping.

Omission selects legacy; approved is explicit. Reuse the selected profile's current grammar evidence for both source and result. Preserve Atom/atom case distinction, reject unsupported forms, and retain private exact scalar-span evidence. Validate complete source and result, preserving every unrelated byte and intended Status. Select complete stable-ID originals; exclude Draft and archived carriers by Status and placement and reject unavailable or ambiguous authority.

Default local preview writes nothing. Opt-in local `run --stage-preview` exports only the existing illustrative proposed bytes under CA-D-425 into fresh generated temporary candidates. Independently read back bytes/hashes, validate at the original logical source context, and repeat the same pinned preview/time check before returning its closed manifest. Source drift refuses success; partial failures retain truthful artifact references without unsafe cleanup.

Staging performs no authoritative, archive/history, Journal, promotion or MCP effect. It does not create source effect-time evidence, bypass the standalone apply guard, change the staged-only migration scope or reopen deferred live changed-Subject publication. New contract authoring is not implementation or runtime readiness; affected use still needs the independently verified realization.

### Admitted one-target Subject effect

The existing selected update route retains its completed current Analysis Report and exact O067/O145 assessment, O129 lineage, actual selected Session and canonically recorded O030 Action start. Reopen those persisted bindings; a matching assessment hash alone is insufficient. For the one admitted target, bind deterministic intended Subject bytes with old Version/time, execution-time metadata rule and exact predecessor destination; no-op preserves them. Effect-time materialization and actual current/history readback remain distinct from illustrative preview and intent.

### Selected staged-review publication access

1. Before the publication window, stage and review the exact admitted source-bound change, retaining the existing sealed source/delta/intent, completed assessment, permission and Run evidence. Reopen the review evidence; a candidate or manifest is not an approval token. Candidate time remains illustrative and the existing actual-effect metadata materialization rule is unchanged.
2. Establish a short exclusive window over the affected current Carrier, predecessor-history destination and governing authority sources. No manual editing, Git operation or synchronization may change that frontier during the window. Acquire the one shared cooperative Engine publication lock before the final complete revalidation; inability to establish the window or lock stops before effects.
3. While holding the lock, reopen and revalidate the exact source, ownership, grammar, report, complete-carrier, definition, permission, intent and current/history destination evidence. Apply only the already admitted one-target effect; materialize actual metadata once, retain exact predecessor bytes and independently read back current/history facts.
4. Hold the same lock and window through those effects and readback and any invoked existing Action-local restoration. Retain the exact verified mutable-frontier and attempt-owned-history rules, pre-existing history and accepted Journal evidence. Unknown effects, failed restoration or incomplete required recording retain their existing truthful disposition; never infer success or replay the effect.

This model excludes only writers respecting the exclusive window and cooperative lock. It does not itself establish crash-atomic multi-Carrier publication or a stronger guarantee and cannot protect against outside writers ignoring the window. Existing safety requirements remain unchanged. The model adds no public request fields, Boolean approval, local writer, transport or new retry/recovery framework.

Live changed-Subject publication remains blocked under its existing explicit guard until this selected access binding and combined verification are independently accepted. This definition is not implementation or readiness, does not remove that guard, activate MCP, alter native meaning or authorize Core migration.

### Run recording

Bind each actual standalone **or** nested Action Run **to** the shared every-Run contract in CA-P-1117 v3, Done CA-P-1443 J01–J08, independently reviewed by CA-P-1451: exact admitted definition Revision, actual Run identity/lineage, safe input/result/effect references, start, truthful terminal **or** still-pending interruption, **and** durable canonical Journal receipts under CA-R-1720. Workflow-contained bindings also follow CA-R-1525; standalone coverage is the selected Epic obligation, **not** a broadened applicability claim for that Requirement. Reuse the shared recording capability **without** owning another Journal implementation. Preserve accepted events **and** pending evidence; retry failed recording with the same Event identity/payload, **not** the performed Action. No receipt, intake acknowledgment, **or** Git Commit alone proves successful effects **or** complete Run recording.
