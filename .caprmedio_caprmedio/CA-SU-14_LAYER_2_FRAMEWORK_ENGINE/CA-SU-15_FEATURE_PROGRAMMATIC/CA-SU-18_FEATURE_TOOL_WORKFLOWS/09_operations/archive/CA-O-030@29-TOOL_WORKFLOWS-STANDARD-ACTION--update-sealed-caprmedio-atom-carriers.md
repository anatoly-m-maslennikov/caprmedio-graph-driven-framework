---
atom_id: CA-O-030@29
content_role: Operations
type: Action
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Engineering/Carrier
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Engineering/Tool//ATOM_UPDATE
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/History/Journal.Record
  - Subject/Domain/Node/Continuant/Atom.Summary
  - Atom/Revision/Updated At
  - Subject/Engineering/Carrier
version: 29
updated_at: 2026-10-24 00:51:05 +0400
relations: {}
tier: 3
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

### Existing full-content Concern repair

For an explicitly selected, already identified Concern under `01_concern`, a legacy single descriptive first H1 may supply the source Summary value for a same-ID full-content repair. Require exactly one nonempty unfenced H1 and no competing Summary; do not infer or assign an identity. The proposed body must use the canonical literal `# Summary` with that exact value and pass complete Concern validation. Preserve ID, path, Type and intended Status; a changed Summary value still requires replacement. Reuse existing assessment, authorization, exact source checks, Version N+1/actual Updated At, exact predecessor history and result readback. This source-input normalization adds no endpoint, flag or proof/approval mechanism and does not relax Subjects-only source validation.

This uses the existing full-content update path under CA-R-866, not the one-Section edit operation under CA-R-1933/CA-M-373. Its explicit approved proposal may reorganize the legacy Concern body into its canonical sections; unrelated changes remain excluded.

### Workflow-owned policy and connector boundary

Identity, Summary/Type replacement classification, Version/time, Status, history, semantic validation, authorization and independent-target progression are owned by this workflow feature, not inferred by a mechanical connector. Any selected connector delegation uses D625's explicit logical `modify` request with supplied target, complete delta/content, expected_state and authorization/context; D527's outer transport is unchanged. This definition does not add a runnable binding.

### Per-Atom effect and batch boundary

A requested batch is an ordered list of independently authorized Atom Actions. Invoke one Action at a time; advance to the next distinct explicit Atom only after confirmed success. On the first failure, stop, retain all earlier successful effects and their evidence, and leave the remaining targets untouched. Never roll back earlier successful Atoms to simulate a cross-Atom transaction. Validation, stale-source checks, permissions, safe effects and recovery within the failing Atom Action remain required. Automatic retry or resume of this new batch policy is deferred; Journal append/read never replays a performed Action and introduces no automatic recording retry or recovery.

Resolve the current original and exact proposal, recheck admitted identity classification and actual authority, and retain the mutation-free preview before execution. Apply only through the existing admitted Project-local route with its exact sealed permission, selected Session, completed required assessment and actual Action start retained in the selected Run. A direct call, caller Boolean, candidate acceptance or local preview grants no effect permission. Bind and recheck the source, proposal, validation, definition, destination and history evidence before the one-Atom effect.

Every actual same-ID Atom change, including Status-only, carrier-only and equivalent refinement, advances exactly from Version N to N+1 and records actual Project-time updated_at. Preserve the exact prior N bytes as history without rewriting their metadata. A no-op retains Version/time and creates no history or change event. Identity classification remains required, but it cannot exempt an actual change from this Version rule. Preserve Summary, identity, intended Status, unrelated bytes and prior semantic history. Recover only the verified mutable frontier and attempt-owned history of this Action on its failure; preserve pre-existing history, earlier successful Atoms and accepted Journal evidence. Missing or unverifiable source-effect recovery is not success. Journal recording is not a source-effect completion prerequisite or proof.

### Subject-only preview and staged candidates

The closed Subject preview root remains `{atoms, subject_profile?}`; each selected logical Atom has pinned identity/Version/source evidence and explicit `subject_patches`. A patch names governs or depends_on, exact old/current value and explicit new value. Resolve a dependency replacement by its unique current value and reject a caller index, missing/ambiguous old value, resulting duplicate or mixed body/complete-frontmatter request. Syntax checking neither establishes meaning nor chooses a mapping.

Omission selects legacy; approved is explicit. Reuse the selected profile's current grammar evidence for both source and result. Preserve Atom/atom case distinction, reject unsupported forms, and retain private exact scalar-span evidence. Validate complete source and result, preserving every unrelated byte and intended Status. Select complete stable-ID originals; exclude Draft and archived carriers by Status and placement and reject unavailable or ambiguous authority.

Default local preview writes nothing. Opt-in local `run --stage-preview` exports only the existing illustrative proposed bytes under CA-D-425 into fresh generated temporary candidates. Independently read back bytes/hashes, validate at the original logical source context, and repeat the same pinned preview/time check before returning its closed manifest. Source drift refuses success; partial failures retain truthful artifact references without unsafe cleanup.

Staging performs no authoritative, archive/history, Journal, promotion or MCP effect. It does not create source effect-time evidence, bypass the standalone apply guard, change the staged-only migration scope or reopen deferred live changed-Subject publication. New contract authoring is not implementation or runtime readiness; affected use still needs the independently verified realization.

### Instructed Subjects-only batch effect

CA-R-866's exact ordered batch uses the actual Operator instruction and existing request Initiative/authorization. Retain packet/member and request bindings, without a separate batch form, review/pause response, content review, per-Atom Analysis Report/O067/O145 result or confirmation receipt. Public batch effects need no initial intent-hash metadata; derive fresh native intent internally when needed.

The caller commits current state, creates and commits edit drafts, then invokes independent existing one-Atom archive/promote effects in packet order and rebuilds the graph only after completion. Retain normal target/draft/patch/layout, current source, conditional-write, exact archive, N+1/actual-time and readback checks; no redundant full-candidate validation pass is a batch gate. Stop first failure or uncertainty, keep completed effects and leave remaining and held sources untouched. Existing native failed-write restoration remains; no automatic batch rollback, replay, retry or resume is added. Actual results and logging failures are separate observations. Ordinary singleton assessment/form/session requirements below remain unchanged and do not apply to this batch.

### Ordinary one-target Subject effect

The existing selected update route retains its current completed assessment evidence from a shared review package or a Done Analysis Report and exact O067/O145 assessment, O129 lineage, actual selected Session and actual O030 Action start retained in the selected Run. Reopen those persisted bindings; a matching assessment hash alone is insufficient. For the one admitted target, bind deterministic intended Subject bytes with old Version/time, execution-time metadata rule and exact predecessor destination; no-op preserves them. Effect-time materialization and actual current/history readback remain distinct from illustrative preview and intent.

### Selected staged-review publication access

For ordinary one-target Subject publication outside the reviewed batch branch:

1. Before the publication window, stage and review the exact admitted source-bound change, retaining the existing sealed source/delta/intent, completed assessment, permission and Run evidence. Reopen the review evidence; a candidate or manifest is not an approval token. Candidate time remains illustrative and the existing actual-effect metadata materialization rule is unchanged.
The existing `authorization_ref` must resolve a fresh purpose-specific trusted-host record of the Operator's explicit review of the exact source-bound intended change and manual editing/maintenance-script/Git/sync pause confirmation for the affected frontier. Accept the connected Codex Session's form response as sufficient Operator confirmation, without separate identity proof, only when the form shows the exact request, selected Session/Run, intended change and affected files and explicitly confirms review and the pause. Tool arguments, client names, model assertions, caller-written JSON/hash and arbitrary callbacks cannot supply that response. Bind the record to the exact existing request, source/delta/intent, selected Session/Run and affected files. Privately issue and consume the nonserializable one-use confirmation through the existing selected dispatch in the same process, preserving the public API, route and request fields. Decline, cancel, malformed response, timeout, disconnect, missing issuer/resolver, missing or mismatched confirmation and bound-evidence drift stop before effects. Building this connection grants no publication or runtime-activation permission.

This exact changed Subject-only execution may stay in the existing connected MCP host process through confirmation and the existing selected dispatch rather than DBOS enqueue. The actual outer request/session owns the form; a child-session callback, caller argument or queue worker cannot supply it. Retain the existing normalized request, frozen graph/admission, actual selected Run/Action start and shared lifecycle/Journal composition. No second executor, writer or Run schema is introduced. Every other selected execution remains queued; inability to admit this exception stops rather than falling back to another publication path.

2. Establish a short exclusive window over the affected current Carrier, predecessor-history destination and governing authority sources. No manual editing, maintenance/script write, Git operation or synchronization may change that frontier during the window. Inability to establish the window stops before effects. No project-wide Engine write lock or replacement is required; distinct existing resource-specific locks remain unchanged.
3. Within that window, reopen and revalidate the exact source, ownership, grammar, report, complete-carrier, definition, permission, intent and current/history destination evidence. Apply only the already admitted one-target effect; materialize actual metadata once, retain exact predecessor bytes and independently read back current/history facts.
After the one admitted effect, verify exact intended current/history bytes,
metadata and ownership. Do not repeat the pre-effect old-rule fingerprint gate:
when an explicitly approved target is itself a governing source, its intended
new bytes must not fail merely for differing from that source's before-state.
Resolve current rules afresh for a later operation. This removes no pre-effect
source/grammar/definition/permission check, target/intent seal, staging check,
actual effect readback, unrelated-source protection or restoration duty.

4. Hold the same window through those effects and readback and any invoked existing Action-local restoration. Retain the exact verified mutable-frontier and attempt-owned-history rules, pre-existing history and accepted Journal evidence. Unknown effects or failed restoration retain their existing truthful disposition; never infer success or replay the effect. Record any actual Journal I/O failure without a receipt gate, automatic recording retry or recovery.

This model does not exclude other Engine writers. It does not itself establish crash-atomic multi-Carrier publication or a stronger guarantee and cannot protect against outside writers ignoring the window. Existing safety requirements remain unchanged. The model adds no public request fields, Boolean approval, local writer, transport or new retry/recovery framework.

### Selected Subject publication failure envelope

Successful source-effect completion requires all admitted current/history postconditions; Journal append/read is not permission, proof or a completion gate. For caught publication/postcondition errors, retain the exclusive window while attempting exact restoration of the verified mutable before-frontier and removal of attempt-owned history; preserve pre-existing history and accepted Journal evidence. Confirmed restoration reports a failed attempt, not update success. Failed or unverified restoration is partial/unknown. Abrupt crash or interruption is not crash-atomic and remains interrupted: inspect actual affected current/history files and Run evidence before any separately admitted continuation. Never automatically replay an Atom effect. This adds no crash-recovery framework and changes no other Action's safety boundary.

Ordinary one-target changed-Subject publication remains blocked under its existing explicit guard until this selected access binding and combined verification are independently accepted. The reviewed batch branch separately requires its actual implementation and verification before execution. This definition is not implementation or readiness, does not remove that guard, activate MCP, alter native meaning or authorize Core migration.

### Run recording

Retain each actual standalone **or** nested Action Run's exact admitted definition Revision, actual Run identity/lineage, safe input/result/effect references, start **and** truthful terminal **or** still-pending interruption under the existing shared Run contract. Workflow-contained bindings also follow CA-R-1525; standalone coverage remains the selected Epic obligation. Reuse plain Project Journal append/read under CA-R-1720 **to** record supplied actual observations, **without** prior-history, chain, validation, canonical receipts, deduplication, recording retry **or** recovery machinery. Preserve existing entries **and** truthful I/O failures; never fabricate a baseline **or** replay an effect. The Journal is not a permission, completion or proof gate; actual Run/source-effect evidence **and** all independent admission/postcondition checks remain required.

### Direct Subject preparation Tool calls

CA-D-425's atom_update MCP provider admits only preview_subjects and stage_subjects, separately from selected update_atom. They reuse this definition's preparation policy but are not actual Atom-update Action Runs. They require no selected Session, completed O067/O145 assessment or fabricated authorization/context reference. Preview writes nothing. Explicit stage permits only the fixed generated scratch candidates/manifest after the native helper checks its own preview against the requested seal before any scratch creation, preserving exact source pins and illustrative time.

These direct calls preserve the existing no-Journal local preparation policy: no Session/Run/event receipt, source Version/time change, archive, promotion or publication is claimed. Actual enclosing-Step Tool-call recording remains required. Local no-MCP statements above describe the CLI, not this separately declared direct binding. Existing update_atom assessment, actual Action-Run observation, trusted-host confirmation, exclusive window, restoration and live-publication guard remain unchanged. Scratch failure retains truthful artifact evidence; a preview hash or candidate never grants effect permission.

### Existing-Atom edit-draft publication

The instructed draft-backed batch uses CA-D-446/CA-D-425's source-pinned full drafts and final schema1 packet. Existing request authorization admits their exact promotion without an additional review/form/confirmation round. A new Draft may be ID-free or carry `CA-R-draft`; an edit Draft carries `<canonical-ID>@<proposed-version>-draft`, with legacy `<canonical-ID>@draft` accepted only when the request supplies the proposed Version. Reopen exact source and draft at the operation, verify the explicit target, expected predecessor Version/digest and marker, restore the canonical ID and original source Status, archive the exact predecessor when one exists, publish the proposed Version with actual time, and independently read back the actual effect. No separate full-candidate preflight, retained Draft-history/lineage requirement, Journal gate or public initial intent metadata is required. Keep existing native failed-write handling and truthful partial/unknown results; proposal existence is not publication. After verified canonical output and any required predecessor readback, conditionally remove only that member's exact packet-pinned draft bytes. If draft cleanup fails or its bytes have drifted, stop and report the actual cleanup failure, preserving the published canonical Revision and archive; do not roll them back or remove another file.
