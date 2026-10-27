---
atom_id: CA-P-1959@157
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 18
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Projection
  - Subject/Graph/Relation
  - Subject/Graph/Rule
version: 157
updated_at: 2026-10-25 00:04:10 +0400
relations: {}
tier: 3
---
# Summary

Improve entity model — Stage 2

## Objective

Complete Candidate #7's methodology migration: Subjects, defining rules, Types, global properties and Atom IDs. Rebuild the affected Subject projections from the actual migrated sources. Keep general content migration separate.

## Details

### Latest Operator order — 2026-10-25

Run these stages in order:

1. Migrate Subjects.
2. Add missing Atoms.
3. Archive obsolete Atoms.
4. Fix properties.
5. Update Atom content last, under CA-P-1970.

Complete the Methodology pass first. Then repeat the sequence for PROGRAMMATIC
RMED Atoms only. No PROGRAMMATIC code or runtime implementation is authorized.
Do not interleave new PROGRAMMATIC corrections ahead of Methodology's pass.
Preserve work already applied or staged; this order is not a rollback.

Create new proposed revisions as Drafts and refine them in iterations. Keep
Current originals unchanged until a proposal is ready and applied. Preserve
existing Drafts, Archives, protected owners and explicit deferrals. Stage a
concrete uncertain proposal without claiming it is approved; ask the Operator
only where refinement still requires a real decision.

Stage 1 changes Subjects, not ordinary Content, properties or lifecycle state.
Later-stage gaps may be inventoried now, but are not permission to execute them
early. Normal maintenance of these execution Plans records the new order; it
does not count as migration of a model Atom's Content.

Mapping, application and verification are per-pass milestones. Methodology
completion opens Methodology content work; it must not wait on the later
PROGRAMMATIC pass. Verify each pass separately before its content stage.
Keep CA-P-1959@157 Active while its retained work remains unproved. Earlier mixed
increment schedules and global all-pass wording below are historical where
they conflict with this order.

### Latest verified checkpoint — 453–477

Mapping460 applied 77 independently reviewed Subjects-only corrections in
77 Current sources, with unchanged bodies and predecessor archives.
Verification461 passed. Citation453 separately corrected only R2102's stale
Project Goal rule reference to current R2132; its predecessor is preserved.

Inventory463 observes 3,967 Current PRMEDO sources and 18,777 Subject
occurrences. Its 782 remaining non-root occurrences belong to 645 owners:
344 P and 438 RMEDO. These are review items, not automatic deferrals.
Views471 and verification472 cover all 2,246 Current RMEDO sources with stable
IDs006–008: Core810, project methodology409 and Engine1,027. Current Plans
are covered separately; the views do not certify complete semantic migration.

Drafts465,469 and477 contain 95 newly created Draft revisions representing
99 proposed Subject corrections. Their Current originals are unchanged.
The three465 Drafts still need the refinement recorded in review466; the
other batches mix reviewed proposals and explicitly tentative candidates.
Draft creation is not promotion, source application or Epic completion.
Previously existing Drafts and Archives were not migrated.

The MCP agent-facing interface is UX. Server, transport, queue and adapters
remain Engineering. Classify the governed aspect; do not move every MCP Atom
to one branch or infer its Content Role from its Subject.


### Current source and view frontier — 392–395, 2026-10-24

Inventory392 and worklist393 observe3,967 unique Current PRMEDO sources,
including1,721 Plans, and18,812 Subject occurrences. Remaining review covers
1,109 non-root occurrences across917 owners:469 P and640 RMEDO, plus51
canonical legacy flags. All50 previous whole-owner holds remain preserved.
These are actual remaining items, not automatically deferred or applied.

Views394 retain stable IDs006–008 and cover all2,246 Current RMEDO sources:
Core810, project methodology409 and Engine1,027. Verification395 passes live
source/configuration pins, disjoint coverage, one-root mechanical trees,
tab indentation and property sections. Separate P inventory coverage is not
an invented Plan Projection or evidence of complete semantic migration.

The Operator deferred conflict-workflow O updates and requested an issues
report. Done Analysis A1217 records automatic Tier/Updated At winner selection,
decision-step bypasses and obsolete Evaluation expectations. O007 already
provides an explicit decision step. No conflict-policy source is changed by
that report or this checkpoint. Continue unrelated methodology work; Terms,
instance naming and existing C/A, Draft and Archive instance migration remain
outside this continuation. New report creation was explicitly requested.

Seven bounded lanes prepare further mappings, review legacy flags and check
applied effects; root alone integrates authoritative writes. All source and
runtime outcomes remain distinct. Keep the Epic Active until the retained
work has actual verified dispositions; no PROGRAMMATIC implementation,
runtime test, MCP deployment, commit, push or release is claimed.

### Applied checkpoint — 356–390, 2026-10-24

These source batches record454 Current update events plus one retirement,
with predecessor archives. They are not454 unique Atoms or completed Tasks.
Verification367/383/387 and the batch-specific readbacks check the actual
source/archive effects; precision review385 corrects the final tail before
mapping390 applies it. Further proposed packets are not applied by association.

The updates correct overbroad Configuration dependencies, distinguish the
operating Framework Instance from the framework product, align13 retained
execution Plans, and apply inspected Plan/RMEDO topic aliases. Owned-Atom
selections stay Selections, Journal records stay distinct from live Events,
and duplicate Container/Hub dependencies do not create new Atom kinds.
No new Domain kind, Term layer or instance-naming convention is introduced.

R031's mandatory Structural Level model is retired under the already-approved
ancestry model. Its seven Current consumers are repaired together; E445 and
R775 lose the obsolete depth requirements, and R706 uses the existing Project
Principle Universe rather than a named Tier. No new root-to-descendant
Evaluation links are added. Existing cross-Scope relation holds remain in the
separate content-migration work; this is not full relation conformance.

Keep this Epic and its retained execution tasks Active. Refresh the Current
worklist, the three stable Subject views and metadata evidence from the actual
post-write frontier. Continue remaining supported mappings and explicit
source dispositions; do not hide an unresolved case with a generic prefix.
Existing C/A, Drafts, Archives, Terms and instance naming retain their scope
boundaries. No PROGRAMMATIC implementation, workflow code, test suite,
runtime, MCP deployment, Journal append, Git commit/push or release is claimed.

### Current checkpoint — 339–350, 2026-10-24

Instance naming in Subjects is explicitly deferred and out of scope. The
latest deferral supersedes the earlier Summary-based naming approval. Keep
existing names and disclose ambiguous notation; no naming solution is chosen
or required to finish this pass. Terms and prior whole-owner holds remain
deferred separately.

Batches339/340/341/342/344/345/346 apply275 checked Subjects-only updates
across269 IDs, with predecessor archives and unchanged bodies, identities,
statuses and other properties. They correct inspected Plan/report/testing/
release/configuration topics, technical aliases and precise Evaluation,
actor-permission and Analysis Report targets. These are source updates, not
completed Tasks. No new Domain entity is introduced; App Interface is an
Engineering topic. Existing content is not thereby accepted as aligned.

Inventory347 includes3,968 unique Current PRMEDO sources and18,949 Subject
occurrences. The remaining1,551 non-root occurrences comprise614 P and937
RMEDO across1,148 owners;55 additional canonical-looking legacy cases need
semantic review. The current-prmedo-subject-worklist records all occurrences,
remaining-owner pins, routing groups and existing holds. Groups are review
routing, not target mappings or additional Operator deferrals. Do not use
the older P-excluding worklist as the current queue.

Views348 retain IDs006–008 and all2,247 Current RMEDO sources: Core810,
project methodology410 and Engine1,027. Verification349 passes actual source
and configuration pins, complete disjoint partitions, one-root trees,
literal-tab indentation and property sections. Thirteen old operator-bearing
Step names remain a declared limitation under the explicit naming deferral.
Current Plans remain covered separately rather than silently omitted.

Full migration remains incomplete. Keep this Epic and retained tasks Active;
continue supported remaining mappings and explicit source dispositions, then
refresh final evidence. No PROGRAMMATIC implementation, test suite, runtime,
MCP, new Journal append, commit/push or release is performed in this checkpoint.

### Applied non-Terms continuation — 318–334, 2026-10-24

Latest Operator scope override: Terms remain deferred. Terms326 is scratch
preparation only; neither its proposed M439 nor its eight source edits is
applied. Do not build a Terms Graph or continue Terms-rule alignment in this
Epic continuation. Earlier applied Terms changes remain historical facts,
not authorization for more Terms work. M113/M114 and other explicit whole-owner
holds remain unchanged. The two Terms Graph Plans P1497/P1514 are excluded
from331, and329 leaves its fifty Terms-related or previously held sources
unchanged. A broader Terms dependency is conservatively left held rather
than used to expand this pass.

Filename318/verification319 completes the formerly pending285 closure:
25 Current updates, fifteen file renames and eighteen live references in
sixteen consumers. P1121's matching container folder is moved with its file;
five unchanged child/history files keep their bytes, and only the two actual
reference-changing children receive new Versions. Summaries and Roles stay
unchanged. The older285-pending statements below are superseded by this
actual result, not by a filename-only proposal.

Content321/verification322 updates ten defining/consumer sources and retires
the obsolete universal one-Claim rule R918. Role-specific Content and the
formal Graph Rule YAML exception are expressed by current methodology;
four typed consumers now target R2102 at valid same-Scope Tiers. Existing
instance Markdown is not mass-migrated. R2159's Summary change creates new
R2160, Define Atom Content Scope, before retiring R2159; twenty-three Subjects
use Content.Scope. Verification325 checks the successor, predecessor and
one actual atom_replaced Journal record. That real direct-authoring event
has no invented baseline or Workflow Run. Earlier no-Journal statements
describe their earlier checkpoints, not this replacement.

Content329 applies254 exact Atom.Substance-to-Atom.Content Subject occurrences
in252 Current sources. Plans331 applies48 inspected governing-topic mappings:
27 Analysis-report harvest Plans, seven RMED reviews, five source-Atom
corrections and nine implementation Plans. These are300 Current updates,
not300 completed tasks. All bodies, other properties, identities and statuses
are unchanged; every predecessor and both hold lists pass readback. C590
and C592 are resolved from already-applied source evidence, without migrating
other C/A or choosing new Engine behavior.

Inventory332 contains3,968 unique Current PRMEDO sources, including1,721
Plans, and18,949 Subject occurrences. It exposes1,830 non-root occurrences:
816 P and1,014 RMEDO. Views333 preserve IDs006–008 and cover all2,247 Current
RMEDO sources: Core810, project methodology410 and Engine1,027. Verification334
passes source/configuration hashes, complete disjoint selections, tree and
property rendering. P evidence remains separate. These mechanical checks do
not certify every Subject meaning or close the migration.

Instance naming in Subjects is deferred by the latest Operator decision,
superseding the earlier approval to use existing Summaries. The thirteen old
operator-containing Step names stay unchanged and visible as a projection
limitation. Do not choose a naming/escaping solution or make this deferred
work a completion gate. Remaining exact mappings,
held source/Scope/configuration cases and final acceptance stay open. Keep
this Epic and retained tasks Active. No PROGRAMMATIC implementation, schemas,
test suite, runtime, MCP, Git commit/push or release is performed.

### Applied continuation — batches300–310, 2026-10-24

Verification310 passes 245 PRMEDO source events across 217 distinct IDs:
242 same-ID update events and three retirements. All predecessor archives,
final current heads and overlapping hash/Version chains were checked. No
Current typed relations target retired R126, R1766 or R2103. Counts describe
source events, not distinct completed tasks. This later administrative update
is recorded separately and keeps the Epic Active.

Batch300 aligns the identity rule to Summary or Content Role changes, named
primary-instance Subjects and per-kind name uniqueness. Five reviewed
framework requirements/principles use Subject/Product: CAPRMEDIO Framework.
The pure universal Definition-Atom gate R126 is retired in274; four related
Terms/Semantics sources preserve definitions derived from source use and
different meanings in non-overlapping contexts.

Reviewed packets290/291 are merged in303: 72 occurrences, 67 source updates,
five overlaps handled once. Packet287 is rebased in304: 52 supported Subject
changes, with all 32 held occurrences excluded. Batch308 maps 50 concrete
Carrier/Markdown-structure/package aliases. Batch309 maps 60 references in
59 sources to existing named Workflow/Action instances; no new Domain kind
or instance name is invented. These actual applications supersede the older
pending lists for274/287/290/291 below. Filename285 still lacks its consumer
body edits; that packet is not applied.

C588/C595/C602 are Resolved. C599 distinguishes the settled removal of
Atom.Entity from generic Entity tags; fresh inventories contain no standalone
Entity tag in Current Plans. Existing C/A, Drafts and Archives are not migrated.
Only this work's new bounded Question records and new predecessor archives
are updated under their existing authorization.

One concrete methodology choice remains: thirteen existing Step Subjects use
old encoded names such as Public release/Step: finalize actual Version History
link. After // those characters can be read as graph operators, not one name.
Do not silently add quoting syntax, rename instances or interpret a property
as a primary instance. All187 current Operation Summaries are unique within
their Workflow/Step/Action kinds and contain none of the reserved characters;
using Summary was proposed and briefly approved, then superseded by the
Operator's explicit deferral of instance naming in Subjects. Those thirteen
source Subjects stay unchanged. No naming-model solution is selected in this
pass; this deferred work does not block completion.

The completion progress records fresh inventory and projection checks after
these batches. Remaining source-specific mappings, held aliases, carrier
consumer closure and explicit semantic exceptions still prevent closure.
No PROGRAMMATIC implementation, test-suite run, runtime, Journal append,
commit, push or release is performed or implied.

### Current P-inclusive checkpoint — 293/294, 2026-10-24

Inventory293 contains 3,972 unique Current PRMEDO sources, including 1,721
Plans. The four obsolete partition definitions retired by batch270 explain
the count change; no Current status group was excluded. Existing C/A, Draft
and Archive migration remains outside scope. P040/P101 parent recovery and
the 221 cross-Scope relation cases retain their explicit high-blast holds.

Filename277 applied 354 carrier-only corrections. Independent verification284
passes all Current/archive pairs, bodies, Summaries, IDs and permitted metadata
changes; its fifteen held moves remain unchanged. Subject281 applied 62
Subjects-only updates: 21 maps and 41 unsupported-context removals. Verification292
passes all pairs and unchanged bodies, with eight held sources untouched.
Metadata289 passes all 3,972 sources before that Subjects-only batch.

Views294 preserve stable Projection IDs006–008 and verify all 2,251 Current
RMEDO source pins: Core813, methodology411 and Engine1,027. Verification294b
passes source/configuration hashes, complete disjoint partitions, indentation,
property sections and visible unresolved Subjects. The first verifier retained
the old Core817 baseline; its diagnostic is preserved rather than counted as
a source failure. Separate P coverage remains in inventory293, which records
984 non-root P and 1,131 non-root RMEDO occurrences. This administrative Plan
update comes after inventory293 and does not change any RMEDO view source pin.

The subsequent Operator answers resolve the product/project distinction,
role-specific Content, named Selections, primary-instance notation and name
uniqueness per kind. Batch300 applies nine updates and two retirements;
verification301 passes the Current/archive checks. R1432 now creates a new
identity only for Summary or Content Role changes. R1766 and the obsolete
project exception R2103 are archived. R2002/R1321 describe primary-instance
// and a following property; P1087 names its bounded Selection. Five reviewed
framework requirements/principles now govern Subject/Product: CAPRMEDIO
Framework, without a blanket Project mapping. Other content stays unchanged.

C588/C595/C602 are Resolved; C599 records removal of Atom.Entity without
pretending every generic Entity tag has been mapped. The latest goal is to
continue without interruptions, no PROGRAMMATIC implementation and no new
subagents. Below95% confidence, check Candidate7, plan, this chat's latest
two days and active principles; ask if still uncertain. Existing explicit
deferrals, including Engine-only questions, remain separate. Prepared274/285/
287/290/291 remain proposals until their actual application is recorded.
Filename285 still lacks its consumer-body edits. Views294 predate the new
source versions and must be refreshed before final verification.

Keep this Epic and its retained tasks Active. Remaining Subject dispositions,
carrier reconciliation and final completion checks are open. No production
implementation, runtime, test-suite pass, Journal append, commit, push or
release is claimed. Earlier checkpoint numbers below remain historical.

### Latest execution boundary — 2026-10-24

The Operator re-added P migration. Apply Candidate #7 to Current P/R/M/E/D/O source Atoms and Governing Configurations, including Current Plans in the Project root and declared Scope Units. Current includes Active, Done, Canceled, Backlog and other non-Draft/non-Archived statuses. Do not migrate existing C/A, Draft or Archived Atoms. Create predecessor archives only for Current updates. Universal definitions may describe excluded forms; migrating those instances is not a completion gate.

Complete this Epic without interruptions and without PROGRAMMATIC implementation. Below 95% confidence, recheck Candidate #7, this plan, the Operator's exact inputs from this chat's latest two days and active principles; latest human words win. For a small-blast uncertainty, create a C/Question, choose the best bounded interpretation and continue. Explicitly defer a high-blast uncertainty and continue independent work. New C/Questions are allowed; this does not authorize migration of existing C/A. Do not invent new Domain entities or properties.

Keep Current P mapping and metadata checks separate from RMEDO counts. The expanded frontier originally contained 1,724 Current P candidates with unique canonical IDs. Three normative rules misfiled as Plans now have Requirement successors: CA-P-032 → CA-R-2156, CA-P-033 → CA-R-2157 and CA-P-034 → CA-R-2158. Their original Claims are preserved, twelve Current consumers have thirteen typed references rebound, and the three old Plans are archived. The resulting frontier contains 1,721 Current Plans; the total Current PRMEDO count remains 3,976. These role corrections are not extra completed Plan tasks.

P metadata changes, 1,203 earlier exact Subject-alias updates, fourteen legacy-tag corrections, and 182 further alias-owner updates have source/archive evidence. All 62 multiple-GOVERNS Plan cases have one supported governing Subject after source-specific review; this does not certify every retained dependency literal. P2062 now has a coherent Epic file/folder name and links; its four path-only moved children retain their Versions. Preserve existing Plan statuses, body content, identities and containment unless an exact correction is supported. Remaining Subject meanings and relation/containment consistency still need their recorded dispositions. No existing Draft or Archive is edited to make the count pass.

### Current P/RMEDO continuation — 2026-10-24

Increments 125/128/130/131 apply 638 versioned source-update events: 551 Plan events and 87 Evaluation events, not 638 distinct owners or completed tasks. They correct 639 Subject occurrences: contextual Implementation, Plan confidence thresholds, Framework Settings, supported methodology-source/manifest topics, and source-specific Evaluation targets. Objectives, fixtures, lifecycle statuses and unrelated content stay unchanged. New predecessor archives preserve the actual old versions. C600 records the bounded contextual Implementation-topic choice. Rejected and held proposals remain explicit; a whole archived Atom is not reduced to its Version Number.

The three readable Subject Graph views use the existing R2150/D653 Type and new stable IDs CA-PROJ-006 (Core), CA-PROJ-007 (project methodology) and CA-PROJ-008 (Engine). Their admitted source selection is Current RMEDO; separate full Current P inventory and applied-effect evidence remain mandatory. They expose unmapped expressions as limitations rather than claiming a clean final hierarchy. Refresh the affected view after source updates before final verification.

The refreshed inventory and independent per-batch checks are recorded in the completion progress. Remaining exact Subjects, high-blast non-ancestor governing relations, obsolete source premises and Governing Configuration exceptions still need their final explicit dispositions. The 221 cross-Scope relation occurrences have an owner/target evidence ledger for later content/ownership review under CA-P-1970; no Tier adjustment silently admits them. Keep this Epic and the retained mapping/application/verification tasks Active until their actual DoDs pass.

### Applied carrier continuation — 2026-10-24

Increments 150/154/160/162 add 450 versioned Current-source update events, not 450 distinct Atoms or completed Plan tasks. Fifty-six Plan stems lose only redundant Scope tokens; P2281 retains its matching file/directory bundle and twelve current child links. Nine existing archived children retain their bytes. Four exactly redundant untyped links are removed while their precise direct counterparts remain. Independent verification passed both increments.

The Delivery increment corrects 333 Type filename encodings and 46 exact live references, combined into 360 source updates; all 166 historical/quoted references remain unchanged. The thirty further exact Subject aliases use existing defined properties/roles and preserve their bodies. Writer readbacks passed; independent checks of these two later increments remain pending. Production references were handed to CA #3: PROGRAMMATIC; this Epic changes no code.

Checkpoint 164 rebuilds the three readable Subject Graph Projections from all 2,255 Current RMEDO sources, with stable IDs 006–008. The separate post-162 inventory covers all 3,976 Current PRMEDO sources, including 1,721 Plans, and still records 3,399 non-root Subject occurrences. Numeric-tier filename consumers and source-specific remaining meanings are under review. These are explicit remaining obligations, not a reason to claim this Epic Done. Existing Draft/Archive and C/A migration remain excluded.

### Re-added P migration — checkpoint 181, 2026-10-24

P migration remains part of this Epic, including Current Active, Done, Canceled,
Backlog and other non-Draft/non-Archived Plans. Candidate #7, the application
plan and P1966/P1968/P1969 explicitly share that boundary. Existing C/A, Drafts
and Archives remain excluded; create predecessors only for Current updates.

Increments 173/174/175/178/179/180 apply 361 further source-update events,
including 294 P events, not distinct-Atom or completed-task counts. The five
Subject batches correct 433 occurrences. Increment 179 maps 126 Plan governing
Subjects to reviewed existing topics and 27 related RMED occurrences. Increment
180 fixes fourteen extra META_MTHD Plan leaf tokens without changing their Done
statuses, text, ownership or parent directory; each receives its next Version
and predecessor archive. Keep the independent checks in the completion record.

The fresh inventory selects 3,976 unique Current PRMEDO Atoms, including 1,721
Plans. Remaining non-root Subjects are 1,573 P and 1,363 RMEDO, with zero
malformed Subject-root expressions. Rebuilt views 006–008 at checkpoint 182
passed independent verification of all 2,255 RMEDO sources and expose their
remaining limitations. They do not certify Plan migration or all meanings.

Two parent carriers remain high-blast holds: P040 and P101 have children but no
recoverable Markdown parent. Preserve all children/history; do not invent
parents or links from folder names. Record recovery in the later content/carrier
review under P1970. The separate empty P101 shell is residue, not an Atom.

Keep this Epic Active: remaining Subject dispositions, filename work and final
verification are open. No PROGRAMMATIC implementation, runtime, test-suite pass,
Journal append, commit or release is implied.

### Current authority and scope

Use [Candidate #7](../_projection/core-entity-review/presentation/operator.model.candidate-7.md) and the latest Operator decisions. The [application plan](../_projection/core-entity-review/presentation/candidate-7.methodology-application.md) describes the boundary. The [applied increment](../_projection/core-entity-review/presentation/candidate-7.methodology-increment-2026-10-22.md) records actual source changes, not full completion.

This Epic changes methodology source files and Plans only. Direct file edits are authorized for this continuation. Tool implementation, code, implementation schemas, tests, MCP, Settings values, runtime, releases and commits are outside this work. Do not repair a missing tool route to proceed.

Subject is the root. Product, Domain, Engineering, UX, Design and Documentation are current, expandable topic branches; Graph/Relation and Graph/Rule apply across them. Preserve full paths, classifier values and inherited properties. Leave existing instance names unchanged: instance-naming changes and Terms remain deferred. Exact new Type-to-tier restrictions remain deferred except for the established Project Goal exception.

Core stays abstract and reusable. Project-specific procedures and choices belong to Project Configuration. Source Atoms, not derived views or delivered copies, hold authority. Keep the PROGRAMMATIC chat's changes intact.

### 2026-10-23 — Operator instruction to finish the migration

The Operator requested: update this Epic and complete Candidate #7 and its migration plan. Continue the existing direct methodology-file route. This does not authorize Tool/code/runtime repair, release or Git commits, and it does not waive unresolved cases or prior write holds.

The Operator clarified during execution that methodology is the source of truth, not code. The approved Tier/Scope semantics therefore govern the formal R/D source contract; implementation support is a separate consumer task and cannot veto the methodology. CA-P-2167 has moved to a sibling bundle outside this Epic; its link/history verification is complete and its lifecycle remains Active.

Earlier completion lanes — later ordering takes precedence:

1. Refresh the actual authoritative Current P/R/M/E/D/O and Governing Configuration frontier; finish exact Subject mappings and source dispositions without introducing an unapproved Domain entity.
2. Complete numeric Tier and Global Tier/Structural Level methodology alignment with its dependency closure. Methodology, not existing code, is the source of truth. Give the already-approved ordering rule its smallest formal methodology representation; missing parser/runtime support does not block source authoring. Do not invent new rule semantics or change production Tools.
3. Classify PROGRAMMATIC M/D consumers as Eng Policy or Eng Decision using actual child declarations and applicability, not file names or an automatic Role default. Resolve legacy Type/filename continuity and preserve the latest Summary-or-Content-Role identity rule; Type alone does not create a new identity.
4. Complete Current in-scope IDs, required properties and uniqueness. Resolve identity collisions from evidence. Existing Draft/Archive instance migration is excluded; use the latest confidence/Question/defer policy above.
5. Re-home the independent CA-P-2167 bundle before the parent Done cascade, preserving its lifecycle and child bundles.
6. Rebuild the affected Subject views from the resulting authoritative sources using an existing local generator; do not change production Tools to obtain a green result.
7. Independently verify the final source, archive, identity, classification and projection evidence. Mark the retained tasks and this Epic Done only when their real completion conditions hold. Stop an affected lane on a concrete unresolved choice while continuing independent safe work.

Core source definitions already applied in the preceding increment are not replayed. Root owns integration, shared planning files and any final closure; worker scopes remain disjoint. General content migration and independent Tools implementation stay outside this Epic.

### 2026-10-23 — completion progress

[Completion progress](../_projection/core-entity-review/presentation/candidate-7.completion-progress-2026-10-23.md) records two applied M/D classification batches: 179 Current carriers, 40 Eng Policy and 139 Eng Decision, 39 filename-token changes and 179 predecessor archives. Summary and Substance remain unchanged. Both batches passed exact writer readback and independent bounded checks for every Current/archive pair. Missing-header carriers and the six controlled holds were not silently admitted or changed.

CA-P-2167 and its bundle are re-homed outside this Epic. Forty link-changing Current carriers received their own Version/time changes and predecessor archives; unchanged children did not receive path-only Version bumps. This containment gate is complete, not a request to complete the independent Tools backlog.

Numeric Tier defining sources and formal Endpoint Constraint methodology are being aligned with the approved semantics; data/consumer closure and independent review remain open. Code support is not a source-authoring gate. Remaining Subjects, IDs/properties, rebuilt views and final verification still prevent this Epic from closing. The Operator approved missing Status normalization: use the existing status folder where present; otherwise set Active outside Draft/Archive, leaving content unchanged. Record actual normalization effects separately; this approval alone does not mean the headers were updated.

### 2026-10-23 — R/M, Subject and Eng-Type definition alignment

[Applied source increment](../_projection/core-entity-review/presentation/candidate-7.methodology-alignment-2026-10-23.md): seven same-ID updates, four successor replacements and one new Project Configuration rule; 12 Current source carriers and 11 predecessor archives. Independent bounded read-only checks passed. The source record includes exact paths, Versions and observed hashes.

R1339/R1340/R1548/R1694 distinguish outcomes from means without losing model-definition coverage. R2004/R2006 state Subject/content-role independence and Graph's global scope. R2119–R2122 replace the four old Eng-Type definitions; R1665 references the new Delivery definitions; R2123 limits PROGRAMMATIC/descendant M/D to Eng Policy or Eng Decision. The six PROGRAMMATIC write holds remain untouched.

R2005's authoritative Current carrier is absent and its v1 archive exists; semantic cleanup of remaining Method-root references is still open. Existing M/D consumer classifications, legacy Type/filename continuity, numeric-Tier and Structural Level/data migration, remaining Subjects, graph rebuild, CA-O-188 identity collision and CA-P-2167 rehoming remain incomplete. No Tools/code, schema, Settings, runtime, tests, Journal, Git commit or release is implied. Keep this Epic Active.

### 2026-10-23 — bounded bare-Tool source cleanup

The Operator authorized source-specific review of 207 bare-Tool owners, including replacement/splitting, tier and Scope Unit changes where justified. Check whether the real Subject is an existing Domain entity; do not introduce a new Domain entity without asking the Operator. This bounded permission does not turn the rest of this Epic into general content migration.

[Applied result](../_projection/core-entity-review/presentation/candidate-7.tool-atom-cleanup-2026-10-23.md): 205 same-ID updates, 153 Type corrections, six ownership/carrier moves and one duplicate retirement, with 206 predecessor archives. Governing Subjects use 91 existing Domain bearers and 114 Engineering topics; no new Domain entity, Summary or Substance was introduced. E567 remains unchanged under PROGRAMMATIC ownership. Independent post-write checks passed.

This is not full completion. Keep the wider legacy dependency mapping, property/ID and filename work, graph rebuild and final verification in the queue. O160's later ownership/Subject correction is recorded in the staged checkpoint below; its body remains unchanged. Do not reuse the earlier worklist's changed source pins as if still current.

### 2026-10-23 — applied remaining-source increments

Luna reviewed seven disjoint mapping lanes against the captured 2,901-source C/A/R/M/E/D/O frontier. Missing-Status legacy carriers were included rather than silently excluded. Plans remain a separate metadata frontier.

[Applied checkpoint](../_projection/core-entity-review/presentation/candidate-7.remaining-corrections-2026-10-23.md): 2,219 distinct source Atoms, 3,244 versioned updates/archives, 5,132 Subject corrections excluding the separate O160 correction, and 732 missing carried IDs repaired from unambiguous existing filenames. Bodies and Summaries remain unchanged. No new Domain entity was introduced; no identity was allocated. O160 joins O158/O159 in Project Configuration.

This is still partial. The checkpoint/JSON ledger records remaining exact literals, header gaps, unapplied glossary retirement proposals and the CA-O-188 identity collision. Do not hide them or close this Epic. Tools/runtime and general content migration stay separate. The older lexical worklist is historical input, not the current applied frontier. Keep PROGRAMMATIC's six write holds intact.

### Earlier execution order — superseded by the 2026-10-25 sequence

1. Refresh current-source mapping worklists and resolve the remaining exact Subjects. Keep source-specific uncertainty and malformed legacy carriers visible. Do not guess from a folder, Content Role or prefix alone.
2. Apply supported Candidate #7 increments: Subjects; required property/ID data; Type classification; needed R/D rule alignment; and filename-token alignment. Review defining-R coverage and add only genuine missing definitions. General Substance rewrites stay outside this Epic.
3. Verify actual effects and rebuild the affected Core, Project Configuration and Engine Subject views from the resulting sources. Preserve unresolved cases in the output; do not hide them to produce a clean-looking tree.
4. Completed: CA-P-2167 and its child bundle are re-homed outside this Epic's containment tree, with their independent lifecycles preserved. Verify that separation at final closure; do not repeat the move or require the independent Tools backlog to finish. The parent's Done cascade must not cancel that work.

Mapping, source application and final verification are separate responsibilities. The current mapping worklist is a source-derived planning aid, not a new authority or proof that every canonical-looking path is semantically correct.

### Current task groups

- [CA-P-1966 — Map current Core Subject origins](18-CA-P-1959@157-EPIC--improve-entity-model-stage-2/08-CA-P-1966-EPIC--map-current-core-subject-origins.md): maintain the current mapping frontier and integrate exact dispositions.
- [CA-P-1968 — Apply approved Subject migration batches](18-CA-P-1959@157-EPIC--improve-entity-model-stage-2/10-CA-P-1968-EPIC--apply-approved-subject-migration-batches.md): organize the remaining Candidate #7 methodology-source increments, including the approved property, ID and Type work.
- [CA-P-1969 — Verify Subjects before content updates](18-CA-P-1959@157-EPIC--improve-entity-model-stage-2/11-CA-P-1969-TASK--verify-subject-migration-before-content-updates.md): verify the actual Candidate #7 effects and rebuilt views, not the earlier Candidate #4 batch.
- [CA-P-2167 — Finish Tools before Stage 2 execution](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution.md): independent Tools backlog retained for later work. Its historical title does not make it a prerequisite for this direct methodology migration.

General content review/update belongs to CA-P-1970, outside this Epic's completion criteria. No Tools, release, runtime or general content work must be completed merely to close this methodology migration.

### Worklists and evidence

The [remaining Subject worklist](../_projection/core-entity-review/presentation/candidate-7.current-prmedo-subject-worklist.json) and its [reading note](../_projection/core-entity-review/presentation/candidate-7.current-prmedo-subject-worklist.md) replace the old fixed-count research assignments. Read their source boundary and exclusions. A lexical routing lane is not a proposed target Subject. Refresh changed source records before use; do not require unchanged historical rule fingerprints or a fixed global frontier for every independent edit.

The seven mapping lanes are history_actor, content_roles_types, operations, relations_subjects, carrier_storage, methodology_configuration and other. Each remaining occurrence has one routing lane. Canonical-form occurrences and excluded carriers remain separately reported.

The older specification worklist excludes Plans and cannot certify their migration. P is now included through a separate Current Plan inventory and application ledger under CA-P-1968. Include Current Plan Subjects, required properties, Types, IDs and numeric Tiers; do not migrate existing Draft or Archived Plans.

Record actual changed paths, Versions, predecessor archives and unresolved items. Scratch records and derived views are not Journal events, executed Workflows, commits or runtime acceptance.

### Update and archive rules

Every real Current-Atom update advances Version by one and updates Updated At. Changing Summary or Content Role creates a new Atom identity. Other Content, Type or property changes retain the base ID when Summary and Content Role stay unchanged; this is not a migration-only classification exception.

Archive the predecessor with Archived Status and its old Version qualifier in its carried ID and filename. Keep the archived numeric Version, Updated At and unrelated content unchanged. Exact-old-bytes preservation is not the archive contract. Git retains the pre-change file history.

Current includes Active, Done, Canceled and Backlog, but excludes Draft and Archived. Current IDs remain unique. Draft and Archived IDs follow Candidate #7's group-qualified forms. Default Atom relations address unsuffixed Current IDs.

Stop the affected increment on a failed effect. Below95% confidence, recheck Candidate #7, this plan, the latest two days of exact human input and active principles; if still uncertain, ask the Operator. Do not silently apply the superseded best-choice or self-defer policy. Preserve completed effects and the untouched remainder. Do not invent receipts or automatically reset, replay or roll back a batch.

### Completed and canceled work

The first Candidate #7 source increment is applied and checked; its result report lists the actual changes and remaining gaps. It is not full migration completion.

The Operator canceled the outdated Candidate #3/#4 review-packet, sealed-preview and staging chain: 58 Plans, including the CA-P-2193 subtree and CA-P-1967/1973/2188/2189/2190/2191. Their predecessor archives preserve prior results. Canceled tasks do not have to become Done and must not block the retained migration.

Old 611-Atom and 746-Atom migration results remain historical evidence for their own frontiers. They are not Candidate #7 verification. Old Candidate #3/#4 pins, separate sealed-packet approvals, deep per-Atom review packets and Tools-first gates are not current execution prerequisites.

The full former Epic, including historical checkpoints and prior task indexes, is preserved in [CA-P-1959@132](archive/CA-P-1959@132-EPIC--improve-entity-model-stage-2.md). Read it as history, not as another set of current instructions.

## Definition of Done

- All in-scope Candidate #7 Subject, Type, property, ID and defining-rule work has an actual source disposition: applied, unchanged with evidence, or explicitly deferred by the Operator. A high-blast skipped case must identify its affected sources, reason and follow-up; do not silently omit it or report it applied. Bounded C/Question dispositions follow the latest Operator instruction above.
- Current P/R/M/E/D/O identities, mandatory properties, applicable Types, effective labels and filename rules have been checked against the settled model. New predecessor archives use the settled qualified identity. Existing Draft/Archived instances and C/A migration remain excluded; specialized Graph Rule exceptions remain valid.
- Applied updates have the expected Version/time effects and predecessor archives. Intended statuses, ownership and unrelated content are preserved unless the approved increment explicitly changes them.
- The affected Subject projections have been rebuilt from the final actual source frontier, with source Versions and visible limitations. Older saved graphs, mapping candidates and bounded PROGRAMMATIC policy bundles are not substitutes.
- Current mapping/application/verification tasks have their actual outcomes recorded. Canceled tasks and independent Tools backlog are not completion gates.
- Unfinished independent Tools Plans have been re-homed outside this Epic before its Done transition. Do not close this Epic while its containment cascade would cancel them.

Keep this Epic Active until these conditions are met. General content migration, Tools implementation, runtime tests, deployment and release remain separate.
