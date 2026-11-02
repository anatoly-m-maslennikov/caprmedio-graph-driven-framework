---
atom_id: CA-O-129
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run.Agentic Step Execution Context
version: 19
updated_at: 2026-10-27 19:59:46 +0400
relations: {}
tier: 3
---
# Summary

Apply an admitted Atom lifecycle change

## Operation

This Step invokes exactly CA-O-128, apply authorized Atom lifecycle changes, as one Agentic Action. Its context is Integrated under R1527; missing required capability blocks admission, not silent context substitution.

For Move Atom, bind one existing current target, exact source locator and digest, explicit destination mapping, current Revision, collision/path/content-role checks, permissions and effect admission. Recheck those bindings immediately before O128; preserve identity, Summary, Type and Substance. A same-location request is a no-op; an ambiguous, stale, colliding or semantically unresolved destination remains unchanged and returns its truthful outcome.

### Input and parameter binding

Bind request kind, exactly one Create target or one existing current target/predecessor, its complete frozen Carrier/proposal or status/replacement mapping, current models/authority, permissions/effect admission, effect/recovery capabilities and check expectations from the exact admitted Workflow request and revalidated current evidence, plus an independent canonical Journal append attempt. For Change Status, bind actual target Content Role, optional Type, exact applicable model source/revision (including R1874 for Operations and R1875 for Analysis), current and requested status, qualified-model value admission and the most-specific Delivery destination rule. Bind a declared Role/Type override only when it exists; otherwise bind the role model. No required intermediate Atom Status or transition matrix gates the request. A missing/ambiguous/unsupported model, unadmitted Status value, collision, or archive request without model-defined archival status returns its truthful unchanged outcome before O128. Ordinary schema, identity, expected-source/currentness and permission safeguards remain. For Replace preserve the complete accepted set of >=1 successors for that one predecessor. An ambiguous or multi-target/predecessor request returns invalid before invoking O128; separate requests require separate admitted Workflow Runs. Archive shortcut normalization remains subject to O128's actual status-model guard. A Journal append failure is a recording diagnostic, never an admission or completion gate.

For a caller-composed containment cascade under R1521, bind only this Run's one explicit target and requested Status. Recheck its actual latest Revision, source pin, own qualified model, matching Directory Carrier when present, containment-preserving destination and permission immediately before its Action. Earlier successful placement changes do not authorize a stale locator or source pin. The caller retains the complete target set, independent ordering and overall completion; this Step neither discovers descendants nor dispatches another target, and its successful result does not prove the whole cascade complete.

For ordinary Update outside the instructed Subjects-only batch branch, bind the exact identity-preserving assessment and target/proposal/evidence from the latest completed O145 Step Run in this Workflow whose O067 binding matches the current proposal; do not accept an arbitrary historical pass. For other kinds no Update assessment is fabricated. Bind available prior effect evidence and actual Run/parent references, not guessed success; a missing Journal receipt neither blocks the request nor authorizes replay.

Return O128's result and evidence unchanged to the Workflow. This Step has no second Action reference, alternate classifier, routing decision or implicit retry.

## Details

The Workflow decides whether to dispatch or terminate after this result. For Move, O128 owns the same-ID carrier effect and this Step owns only the one-target binding and pre-effect recheck. Every dispatch is a distinct Step Run with its exact O128 definition/input/context binding; completed effects are not replayed when a Journal receipt is pending or its append failed. Tool adapter calls are implementation details, not extra graph nodes or authority.

### Instructed Subjects-only batch member

Bind this one member's exact source/profile/patches and optional complete draft pins to the actual instructed operation and existing Initiative/Operator authorization. Pass that independent member to O128 without a separate form, review/pause response, content-review round, confirmation receipt or fabricated O145/O067/Analysis Report. Retain normal per-target source/draft/patch/layout, archive, Version/time and conditional-write/readback checks, not a redundant full-candidate validation or initial intent-metadata gate. Fresh native intent remains internal where needed.

For draft-backed promotion restore canonical ID/original Status and materialize actual time without authorizing unrelated bytes; Active sources promote Active and generic non-Active semantics stay intact. Ordinary content-update and new-Atom Draft requirements remain unchanged. The caller commits current, creates/commits drafts, promotes and rebuilds graph after completion; stop first failure/uncertainty, retain completed effects, preserve held/remaining sources, keep native failed-write handling and never automatically roll back/replay/retry/resume the batch.
